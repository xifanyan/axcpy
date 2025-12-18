from enum import Enum

class FieldDescription_type(str, Enum):
    Identifier = "identifier",
    Content = "content",
    Text = "text",
    Integer = "integer",
    Float = "float",
    Date = "date",
    SingleValue = "singleValue",
    MultiValue = "multiValue",
    Binary = "binary",
    Hierarchy = "hierarchy",
    ParameterizedLong = "parameterizedLong",
    Texts = "texts",

