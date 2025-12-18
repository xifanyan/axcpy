from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .deletion_mode import DeletionMode
    from .record_data import RecordData
    from .search_request import SearchRequest

@dataclass
class InsertRemoveRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    from .deletion_mode import DeletionMode

    # Allows to select how deletions should be applied. The mode 'delete' deletes a category (no undo). The mode 'softdelete' merely marks the category for deletion ('hidden') such that it is gone for all practical purposes (except background maintenance tasks).
    deletion_mode: Optional[DeletionMode] = DeletionMode("delete")
    # 0-n records to be created.
    new_records: Optional[list[RecordData]] = None
    # 0-n record ids which are to be deleted. Specifying a record as both 'delete' and 'new' has re-insert semantics. The specified ids have to be in one of the following formats: 1. they can resemble the 'id' as returned by the records endpoint (aka url-safe string). 2. they can be a folder id (only applicable if you are connected against a folder collection). 3. If connected with a folder collection, you can optionally specify folderId::VALUE here where VALUE is a folder id.
    records_to_delete: Optional[list[str]] = None
    # A query.
    records_to_delete_by_query: Optional[SearchRequest] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InsertRemoveRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InsertRemoveRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InsertRemoveRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .deletion_mode import DeletionMode
        from .record_data import RecordData
        from .search_request import SearchRequest

        from .deletion_mode import DeletionMode
        from .record_data import RecordData
        from .search_request import SearchRequest

        fields: dict[str, Callable[[Any], None]] = {
            "deletionMode": lambda n : setattr(self, 'deletion_mode', n.get_enum_value(DeletionMode)),
            "newRecords": lambda n : setattr(self, 'new_records', n.get_collection_of_object_values(RecordData)),
            "recordsToDelete": lambda n : setattr(self, 'records_to_delete', n.get_collection_of_primitive_values(str)),
            "recordsToDeleteByQuery": lambda n : setattr(self, 'records_to_delete_by_query', n.get_object_value(SearchRequest)),
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
        writer.write_enum_value("deletionMode", self.deletion_mode)
        writer.write_collection_of_object_values("newRecords", self.new_records)
        writer.write_collection_of_primitive_values("recordsToDelete", self.records_to_delete)
        writer.write_object_value("recordsToDeleteByQuery", self.records_to_delete_by_query)
        writer.write_additional_data_value(self.additional_data)
    

