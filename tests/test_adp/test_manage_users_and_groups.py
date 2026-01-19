"""Test manage_users_and_groups models."""

from axcpy.adp.models.manage_users_and_groups import (
    UserDefinition,
    GroupDefinition,
    UserToGroup,
    ApplicationRoles,
    Group,
    User,
    ManageUsersAndGroupsTaskConfig,
    ManageUsersAndGroupsResult,
)


def test_user_definition() -> None:
    """Test UserDefinition model."""
    user = UserDefinition(
        Enabled=True,
        ExternalUser=False,
        Password="test123",
        Remove=False,
        UserName="testuser",
    )
    assert user.UserName == "testuser"
    assert user.Enabled is True
    assert user.ExternalUser is False


def test_group_definition() -> None:
    """Test GroupDefinition model."""
    group = GroupDefinition(
        Enabled=True,
        GroupName="testgroup",
        Remove=False,
    )
    assert group.GroupName == "testgroup"
    assert group.Enabled is True


def test_manage_users_and_groups_config() -> None:
    """Test ManageUsersAndGroupsTaskConfig model."""
    config = ManageUsersAndGroupsTaskConfig(
        adp_manageUsersAndGroups_AppIdsToFilterFor="app1,app2",
        adp_manageUsersAndGroups_GroupUserIdsToFilterFor="group1,group2",
    )
    assert config.adp_manageUsersAndGroups_AppIdsToFilterFor == "app1,app2"
    assert config.adp_loggingEnabled is True  # From BaseTaskConfig


def test_manage_users_and_groups_result() -> None:
    """Test ManageUsersAndGroupsResult model."""
    result = ManageUsersAndGroupsResult(
        adp_manageUsersAndGroups_output_file_name="/path/to/output.json",
    )
    assert result.adp_manageUsersAndGroups_output_file_name == "/path/to/output.json"
    assert result.adp_manageUsersAndGroups_json_output.Groups == {}
    assert result.adp_manageUsersAndGroups_json_output.Users == {}


def test_group_model() -> None:
    """Test Group model."""
    group = Group(
        DisplayName="Test Group",
        Name="testgroup",
        Description="Test description",
        Existent=True,
        Users=["user1", "user2"],
    )
    assert group.Name == "testgroup"
    assert group.DisplayName == "Test Group"
    assert len(group.Users) == 2


def test_user_model() -> None:
    """Test User model."""
    user = User(
        DisplayName="Test User",
        Name="testuser",
        Description="Test description",
        Existent=True,
        External=False,
        EmailAddress="test@example.com",
    )
    assert user.Name == "testuser"
    assert user.DisplayName == "Test User"
    assert user.External is False
    assert user.EmailAddress == "test@example.com"


def test_user_definition_validation_empty_username() -> None:
    """Test that UserDefinition raises error for empty UserName when Remove is False."""
    import pytest
    from pydantic import ValidationError

    with pytest.raises(ValidationError) as exc_info:
        UserDefinition(
            Enabled=True,
            ExternalUser=False,
            Password="test123",
            Remove=False,
            UserName="",  # Empty UserName with Remove=False should fail
        )
    assert "UserName must be provided and cannot be empty" in str(exc_info.value)


def test_user_definition_validation_with_remove() -> None:
    """Test that UserDefinition allows empty UserName when Remove is True."""
    user = UserDefinition(
        Enabled=False,
        ExternalUser=False,
        Password="",
        Remove=True,
        UserName="",  # Empty UserName is allowed when Remove=True
    )
    assert user.Remove is True
    assert user.UserName == ""


def test_group_definition_validation_empty_groupname() -> None:
    """Test that GroupDefinition raises error for empty GroupName when Remove is False."""
    import pytest
    from pydantic import ValidationError

    with pytest.raises(ValidationError) as exc_info:
        GroupDefinition(
            Enabled=True,
            GroupName="",  # Empty GroupName with Remove=False should fail
            Remove=False,
        )
    assert "GroupName must be provided and cannot be empty" in str(exc_info.value)


def test_group_definition_validation_with_remove() -> None:
    """Test that GroupDefinition allows empty GroupName when Remove is True."""
    group = GroupDefinition(
        Enabled=False,
        GroupName="",  # Empty GroupName is allowed when Remove=True
        Remove=True,
    )
    assert group.Remove is True
    assert group.GroupName == ""


def test_user_to_group_validation() -> None:
    """Test that UserToGroup raises error for empty names when Remove is False."""
    import pytest
    from pydantic import ValidationError

    # Test empty UserName
    with pytest.raises(ValidationError) as exc_info:
        UserToGroup(
            Enabled=True,
            GroupName="TestGroup",
            Remove=False,
            UserName="",  # Empty UserName should fail
        )
    assert "UserName must be provided and cannot be empty" in str(exc_info.value)

    # Test empty GroupName
    with pytest.raises(ValidationError) as exc_info:
        UserToGroup(
            Enabled=True,
            GroupName="",  # Empty GroupName should fail
            Remove=False,
            UserName="testuser",
        )
    assert "GroupName must be provided and cannot be empty" in str(exc_info.value)


def test_application_roles_validation() -> None:
    """Test that ApplicationRoles raises error for empty fields when Enabled is True."""
    import pytest
    from pydantic import ValidationError

    # Test empty GroupOrUserName
    with pytest.raises(ValidationError) as exc_info:
        ApplicationRoles(
            GroupOrUserName="",  # Empty GroupOrUserName should fail
            Enabled=True,
            ApplicationIdentifier="app1",
            Roles="role1",
        )
    assert "GroupOrUserName must be provided and cannot be empty" in str(exc_info.value)

    # Test empty ApplicationIdentifier
    with pytest.raises(ValidationError) as exc_info:
        ApplicationRoles(
            GroupOrUserName="testuser",
            Enabled=True,
            ApplicationIdentifier="",  # Empty ApplicationIdentifier should fail
            Roles="role1",
        )
    assert "ApplicationIdentifier must be provided and cannot be empty" in str(exc_info.value)


def test_application_roles_validation_disabled() -> None:
    """Test that ApplicationRoles allows empty fields when Enabled is False."""
    app_roles = ApplicationRoles(
        GroupOrUserName="",  # Empty GroupOrUserName is allowed when Enabled=False
        Enabled=False,
        ApplicationIdentifier="",  # Empty ApplicationIdentifier is allowed when Enabled=False
        Roles="",
    )
    assert app_roles.Enabled is False


if __name__ == "__main__":
    test_user_definition()
    print("[+] UserDefinition test passed")
    test_group_definition()
    print("[+] GroupDefinition test passed")
    test_manage_users_and_groups_config()
    print("[+] ManageUsersAndGroupsTaskConfig test passed")
    test_manage_users_and_groups_result()
    print("[+] ManageUsersAndGroupsResult test passed")
    test_group_model()
    print("[+] Group model test passed")
    test_user_model()
    print("[+] User model test passed")
    print("\nAll tests passed!")
