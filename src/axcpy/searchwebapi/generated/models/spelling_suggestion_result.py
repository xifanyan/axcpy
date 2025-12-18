from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .spelling_suggestion import SpellingSuggestion

@dataclass
class SpellingSuggestionResult(AdditionalDataHolder, Parsable):
    """
    A list of matching spelling suggestions (if configured for the target project). The return value 'null' means that such suggestions have not been requested.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The suggestedWords property
    suggested_words: Optional[list[SpellingSuggestion]] = None
    # The total improvement in percent if all suggestions are applied (between 0 and 1). Note that this number is unrelated to the individual improvements of suggested words as it also takes those words into account for which no suggestion has been returned.
    total_improvement_percent: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SpellingSuggestionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SpellingSuggestionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SpellingSuggestionResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .spelling_suggestion import SpellingSuggestion

        from .spelling_suggestion import SpellingSuggestion

        fields: dict[str, Callable[[Any], None]] = {
            "suggestedWords": lambda n : setattr(self, 'suggested_words', n.get_collection_of_object_values(SpellingSuggestion)),
            "totalImprovementPercent": lambda n : setattr(self, 'total_improvement_percent', n.get_float_value()),
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
        writer.write_collection_of_object_values("suggestedWords", self.suggested_words)
        writer.write_float_value("totalImprovementPercent", self.total_improvement_percent)
        writer.write_additional_data_value(self.additional_data)
    

