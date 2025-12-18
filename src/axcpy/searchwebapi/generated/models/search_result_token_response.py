from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.api_error import APIError
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .status_object import StatusObject

@dataclass
class SearchResultTokenResponse(APIError, AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The date at which this token expires and will be deleted. It has to be touched or used before this timestamp in order to keep it alive. The format is 'yyyy-MM-dd'T'HH:mm:ss.SSSXXX' in UTC timezone. Note that a search token is bound to the user session as well: it will be closed if the user session times out or if the users logs out.
    eol: Optional[str] = None
    # The number of results found by the search.
    number_results: Optional[int] = None
    # The status of the response.
    status: Optional[StatusObject] = None
    # The search result token.
    token: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SearchResultTokenResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SearchResultTokenResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SearchResultTokenResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .status_object import StatusObject

        from .status_object import StatusObject

        fields: dict[str, Callable[[Any], None]] = {
            "eol": lambda n : setattr(self, 'eol', n.get_str_value()),
            "numberResults": lambda n : setattr(self, 'number_results', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_object_value(StatusObject)),
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
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
        writer.write_str_value("eol", self.eol)
        writer.write_int_value("numberResults", self.number_results)
        writer.write_object_value("status", self.status)
        writer.write_str_value("token", self.token)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def primary_message(self) -> Optional[str]:
        """
        The primary error message.
        """
        return super().message

