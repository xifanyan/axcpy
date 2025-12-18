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
    from ......models.fields_result import FieldsResult
    from .item.with_field_item_request_builder import WithFieldItemRequestBuilder

class FiltersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /projects/{projectId}/collections/{collectionId}/filters
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FiltersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/projects/{projectId}/collections/{collectionId}/filters", path_parameters)
    
    def by_field_id(self,field_id: str) -> WithFieldItemRequestBuilder:
        """
        Gets an item from the SearchWebApiSDK.projects.item.collections.item.filters.item collection
        param field_id: Folder field (taxonomy, smart filter) for which resources should be retrieved.
        Returns: WithFieldItemRequestBuilder
        """
        if field_id is None:
            raise TypeError("field_id cannot be null.")
        from .item.with_field_item_request_builder import WithFieldItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["fieldId"] = field_id
        return WithFieldItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[bytes]:
        """
        Returns the list of available folder fields (taxonomies, smart filters) and their properties. Folder fields can be used for filtering a search result by restricting to documents having a given folder in a given folder field. Also values can be accumulated across documents having a certain folder in a given folder field.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.fields_result import FieldsResult

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": FieldsResult,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the list of available folder fields (taxonomies, smart filters) and their properties. Folder fields can be used for filtering a search result by restricting to documents having a given folder in a given folder field. Also values can be accumulated across documents having a certain folder in a given folder field.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> FiltersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FiltersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FiltersRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class FiltersRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

