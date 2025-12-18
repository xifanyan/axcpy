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
    from .......models.start_transaction_request import StartTransactionRequest
    from .......models.start_transaction_result import StartTransactionResult
    from .item.with_indexing_buffer_item_request_builder import WithIndexingBufferItemRequestBuilder

class BulkInsertRemoveTransactionRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /projects/{projectId}/collections/{collectionId}/records/bulkInsertRemoveTransaction
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BulkInsertRemoveTransactionRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/projects/{projectId}/collections/{collectionId}/records/bulkInsertRemoveTransaction", path_parameters)
    
    def by_indexing_buffer_id(self,indexing_buffer_id: str) -> WithIndexingBufferItemRequestBuilder:
        """
        Gets an item from the SearchWebApiSDK.projects.item.collections.item.records.bulkInsertRemoveTransaction.item collection
        param indexing_buffer_id: A transaction ID name. Must resemble a value returned in a StartTransactionResult.
        Returns: WithIndexingBufferItemRequestBuilder
        """
        if indexing_buffer_id is None:
            raise TypeError("indexing_buffer_id cannot be null.")
        from .item.with_indexing_buffer_item_request_builder import WithIndexingBufferItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["indexingBufferId"] = indexing_buffer_id
        return WithIndexingBufferItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: StartTransactionRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[bytes]:
        """
        Prepare a server-sided buffer for an upcoming insert/remove transaction. The transaction must be finished by the user.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .......models.start_transaction_result import StartTransactionResult

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": StartTransactionResult,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_post_request_information(self,body: StartTransactionRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Prepare a server-sided buffer for an upcoming insert/remove transaction. The transaction must be finished by the user.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> BulkInsertRemoveTransactionRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: BulkInsertRemoveTransactionRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return BulkInsertRemoveTransactionRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class BulkInsertRemoveTransactionRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

