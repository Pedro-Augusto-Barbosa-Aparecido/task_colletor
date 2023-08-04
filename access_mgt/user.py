import keyring

from dataclasses import dataclass
from exceptions.access_mgt import CredentialNotFound


@dataclass
class UserCredentials:
    email: str
    password: str


class UserManagement:
    KEYRING_SERVICE_NAME = "task_collector"

    @staticmethod
    def get_user_management() -> UserCredentials:
        user = keyring.get_credential(UserManagement.KEYRING_SERVICE_NAME, "")

        if user is None or user.username is None:
            raise CredentialNotFound("Credentials not found")

        return UserCredentials(email=user.username, password=user.password)

    @staticmethod
    def set_user_management(email: str, password: str) -> UserCredentials:
        keyring.set_password(
            UserManagement.KEYRING_SERVICE_NAME,
            email,
            password
        )

        return UserCredentials(email, password)
