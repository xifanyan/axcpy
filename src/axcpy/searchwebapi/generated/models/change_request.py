from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .change_request_type import ChangeRequest_type

@dataclass
class ChangeRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The field to change.
    field: Optional[str] = None
    # Zero, one, or more folder ids. This value is evaluated for the following choices of 'type': 'ADD_FOLDERS', 'SET_FOLDERS', 'REMOVE_FOLDERS', 'REMOVE_FOLDERS_AND_BRANCH', 'SET_PARENT'. A folder id can be one of two possible formats: either it is the (unencoded) folder id as returned by other software components or it is the 'id' returned by the records endpoint when searching in the folder collection.
    folder_ids: Optional[list[str]] = None
    # A string text. This value is evaluated for the following choices of 'type': 'SET_TEXT', 'APPEND_TEXT'. The type 'SET_TEXT' without a 'text' clears the field. Note that changes in a numeric field also use this parameter. If 'pages' is a configured numeric type, you can use field=pages, text='42', type='SET_TEXT'
    text: Optional[str] = None
    # A sequence of strings. This value is evaluated for the following choices of 'type': 'SET_TEXTS'.
    texts: Optional[list[str]] = None
    # The type of change (case sensitive!). The semantics is as follows: * ADD_FOLDERS tags all documents in scope into the folders specified in folderIds. * SET_FOLDERS ensures that all documents in scope have exactly the folders specified in folderIds. * REMOVE_FOLDERS untags all documents in scope from the folders specified in folderIds. * REMOVE_FOLDERS_AND_BRANCH is similiar to removeFolders. However, for a hierarchical folder collection with enabled 'full hierarchy', parent associations will also be removed unless another child references the documents. * MAKE_ROOT requires that the identified collection is a hierarchical folder collection (=taxonomy), and that field is set to 'rm_prop_parent'. In this case, it ensures that the documents in scope (which are folder ids) will become top-level folders (example: projectId='singleMindServer.project', collectionId='my_workspace', field='rm_prop_parent', type='MAKE_ROOT', recordId='unencoded category id'). * SET_PARENT has the same requirements as MAKE_ROOT, but it also expects exactly one argument in 'folderIds' (the new parent). It changes the hierarchy of the specified categories. * SET_TEXT changes the content to the value specified in 'text' in the specified 'field' for all documents in scope. This is also possible for numeric fields or date fields. Note that date fields can be changed to a string resembling the milli seconds since 1970 suffixed with 'L' or a date pattern which must be configured in the singleMindServer configuration. * APPEND_TEXT is similar to SET_TEXT, but it appends to the existing text (if any). This is impossible for numeric or date fields. * SET_TEXTS can be used to modify folder properties by assigning a list of strings. It expects the value in 'texts'. Note that changes for content fields necessarily require to use content-type multipart/form-data combined with type=SET_TEXT and value an integer index referencing the associated binary XML stream.
    type: Optional[ChangeRequest_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChangeRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChangeRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChangeRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .change_request_type import ChangeRequest_type

        from .change_request_type import ChangeRequest_type

        fields: dict[str, Callable[[Any], None]] = {
            "field": lambda n : setattr(self, 'field', n.get_str_value()),
            "folderIds": lambda n : setattr(self, 'folder_ids', n.get_collection_of_primitive_values(str)),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "texts": lambda n : setattr(self, 'texts', n.get_collection_of_primitive_values(str)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(ChangeRequest_type)),
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
        writer.write_collection_of_primitive_values("folderIds", self.folder_ids)
        writer.write_str_value("text", self.text)
        writer.write_collection_of_primitive_values("texts", self.texts)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

