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

if TYPE_CHECKING:
    from ......models.cached_search_description import CachedSearchDescription

class CachedSearchesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /projects/{projectId}/collections/{collectionId}/cachedSearches
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CachedSearchesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/projects/{projectId}/collections/{collectionId}/cachedSearches{?creationTraceIds*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[CachedSearchesRequestBuilderDeleteQueryParameters]] = None) -> Optional[bytes]:
        """
        Drops cached searches.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.cached_search_description import CachedSearchDescription

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": CachedSearchDescription,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[bytes]:
        """
        Returns a list of cached searches. Search web api automatically caches search results such that paging or following actions are fast without re-executing the same query. This method allows to inspect the available caches for the current session and for the selected project / collection. The result value resembles a trace id for each cached search; more precisely: the trace id which created the cached search result. Trace ids can be set using the request header SWA-MDC-TOKEN; they typically serve as log file analysis utility - in case of searches, they also identify the search initiator context.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.cached_search_description import CachedSearchDescription

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": CachedSearchDescription,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[CachedSearchesRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        Drops cached searches.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of cached searches. Search web api automatically caches search results such that paging or following actions are fast without re-executing the same query. This method allows to inspect the available caches for the current session and for the selected project / collection. The result value resembles a trace id for each cached search; more precisely: the trace id which created the cached search result. Trace ids can be set using the request header SWA-MDC-TOKEN; they typically serve as log file analysis utility - in case of searches, they also identify the search initiator context.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> CachedSearchesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CachedSearchesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CachedSearchesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CachedSearchesRequestBuilderDeleteQueryParameters():
        """
        Drops cached searches.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "creation_trace_ids":
                return "creationTraceIds"
            return original_name
        
        # A comma-separated list of creation trace ids. Only these associated caches will be cleared. Omitting this value will close all available searches for the specified collection. Such values can be retrieved using the GET endpoint.
        creation_trace_ids: Optional[str] = None

    
    @dataclass
    class CachedSearchesRequestBuilderDeleteRequestConfiguration(RequestConfiguration[CachedSearchesRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CachedSearchesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

