from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .status_object_backend_status import StatusObject_backendStatus

@dataclass
class StatusObject(AdditionalDataHolder, Parsable):
    """
    The status of the response.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The status of the backend response if there is one. This can be 'null'. The value 'meaningless search terms' indicates that the query consists only of stop words and the-like and results in HTTP code 200. The value 'all search terms unknown' is similiar, but the server does not know any of the provided terms. The special value 'incomplete search results due to pending synchronization' can only occur in early startup phases of the target server (if synchronizes searchable folder properties asynchronously); it results in HTTP code 200. The value 'child collection invalid' means that a sub-engine is currently unreachable and its results are not part of the result and also results in code 200. The value 'unexpandable wildcard' indicates that a wildcard prefix is too short (it results in HTTP code 400). The value 'expanded query too long' indicates that a wildcard expression resulted in too many terms (which is also code 400). The values here are constants and are subject to api stability requirements. The value 'syntax error' indicates a syntax error in a query. The value 'unsupported expression' indicates that the query as such is valid, but cannot be used in the current context.
    backend_status: Optional[StatusObject_backendStatus] = None
    # A short description of the error. This can be 'null'
    error_message: Optional[str] = None
    # The http status of the response. The status depends on 'backendStatus': 'unknown error' is mapped to 'BAD REQUEST' and all others are mapped to 'OK' 
    http_status: Optional[int] = None
    # Will be 'true' if the request was fully successful.
    successful: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StatusObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StatusObject
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StatusObject()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .status_object_backend_status import StatusObject_backendStatus

        from .status_object_backend_status import StatusObject_backendStatus

        fields: dict[str, Callable[[Any], None]] = {
            "backendStatus": lambda n : setattr(self, 'backend_status', n.get_enum_value(StatusObject_backendStatus)),
            "errorMessage": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "httpStatus": lambda n : setattr(self, 'http_status', n.get_int_value()),
            "successful": lambda n : setattr(self, 'successful', n.get_bool_value()),
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
        writer.write_enum_value("backendStatus", self.backend_status)
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_int_value("httpStatus", self.http_status)
        writer.write_bool_value("successful", self.successful)
        writer.write_additional_data_value(self.additional_data)
    

