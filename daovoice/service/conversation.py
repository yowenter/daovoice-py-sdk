from base_service import BaseService
from daovoice.api_operations import Get
from daovoice import models


class Conversation(BaseService, Get):
    @property
    def resource_class(self):
        return models.Conversation

    def reply(self, **params):
        url = self.resource_url(params['id'])
        url = "%s/reply" % url

        admin_id = params.get("admin_id")
        message_type = params.get("message_type", "comment")
        body = params.get("body")

        post_data = dict(
            admin={
                'admin_id': admin_id
            },
            message_type=message_type,
            body=body
        )

        self.client._post_json(url, post_data)

    def assign(self, **params):
        pass
