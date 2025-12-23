from __future__ import annotations

import json
import logging

import httpx

from axcpy.adp.models.request import ADPTaskRequest

logger = logging.getLogger(__name__)


class ADPClient:
    """HTTP client for interacting with ADP endpoints using PUT-only semantics.

    NOTE: File renamed from `adp_client.py` to `client.py` for concise imports.

    Parameters
    ----------
    base_url: str
        Base URL for the ADP service (e.g. https://example.com/api)
    ignore_tls: bool, default False
        If True, disables TLS certificate verification (useful for testing against self-signed hosts).
    timeout: float | httpx.Timeout | None
        Optional default timeout applied to all requests (can be overridden per call).
    headers: dict[str, str] | None
        Default headers merged with per-call headers.
    debug: bool, default False
        If True, logs the request payload as a JSON string at DEBUG level.
    """

    def __init__(
        self,
        base_url: str,
        *,
        ignore_tls: bool = False,
        timeout: float | None = None,
        headers: dict[str, str] | None = None,
        debug: bool = False,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.ignore_tls = ignore_tls
        self.debug = debug
        self._default_headers = headers or {"Content-Type": "application/json"}
        client_timeout = (
            httpx.Timeout(timeout) if isinstance(timeout, (int, float)) else timeout
        )
        self._client = httpx.Client(
            base_url=self.base_url,
            timeout=client_timeout,
            verify=not ignore_tls,  # invert for httpx verify flag
        )

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "ADPClient":  # pragma: no cover
        return self

    def __exit__(self, exc_type, exc, tb) -> None:  # pragma: no cover
        self.close()

    def _execute_task(
        self,
        task: ADPTaskRequest,
        endpoint: str,
        *,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
    ) -> httpx.Response:
        """Common task execution logic."""
        merged_headers = {**self._default_headers, **(headers or {})}
        payload = task.as_payload()

        # Log request payload if debug mode is enabled
        if self.debug and logger.isEnabledFor(logging.DEBUG):
            try:
                payload_str = json.dumps(payload, indent=2)
                logger.debug(
                    "Request to %s:\nPayload:\n%s",
                    endpoint,
                    payload_str,
                )
            except Exception as e:
                logger.debug("Failed to serialize request payload: %s", e)

        response = self._client.put(
            endpoint,
            json=payload,
            headers=merged_headers,
            timeout=timeout,
        )

        # Log response if debug mode is enabled
        if self.debug and logger.isEnabledFor(logging.DEBUG):
            try:
                response_data = response.json()
                response_str = json.dumps(response_data, indent=2)
                logger.debug(
                    "Response from %s (status=%s):\n%s",
                    endpoint,
                    response.status_code,
                    response_str,
                )
            except Exception as e:
                logger.debug(
                    "Response from %s (status=%s): <non-JSON or failed to parse>",
                    endpoint,
                    response.status_code,
                )

        response.raise_for_status()
        return response

    def run(
        self,
        task: ADPTaskRequest,
        *,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
    ) -> httpx.Response:
        """Send a task to the ADP service via PUT (synchronous execution)."""
        return self._execute_task(
            task,
            "/adp/rest/api/task/executeAdpTask",
            headers=headers,
            timeout=timeout,
        )

    def run_async(
        self,
        task: ADPTaskRequest,
        *,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
    ) -> httpx.Response:
        """Send a task to the ADP service via PUT (asynchronous execution)."""
        return self._execute_task(
            task,
            "/adp/rest/api/task/executeAdpTaskAsync",
            headers=headers,
            timeout=timeout,
        )

    def statusAndProgress(
        self,
        task: ADPTaskRequest,
        *,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
    ) -> httpx.Response:
        """Check the status and progress of an asynchronously submitted task."""
        return self._execute_task(
            task,
            "/adp/rest/api/task/statusAndProgress",
            headers=headers,
            timeout=timeout,
        )


__all__ = ["ADPClient"]
