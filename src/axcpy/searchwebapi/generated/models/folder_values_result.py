from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.api_error import APIError
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .folder_record import FolderRecord
    from .status_object import StatusObject

@dataclass
class FolderValuesResult(APIError, AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The number of results found by the search. With paging this may be more than available in the result. NOTE: this number will be 2147483647 (max int) if paging through folder results of a merging meta engine. This is due to a performance optimization when merging results. In such a case, you will need to page forward until the system has received all results (in which case the final page will contain the correct numberResults).
    number_results: Optional[int] = None
    # The list of folders (categories).
    results: Optional[list[FolderRecord]] = None
    # The status of the response.
    status: Optional[StatusObject] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FolderValuesResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FolderValuesResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FolderValuesResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .folder_record import FolderRecord
        from .status_object import StatusObject

        from .folder_record import FolderRecord
        from .status_object import StatusObject

        fields: dict[str, Callable[[Any], None]] = {
            "numberResults": lambda n : setattr(self, 'number_results', n.get_int_value()),
            "results": lambda n : setattr(self, 'results', n.get_collection_of_object_values(FolderRecord)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(StatusObject)),
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
        writer.write_int_value("numberResults", self.number_results)
        writer.write_collection_of_object_values("results", self.results)
        writer.write_object_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def primary_message(self) -> Optional[str]:
        """
        The primary error message.
        """
        return super().message

