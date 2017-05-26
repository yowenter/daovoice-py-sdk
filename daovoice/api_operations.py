class Get(object):
    def get(self, **params):
        url = self.resource_url(params.get("id"))

        result = self.client._result(self.client._get(url))

        return self.resource_class.from_resp_json(result)


class SimpleAll(object):
    def all(self, **kwargs):
        url = self.resource_url()

        result = self.client._result(self.client._get(url))

        return self.resource_class.from_resp_json(result)


class Save(object):
    def create(self, **kwargs):
        url = self.resource_url()
        result = self.client._result(self.client._post_json(url, kwargs))
        
        return self.resource_class.from_resp_json(result)
    
    
    

class Pagination(object):
    pass

    
    
        
    
    
    
