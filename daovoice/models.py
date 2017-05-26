# -*-encoding:utf-8-*-


from utils.data_mapper import DataMapperBase


class Model(DataMapperBase):
    def __init__(self, src_data):
        super(Model, self).__init__(src_data=src_data)

        for k, v in iter(self):
            setattr(self, k, v)

        self.changed_attributes = []

    @classmethod
    def from_resp_json(cls, resp_json):
        if isinstance(resp_json, dict):
            return cls(resp_json)
        elif isinstance(resp_json, list):
            return [cls(l) for l in resp_json]


    def __setattr__(self, key, value):
        if hasattr(self, key) and getattr(self, key) != value:
            self.changed_attributes.append(key)

        super(Model, self).__setattr__(key, value)
        
        
    
        
    
    



class Conversation(Model):
    resource_path = "conversations"
    mapper = {
        "conversation_parts": ["conversation_parts", "daovoice.models.ConversationPart"],
        "conversation_message": ["conversation_message", "daovoice.models.ConversationMessage"],
        "user": ["user", "daovoice.models.User"]
    }


class ConversationPart(Model):
    mapper = {"author": ["author", "daovoice.models.Author"]}


class ConversationMessage(Model):
    mapper = {"author": ["author", "daovoice.models.Author"]}


class Author(Model):
    mapper = {
        "companies": ["companies", "daovoice.models.Company"]
    }


class Admin(Author):
    resource_path = "admins"


class User(Author):
    resource_path = "users"


class Company(Model):
    pass

