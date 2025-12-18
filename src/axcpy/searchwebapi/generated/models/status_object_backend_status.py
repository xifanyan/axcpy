from enum import Enum

class StatusObject_backendStatus(str, Enum):
    Ok = "ok",
    MeaninglessSearchTerms = "meaningless search terms",
    UnknownError = "unknown error",
    AllSearchTermsUnknown = "all search terms unknown",
    ChildCollectionInvalid = "child collection invalid",
    IncompleteSearchResultsDueToPendingSynchronization = "incomplete search results due to pending synchronization",
    UnexpandableWildcard = "unexpandable wildcard",
    ExpandedQueryTooLong = "expanded query too long",
    SyntaxError = "syntax error",
    UnsupportedExpression = "unsupported expression",

