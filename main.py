from exceptions.access_mgt import CredentialNotFound
from ms.microsoft_teams import MicrosoftTeams
from access_mgt.user import UserManagement


try:
    user = UserManagement.get_user_management()
except CredentialNotFound:
    email = input("E-mail: ")
    password = input("Password: ")

    user = UserManagement.set_user_management(email, password)


microsoft_teams = MicrosoftTeams(
    email=user.email,
    password=user.password
)

microsoft_teams.get_home_works_todo()
