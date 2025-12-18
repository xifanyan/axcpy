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
    from ..models.projects_result import ProjectsResult
    from .item.with_project_item_request_builder import WithProjectItemRequestBuilder

class ProjectsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /projects
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ProjectsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/projects", path_parameters)
    
    def by_project_id(self,project_id: str) -> WithProjectItemRequestBuilder:
        """
        Gets an item from the SearchWebApiSDK.projects.item collection
        param project_id: Identifies the MindServer to connect to. It can be a fully qualified MindServer identifier like singleMindServer.ABCD or mergingMeta.DEF . The engine type prefix (like 'singleMindServer.') can omitted in which case the API will automatically test engine prefixes until it finds a matching MindServer. It tests the following engine type prefixes (in this order): 'metaMindServer.', 'mergingMeta.', 'singleMindServer.' . If in doubt, the correct project to connect to should be the ID of the topmost engine, the one directly below the corresponding application.
        Returns: WithProjectItemRequestBuilder
        """
        if project_id is None:
            raise TypeError("project_id cannot be null.")
        from .item.with_project_item_request_builder import WithProjectItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["projectId"] = project_id
        return WithProjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[bytes]:
        """
        Discover available projects, i.e. all projects that are present in an installation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.projects_result import ProjectsResult

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ProjectsResult,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Discover available projects, i.e. all projects that are present in an installation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ProjectsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ProjectsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ProjectsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ProjectsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

