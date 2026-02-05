from __future__ import annotations

import logging
from typing import Any

from axcpy.adp.models.create_data_source import (
    CreateDataSourceResult,
    CreateDataSourceTaskConfig,
)
from axcpy.adp.models.create_ocr_job import CreateOcrJobTaskConfig
from axcpy.adp.models.export_documents import (
    ExportDocumentsResult,
    ExportDocumentsTaskConfig,
)

# ruff: noqa: N802 - Method name must match API specification
from axcpy.adp.models.list_entities import ListEntitiesResult, ListEntitiesTaskConfig
from axcpy.adp.models.manage_host_roles import (
    ManageHostRolesResult,
    ManageHostRolesTaskConfig,
)
from axcpy.adp.models.manage_users_and_groups import (
    ManageUsersAndGroupsResult,
    ManageUsersAndGroupsTaskConfig,
)
from axcpy.adp.models.query_engine import QueryEngineResult, QueryEngineTaskConfig
from axcpy.adp.models.read_configuration import (
    ReadConfigurationResult,
    ReadConfigurationTaskConfig,
)
from axcpy.adp.models.read_service_alerts import (
    ReadServiceAlertsResult,
    ReadServiceAlertsTaskConfig,
)
from axcpy.adp.models.request import ADPTaskRequest
from axcpy.adp.models.response import ADPTaskResponse
from axcpy.adp.models.start_application import (
    StartApplicationResult,
    StartApplicationTaskConfig,
)
from axcpy.adp.models.task_spec import TASK_SPECS  # type: ignore
from axcpy.adp.models.taxonomy_statistic import (
    TaxonomyStatisticResult,
    TaxonomyStatisticTaskConfig,
)

from .client import ADPClient

logger = logging.getLogger(__name__)


