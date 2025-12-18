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
    from ........models.change_request import ChangeRequest
    from ........models.change_result import ChangeResult
    from ........models.record import Record

class ContentRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /projects/{projectId}/collections/{collectionId}/records/{recordId}/content
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ContentRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/projects/{projectId}/collections/{collectionId}/records/{recordId}/content{?blockUntilComplete*,body*,fields*,fieldsHighlighted*,folderFields*,folderFieldsWithProperties*,highlightFolderFieldList*,highlightHitNavigation*,highlightSearchTermJoinRestriction*,highlightSearchTermLanguage*,highlightSearchTermQuery*,highlightUserTerms*,page*,summarize*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ContentRequestBuilderGetQueryParameters]] = None) -> Optional[bytes]:
        """
        Returns selected properties (possibly including paged body content) for the record in question.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.change_result import ChangeResult
        from ........models.record import Record

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": Record,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    async def put(self,body: list[ChangeRequest], request_configuration: Optional[RequestConfiguration[ContentRequestBuilderPutQueryParameters]] = None) -> Optional[bytes]:
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
        from ........models.change_result import ChangeResult
        from ........models.record import Record

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ChangeResult,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ContentRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns selected properties (possibly including paged body content) for the record in question.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: list[ChangeRequest], request_configuration: Optional[RequestConfiguration[ContentRequestBuilderPutQueryParameters]] = None) -> RequestInformation:
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
    
    def with_url(self,raw_url: str) -> ContentRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ContentRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ContentRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ContentRequestBuilderGetQueryParameters():
        """
        Returns selected properties (possibly including paged body content) for the record in question.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "fields_highlighted":
                return "fieldsHighlighted"
            if original_name == "folder_fields":
                return "folderFields"
            if original_name == "folder_fields_with_properties":
                return "folderFieldsWithProperties"
            if original_name == "highlight_folder_field_list":
                return "highlightFolderFieldList"
            if original_name == "highlight_hit_navigation":
                return "highlightHitNavigation"
            if original_name == "highlight_search_term_join_restriction":
                return "highlightSearchTermJoinRestriction"
            if original_name == "highlight_search_term_language":
                return "highlightSearchTermLanguage"
            if original_name == "highlight_search_term_query":
                return "highlightSearchTermQuery"
            if original_name == "highlight_user_terms":
                return "highlightUserTerms"
            if original_name == "body":
                return "body"
            if original_name == "fields":
                return "fields"
            if original_name == "page":
                return "page"
            if original_name == "summarize":
                return "summarize"
            return original_name
        
        # Indicate whether to retrieve content for the record, default is false. This parameter is required in order to display highlighting results. It fetches fields configured as 'Content Fields' in the data model, applies highlighting, paging, and summarization as needed, and returns the resulting XML.
        body: Optional[bool] = None

        # An URI-encoded, comma-separated list of fields to be retrieved for each document. Valid field names are typically those which can be inspected using the fields endpoint (i.e. those configured in the data model). In addition, search results support to retrieve dynamic properties as field name: 'rm_is_best_bet' returns true if and only if 'Best bets boosting' is active and a match is a best bet.
        fields: Optional[str] = None

        # An URI-encoded, comma-separated list of fields which will be fetched in XML form for which highlighting has been applied. The resulting field content is in XML form with <recomDescriptiveWord> tags for highlighted words. The response object will contain one field for each item in this list, and the result items will be have the suffix 'Xml' to indicate that the highlighted value is in XML form (example 'titleXml'). Note that fields specified in this context do not necessarily need to be known in the data model. Note furthermore that highlighting will only match for indexed fields.
        fields_highlighted: Optional[str] = None

        # An URI-encoded, comma-separated list of folder fields (taxonomies) to be retrieved for each document. Note that folder fields can be returned by 'fields' as well in which case an array of folder ids is returned. Use 'folderFields' if you need the folder and its display name.
        folder_fields: Optional[str] = None

        # An (exclusive) alternative to 'folderFields': it also allows to define folder fields to fetch, but it has the ability to specify properties to fetch as well. Note that the display name is always returned. All other arguments need a JSON representation of FolderPropertiesRequestParameter (url encoded json). If you leave this empty (or do not specify the parameter), the system will fetch folder ids and folder display names for all elements specified in in 'folderFields'. If you specify elements here, it is required that 'folderFields' is empty.
        folder_fields_with_properties: Optional[str] = None

        # An argument to 'body': A comma-separated list of folder field names for which folder-specific highlighting is to be applied.
        highlight_folder_field_list: Optional[str] = None

        # An argument to 'body': Allows to return specific highlighted positions within the document. Valid choices are 'first', 'previous', 'next', 'last', 'firstUser', 'nextUser'. Default is to use no hit navigation. Note that 'first', 'last', and 'firstUser' ignore the page number and jump to the first resp. last hit. The choice 'next' jumps to the first page containing a hit which has a page number bigger than the 'page' parameter. If 'page' is the last page, it continues searching at the first page.
        highlight_hit_navigation: Optional[str] = None

        # This is a part of search-term based highlighting, see 'highlightSearchTermQuery'. It has the same syntax as 'joinRestriction' for searches.
        highlight_search_term_join_restriction: Optional[str] = None

        # Specify a language to be used when interpreting the query. The default is to use the result of the query language detection. The argument is a two-letter ISO 639 language code like 'en'. The language is used in order to define stemming rules, for example.
        highlight_search_term_language: Optional[str] = None

        # A query expression which should be used to highlight hits in the requested document. The query expression resembles the value of 'query' for search operations, but it is only used for search term highlighting and concept highlighting. Note that the record id in question does not necessarily need to match the query in question.
        highlight_search_term_query: Optional[str] = None

        # An argument to 'body': A comma-separated list of terms to highlight.
        highlight_user_terms: Optional[str] = None

        # Define which page to retrieve (counting starts at 1). Default is 1. A page number which is too large will automatically be replaced by the highest page number.
        page: Optional[int] = None

        # An argument to 'body': indicates whether to provide a textual summary for the record, default is false in this context. The summary shows text portions around matching highlighted words in the document.
        summarize: Optional[bool] = None

    
    @dataclass
    class ContentRequestBuilderGetRequestConfiguration(RequestConfiguration[ContentRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ContentRequestBuilderPutQueryParameters():
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
            return original_name
        
        # Specifies whether the call should block until all indexes are updated. The default value 'false' is to return immediately which means that the display of values is always correct, but search indices may be outdated until all indices have been updated eventually (that means: queries will not respect the change until the index is updated). The change is persisted as soon as the API call returns, irrespective of 'blockUntilComplete'.
        block_until_complete: Optional[bool] = None

    
    @dataclass
    class ContentRequestBuilderPutRequestConfiguration(RequestConfiguration[ContentRequestBuilderPutQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

