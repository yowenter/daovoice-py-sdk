from base_service import BaseService
from daovoice.api_operations import Get
from daovoice import models


class Conversation(BaseService, Get):
    def reply(self):
        pass

    @property
    def resource_class(self):
        return models.Conversation