class Session:
    """High-level wrapper that manages authentication headers for ADPClient.

    Sessions always use a shared ADPClient instance and never create their own.
    This ensures efficient resource usage and connection pooling.

    Parameters
    ----------
    client: ADPClient
        Shared ADPClient instance that this session will use. The client will not be
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
        client: ADPClient,
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
    def client(self) -> ADPClient:
        return self._client

    def _process_response(self, response) -> None | dict:
        """Process HTTP response and extract JSON data."""
        try:
            return response.json()
        except Exception:  # pragma: no cover - non-JSON response
            return None

    def run(
        self,
        task: ADPTaskRequest,
        *,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
    ) -> None | dict:
        """Send a task via PUT using underlying ADPClient (synchronous execution).

        Returns response JSON (dict) or None if no JSON body.
        """
        merged = {**self._base_headers, **(headers or {})}
        response = self._client.run(task, headers=merged, timeout=timeout)
        return self._process_response(response)

    def run_async(
        self,
        task: ADPTaskRequest,
        *,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
    ) -> None | dict:
        """Send a task via PUT using underlying ADPClient (asynchronous execution).

        Returns response JSON (dict) or None if no JSON body.
        """
        merged = {**self._base_headers, **(headers or {})}
        response = self._client.run_async(task, headers=merged, timeout=timeout)
        return self._process_response(response)

    def statusAndProgress(
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
        response = self._client.statusAndProgress(task, headers=merged, timeout=timeout)
        return self._process_response(response)

    def list_entities(
        self,
        config: ListEntitiesTaskConfig,
        *,
        timeout: float | None = None,
    ) -> ListEntitiesResult:
        return self.run_task(
            "list_entities",
            config=config,
            timeout=timeout,
        )

    def manage_host_roles(
        self,
        config: ManageHostRolesTaskConfig,
        *,
        timeout: float | None = None,
    ) -> ManageHostRolesResult:
        return self.run_task(
            "manage_host_roles",
            config=config,
            timeout=timeout,
        )

    def read_configuration(
        self,
        config: ReadConfigurationTaskConfig,
        *,
        timeout: float | None = None,
    ) -> ReadConfigurationResult:
        return self.run_task(
            "read_configuration",
            config=config,
            timeout=timeout,
        )

    def query_engine(
        self,
        config: QueryEngineTaskConfig,
        *,
        timeout: float | None = None,
    ) -> QueryEngineResult:
        return self.run_task(
            "query_engine",
            config=config,
            timeout=timeout,
        )

    def taxonomy_statistic(
        self,
        config: TaxonomyStatisticTaskConfig,
        *,
        timeout: float | None = None,
    ) -> TaxonomyStatisticResult:
        return self.run_task(
            "taxonomy_statistic",
            config=config,
            timeout=timeout,
        )

    def export_documents(
        self,
        config: ExportDocumentsTaskConfig,
        *,
        timeout: float | None = None,
    ) -> ExportDocumentsResult:
        return self.run_task(
            "export_documents",
            config=config,
            timeout=timeout,
        )

    def create_data_source(
        self,
        config: CreateDataSourceTaskConfig,
        *,
        timeout: float | None = None,
    ) -> CreateDataSourceResult:
        """Create a new data source.

        Parameters
        ----------
        config : CreateDataSourceTaskConfig
            Configuration for the Create Data Source task.
        timeout : float | None
            Optional timeout in seconds for this request.

        Returns
        -------
        CreateDataSourceResult
            Result containing created data source information.
        """
        return self.run_task(
            "create_data_source",
            config=config,
            timeout=timeout,
        )

    def manage_users_and_groups(
        self,
        config: ManageUsersAndGroupsTaskConfig,
        *,
        timeout: float | None = None,
    ) -> ManageUsersAndGroupsResult:
        """Manage users, groups, and their roles.

        Parameters
        ----------
        config : ManageUsersAndGroupsTaskConfig
            Configuration for the Manage Users and Groups task.
        timeout : float | None
            Optional timeout in seconds for this request.

        Returns
        -------
        ManageUsersAndGroupsResult
            Result containing users, groups, and role information.
        """
        return self.run_task(
            "manage_users_and_groups",
            config=config,
            timeout=timeout,
        )

    def read_service_alerts(
        self,
        config: ReadServiceAlertsTaskConfig,
        *,
        timeout: float | None = None,
    ) -> ReadServiceAlertsResult:
        """Read service alerts from the system.

        Parameters
        ----------
        config : ReadServiceAlertsTaskConfig
            Configuration for the Read Service Alerts task.
        timeout : float | None
            Optional timeout in seconds for this request.

        Returns
        -------
        ReadServiceAlertsResult
            Result containing service alert information.
        """
        return self.run_task(
            "read_service_alerts",
            config=config,
            timeout=timeout,
        )

    def start_application(
        self,
        config: StartApplicationTaskConfig,
        *,
        timeout: float | None = None,
    ) -> StartApplicationResult:
        """Start an application.

        Parameters
        ----------
        config : StartApplicationTaskConfig
            Configuration for the Start Application task.
        timeout : float | None
            Optional timeout in seconds for this request.

        Returns
        -------
        StartApplicationResult
            Result containing the started application URL.
        """
        return self.run_task(
            "start_application",
            config=config,
            timeout=timeout,
        )

    def create_ocr_job(
        self,
        config: CreateOcrJobTaskConfig,
        *,
        timeout: float | None = None,
    ) -> str:
        """Create an OCR job to process documents.

        This task is executed asynchronously and returns immediately.
        Use statusAndProgress() with the returned execution ID to monitor job completion.

        Parameters
        ----------
        config : CreateOcrJobTaskConfig
            Configuration for the Create OCR Job task.
        timeout : float | None
            Optional timeout in seconds for this request.

        Returns
        -------
        str
            The execution ID (UUID as string) from the async job submission.
        """
        return self.run_task_async("create_ocr_job", config=config, timeout=timeout)

    # --------------------------------------------------------------
    # Generic task execution via registry (spec definitions in task_spec.py)
    # --------------------------------------------------------------

    def run_task(
        self,
        key: str,
        *,
        config,
        timeout: float | None = None,
    ) -> Any:
        """Run a registered task by key and return typed result.

        Adding a new task:
            1. Define its Pydantic TaskConfig & Result models.
            2. Add an entry to TASK_SPECS with a parser that builds the Result.
            3. Optionally add a thin wrapper method for discoverability.
        """
        spec = TASK_SPECS.get(key)
        if not spec:
            raise KeyError(f"Unknown task key: {key}")
        # Apply per-task default overrides conditionally:
        # Only override if the current attribute value is still equal to the class default
        # (i.e., the user did not supply a custom value). For Pydantic models we can
        # inspect model_fields for defaults. If attribute is missing or equal to the default,
        # apply registry value; otherwise preserve user-provided value.
        defaults = spec.get("defaults")
        if defaults:
            # Attempt to get model field defaults (Pydantic v2 style)
            field_defaults: dict[str, Any] = {}
            try:
                # model_fields mapping: name -> FieldInfo
                for fname, finfo in getattr(config.__class__, "model_fields", {}).items():
                    if finfo.default is not None:
                        field_defaults[fname] = finfo.default
            except Exception:  # pragma: no cover - defensive
                pass
            for attr, value in defaults.items():
                try:
                    current = getattr(config, attr)
                except AttributeError:
                    # If attribute not present we skip silently
                    continue
                default_val = field_defaults.get(attr, None)
                # Override only when unchanged (equal to default or both are None)
                if (default_val is not None and current == default_val) or (
                    default_val is None and current is None
                ):
                    try:
                        setattr(config, attr, value)
                    except AttributeError:
                        continue

        task = ADPTaskRequest(
            taskType=spec["task_type"],
            taskConfiguration=config,
            taskDisplayName=spec["display_name"],
            taskDescription=spec["description"],
        )
        response = self.run(task, timeout=timeout)
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
            raise RuntimeError(f"{spec['task_type']} task completed but returned no metadata")
        try:
            return spec["parser"](metadata)
        except Exception as e:  # pragma: no cover - defensive
            raise ValueError(f"Failed to parse metadata for {spec['task_type']}: {e}")

    def run_task_async(
        self,
        key: str,
        *,
        config,
        timeout: float | None = None,
    ) -> str:
        """Run a registered task asynchronously and return execution ID.

        This method submits the task for asynchronous execution and immediately
        returns the execution ID. Use statusAndProgress() to monitor completion.

        Parameters
        ----------
        key : str
            Task key in TASK_SPECS registry (e.g., 'list_entities').
        config : BaseTaskConfig
            Task configuration object.
        timeout : float | None
            Optional timeout in seconds for this request.

        Returns
        -------
        str
            The execution ID (UUID as string) for monitoring task progress.

        Raises
        ------
        KeyError
            If the task key is not found in TASK_SPECS.
        RuntimeError
            If task submission fails or response cannot be parsed.
        """
        spec = TASK_SPECS.get(key)
        if not spec:
            raise KeyError(f"Unknown task key: {key}")

        # Apply per-task default overrides (same logic as run_task)
        defaults = spec.get("defaults")
        if defaults:
            field_defaults: dict[str, Any] = {}
            try:
                for fname, finfo in getattr(config.__class__, "model_fields", {}).items():
                    if finfo.default is not None:
                        field_defaults[fname] = finfo.default
            except Exception:  # pragma: no cover - defensive
                pass
            for attr, value in defaults.items():
                try:
                    current = getattr(config, attr)
                except AttributeError:
                    continue
                default_val = field_defaults.get(attr, None)
                if (default_val is not None and current == default_val) or (
                    default_val is None and current is None
                ):
                    try:
                        setattr(config, attr, value)
                    except AttributeError:
                        continue

        task = ADPTaskRequest(
            taskType=spec["task_type"],
            taskConfiguration=config,
            taskDisplayName=spec["display_name"],
            taskDescription=spec["description"],
        )
        response = self.run_async(task, timeout=timeout)
        if not response:
            raise RuntimeError(f"{spec['task_type']} task failed: No response received")

        # Parse response as ADPTaskResponse to access execution_id
        try:
            task_response = ADPTaskResponse(**response)
        except Exception as e:
            raise RuntimeError(f"Failed to parse {spec['task_type']} response: {e}")

        if not task_response.is_success():
            raise RuntimeError(
                f"{spec['task_type']} task failed with status: {task_response.execution_status}"
            )

        return str(task_response.execution_id)

    def close(self) -> None:
        """Close the session. The shared client is not closed."""
        pass  # Session never owns the client, so nothing to close

    def __enter__(self) -> Session:  # pragma: no cover
        return self

    def __exit__(self, exc_type, exc, tb) -> None:  # pragma: no cover
        self.close()


__all__ = ["Session"]
