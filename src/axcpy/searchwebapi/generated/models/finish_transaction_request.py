from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class FinishTransactionRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The size of documents which has been analyzed
    analyzed_size_gb: Optional[int] = None
    # The number of documents
    number_documents: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FinishTransactionRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FinishTransactionRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FinishTransactionRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "analyzedSizeGb": lambda n : setattr(self, 'analyzed_size_gb', n.get_int_value()),
            "numberDocuments": lambda n : setattr(self, 'number_documents', n.get_int_value()),
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
        writer.write_int_value("analyzedSizeGb", self.analyzed_size_gb)
        writer.write_int_value("numberDocuments", self.number_documents)
        writer.write_additional_data_value(self.additional_data)
    

