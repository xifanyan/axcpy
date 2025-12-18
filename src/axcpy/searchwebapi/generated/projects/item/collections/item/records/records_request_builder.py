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
    from ......models.change_request import ChangeRequest
    from ......models.change_result import ChangeResult
    from ......models.search_result import SearchResult
    from .bulk_insert_remove_transaction.bulk_insert_remove_transaction_request_builder import BulkInsertRemoveTransactionRequestBuilder
    from .insert_remove_transaction.insert_remove_transaction_request_builder import InsertRemoveTransactionRequestBuilder
    from .item.with_record_item_request_builder import WithRecordItemRequestBuilder

class RecordsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /projects/{projectId}/collections/{collectionId}/records
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RecordsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/projects/{projectId}/collections/{collectionId}/records{?blockUntilComplete*,body*,fields*,folderFields*,folderFieldsWithProperties*,highlight*,joinRestriction*,language*,limit*,order*,page*,query*,spellingSuggestions*,sponsoredLinks*}", path_parameters)
    
    def by_record_id(self,record_id: str) -> WithRecordItemRequestBuilder:
        """
        Gets an item from the SearchWebApiSDK.projects.item.collections.item.records.item collection
        param record_id: An id uniquely qualifying a single record. It resembles the 'id' returned by the records endpoint. Note that this id is url-safe and needs no additional encoding.
        Returns: WithRecordItemRequestBuilder
        """
        if record_id is None:
            raise TypeError("record_id cannot be null.")
        from .item.with_record_item_request_builder import WithRecordItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["recordId"] = record_id
        return WithRecordItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[RecordsRequestBuilderGetQueryParameters]] = None) -> Optional[bytes]:
        """
        Returns the list of records as specified by the parameters.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.change_result import ChangeResult
        from ......models.search_result import SearchResult

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": SearchResult,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    async def put(self,body: list[ChangeRequest], request_configuration: Optional[RequestConfiguration[RecordsRequestBuilderPutQueryParameters]] = None) -> Optional[bytes]:
        """
        Allows to change properties of documents, for example by tagging them into folders or by modifying textual content.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ......models.change_result import ChangeResult
        from ......models.search_result import SearchResult

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ChangeResult,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[RecordsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the list of records as specified by the parameters.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: list[ChangeRequest], request_configuration: Optional[RequestConfiguration[RecordsRequestBuilderPutQueryParameters]] = None) -> RequestInformation:
        """
        Allows to change properties of documents, for example by tagging them into folders or by modifying textual content.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> RecordsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RecordsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RecordsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bulk_insert_remove_transaction(self) -> BulkInsertRemoveTransactionRequestBuilder:
        """
        The bulkInsertRemoveTransaction property
        """
        from .bulk_insert_remove_transaction.bulk_insert_remove_transaction_request_builder import BulkInsertRemoveTransactionRequestBuilder

        return BulkInsertRemoveTransactionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def insert_remove_transaction(self) -> InsertRemoveTransactionRequestBuilder:
        """
        The insertRemoveTransaction property
        """
        from .insert_remove_transaction.insert_remove_transaction_request_builder import InsertRemoveTransactionRequestBuilder

        return InsertRemoveTransactionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class RecordsRequestBuilderGetQueryParameters():
        """
        Returns the list of records as specified by the parameters.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "folder_fields":
                return "folderFields"
            if original_name == "folder_fields_with_properties":
                return "folderFieldsWithProperties"
            if original_name == "join_restriction":
                return "joinRestriction"
            if original_name == "spelling_suggestions":
                return "spellingSuggestions"
            if original_name == "sponsored_links":
                return "sponsoredLinks"
            if original_name == "body":
                return "body"
            if original_name == "fields":
                return "fields"
            if original_name == "highlight":
                return "highlight"
            if original_name == "language":
                return "language"
            if original_name == "limit":
                return "limit"
            if original_name == "order":
                return "order"
            if original_name == "page":
                return "page"
            if original_name == "query":
                return "query"
            return original_name
        
        # Indicate whether to retrieve summarized content for the record, default is false. This argument retrieves only parts of the content, namely the part which is relevant for the query or the first sentences of the document.
        body: Optional[bool] = None

        # An URI-encoded, comma-separated list of fields to be retrieved for each document. Valid field names are typically those which can be inspected using the fields endpoint (i.e. those configured in the data model). In addition, search results support to retrieve dynamic properties as field name: 'rm_is_best_bet' returns true if and only if 'Best bets boosting' is active and a match is a best bet.
        fields: Optional[str] = None

        # An URI-encoded, comma-separated list of folder fields (taxonomies) to be retrieved for each document. Note that folder fields can be returned by 'fields' as well in which case an array of folder ids is returned. Use 'folderFields' if you need the folder and its display name.
        folder_fields: Optional[str] = None

        # An (exclusive) alternative to 'folderFields': it also allows to define folder fields to fetch, but it has the ability to specify properties to fetch as well. Note that the display name is always returned. All other arguments need a JSON representation of FolderPropertiesRequestParameter (url encoded json). If you leave this empty (or do not specify the parameter), the system will fetch folder ids and folder display names for all elements specified in in 'folderFields'. If you specify elements here, it is required that 'folderFields' is empty.
        folder_fields_with_properties: Optional[str] = None

        # An argument to 'body': Indicate whether to provide highlighting information (via XML tags of the form <recomDescriptiveWord>, default is true
        highlight: Optional[bool] = None

        # Specify a restriction using a joined collection. The argument is expected to be of the form <targetFieldID>:<query>. Example: doc_author_id:office="New York" fired against a documents collection might restrict the result to all documents for which the author has an office in New York. The <targetFieldID> id refers to a field which is the target of a configured join. Joins are configured in the 'Dynamic join' section of the meta-engine configuration. The <query> is the query to be run as a restriction on the source collection in order to limit the results on the target (should be URI-encoded). Some remarks: 1. In the case of using the query for a filter value request: Since dynamic join restrictions influence the result set, and hence the counts, they should be supplied independent of the filter selected. 2. A requests of sorts { joinRestriction=doc_author_id:office=A, query=york } is equivalent to query=york AND doc_author_id.find(office=A), i.e. joinRestriction=<targetFieldID>:<query> and the query syntax <targetFieldID>find(<query>) are equivalent. 3. For meta engine projects, <targetFieldID> is valid independent of the collectionId (i.e. you can use collectionId=people and a <targetFieldID> which is in the people collection).
        join_restriction: Optional[str] = None

        # Specify a language to be used when interpreting the query, default is to use language recognition.
        language: Optional[str] = None

        # Define a page size / limit on the number of results returned. Default is 20. The maximally allowed value is 1000 for all standard paging use-cases. However, if the 'accept' header is set to 'application/x-ndjson', the result will be returned in streaming mode which allows to specify page=1, limit=-1 in order to return all documents (see response documentation for details).
        limit: Optional[int] = None

        # Provide order criteria. Format - <field1>[:asc,:desc],field2>[:asc,:desc],...,<fieldN>[:asc,:desc] Examples - 'order=title',  order=custodian:asc,title. Default sorting is as returned by the engine, which is descending by relevancy. The default order for given field sort criteria is 'ascending'.
        order: Optional[str] = None

        # Define which page to retrieve (counting starts at 1). Default is 1.
        page: Optional[int] = None

        # The query expression. Such a query expression (also known as 'main query') contains simple word matches like 'York', implicit phrases like 'New York', explicit phrases like '"An explicit phrase"', fielded searches, boolean expression like 'berlin and vacation', containing near operators etc. Multiple expressions can be submitted with AND semantics (can also be seen as a 'search in' of the second expression in the first expression). Field-based expressions must respect the fields configured for the selected projectId/collectionId. Specifying this value as GET parameter requires the usual URI encoding. Note that field-based-searches for date fields support '<', '=', '>', '<=', '>=' just as for numeric values; the accepted values are either the milli seconds since 1970 followed by 'L' or a (partial) date pattern as specified in the singleMindServer configuration. Please refer to the reference manual for more details. Use 'NOT *' if you want to match no documents. Default query is '*', i.e. no query restriction. 
        query: Optional[str] = None

        # Computes and returns any configured spelling suggestions for the provided query. Note that this requires spelling suggestions to be configured in the project's data model. Default is to not compute spelling suggestions.
        spelling_suggestions: Optional[bool] = None

        # Computes and returns any configured sponsored links for the provided query. Note that this requires sponsored links to be configured in the project's data model. Default is to not compute sponsored links.
        sponsored_links: Optional[bool] = None

    
    @dataclass
    class RecordsRequestBuilderGetRequestConfiguration(RequestConfiguration[RecordsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class RecordsRequestBuilderPutQueryParameters():
        """
        Allows to change properties of documents, for example by tagging them into folders or by modifying textual content.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "block_until_complete":
                return "blockUntilComplete"
            if original_name == "language":
                return "language"
            if original_name == "query":
                return "query"
            return original_name
        
        # Specifies whether the call should block until all indexes are updated. The default value 'false' is to return immediately which means that the display of values is always correct, but search indices may be outdated until all indices have been updated eventually (that means: queries will not respect the change until the index is updated). The change is persisted as soon as the API call returns, irrespective of 'blockUntilComplete'.
        block_until_complete: Optional[bool] = None

        # Specify a language to be used when interpreting the query, default is to use language recognition.
        language: Optional[str] = None

        # The query expression. Such a query expression (also known as 'main query') contains simple word matches like 'York', implicit phrases like 'New York', explicit phrases like '"An explicit phrase"', fielded searches, boolean expression like 'berlin and vacation', containing near operators etc. Multiple expressions can be submitted with AND semantics (can also be seen as a 'search in' of the second expression in the first expression). Field-based expressions must respect the fields configured for the selected projectId/collectionId. Specifying this value as GET parameter requires the usual URI encoding. Note that field-based-searches for date fields support '<', '=', '>', '<=', '>=' just as for numeric values; the accepted values are either the milli seconds since 1970 followed by 'L' or a (partial) date pattern as specified in the singleMindServer configuration. Please refer to the reference manual for more details. Use 'NOT *' if you want to match no documents. Default query is '*', i.e. no query restriction. 
        query: Optional[str] = None

    
    @dataclass
    class RecordsRequestBuilderPutRequestConfiguration(RequestConfiguration[RecordsRequestBuilderPutQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

