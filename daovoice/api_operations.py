class Get(object):
    def get(self, **params):
        base_url = self.client._url(self.resource_class.resource_path)
        if "id" in params:
            url = "%s/%s" % (base_url, params["id"])
            result = self.client._result(self.client._get(url))

        return self.resource_class.from_resp_json(result)




