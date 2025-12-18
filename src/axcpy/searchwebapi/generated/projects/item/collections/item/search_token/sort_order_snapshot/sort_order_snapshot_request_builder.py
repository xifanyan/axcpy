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
    from .......models.search_result_token import SearchResultToken

class SortOrderSnapshotRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /projects/{projectId}/collections/{collectionId}/searchToken/sortOrderSnapshot
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SortOrderSnapshotRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/projects/{projectId}/collections/{collectionId}/searchToken/sortOrderSnapshot{?topN*}", path_parameters)
    
    async def post(self,body: SearchResultToken, request_configuration: Optional[RequestConfiguration[SortOrderSnapshotRequestBuilderPostQueryParameters]] = None) -> Optional[bytes]:
        """
        Computes a sort order snapshot of the specified search result token and stores it for the token. A 'sort order snapshot' is an atomically created sorted list of documents of the token, sorted according to its ordering. Its purpose is to allow a consistent sort order even if the sort keys are subject to concurrent modification. Keep in mind that mindserver always uses partial sort when requesting a page from a search result, i.e. any modifications to sort keys between two page fetches can and will affect the resulting sort order! The sort order snapshot allows to create a presorted consistent result.  Sort order snapshots can and need to be dereferenced explicitly. The suggested workflow is as follows: <ol> <li>search result token A is based on an ordering which is known to be subject to concurrent modification,</li> <li>you explicitly create a sort order snapshot for token A,</li> <li>search result token B is based on a field-based-search expression including SEARCH_IN_SEARCHRESULT_RANGE referencing token A using a range of your choice. example: SEARCH_IN_SEARCHRESULT_RANGE=A;0;10 . In this context, the results returned from token A use the sort order snapshot.</li> </ol> Thus, a sort order snapshots allows to access the ordering by means of this field-based-search expression. It does _not_ allow to access the scores of A. The sorted list of documents is stored in memory, next to the token's state. It is cleared if the token is closed or the engine gets restarted.  There can be at most one sort order snapshot per token; any previously existing sort order snap shot will be overwritten.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", None)
    
    def to_post_request_information(self,body: SearchResultToken, request_configuration: Optional[RequestConfiguration[SortOrderSnapshotRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Computes a sort order snapshot of the specified search result token and stores it for the token. A 'sort order snapshot' is an atomically created sorted list of documents of the token, sorted according to its ordering. Its purpose is to allow a consistent sort order even if the sort keys are subject to concurrent modification. Keep in mind that mindserver always uses partial sort when requesting a page from a search result, i.e. any modifications to sort keys between two page fetches can and will affect the resulting sort order! The sort order snapshot allows to create a presorted consistent result.  Sort order snapshots can and need to be dereferenced explicitly. The suggested workflow is as follows: <ol> <li>search result token A is based on an ordering which is known to be subject to concurrent modification,</li> <li>you explicitly create a sort order snapshot for token A,</li> <li>search result token B is based on a field-based-search expression including SEARCH_IN_SEARCHRESULT_RANGE referencing token A using a range of your choice. example: SEARCH_IN_SEARCHRESULT_RANGE=A;0;10 . In this context, the results returned from token A use the sort order snapshot.</li> </ol> Thus, a sort order snapshots allows to access the ordering by means of this field-based-search expression. It does _not_ allow to access the scores of A. The sorted list of documents is stored in memory, next to the token's state. It is cleared if the token is closed or the engine gets restarted.  There can be at most one sort order snapshot per token; any previously existing sort order snap shot will be overwritten.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> SortOrderSnapshotRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SortOrderSnapshotRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SortOrderSnapshotRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SortOrderSnapshotRequestBuilderPostQueryParameters():
        """
        Computes a sort order snapshot of the specified search result token and stores it for the token. A 'sort order snapshot' is an atomically created sorted list of documents of the token, sorted according to its ordering. Its purpose is to allow a consistent sort order even if the sort keys are subject to concurrent modification. Keep in mind that mindserver always uses partial sort when requesting a page from a search result, i.e. any modifications to sort keys between two page fetches can and will affect the resulting sort order! The sort order snapshot allows to create a presorted consistent result.  Sort order snapshots can and need to be dereferenced explicitly. The suggested workflow is as follows: <ol> <li>search result token A is based on an ordering which is known to be subject to concurrent modification,</li> <li>you explicitly create a sort order snapshot for token A,</li> <li>search result token B is based on a field-based-search expression including SEARCH_IN_SEARCHRESULT_RANGE referencing token A using a range of your choice. example: SEARCH_IN_SEARCHRESULT_RANGE=A;0;10 . In this context, the results returned from token A use the sort order snapshot.</li> </ol> Thus, a sort order snapshots allows to access the ordering by means of this field-based-search expression. It does _not_ allow to access the scores of A. The sorted list of documents is stored in memory, next to the token's state. It is cleared if the token is closed or the engine gets restarted.  There can be at most one sort order snapshot per token; any previously existing sort order snap shot will be overwritten.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "top_n":
                return "topN"
            return original_name
        
        # an optional limit describing how many documents should become part of the sort order snapshot. A negative value (or a value which is larger than the search result) include all documents. All other values restrict the sort order snapshot to the N top-ranked documents of the last search. Consequently, usage of the sort order snapshot will return at most these N top ranked documents. Default is to use the entire search result.
        top_n: Optional[int] = None

    
    @dataclass
    class SortOrderSnapshotRequestBuilderPostRequestConfiguration(RequestConfiguration[SortOrderSnapshotRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

