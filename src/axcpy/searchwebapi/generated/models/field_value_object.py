from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Field_valueObject(AdditionalDataHolder, Parsable):
    """
    This is either null or redundant: it provides the very same data as in 'value', but as typed object. This property is populated if and only if the result is not a plain string. Examples where this property is populated and contains useful values are: integer fields, date fields (which return the number of milliseconds since January 1, 1970, 00:00:00 GMT, formatted as string) or an array of folder values (if they have been requested as 'fields'). Note that 'value' will always be populated with a string-representation of the value. Use 'valueObject' in order to have type-safe access (especially if you retrieved a list of folder ids).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Field_valueObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Field_valueObject
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Field_valueObject()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
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
        writer.write_additional_data_value(self.additional_data)
    

