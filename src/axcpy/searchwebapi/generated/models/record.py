from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.api_error import APIError
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .field import Field
    from .folder_set import FolderSet

@dataclass
class Record(APIError, AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Content or part of the content of the record (document). This can be 'null'.
    body: Optional[str] = None
    # A list of field-value pairs, if any requested.
    fields: Optional[list[Field]] = None
    # A list of sets of folder-value pairs (also including the folder display name), if any requested.
    folder_sets: Optional[list[FolderSet]] = None
    # The ID of the record (document).
    id: Optional[str] = None
    # Shows the page number of the current result. Only populated if body for single documents has been retrieved (not in the result listing of a search).
    page: Optional[int] = None
    # Shows the number of pages in the document. Only populated if body for single documents has been retrieved (not in the result listing of a search).
    page_count: Optional[int] = None
    # The list position of the record in the list of found records. The first record has rank 1.
    rank: Optional[int] = None
    # Calculated relevance (between 0 and 1) corresponding to how well content and properties match the search expression.
    relevance: Optional[float] = None
    # A human-readable unique field. This field should only be used for logging or investigation, there is no guarantee about the value.
    unique_field: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Record:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Record
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Record()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .field import Field
        from .folder_set import FolderSet

        from .field import Field
        from .folder_set import FolderSet

        fields: dict[str, Callable[[Any], None]] = {
            "body": lambda n : setattr(self, 'body', n.get_str_value()),
            "fields": lambda n : setattr(self, 'fields', n.get_collection_of_object_values(Field)),
            "folderSets": lambda n : setattr(self, 'folder_sets', n.get_collection_of_object_values(FolderSet)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "page": lambda n : setattr(self, 'page', n.get_int_value()),
            "pageCount": lambda n : setattr(self, 'page_count', n.get_int_value()),
            "rank": lambda n : setattr(self, 'rank', n.get_int_value()),
            "relevance": lambda n : setattr(self, 'relevance', n.get_float_value()),
            "uniqueField": lambda n : setattr(self, 'unique_field', n.get_str_value()),
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
        writer.write_str_value("body", self.body)
        writer.write_collection_of_object_values("fields", self.fields)
        writer.write_collection_of_object_values("folderSets", self.folder_sets)
        writer.write_str_value("id", self.id)
        writer.write_int_value("page", self.page)
        writer.write_int_value("pageCount", self.page_count)
        writer.write_int_value("rank", self.rank)
        writer.write_float_value("relevance", self.relevance)
        writer.write_str_value("uniqueField", self.unique_field)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def primary_message(self) -> Optional[str]:
        """
        The primary error message.
        """
        return super().message

