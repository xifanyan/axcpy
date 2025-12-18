from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.api_error import APIError
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .measure_dimension_result import MeasureDimensionResult

@dataclass
class MeasureCube(APIError, AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The dimensions property
    dimensions: Optional[list[MeasureDimensionResult]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MeasureCube:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MeasureCube
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MeasureCube()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .measure_dimension_result import MeasureDimensionResult

        from .measure_dimension_result import MeasureDimensionResult

        fields: dict[str, Callable[[Any], None]] = {
            "dimensions": lambda n : setattr(self, 'dimensions', n.get_collection_of_object_values(MeasureDimensionResult)),
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
        writer.write_collection_of_object_values("dimensions", self.dimensions)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def primary_message(self) -> Optional[str]:
        """
        The primary error message.
        """
        return super().message

