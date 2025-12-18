from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.api_error import APIError
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .highlight_result_entity import HighlightResultEntity
    from .stored_search_highlight_result import StoredSearchHighlightResult

@dataclass
class HighlightedWordResult(APIError, AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The conceptTerms property
    concept_terms: Optional[HighlightResultEntity] = None
    # The searchTerms property
    search_terms: Optional[HighlightResultEntity] = None
    # The storedSearchHighlightingByCategory property
    stored_search_highlighting_by_category: Optional[list[StoredSearchHighlightResult]] = None
    # The trainingTerms property
    training_terms: Optional[HighlightResultEntity] = None
    # The userTerms property
    user_terms: Optional[HighlightResultEntity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HighlightedWordResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HighlightedWordResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HighlightedWordResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .highlight_result_entity import HighlightResultEntity
        from .stored_search_highlight_result import StoredSearchHighlightResult

        from .highlight_result_entity import HighlightResultEntity
        from .stored_search_highlight_result import StoredSearchHighlightResult

        fields: dict[str, Callable[[Any], None]] = {
            "conceptTerms": lambda n : setattr(self, 'concept_terms', n.get_object_value(HighlightResultEntity)),
            "searchTerms": lambda n : setattr(self, 'search_terms', n.get_object_value(HighlightResultEntity)),
            "storedSearchHighlightingByCategory": lambda n : setattr(self, 'stored_search_highlighting_by_category', n.get_collection_of_object_values(StoredSearchHighlightResult)),
            "trainingTerms": lambda n : setattr(self, 'training_terms', n.get_object_value(HighlightResultEntity)),
            "userTerms": lambda n : setattr(self, 'user_terms', n.get_object_value(HighlightResultEntity)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("conceptTerms", self.concept_terms)
        writer.write_object_value("searchTerms", self.search_terms)
        writer.write_collection_of_object_values("storedSearchHighlightingByCategory", self.stored_search_highlighting_by_category)
        writer.write_object_value("trainingTerms", self.training_terms)
        writer.write_object_value("userTerms", self.user_terms)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def primary_message(self) -> Optional[str]:
        """
        The primary error message.
        """
        return super().message

