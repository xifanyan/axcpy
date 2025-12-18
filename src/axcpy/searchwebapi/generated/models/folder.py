from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .field import Field

@dataclass
class Folder(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The display name of the folder. Generally, for most folders, this will be the same as the ID.
    display_name: Optional[str] = None
    # The folder ID.
    id: Optional[str] = None
    # A list of field-value pairs, if any requested.
    properties: Optional[list[Field]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Folder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Folder
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Folder()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .field import Field

        from .field import Field

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_object_values(Field)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_collection_of_object_values("properties", self.properties)
        writer.write_additional_data_value(self.additional_data)
    

