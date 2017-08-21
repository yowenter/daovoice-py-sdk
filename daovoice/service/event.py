from base_service import BaseService
from daovoice import models


class Event(BaseService):
    @property
    def resource_class(self):
        return models.Event

