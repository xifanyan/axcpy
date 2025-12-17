"""Configuration management for axcpy."""

from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class AxcelerateConfig(BaseSettings):
    """Application configuration using Pydantic settings.

    Configuration can be loaded from environment variables or .env file.
    """

    model_config = SettingsConfigDict(
        env_prefix="AXCELERATE_",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    adp_base_url: Optional[str] = None
    search_base_url: Optional[str] = None
    api_key: Optional[str] = None
    timeout: int = 30
    max_retries: int = 3
    verify_ssl: bool = True


# Global configuration instance
_config: Optional[AxcelerateConfig] = None


def get_config() -> AxcelerateConfig:
    """Get the global configuration instance."""
    global _config
    if _config is None:
        _config = AxcelerateConfig()
    return _config


def configure(**kwargs: object) -> None:
    """Configure axcpy with custom settings.

    Args:
        **kwargs: Configuration key-value pairs
    """
    global _config
    _config = AxcelerateConfig(**kwargs)  # type: ignore
