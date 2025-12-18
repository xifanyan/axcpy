from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

class ContentRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /projects/{projectId}/collections/{collectionId}/binary/{recordId}/content
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ContentRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/projects/{projectId}/collections/{collectionId}/binary/{recordId}/content{?field*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ContentRequestBuilderGetQueryParameters]] = None) -> Optional[bytes]:
        """
        Returns one binary which matches the specified search criteria. The field containing the binary data must be specified. If more than one record matches the query, the binary of the record with index 'selectedIndex' is returned. You can inspect the ordering and the number of hits by sending the same query to the records endpoint. The returned filename always starts with the value which is returned when fetching the field via the records endpoint. It ends with the file extension as available to the storage. If the storage knows some original file name, the original file name becomes an infix of sorts ___fileName just before the file extension. The mindserver storage can be accessed by using the singleMindServer identifier as projectId and the collectionId should be 'rm_storage:Image files' or 'rm_storage:Native files' . The precise value after the colon resembles the storage element type in the mindserver configuration.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ContentRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns one binary which matches the specified search criteria. The field containing the binary data must be specified. If more than one record matches the query, the binary of the record with index 'selectedIndex' is returned. You can inspect the ordering and the number of hits by sending the same query to the records endpoint. The returned filename always starts with the value which is returned when fetching the field via the records endpoint. It ends with the file extension as available to the storage. If the storage knows some original file name, the original file name becomes an infix of sorts ___fileName just before the file extension. The mindserver storage can be accessed by using the singleMindServer identifier as projectId and the collectionId should be 'rm_storage:Image files' or 'rm_storage:Native files' . The precise value after the colon resembles the storage element type in the mindserver configuration.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def with_url(self,raw_url: str) -> ContentRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ContentRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ContentRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ContentRequestBuilderGetQueryParameters():
        """
        Returns one binary which matches the specified search criteria. The field containing the binary data must be specified. If more than one record matches the query, the binary of the record with index 'selectedIndex' is returned. You can inspect the ordering and the number of hits by sending the same query to the records endpoint. The returned filename always starts with the value which is returned when fetching the field via the records endpoint. It ends with the file extension as available to the storage. If the storage knows some original file name, the original file name becomes an infix of sorts ___fileName just before the file extension. The mindserver storage can be accessed by using the singleMindServer identifier as projectId and the collectionId should be 'rm_storage:Image files' or 'rm_storage:Native files' . The precise value after the colon resembles the storage element type in the mindserver configuration.
        """
        # A single field name storing binary data.
        field: Optional[str] = None

    
    @dataclass
    class ContentRequestBuilderGetRequestConfiguration(RequestConfiguration[ContentRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

