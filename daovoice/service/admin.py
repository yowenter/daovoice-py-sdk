from base_service import BaseService
from daovoice import models
from daovoice.api_operations import SimpleAll


class Admin(BaseService, SimpleAll):
    @property
    def resource_class(self):
        return models.Admin

