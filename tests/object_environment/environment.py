from tests.object_environment.provider import Provider


class ObjectEnvironment:

    def __init__(self, provider: Provider) -> None:
        self.provider = provider
        super().__init__()

    def create(self, **kwargs):
        raise NotImplementedError()

    def _default(self):
        raise NotImplementedError()

    def _create_references_if_missing(self, obj):
        raise NotImplementedError()
