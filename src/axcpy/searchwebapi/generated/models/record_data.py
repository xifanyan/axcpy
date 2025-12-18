from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .field_data import FieldData

@dataclass
class RecordData(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The fieldData property
    field_data: Optional[list[FieldData]] = None
    # A unique identifier for the record. It resembles the value of 'uniqueField' when fetching records and must be provided at insertion time.
    unique_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RecordData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecordData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RecordData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .field_data import FieldData

        from .field_data import FieldData

        fields: dict[str, Callable[[Any], None]] = {
            "fieldData": lambda n : setattr(self, 'field_data', n.get_collection_of_object_values(FieldData)),
            "uniqueId": lambda n : setattr(self, 'unique_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("fieldData", self.field_data)
        writer.write_str_value("uniqueId", self.unique_id)
        writer.write_additional_data_value(self.additional_data)
    

