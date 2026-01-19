from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field, model_validator

from .base import BaseTaskConfig

__all__ = [
    "UserDefinition",
    "GroupDefinition",
    "UserToGroup",
    "ApplicationRoles",
    "Group",
    "User",
    "UsersAndGroups",
    "ManageUsersAndGroupsTaskConfig",
    "ManageUsersAndGroupsResult",
]


class UserDefinition(BaseModel):
    """Definition for a user in the Manage Users and Groups task."""

    model_config = {"populate_by_name": True}

    Enabled: bool = Field(default=True, alias="Enabled")
    ExternalUser: bool = Field(default=False, alias="External user")
    Password: str = Field(default="", alias="Password")
    Remove: bool = Field(default=False, alias="Remove")
    UserName: str = Field(default="", alias="User name")

    @model_validator(mode="after")
    def validate_username(self) -> UserDefinition:
        """Validate that UserName is provided and not empty unless Remove is True."""
        if self.Remove is False and not self.UserName.strip():
            raise ValueError(
                "UserName must be provided and cannot be empty when Remove is False"
            )
        return self


class GroupDefinition(BaseModel):
    """Definition for a group in the Manage Users and Groups task."""

    model_config = {"populate_by_name": True}

    Enabled: bool = Field(default=True, alias="Enabled")
    GroupName: str = Field(default="", alias="Group name")
    Remove: bool = Field(default=False, alias="Remove")

    @model_validator(mode="after")
    def validate_group_name(self) -> GroupDefinition:
        """Validate that GroupName is provided and not empty unless Remove is True."""
        if self.Remove is False and not self.GroupName.strip():
            raise ValueError(
                "GroupName must be provided and cannot be empty when Remove is False"
            )
        return self


class UserToGroup(BaseModel):
    """Assignment of a user to a group in the Manage Users and Groups task."""

    model_config = {"populate_by_name": True}

    Enabled: bool = Field(default=True, alias="Enabled")
    GroupName: str = Field(default="", alias="Group name")
    Remove: bool = Field(default=False, alias="Remove")
    UserName: str = Field(default="", alias="User name")

    @model_validator(mode="after")
    def validate_names(self) -> UserToGroup:
        """Validate names are provided when Remove is False."""
        if self.Remove is False:
            if not self.UserName.strip():
                raise ValueError(
                    "UserName must be provided and cannot be empty when Remove is False"
                )
            if not self.GroupName.strip():
                raise ValueError(
                    "GroupName must be provided and cannot be empty when Remove is False"
                )
        return self


class ApplicationRoles(BaseModel):
    """Application roles for a user or group in the Manage Users and Groups task."""

    model_config = {"populate_by_name": True}

    GroupOrUserName: str = Field(default="", alias="Group or user name")
    Enabled: bool = Field(default=True, alias="Enabled")
    ApplicationIdentifier: str = Field(default="", alias="Application identifier")
    Roles: str = Field(default="", alias="Roles")

    @model_validator(mode="after")
    def validate_fields(self) -> ApplicationRoles:
        """Validate fields are not empty when Enabled is True."""
        if self.Enabled is True:
            if not self.GroupOrUserName.strip():
                raise ValueError(
                    "GroupOrUserName must be provided and cannot be empty when Enabled is True"
                )
            if not self.ApplicationIdentifier.strip():
                raise ValueError(
                    "ApplicationIdentifier must be provided and cannot be empty "
                    "when Enabled is True"
                )
        return self


class UserGroupCommon(BaseModel):
    """Common fields for users and groups."""

    DisplayName: str = Field(default="")
    Name: str = Field(default="")
    Description: str = Field(default="")
    Existent: bool = Field(default=False)


class Group(BaseModel):
    """Represents a group with its associated users."""

    DisplayName: str = Field(default="")
    Name: str = Field(default="")
    Description: str = Field(default="")
    Existent: bool = Field(default=False)
    Users: list[str] = Field(default_factory=list)


class User(BaseModel):
    """Represents a user with additional information."""

    DisplayName: str = Field(default="")
    Name: str = Field(default="")
    Description: str = Field(default="")
    Existent: bool = Field(default=False)
    External: bool = Field(default=False)
    EmailAddress: str = Field(default="")


class UsersAndGroups(BaseModel):
    """Container for users and groups in the Manage Users and Groups task."""

    Groups: dict[str, Group] = Field(default_factory=dict)
    Users: dict[str, User] = Field(default_factory=dict)


# ruff: noqa: N815 - Field names must match API specification


class ManageUsersAndGroupsTaskConfig(BaseTaskConfig):
    """Configuration model for Manage Users and Groups task."""

    adp_manageUsersAndGroups_outputFilename: str = Field(
        default="adp_manageUsersAndGroups_output_file_name"
    )
    adp_manageUsersAndGroups_file: str = Field(default="output.json")
    adp_manageUsersAndGroups_outputJson: str = Field(
        default="adp_manageUsersAndGroups_json_output"
    )
    adp_manageUsersAndGroups_userDefinition: list[dict[str, Any]] = Field(
        default_factory=list, alias="adp_manageUsersAndGroups_userDefinition"
    )
    adp_manageUsersAndGroups_groupDefinition: list[dict[str, Any]] = Field(
        default_factory=list, alias="adp_manageUsersAndGroups_groupDefinition"
    )
    adp_manageUsersAndGroups_assignmentUserToGroup: list[dict[str, Any]] = Field(
        default_factory=list, alias="adp_manageUsersAndGroups_assignmentUserToGroup"
    )
    adp_manageUsersAndGroups_addApplicationRoles: list[dict[str, Any]] = Field(
        default_factory=list, alias="adp_manageUsersAndGroups_addApplicationRoles"
    )
    adp_manageUsersAndGroups_AppIdsToFilterFor: str = Field(default="")
    adp_manageUsersAndGroups_GroupUserIdsToFilterFor: str = Field(default="")
    adp_manageUsersAndGroups_ReturnAllUsersUnderGroup: str = Field(default="")


class ManageUsersAndGroupsResult(BaseModel):
    """Typed representation of Manage Users and Groups execution metadata.

    Example shape:
    {
        "adp_manageUsersAndGroups_output_file_name": "path/to/output.json",
        "adp_manageUsersAndGroups_json_output": {
            "groups": {
                "group1": {
                    "UserGroupCommon": {
                        "displayName": "Group 1",
                        "name": "group1",
                        "description": "Description",
                        "existent": true
                    },
                    "users": ["user1", "user2"]
                }
            },
            "users": {
                "user1": {
                    "UserGroupCommon": {
                        "displayName": "User 1",
                        "name": "user1",
                        "description": "",
                        "existent": true
                    },
                    "external": false,
                    "emailAddress": "user1@example.com"
                }
            },
            "applications": {
                "app1": {
                    "groups": {...},
                    "users": {...}
                }
            }
        }
    }

    The result contains users, groups, and application-specific role assignments.
    Each group maps to its Group structure with associated users.
    Each user maps to its User structure with email and external status.
    Applications contain nested users and groups with role information.
    """

    adp_manageUsersAndGroups_output_file_name: str
    adp_manageUsersAndGroups_json_output: UsersAndGroups = Field(
        default_factory=UsersAndGroups
    )
