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
    from .........models.insert_remove_request import InsertRemoveRequest
    from .........models.insert_remove_result import InsertRemoveResult

class BufferRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /projects/{projectId}/collections/{collectionId}/records/bulkInsertRemoveTransaction/{indexingBufferId}/buffer
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BufferRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/projects/{projectId}/collections/{collectionId}/records/bulkInsertRemoveTransaction/{indexingBufferId}/buffer", path_parameters)
    
    async def post(self,body: InsertRemoveRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[bytes]:
        """
        Creates new records in the specified collection. Note that this end point comes with two flavors: the first accepts application/json. It is intended to insert folders (=categories) into folder collections (=taxonomies). To this end, the projectId should be something like singleMindServer.NAME (or metaMindServer.NAME) and the collectionId should resemble the folder collection name (=taxonomy id). The second flavor accepts multipart/form-data. It is intended to populate collections containing fields requiring some sort of file streaming, typically fields with binary data or with full text content (streamed xml).The mindserver storage can be accessed by using the singleMindServer identifier as projectId and the collectionId should be 'rm_storage:Image files' or 'rm_storage:Native files' (the precise value after the colon resembles the storage element type in the mindserver configuration). The data model for these storage-related collections can be retrieved using the fields endpoint.Note that it is also supported to create new documents. In this case, fields of type CONTENT accept a binary of type application/xml which will be streamed. XML streaming is special in several aspects:  1. The XML contains structured information which is inserted as-is, and the content field(s) are somewhere inside of it.2. The XML can also contain data for standard fields (typically in the form &lt;document&gt;&lt;meta&gt; &lt;field&gt;VALUE&lt;/field&gt;&lt;/meta&gt; .... &lt;/document&gt;). If a field is present in both XML and fields of the RecordData, the RecordData wins.3. It is _mandatory_ that some fields are specified as fields in the RecordData (if they are needed)! This includes rm_attachmentroot, rm_crawlid, rm_checksum, rm_modificationdate.4. If a native is to be inserted together with the document, its value can be specified as field rm_native. More precisely: specify a field with name rm_native, and its value resembles the index of its binary inside of the multipart/formdata.5. If more than one XML content stream is attached, the server will insert an artificial &lt;document&gt; ...&lt;/document&gt; around all streams and will concatenate them.Any streamed fields (i.e. either binary fields or XML content streams) are to be specified as follows: such a field must be specified into the RecordData, and the value for such a field is the integer index of the stream inside of the multipart/formdata. Example : 'fieldName': 'p', 'value': 0.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .........models.insert_remove_result import InsertRemoveResult

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": InsertRemoveResult,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_post_request_information(self,body: InsertRemoveRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates new records in the specified collection. Note that this end point comes with two flavors: the first accepts application/json. It is intended to insert folders (=categories) into folder collections (=taxonomies). To this end, the projectId should be something like singleMindServer.NAME (or metaMindServer.NAME) and the collectionId should resemble the folder collection name (=taxonomy id). The second flavor accepts multipart/form-data. It is intended to populate collections containing fields requiring some sort of file streaming, typically fields with binary data or with full text content (streamed xml).The mindserver storage can be accessed by using the singleMindServer identifier as projectId and the collectionId should be 'rm_storage:Image files' or 'rm_storage:Native files' (the precise value after the colon resembles the storage element type in the mindserver configuration). The data model for these storage-related collections can be retrieved using the fields endpoint.Note that it is also supported to create new documents. In this case, fields of type CONTENT accept a binary of type application/xml which will be streamed. XML streaming is special in several aspects:  1. The XML contains structured information which is inserted as-is, and the content field(s) are somewhere inside of it.2. The XML can also contain data for standard fields (typically in the form &lt;document&gt;&lt;meta&gt; &lt;field&gt;VALUE&lt;/field&gt;&lt;/meta&gt; .... &lt;/document&gt;). If a field is present in both XML and fields of the RecordData, the RecordData wins.3. It is _mandatory_ that some fields are specified as fields in the RecordData (if they are needed)! This includes rm_attachmentroot, rm_crawlid, rm_checksum, rm_modificationdate.4. If a native is to be inserted together with the document, its value can be specified as field rm_native. More precisely: specify a field with name rm_native, and its value resembles the index of its binary inside of the multipart/formdata.5. If more than one XML content stream is attached, the server will insert an artificial &lt;document&gt; ...&lt;/document&gt; around all streams and will concatenate them.Any streamed fields (i.e. either binary fields or XML content streams) are to be specified as follows: such a field must be specified into the RecordData, and the value for such a field is the integer index of the stream inside of the multipart/formdata. Example : 'fieldName': 'p', 'value': 0.
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
    
    def with_url(self,raw_url: str) -> BufferRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: BufferRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return BufferRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class BufferRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

