from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .folder_field_resource_id import FolderFieldResource_id
    from .query_parameter import QueryParameter

@dataclass
class FolderFieldResource(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # This provides a description of available query parameters ('...&<name>=<value>&...') for the resource.
    available_query_parameters: Optional[list[QueryParameter]] = None
    # A description of the resource.
    description: Optional[str] = None
    # The ID of the resource.
    id: Optional[FolderFieldResource_id] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FolderFieldResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FolderFieldResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FolderFieldResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .folder_field_resource_id import FolderFieldResource_id
        from .query_parameter import QueryParameter

        from .folder_field_resource_id import FolderFieldResource_id
        from .query_parameter import QueryParameter

        fields: dict[str, Callable[[Any], None]] = {
            "availableQueryParameters": lambda n : setattr(self, 'available_query_parameters', n.get_collection_of_object_values(QueryParameter)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_enum_value(FolderFieldResource_id)),
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
        writer.write_collection_of_object_values("availableQueryParameters", self.available_query_parameters)
        writer.write_str_value("description", self.description)
        writer.write_enum_value("id", self.id)
        writer.write_additional_data_value(self.additional_data)
    

