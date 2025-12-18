from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .field_value_object import Field_valueObject

@dataclass
class Field(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The field ID.
    id: Optional[str] = None
    # The value for the given document in the given field or null if there is no such value. Date values are formatted as string according to ISO_8601, i.e. in the date format 'yyyy-MM-dd'T'HH:mm:ss.SSSXXX' in UTC timezone. Folder ids are formatted as comma-separated list without any escape characters (see valueObject for a type-safe access).
    value: Optional[str] = None
    # This is either null or redundant: it provides the very same data as in 'value', but as typed object. This property is populated if and only if the result is not a plain string. Examples where this property is populated and contains useful values are: integer fields, date fields (which return the number of milliseconds since January 1, 1970, 00:00:00 GMT, formatted as string) or an array of folder values (if they have been requested as 'fields'). Note that 'value' will always be populated with a string-representation of the value. Use 'valueObject' in order to have type-safe access (especially if you retrieved a list of folder ids).
    value_object: Optional[Field_valueObject] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Field:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Field
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Field()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .field_value_object import Field_valueObject

        from .field_value_object import Field_valueObject

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
            "valueObject": lambda n : setattr(self, 'value_object', n.get_object_value(Field_valueObject)),
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
        writer.write_str_value("id", self.id)
        writer.write_str_value("value", self.value)
        writer.write_object_value("valueObject", self.value_object)
        writer.write_additional_data_value(self.additional_data)
    

