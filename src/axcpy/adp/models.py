"""Pydantic models for ADP API."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Case(BaseModel):
    """Represents a case in Axcelerate."""

    id: int
    name: str
    description: Optional[str] = None
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    status: str

    class Config:
        populate_by_name = True


class Document(BaseModel):
    """Represents a document in Axcelerate."""

    id: str
    case_id: int = Field(alias="caseId")
    title: str
    content: Optional[str] = None
    file_type: str = Field(alias="fileType")
    size_bytes: int = Field(alias="sizeBytes")
    created_at: datetime = Field(alias="createdAt")

    class Config:
        populate_by_name = True


class SearchRequest(BaseModel):
    """Search request parameters."""

    query: str
    case_id: Optional[int] = Field(default=None, alias="caseId")
    limit: int = 100
    offset: int = 0

    class Config:
        populate_by_name = True


class SearchResult(BaseModel):
    """Search result response."""

    total: int
    documents: list[Document]
    query: str
