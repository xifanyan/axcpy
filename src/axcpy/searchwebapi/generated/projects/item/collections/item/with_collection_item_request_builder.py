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
    from .....models.collection_resources_result import CollectionResourcesResult
    from .binary.binary_request_builder import BinaryRequestBuilder
    from .cached_searches.cached_searches_request_builder import CachedSearchesRequestBuilder
    from .changes.changes_request_builder import ChangesRequestBuilder
    from .fields.fields_request_builder import FieldsRequestBuilder
    from .filters.filters_request_builder import FiltersRequestBuilder
    from .measures.measures_request_builder import MeasuresRequestBuilder
    from .records.records_request_builder import RecordsRequestBuilder
    from .search.search_request_builder import SearchRequestBuilder
    from .search_token.search_token_request_builder import SearchTokenRequestBuilder

class WithCollectionItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /projects/{projectId}/collections/{collectionId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithCollectionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/projects/{projectId}/collections/{collectionId}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[bytes]:
        """
        Discover available collection-level resources. Examples are 'records' which describes the actual searchable objects in the domain, 'filters' which describes the folder fields (taxonomies, smart filters), and 'fields' which describs the available fields.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.collection_resources_result import CollectionResourcesResult

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": CollectionResourcesResult,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Discover available collection-level resources. Examples are 'records' which describes the actual searchable objects in the domain, 'filters' which describes the folder fields (taxonomies, smart filters), and 'fields' which describs the available fields.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithCollectionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithCollectionItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithCollectionItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def binary(self) -> BinaryRequestBuilder:
        """
        The binary property
        """
        from .binary.binary_request_builder import BinaryRequestBuilder

        return BinaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cached_searches(self) -> CachedSearchesRequestBuilder:
        """
        The cachedSearches property
        """
        from .cached_searches.cached_searches_request_builder import CachedSearchesRequestBuilder

        return CachedSearchesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def changes(self) -> ChangesRequestBuilder:
        """
        The changes property
        """
        from .changes.changes_request_builder import ChangesRequestBuilder

        return ChangesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fields(self) -> FieldsRequestBuilder:
        """
        The fields property
        """
        from .fields.fields_request_builder import FieldsRequestBuilder

        return FieldsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def filters(self) -> FiltersRequestBuilder:
        """
        The filters property
        """
        from .filters.filters_request_builder import FiltersRequestBuilder

        return FiltersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def measures(self) -> MeasuresRequestBuilder:
        """
        The measures property
        """
        from .measures.measures_request_builder import MeasuresRequestBuilder

        return MeasuresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def records(self) -> RecordsRequestBuilder:
        """
        The records property
        """
        from .records.records_request_builder import RecordsRequestBuilder

        return RecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def search(self) -> SearchRequestBuilder:
        """
        The search property
        """
        from .search.search_request_builder import SearchRequestBuilder

        return SearchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def search_token(self) -> SearchTokenRequestBuilder:
        """
        The searchToken property
        """
        from .search_token.search_token_request_builder import SearchTokenRequestBuilder

        return SearchTokenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithCollectionItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

