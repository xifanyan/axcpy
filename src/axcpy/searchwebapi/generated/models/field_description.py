from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .field_description_type import FieldDescription_type

@dataclass
class FieldDescription(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A field display name. The value is never null, it falls back to the field id if there is no display name. Display names can be configured in the server configuration.
    display_name: Optional[str] = None
    # The field ID. The ID is the one to be used where the API requires a field ID (or folder field ID, depending on the context).
    id: Optional[str] = None
    # True if the field is a folder field (taxonomy, smart filter). A document can be associated with a folder in such a folder field (or with multiple folders, depending on folder field). A folder field can be used for filtering. Values (e.g. the document count) can be accumulated for folders.
    is_folder_field: Optional[bool] = None
    # True if the field is a multi-value folder collection (taxonomy). A folder collection can be used as filter. Each document can be associated with any number of folders of such a folder collection.
    is_multivalue_folder_collection: Optional[bool] = None
    # True if a folder search on the field can be restricted by prefix.
    is_prefix_searchable: Optional[bool] = None
    # True if the field can be used for sorting.
    is_sortable: Optional[bool] = None
    # The data type of the field: identifier (text), content (text), text, integer, float, date, single-value taxonomy, multi-value taxonomy. The type 'binary' is special in that it accepts and returns binary streams. A main use-case is to access Binary storages configured for a singleMindServer. To this end, use projectId=singleMindServer.NAME and collectionId=rm_storage:Native files for 'Native files' or collectionId=rm_storage:Image files to access image files. The syntax is 'rm_storage:' followed by the value configured as 'Storage file type' in the single mind server configuration. The type 'hierarchy' allows to implement tree structures. Its value is a pointer to the nodes parent id. It is intended to be used in folder collections only. The type 'parameterizedLong' is a multi-value type: a single document can have multiple values in such a field, and each value has a 'parameter' (a string) and a long value. Such fields are supposed to contain 'few' parameters, but many different long values. It is possible to insert/change values of the form '<parameter>.<long>' where '<parameter>' is some string chosen by the API user (example: rank.1234). Assuming such a field is called ranks, the associated values are returned by the records endpoint with fields=ranks.A, ranks.B where 'A' and 'B' are parameters. It is possible to search for documents with such values by means of field bases searches of the form 'ranks.A > 42' or 'ranks.B = 1234'. It is also possible to sort by these values: specify the sort field as 'ranks.A:desc' or 'ranks.B:asc'. Fields of type 'texts' contain a list of strings.
    type: Optional[FieldDescription_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FieldDescription:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FieldDescription
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FieldDescription()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .field_description_type import FieldDescription_type

        from .field_description_type import FieldDescription_type

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isFolderField": lambda n : setattr(self, 'is_folder_field', n.get_bool_value()),
            "isMultivalueFolderCollection": lambda n : setattr(self, 'is_multivalue_folder_collection', n.get_bool_value()),
            "isPrefixSearchable": lambda n : setattr(self, 'is_prefix_searchable', n.get_bool_value()),
            "isSortable": lambda n : setattr(self, 'is_sortable', n.get_bool_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(FieldDescription_type)),
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
        writer.write_bool_value("isFolderField", self.is_folder_field)
        writer.write_bool_value("isMultivalueFolderCollection", self.is_multivalue_folder_collection)
        writer.write_bool_value("isPrefixSearchable", self.is_prefix_searchable)
        writer.write_bool_value("isSortable", self.is_sortable)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

