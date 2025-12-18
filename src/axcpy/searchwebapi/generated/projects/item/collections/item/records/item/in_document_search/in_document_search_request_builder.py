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
    from ........models.highlighted_word_result import HighlightedWordResult

class InDocumentSearchRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /projects/{projectId}/collections/{collectionId}/records/{recordId}/inDocumentSearch
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new InDocumentSearchRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/projects/{projectId}/collections/{collectionId}/records/{recordId}/inDocumentSearch{?blockUntilComplete*,contentFieldNames*,highlightFolderFieldList*,highlightFolderFieldsAggregation*,highlightSearchTermJoinRestriction*,highlightSearchTermLanguage*,highlightSearchTermQuery*,highlightUserTerms*,omitHitsPerPage*,pageTag*,requestHitLocationsDocumentRelative*,requestHitLocationsPageRelative*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[InDocumentSearchRequestBuilderGetQueryParameters]] = None) -> Optional[bytes]:
        """
        Searches within the record and returns the matches as string and/or regular expression
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.change_result import ChangeResult
        from ........models.highlighted_word_result import HighlightedWordResult

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": HighlightedWordResult,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    async def put(self,body: list[ChangeRequest], request_configuration: Optional[RequestConfiguration[InDocumentSearchRequestBuilderPutQueryParameters]] = None) -> Optional[bytes]:
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
        from ........models.highlighted_word_result import HighlightedWordResult

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ChangeResult,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[InDocumentSearchRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Searches within the record and returns the matches as string and/or regular expression
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: list[ChangeRequest], request_configuration: Optional[RequestConfiguration[InDocumentSearchRequestBuilderPutQueryParameters]] = None) -> RequestInformation:
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
    
    def with_url(self,raw_url: str) -> InDocumentSearchRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: InDocumentSearchRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return InDocumentSearchRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class InDocumentSearchRequestBuilderGetQueryParameters():
        """
        Searches within the record and returns the matches as string and/or regular expression
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "content_field_names":
                return "contentFieldNames"
            if original_name == "highlight_folder_fields_aggregation":
                return "highlightFolderFieldsAggregation"
            if original_name == "highlight_folder_field_list":
                return "highlightFolderFieldList"
            if original_name == "highlight_search_term_join_restriction":
                return "highlightSearchTermJoinRestriction"
            if original_name == "highlight_search_term_language":
                return "highlightSearchTermLanguage"
            if original_name == "highlight_search_term_query":
                return "highlightSearchTermQuery"
            if original_name == "highlight_user_terms":
                return "highlightUserTerms"
            if original_name == "omit_hits_per_page":
                return "omitHitsPerPage"
            if original_name == "page_tag":
                return "pageTag"
            if original_name == "request_hit_locations_document_relative":
                return "requestHitLocationsDocumentRelative"
            if original_name == "request_hit_locations_page_relative":
                return "requestHitLocationsPageRelative"
            return original_name
        
        # (Optional) Specifies a comma-separated list of XML content tag which are to be searched. Defaults to the configured content tags of the target project.
        content_field_names: Optional[str] = None

        # An argument to 'body': A comma-separated list of folder field names for which folder-specific highlighting is to be applied.
        highlight_folder_field_list: Optional[str] = None

        # A comma-separated list which is as long as highlightFolderFieldList. For each element of highlightFolderFieldList, it defines how to return values of that field: either aggregated 'by field' or 'by folder'. Example: highlightFolderFieldList='field1,field2'  and highlightFolderFieldsAggregation='by field, by folder'
        highlight_folder_fields_aggregation: Optional[str] = None

        # This is a part of search-term based highlighting, see 'highlightSearchTermQuery'. It has the same syntax as 'joinRestriction' for searches.
        highlight_search_term_join_restriction: Optional[str] = None

        # Specify a language to be used when interpreting the query. The default is to use the result of the query language detection. The argument is a two-letter ISO 639 language code like 'en'. The language is used in order to define stemming rules, for example.
        highlight_search_term_language: Optional[str] = None

        # A query expression which should be used to highlight hits in the requested document. The query expression resembles the value of 'query' for search operations, but it is only used for search term highlighting and concept highlighting. Note that the record id in question does not necessarily need to match the query in question.
        highlight_search_term_query: Optional[str] = None

        # An argument to 'body': A comma-separated list of terms to highlight.
        highlight_user_terms: Optional[str] = None

        # Instructs the backend to not compute hits by page, i.e. the return value will be null. This essentially disables paging.
        omit_hits_per_page: Optional[bool] = None

        # Specifies an XML tag name which defines page boundaries. Everything within this page tag is considered to be part of one page.Paging is only used in order to determine how many hits were found on each page.The default is to page automatically (i.e. just as when the XML was text generated using the normal content endpoint).Use omitHitsPerPage in order to disable paging entirely.The argument must be an XML tag name. Note that the page tag must be WITHIN the content tag, otherwise it will be ignored! It is valid to use pagetag name == content tag name.
        page_tag: Optional[str] = None

        # Instructs the backend to return hit locatons for each hit.There will be one location for each hit. The location is a relative number if the hit appears at the beginning of the document (0%) or at the end (100%).
        request_hit_locations_document_relative: Optional[bool] = None

        # Instructs the backend to return hit locations by page.There will be one location for each hit. The location is a relative number if the hit appears at the beginning of its page (0%) or at the end (100%).
        request_hit_locations_page_relative: Optional[bool] = None

    
    @dataclass
    class InDocumentSearchRequestBuilderGetRequestConfiguration(RequestConfiguration[InDocumentSearchRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class InDocumentSearchRequestBuilderPutQueryParameters():
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
    class InDocumentSearchRequestBuilderPutRequestConfiguration(RequestConfiguration[InDocumentSearchRequestBuilderPutQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

