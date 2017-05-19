# -*- coding: utf-8 -*-


class BaseService(object):
    def __init__(self, client):
        self.client = client

    def resource_url(self, _id=None):
        base_url = self.client._url(self.resource_class.resource_path)
        if _id is None:
            return base_url
        else:
            return "%s/%s" % (base_url, _id)
