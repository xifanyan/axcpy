from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .measure_dimension_member import MeasureDimensionMember

@dataclass
class MeasureDimensionResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Documents with any value in this dimension. Negative if this value is unsupported.
    documents_with_any_value: Optional[int] = None
    # Documents without any value in this dimension. Negative if this value is unsupported.
    documents_with_no_value: Optional[int] = None
    # the associated field name
    field_name: Optional[str] = None
    # The dimension members requested by the request.
    members: Optional[list[MeasureDimensionMember]] = None
    # The size of this dimension. For one-dimensional counts, this resembles all available results and can be larger than the elements in 'members' (due to paging). For two-dimensional counts, this value is the same as the size of 'members'.
    size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MeasureDimensionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MeasureDimensionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MeasureDimensionResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .measure_dimension_member import MeasureDimensionMember

        from .measure_dimension_member import MeasureDimensionMember

        fields: dict[str, Callable[[Any], None]] = {
            "documentsWithAnyValue": lambda n : setattr(self, 'documents_with_any_value', n.get_int_value()),
            "documentsWithNoValue": lambda n : setattr(self, 'documents_with_no_value', n.get_int_value()),
            "fieldName": lambda n : setattr(self, 'field_name', n.get_str_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(MeasureDimensionMember)),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
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
        writer.write_int_value("documentsWithAnyValue", self.documents_with_any_value)
        writer.write_int_value("documentsWithNoValue", self.documents_with_no_value)
        writer.write_str_value("fieldName", self.field_name)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_int_value("size", self.size)
        writer.write_additional_data_value(self.additional_data)
    

