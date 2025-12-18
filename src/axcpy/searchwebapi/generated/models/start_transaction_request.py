from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class StartTransactionRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The name of the data source. It is used to track the transaction.
    data_source_id: Optional[str] = None
    # An optional buffer id.
    indexing_buffer_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StartTransactionRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StartTransactionRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StartTransactionRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "dataSourceId": lambda n : setattr(self, 'data_source_id', n.get_str_value()),
            "indexingBufferId": lambda n : setattr(self, 'indexing_buffer_id', n.get_str_value()),
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
        writer.write_str_value("dataSourceId", self.data_source_id)
        writer.write_str_value("indexingBufferId", self.indexing_buffer_id)
        writer.write_additional_data_value(self.additional_data)
    

