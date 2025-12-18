from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DimensionRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The field defining the dimension.
    field: Optional[str] = None
    # Only for folder fields: provide an order criterion for the results. The syntax is the same as 'order' for the records endpoint, i.e. <fieldName> or <filedName>:asc or <fieldName>:desc. In this context, <fieldName> is any folder property. In addition, <fieldName> can be one of the special names 'count', 'relevance', or 'name'. Here, 'name' is the category display name.
    folder_order: Optional[str] = None
    # Define which is the first element to return (first is 0). The system will return the next 'pageSize' following items. Default is to return all matching members. You cannot specify both 'page' and 'offset'.
    offset: Optional[int] = None
    # Define which page to retrieve (counting starts at 1). Default is to return all matching members. You cannot specify both 'page' and 'offset'.
    page: Optional[int] = None
    # Defines the page size. Only used if 'page' or 'offset' is set.
    page_size: Optional[int] = None
    # Only for folder fields: optional query to constrain the folders returned. Examples are rm_folder_id=uniquevalue or rm_display_name=displayname
    restrict_folders_by_query: Optional[str] = None
    # A list of values. For folder fields, the values are folder ids. For fields of numeric or date type, each value can have one of two forms: the inclusive variant '[start,end]' or the exclusive variant '[start,end[' . For DATE fields, both start and end are either milli seconds since 1970 in UTC time followed by the suffix 'L' or a date format in one of the formats 'yyyy-MM-dd'T'HH:mm:ss.SSSXXX', 'yyyy-MM-dd'T'HH:mm:ss.SSS', 'yyyy-MM-dd'T'HH:mm:ss', 'yyyy-MM-dd'T'HH:mm', 'yyyy-MM-dd'T'HH', 'yyyy-MM-dd', 'yyyy-MM', 'yyyy' . Example for a numeric field: [4,5] which counts documents having either value 4 and the value 5. Another example for a numeric field: [4,5[ counts documents having value 4 but not 5. Example for a date field: [2000, 2000-10-01] counts documents with value between 2000-01-01 and 200-10-01 23:59:59.999 (inclusive).    
    restrict_values_by_list: Optional[list[str]] = None
    # Defines if members with count=0 should be returned. Default is false.
    return_empty_members: Optional[bool] = None
    # A comma-separated list of field names. It is only used for folder fields and allows to fetch properties of the returned folders (like rm_display_name).
    returned_fields: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DimensionRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DimensionRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DimensionRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "field": lambda n : setattr(self, 'field', n.get_str_value()),
            "folderOrder": lambda n : setattr(self, 'folder_order', n.get_str_value()),
            "offset": lambda n : setattr(self, 'offset', n.get_int_value()),
            "page": lambda n : setattr(self, 'page', n.get_int_value()),
            "pageSize": lambda n : setattr(self, 'page_size', n.get_int_value()),
            "restrictFoldersByQuery": lambda n : setattr(self, 'restrict_folders_by_query', n.get_str_value()),
            "restrictValuesByList": lambda n : setattr(self, 'restrict_values_by_list', n.get_collection_of_primitive_values(str)),
            "returnEmptyMembers": lambda n : setattr(self, 'return_empty_members', n.get_bool_value()),
            "returnedFields": lambda n : setattr(self, 'returned_fields', n.get_str_value()),
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
        writer.write_str_value("field", self.field)
        writer.write_str_value("folderOrder", self.folder_order)
        writer.write_int_value("offset", self.offset)
        writer.write_int_value("page", self.page)
        writer.write_int_value("pageSize", self.page_size)
        writer.write_str_value("restrictFoldersByQuery", self.restrict_folders_by_query)
        writer.write_collection_of_primitive_values("restrictValuesByList", self.restrict_values_by_list)
        writer.write_bool_value("returnEmptyMembers", self.return_empty_members)
        writer.write_str_value("returnedFields", self.returned_fields)
        writer.write_additional_data_value(self.additional_data)
    

