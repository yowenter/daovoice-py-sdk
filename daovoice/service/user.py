from base_service import BaseService
from daovoice import models
from daovoice.api_operations import Save




class User(BaseService,Save):
    @property
    def resource_class(self):
        return models.User










