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
    from ......models.dimension_request import DimensionRequest
    from ......models.measure_cube import MeasureCube

class MeasuresRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /projects/{projectId}/collections/{collectionId}/measures
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MeasuresRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/projects/{projectId}/collections/{collectionId}/measures{?joinRestriction*,language*,measureType*,query*}", path_parameters)
    
    async def post(self,body: list[DimensionRequest], request_configuration: Optional[RequestConfiguration[MeasuresRequestBuilderPostQueryParameters]] = None) -> Optional[bytes]:
        """
        Returns the measure values. For zero-dimensional measures, it just computes a single value as aggregate over the entire search result. For one-dimensional measures, the result resembles a sorted table in which measure dimensions (like folders) are associated with the measure. For two-dimensional measures, the result is a matrix (a cube) which returns measure value associated with a pair of values. The most simple measure is the count of documents which fall into one of the buckets.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.measure_cube import MeasureCube

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": MeasureCube,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_post_request_information(self,body: list[DimensionRequest], request_configuration: Optional[RequestConfiguration[MeasuresRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Returns the measure values. For zero-dimensional measures, it just computes a single value as aggregate over the entire search result. For one-dimensional measures, the result resembles a sorted table in which measure dimensions (like folders) are associated with the measure. For two-dimensional measures, the result is a matrix (a cube) which returns measure value associated with a pair of values. The most simple measure is the count of documents which fall into one of the buckets.
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
    
    def with_url(self,raw_url: str) -> MeasuresRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MeasuresRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MeasuresRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MeasuresRequestBuilderPostQueryParameters():
        """
        Returns the measure values. For zero-dimensional measures, it just computes a single value as aggregate over the entire search result. For one-dimensional measures, the result resembles a sorted table in which measure dimensions (like folders) are associated with the measure. For two-dimensional measures, the result is a matrix (a cube) which returns measure value associated with a pair of values. The most simple measure is the count of documents which fall into one of the buckets.
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
            if original_name == "measure_type":
                return "measureType"
            if original_name == "language":
                return "language"
            if original_name == "query":
                return "query"
            return original_name
        
        # Specify a restriction using a joined collection. The argument is expected to be of the form <targetFieldID>:<query>. Example: doc_author_id:office="New York" fired against a documents collection might restrict the result to all documents for which the author has an office in New York. The <targetFieldID> id refers to a field which is the target of a configured join. Joins are configured in the 'Dynamic join' section of the meta-engine configuration. The <query> is the query to be run as a restriction on the source collection in order to limit the results on the target (should be URI-encoded). Some remarks: 1. In the case of using the query for a filter value request: Since dynamic join restrictions influence the result set, and hence the counts, they should be supplied independent of the filter selected. 2. A requests of sorts { joinRestriction=doc_author_id:office=A, query=york } is equivalent to query=york AND doc_author_id.find(office=A), i.e. joinRestriction=<targetFieldID>:<query> and the query syntax <targetFieldID>find(<query>) are equivalent. 3. For meta engine projects, <targetFieldID> is valid independent of the collectionId (i.e. you can use collectionId=people and a <targetFieldID> which is in the people collection).
        join_restriction: Optional[str] = None

        # Specify a language to be used when interpreting the query, default is to use language recognition.
        language: Optional[str] = None

        # Defines the aggregate type. The default is to compute counts (i.e. a MeasureTypeParameter with typeName 'count'). All other arguments need a JSON representation of MeasureTypeParameter (url encoded json).
        measure_type: Optional[str] = None

        # The query expression. Such a query expression (also known as 'main query') contains simple word matches like 'York', implicit phrases like 'New York', explicit phrases like '"An explicit phrase"', fielded searches, boolean expression like 'berlin and vacation', containing near operators etc. Multiple expressions can be submitted with AND semantics (can also be seen as a 'search in' of the second expression in the first expression). Field-based expressions must respect the fields configured for the selected projectId/collectionId. Specifying this value as GET parameter requires the usual URI encoding. Note that field-based-searches for date fields support '<', '=', '>', '<=', '>=' just as for numeric values; the accepted values are either the milli seconds since 1970 followed by 'L' or a (partial) date pattern as specified in the singleMindServer configuration. Please refer to the reference manual for more details. Use 'NOT *' if you want to match no documents. Default query is '*', i.e. no query restriction. 
        query: Optional[str] = None

    
    @dataclass
    class MeasuresRequestBuilderPostRequestConfiguration(RequestConfiguration[MeasuresRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

