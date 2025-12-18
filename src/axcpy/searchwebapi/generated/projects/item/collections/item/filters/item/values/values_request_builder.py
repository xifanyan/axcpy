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
    from ........models.folder_values_result import FolderValuesResult

class ValuesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /projects/{projectId}/collections/{collectionId}/filters/{fieldId}/values
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ValuesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/projects/{projectId}/collections/{collectionId}/filters/{fieldId}/values{?joinRestriction*,language*,limit*,offset*,order*,prefix*,query*,restrictFoldersByQuery*,returnEmptyFolders*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ValuesRequestBuilderGetQueryParameters]] = None) -> Optional[bytes]:
        """
        Returns a list of folders (categories) in the given folder field (taxonomy, smart filter). Each resulting folder entry has a count of associated documents. The counts are based on the set of documents found for the given query and restrictions
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.folder_values_result import FolderValuesResult

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": FolderValuesResult,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ValuesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of folders (categories) in the given folder field (taxonomy, smart filter). Each resulting folder entry has a count of associated documents. The counts are based on the set of documents found for the given query and restrictions
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ValuesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ValuesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ValuesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ValuesRequestBuilderGetQueryParameters():
        """
        Returns a list of folders (categories) in the given folder field (taxonomy, smart filter). Each resulting folder entry has a count of associated documents. The counts are based on the set of documents found for the given query and restrictions
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "join_restriction":
                return "joinRestriction"
            if original_name == "restrict_folders_by_query":
                return "restrictFoldersByQuery"
            if original_name == "return_empty_folders":
                return "returnEmptyFolders"
            if original_name == "language":
                return "language"
            if original_name == "limit":
                return "limit"
            if original_name == "offset":
                return "offset"
            if original_name == "order":
                return "order"
            if original_name == "prefix":
                return "prefix"
            if original_name == "query":
                return "query"
            return original_name
        
        # Specify a restriction using a joined collection. The argument is expected to be of the form <targetFieldID>:<query>. Example: doc_author_id:office="New York" fired against a documents collection might restrict the result to all documents for which the author has an office in New York. The <targetFieldID> id refers to a field which is the target of a configured join. Joins are configured in the 'Dynamic join' section of the meta-engine configuration. The <query> is the query to be run as a restriction on the source collection in order to limit the results on the target (should be URI-encoded). Some remarks: 1. In the case of using the query for a filter value request: Since dynamic join restrictions influence the result set, and hence the counts, they should be supplied independent of the filter selected. 2. A requests of sorts { joinRestriction=doc_author_id:office=A, query=york } is equivalent to query=york AND doc_author_id.find(office=A), i.e. joinRestriction=<targetFieldID>:<query> and the query syntax <targetFieldID>find(<query>) are equivalent. 3. For meta engine projects, <targetFieldID> is valid independent of the collectionId (i.e. you can use collectionId=people and a <targetFieldID> which is in the people collection).
        join_restriction: Optional[str] = None

        # Specify a language to be used when interpreting the query, default is to use language recognition.
        language: Optional[str] = None

        # Define a limit on the number of results returned. Default is 20, maximally allowed value is 1000.
        limit: Optional[int] = None

        # Define a relative position from which to start fetching results. Can be positive or zero (default).
        offset: Optional[int] = None

        # Provide an order criterion for the results. Needs to be one of 'count', 'relevance', 'name', 'name:asc', 'name:desc'. The latter three correspond to the display name.
        order: Optional[str] = None

        # Optional prefix to constrain the folders returned. This is equivalent to restrictFoldersByQuery=rm_display_name=VALUE* where VALUE is the prefix of choice.
        prefix: Optional[str] = None

        # The query expression. Such a query expression (also known as 'main query') contains simple word matches like 'York', implicit phrases like 'New York', explicit phrases like '"An explicit phrase"', fielded searches, boolean expression like 'berlin and vacation', containing near operators etc. Multiple expressions can be submitted with AND semantics (can also be seen as a 'search in' of the second expression in the first expression). Field-based expressions must respect the fields configured for the selected projectId/collectionId. Specifying this value as GET parameter requires the usual URI encoding. Note that field-based-searches for date fields support '<', '=', '>', '<=', '>=' just as for numeric values; the accepted values are either the milli seconds since 1970 followed by 'L' or a (partial) date pattern as specified in the singleMindServer configuration. Please refer to the reference manual for more details. Use 'NOT *' if you want to match no documents. Default query is '*', i.e. no query restriction. 
        query: Optional[str] = None

        # Optional query to constrain the folders returned. Examples are rm_folder_id=uniquevalue or rm_display_name=displayname
        restrict_folders_by_query: Optional[str] = None

        # Defines if folders with count=0 should be returned. Default is false.
        return_empty_folders: Optional[bool] = None

    
    @dataclass
    class ValuesRequestBuilderGetRequestConfiguration(RequestConfiguration[ValuesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

