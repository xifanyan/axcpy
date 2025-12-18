from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.api_client_builder import enable_backing_store_for_serialization_writer_factory, register_default_deserializer, register_default_serializer
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.serialization import ParseNodeFactoryRegistry, SerializationWriterFactoryRegistry
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .login.login_request_builder import LoginRequestBuilder
    from .logout.logout_request_builder import LogoutRequestBuilder
    from .projects.projects_request_builder import ProjectsRequestBuilder

class SearchWebApiClient(BaseRequestBuilder):
    """
    The main entry point of the SDK, exposes the configuration and the fluent API.
    """
    def __init__(self,request_adapter: RequestAdapter) -> None:
        """
        Instantiates a new SearchWebApiClient and sets the default values.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if request_adapter is None:
            raise TypeError("request_adapter cannot be null.")
        super().__init__(request_adapter, "{+baseurl}", None)
        if not self.request_adapter.base_url:
            self.request_adapter.base_url = "/searchWebApi"
        self.path_parameters["base_url"] = self.request_adapter.base_url
    
    @property
    def login(self) -> LoginRequestBuilder:
        """
        The login property
        """
        from .login.login_request_builder import LoginRequestBuilder

        return LoginRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def logout(self) -> LogoutRequestBuilder:
        """
        The logout property
        """
        from .logout.logout_request_builder import LogoutRequestBuilder

        return LogoutRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def projects(self) -> ProjectsRequestBuilder:
        """
        The projects property
        """
        from .projects.projects_request_builder import ProjectsRequestBuilder

        return ProjectsRequestBuilder(self.request_adapter, self.path_parameters)
    

