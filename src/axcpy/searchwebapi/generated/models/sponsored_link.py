from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SponsoredLink(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A detailed description of the result.
    description: Optional[str] = None
    # A link into some external system (typically HTTP). Can be null.
    external_link: Optional[str] = None
    # If present, this is the record id associated with the link. It is present if and only if the link resembles a record id in the collection.
    record_id: Optional[str] = None
    # The confidence for this link (between 0 and 1).
    relevance: Optional[float] = None
    # Link text describing the result.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SponsoredLink:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SponsoredLink
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SponsoredLink()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "externalLink": lambda n : setattr(self, 'external_link', n.get_str_value()),
            "recordId": lambda n : setattr(self, 'record_id', n.get_str_value()),
            "relevance": lambda n : setattr(self, 'relevance', n.get_float_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("externalLink", self.external_link)
        writer.write_str_value("recordId", self.record_id)
        writer.write_float_value("relevance", self.relevance)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

