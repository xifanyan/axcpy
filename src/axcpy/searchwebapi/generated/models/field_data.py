from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class FieldData(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The field name. A common use-case is to create new folders. In this case, rm_display_name is the field for the folder's display name. The field rm_prop_parent is the field defining the new record's parent (it resembles the parent's unique id).
    field_name: Optional[str] = None
    # The value to assign to this field. Only one of 'value' or 'valueList' can be populated. If this field data is of type binary, the 'value' must be the index of the binary artifact, i.e. the index within the multipart upload form.
    value: Optional[str] = None
    # A list of values to assign to this field (for multi-value fields only). Only one of 'value' or 'valueList' can be populated.
    value_list: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FieldData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FieldData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FieldData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "fieldName": lambda n : setattr(self, 'field_name', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
            "valueList": lambda n : setattr(self, 'value_list', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("fieldName", self.field_name)
        writer.write_str_value("value", self.value)
        writer.write_collection_of_primitive_values("valueList", self.value_list)
        writer.write_additional_data_value(self.additional_data)
    

