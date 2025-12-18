from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .collection_resource_id import CollectionResource_id
    from .query_parameter import QueryParameter

@dataclass
class CollectionResource(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # This provides a description of available query parameters ('...&<name>=<value>&...') for the resource (e.g. query expressions, paging requests, requested fields)
    available_query_parameters: Optional[list[QueryParameter]] = None
    # A description of the resource.
    description: Optional[str] = None
    # The ID of the resource. Typical resources available will be 'records' which provides access to the actual searchable objects, 'filters' (folder fields, taxonomies, smart filters) which can be used for filtering, etc.
    id: Optional[CollectionResource_id] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CollectionResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CollectionResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CollectionResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .collection_resource_id import CollectionResource_id
        from .query_parameter import QueryParameter

        from .collection_resource_id import CollectionResource_id
        from .query_parameter import QueryParameter

        fields: dict[str, Callable[[Any], None]] = {
            "availableQueryParameters": lambda n : setattr(self, 'available_query_parameters', n.get_collection_of_object_values(QueryParameter)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_enum_value(CollectionResource_id)),
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
    

