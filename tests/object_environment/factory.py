from tests.object_environment.environments.club import ClubEnvironment
from tests.object_environment.environments.member import MemberEnvironment
from tests.object_environment.environments.trainee import TraineeEnvironment
from tests.object_environment.environments.user import UserEnvironment
from tests.object_environment.provider import Provider


class EnvironmentFactory:

    provider = Provider()
    User = UserEnvironment(provider)
    Club = ClubEnvironment(provider)
    Member = MemberEnvironment(provider)
    Trainee = TraineeEnvironment(provider)
