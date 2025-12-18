from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class HighlightResultEntity(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The hitLocationsRel property
    hit_locations_rel: Optional[list[float]] = None
    # The numberHits property
    number_hits: Optional[int] = None
    # The number of hits by page.
    number_hits_by_page: Optional[list[int]] = None
    # a regular expression to identify all these words
    regular_expression: Optional[str] = None
    # The termToHighlightIsWordBoundaryAfter property
    term_to_highlight_is_word_boundary_after: Optional[list[bool]] = None
    # The termToHighlightIsWordBoundaryBefore property
    term_to_highlight_is_word_boundary_before: Optional[list[bool]] = None
    # The list of returned highlights.
    terms_to_highlight: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HighlightResultEntity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HighlightResultEntity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HighlightResultEntity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "hitLocationsRel": lambda n : setattr(self, 'hit_locations_rel', n.get_collection_of_primitive_values(float)),
            "numberHits": lambda n : setattr(self, 'number_hits', n.get_int_value()),
            "numberHitsByPage": lambda n : setattr(self, 'number_hits_by_page', n.get_collection_of_primitive_values(int)),
            "regularExpression": lambda n : setattr(self, 'regular_expression', n.get_str_value()),
            "termToHighlightIsWordBoundaryAfter": lambda n : setattr(self, 'term_to_highlight_is_word_boundary_after', n.get_collection_of_primitive_values(bool)),
            "termToHighlightIsWordBoundaryBefore": lambda n : setattr(self, 'term_to_highlight_is_word_boundary_before', n.get_collection_of_primitive_values(bool)),
            "termsToHighlight": lambda n : setattr(self, 'terms_to_highlight', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("hitLocationsRel", self.hit_locations_rel)
        writer.write_int_value("numberHits", self.number_hits)
        writer.write_collection_of_primitive_values("numberHitsByPage", self.number_hits_by_page)
        writer.write_str_value("regularExpression", self.regular_expression)
        writer.write_collection_of_primitive_values("termToHighlightIsWordBoundaryAfter", self.term_to_highlight_is_word_boundary_after)
        writer.write_collection_of_primitive_values("termToHighlightIsWordBoundaryBefore", self.term_to_highlight_is_word_boundary_before)
        writer.write_collection_of_primitive_values("termsToHighlight", self.terms_to_highlight)
        writer.write_additional_data_value(self.additional_data)
    

