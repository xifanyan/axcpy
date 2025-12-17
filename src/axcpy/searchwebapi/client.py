"""SearchWebAPI client wrapper for Kiota-generated client."""


class SearchWebAPIClient:
    """Wrapper for Kiota-generated SearchWebAPI client.

    This provides a convenient interface around the auto-generated client.
    """

    def __init__(self, base_url: str, api_key: str | None = None) -> None:
        self.base_url = base_url
        self.api_key = api_key
        # TODO: Initialize Kiota-generated client
