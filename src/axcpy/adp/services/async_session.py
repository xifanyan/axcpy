from __future__ import annotations

from typing import Any
import logging

from axcpy.adp.models.list_entities import ListEntitiesResult, ListEntitiesTaskConfig
from axcpy.adp.models.manage_host_roles import (
    ManageHostRolesResult,
    ManageHostRolesTaskConfig,
)
from axcpy.adp.models.query_engine import QueryEngineResult, QueryEngineTaskConfig
from axcpy.adp.models.read_configuration import (
    ReadConfigurationResult,
    ReadConfigurationTaskConfig,
)
from axcpy.adp.models.taxonomy_statistic import (
    TaxonomyStatisticResult,
    TaxonomyStatisticTaskConfig,
)
from axcpy.adp.models.export_documents import (
    ExportDocumentsResult,
    ExportDocumentsTaskConfig,
)
from axcpy.adp.models.request import ADPTaskRequest

from .async_client import AsyncADPClient
from axcpy.adp.models.task_spec import TASK_SPECS  # type: ignore

logger = logging.getLogger(__name__)


class AsyncSession:
    """High-level async wrapper that manages authentication headers for AsyncADPClient.

    Sessions always use a shared AsyncADPClient instance and never create their own.
    This ensures efficient resource usage and connection pooling.

    Parameters
    ----------
    client: AsyncADPClient
        Shared AsyncADPClient instance that this session will use. The client will not be
        closed when this session is closed - you must manage the client lifecycle externally.
    auth_username: str
        Authentication user name passed as `AuthUserName` header.
    auth_password: str
        Authentication password passed as `AuthPassword` header.
    extra_headers: dict[str, str] | None
        Additional headers merged after auth headers; can override them (not recommended).
    """

    AUTH_USERNAME_HEADER = "Auth-Username"
    AUTH_PASSWORD_HEADER = "Auth-Password"

    def __init__(
        self,
        client: AsyncADPClient,
        auth_username: str,
        auth_password: str,
        *,
        extra_headers: dict[str, str] | None = None,
    ) -> None:
        self._client = client
        self.auth_username = auth_username
        self.auth_password = auth_password
        self._base_headers: dict[str, str] = {
            self.AUTH_USERNAME_HEADER: auth_username,
            self.AUTH_PASSWORD_HEADER: auth_password,
        }
        if extra_headers:
            # Extra headers override defaults if they collide
            self._base_headers.update(extra_headers)

    @property
    def client(self) -> AsyncADPClient:
        return self._client

    def _process_response(self, response) -> None | dict:
        """Process HTTP response and extract JSON data."""
        try:
            return response.json()
        except Exception:  # pragma: no cover - non-JSON response
            return None

    async def run(
        self,
        task: ADPTaskRequest,
        *,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
    ) -> None | dict:
        """Send a task via PUT using underlying AsyncADPClient (synchronous execution).

        Returns response JSON (dict) or None if no JSON body.
        """
        merged = {**self._base_headers, **(headers or {})}
        response = await self._client.run(task, headers=merged, timeout=timeout)
        return self._process_response(response)

    async def run_async(
        self,
        task: ADPTaskRequest,
        *,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
    ) -> None | dict:
        """Send a task via PUT using underlying AsyncADPClient (async execution).

        Returns response JSON (dict) or None if no JSON body.
        """
        merged = {**self._base_headers, **(headers or {})}
        response = await self._client.run_async(task, headers=merged, timeout=timeout)
        return self._process_response(response)

    async def statusAndProgress(
        self,
        task: ADPTaskRequest,
        *,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
    ) -> None | dict:
        """Check the status and progress of an asynchronously submitted task.

        Returns response JSON (dict) or None if no JSON body.
        """
        merged = {**self._base_headers, **(headers or {})}
        response = await self._client.statusAndProgress(
            task, headers=merged, timeout=timeout
        )
        return self._process_response(response)

    async def __aenter__(self) -> "AsyncSession":  # pragma: no cover
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:  # pragma: no cover
        pass  # Don't close the client - it's managed externally

    # High-level task execution methods

    async def list_entities(
        self,
        config: ListEntitiesTaskConfig,
        *,
        timeout: float | None = None,
    ) -> ListEntitiesResult:
        return await self.run_task(
            "list_entities",
            config=config,
            timeout=timeout,
        )

    async def manage_host_roles(
        self,
        config: ManageHostRolesTaskConfig,
        *,
        timeout: float | None = None,
    ) -> ManageHostRolesResult:
        return await self.run_task(
            "manage_host_roles",
            config=config,
            timeout=timeout,
        )

    async def read_configuration(
        self,
        config: ReadConfigurationTaskConfig,
        *,
        timeout: float | None = None,
    ) -> ReadConfigurationResult:
        return await self.run_task(
            "read_configuration",
            config=config,
            timeout=timeout,
        )

    async def query_engine(
        self,
        config: QueryEngineTaskConfig,
        *,
        timeout: float | None = None,
    ) -> QueryEngineResult:
        return await self.run_task(
            "query_engine",
            config=config,
            timeout=timeout,
        )

    async def taxonomy_statistic(
        self,
        config: TaxonomyStatisticTaskConfig,
        *,
        timeout: float | None = None,
    ) -> TaxonomyStatisticResult:
        return await self.run_task(
            "taxonomy_statistic",
            config=config,
            timeout=timeout,
        )

    async def export_documents(
        self,
        config: ExportDocumentsTaskConfig,
        *,
        timeout: float | None = None,
    ) -> ExportDocumentsResult:
        return await self.run_task(
            "export_documents",
            config=config,
            timeout=timeout,
        )

    # --------------------------------------------------------------
    # Generic task execution via registry (spec definitions in task_spec.py)
    # --------------------------------------------------------------

    async def run_task(
        self,
        key: str,
        *,
        config,
        timeout: float | None = None,
    ) -> Any:
        """Execute a task using the task registry.

        Args:
            key: Task key in TASK_SPECS (e.g., 'list_entities')
            config: Task configuration object
            timeout: Optional timeout for the request

        Returns:
            Parsed result object specific to the task type

        Raises:
            RuntimeError: If task execution fails or returns non-success status
        """
        spec = TASK_SPECS.get(key)
        if not spec:
            raise ValueError(f"Unknown task key: {key}")

        task = ADPTaskRequest(
            taskType=spec["task_type"],
            taskConfiguration=config,
            taskDisplayName=spec["display_name"],
            taskDescription=spec["description"],
        )
        response = await self.run(task, timeout=timeout)
        if not response:
            raise RuntimeError(f"{spec['task_type']} task failed: No response received")

        status = response.get("executionStatus", "").lower()
        if status != "success":
            error_msg = response.get("errorMessage", "")
            raise RuntimeError(
                f"{spec['task_type']} task failed with status: {status}"
                + (f" - {error_msg}" if error_msg else "")
            )
        metadata = response.get("executionMetaData", {})
        if not metadata:
            raise RuntimeError(
                f"{spec['task_type']} task completed but returned no metadata"
            )
        try:
            return spec["parser"](metadata)
        except Exception as e:  # pragma: no cover - defensive
            raise ValueError(f"Failed to parse metadata for {spec['task_type']}: {e}")


__all__ = ["AsyncSession"]
