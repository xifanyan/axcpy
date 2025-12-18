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
    from ....models.collections_result import CollectionsResult
    from .item.with_collection_item_request_builder import WithCollectionItemRequestBuilder

class CollectionsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /projects/{projectId}/collections
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CollectionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/projects/{projectId}/collections", path_parameters)
    
    def by_collection_id(self,collection_id: str) -> WithCollectionItemRequestBuilder:
        """
        Gets an item from the SearchWebApiSDK.projects.item.collections.item collection
        param collection_id: Defines the collection within the specified project. For a Decisiv Search project this corresponds to the tabs in the UI, eg. 'documents', 'people', 'matter'. In this case, valid choices are configured in the column 'Identifier' in table 'Meta engine configuration: Meta engine sources: Server definitions'. In order to connect to single engines and merging meta engines, you have to specify the string 'default'. If you want to access (properties of) a folder collection (=taxonomy), set collectionId to the folder collection's name. If you need to combine both a meta engine server identifier and a folder collection name, separate them by means of '::'.  Note that single engines provide access to any configured binary storages (SingleMindServer configuraration: Native files: storage). To this end, use collectionId=rm_storage:FILETYPE where FILETYPE is the value configured as 'Storage file type' (like 'Native files', 'Image files').
        Returns: WithCollectionItemRequestBuilder
        """
        if collection_id is None:
            raise TypeError("collection_id cannot be null.")
        from .item.with_collection_item_request_builder import WithCollectionItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["collectionId"] = collection_id
        return WithCollectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[bytes]:
        """
        Decisiv Search offers multiple domains (e.g. Documents, Matter, People, etc) belonging to a project. With this operation, the set of available domains is returned, e.g. for display as tabs in the UI. For any project that is not a non-merging meta-engine, the collection 'default' will be returned as the only collection.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.collections_result import CollectionsResult

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": CollectionsResult,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Decisiv Search offers multiple domains (e.g. Documents, Matter, People, etc) belonging to a project. With this operation, the set of available domains is returned, e.g. for display as tabs in the UI. For any project that is not a non-merging meta-engine, the collection 'default' will be returned as the only collection.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> CollectionsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CollectionsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CollectionsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CollectionsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

