from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .buffer.buffer_request_builder import BufferRequestBuilder
    from .end.end_request_builder import EndRequestBuilder

class WithIndexingBufferItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /projects/{projectId}/collections/{collectionId}/records/bulkInsertRemoveTransaction/{indexingBufferId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithIndexingBufferItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/projects/{projectId}/collections/{collectionId}/records/bulkInsertRemoveTransaction/{indexingBufferId}", path_parameters)
    
    @property
    def buffer(self) -> BufferRequestBuilder:
        """
        The buffer property
        """
        from .buffer.buffer_request_builder import BufferRequestBuilder

        return BufferRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def end(self) -> EndRequestBuilder:
        """
        The end property
        """
        from .end.end_request_builder import EndRequestBuilder

        return EndRequestBuilder(self.request_adapter, self.path_parameters)
    

