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
    from .item.with_record_item_request_builder import WithRecordItemRequestBuilder

class BinaryRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /projects/{projectId}/collections/{collectionId}/binary
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BinaryRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/projects/{projectId}/collections/{collectionId}/binary{?field*,joinRestriction*,language*,order*,query*,selectedIndex*}", path_parameters)
    
    def by_record_id(self,record_id: str) -> WithRecordItemRequestBuilder:
        """
        Gets an item from the SearchWebApiSDK.projects.item.collections.item.binary.item collection
        param record_id: An id uniquely qualifying a single record. It resembles the 'id' returned by the records endpoint. Note that this id is url-safe and needs no additional encoding.
        Returns: WithRecordItemRequestBuilder
        """
        if record_id is None:
            raise TypeError("record_id cannot be null.")
        from .item.with_record_item_request_builder import WithRecordItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["recordId"] = record_id
        return WithRecordItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[BinaryRequestBuilderGetQueryParameters]] = None) -> Optional[bytes]:
        """
        Returns one binary which matches the specified search criteria. The field containing the binary data must be specified. If more than one record matches the query, the binary of the record with index 'selectedIndex' is returned. You can inspect the ordering and the number of hits by sending the same query to the records endpoint. The returned filename always starts with the value which is returned when fetching the field via the records endpoint. It ends with the file extension as available to the storage. If the storage knows some original file name, the original file name becomes an infix of sorts ___fileName just before the file extension. The mindserver storage can be accessed by using the singleMindServer identifier as projectId and the collectionId should be 'rm_storage:Image files' or 'rm_storage:Native files' . The precise value after the colon resembles the storage element type in the mindserver configuration.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[BinaryRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns one binary which matches the specified search criteria. The field containing the binary data must be specified. If more than one record matches the query, the binary of the record with index 'selectedIndex' is returned. You can inspect the ordering and the number of hits by sending the same query to the records endpoint. The returned filename always starts with the value which is returned when fetching the field via the records endpoint. It ends with the file extension as available to the storage. If the storage knows some original file name, the original file name becomes an infix of sorts ___fileName just before the file extension. The mindserver storage can be accessed by using the singleMindServer identifier as projectId and the collectionId should be 'rm_storage:Image files' or 'rm_storage:Native files' . The precise value after the colon resembles the storage element type in the mindserver configuration.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def with_url(self,raw_url: str) -> BinaryRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: BinaryRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return BinaryRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class BinaryRequestBuilderGetQueryParameters():
        """
        Returns one binary which matches the specified search criteria. The field containing the binary data must be specified. If more than one record matches the query, the binary of the record with index 'selectedIndex' is returned. You can inspect the ordering and the number of hits by sending the same query to the records endpoint. The returned filename always starts with the value which is returned when fetching the field via the records endpoint. It ends with the file extension as available to the storage. If the storage knows some original file name, the original file name becomes an infix of sorts ___fileName just before the file extension. The mindserver storage can be accessed by using the singleMindServer identifier as projectId and the collectionId should be 'rm_storage:Image files' or 'rm_storage:Native files' . The precise value after the colon resembles the storage element type in the mindserver configuration.
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
            if original_name == "selected_index":
                return "selectedIndex"
            if original_name == "field":
                return "field"
            if original_name == "language":
                return "language"
            if original_name == "order":
                return "order"
            if original_name == "query":
                return "query"
            return original_name
        
        # A single field name storing binary data.
        field: Optional[str] = None

        # Specify a restriction using a joined collection. The argument is expected to be of the form <targetFieldID>:<query>. Example: doc_author_id:office="New York" fired against a documents collection might restrict the result to all documents for which the author has an office in New York. The <targetFieldID> id refers to a field which is the target of a configured join. Joins are configured in the 'Dynamic join' section of the meta-engine configuration. The <query> is the query to be run as a restriction on the source collection in order to limit the results on the target (should be URI-encoded). Some remarks: 1. In the case of using the query for a filter value request: Since dynamic join restrictions influence the result set, and hence the counts, they should be supplied independent of the filter selected. 2. A requests of sorts { joinRestriction=doc_author_id:office=A, query=york } is equivalent to query=york AND doc_author_id.find(office=A), i.e. joinRestriction=<targetFieldID>:<query> and the query syntax <targetFieldID>find(<query>) are equivalent. 3. For meta engine projects, <targetFieldID> is valid independent of the collectionId (i.e. you can use collectionId=people and a <targetFieldID> which is in the people collection).
        join_restriction: Optional[str] = None

        # Specify a language to be used when interpreting the query, default is to use language recognition.
        language: Optional[str] = None

        # Provide order criteria. Format - <field1>[:asc,:desc],field2>[:asc,:desc],...,<fieldN>[:asc,:desc] Examples - 'order=title',  order=custodian:asc,title. Default sorting is as returned by the engine, which is descending by relevancy. The default order for given field sort criteria is 'ascending'.
        order: Optional[str] = None

        # The query expression. Such a query expression (also known as 'main query') contains simple word matches like 'York', implicit phrases like 'New York', explicit phrases like '"An explicit phrase"', fielded searches, boolean expression like 'berlin and vacation', containing near operators etc. Multiple expressions can be submitted with AND semantics (can also be seen as a 'search in' of the second expression in the first expression). Field-based expressions must respect the fields configured for the selected projectId/collectionId. Specifying this value as GET parameter requires the usual URI encoding. Note that field-based-searches for date fields support '<', '=', '>', '<=', '>=' just as for numeric values; the accepted values are either the milli seconds since 1970 followed by 'L' or a (partial) date pattern as specified in the singleMindServer configuration. Please refer to the reference manual for more details. Use 'NOT *' if you want to match no documents. Default query is '*', i.e. no query restriction. 
        query: Optional[str] = None

        # Define the stream to select (counting starts at 1). This is useful if and only if the query returns more than one result. Default is 1.
        selected_index: Optional[int] = None

    
    @dataclass
    class BinaryRequestBuilderGetRequestConfiguration(RequestConfiguration[BinaryRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

