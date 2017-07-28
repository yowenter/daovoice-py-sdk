#!/usr/bin/env python
# coding=utf-8
# Created by kebe

from base_service import BaseService
from daovoice import models
from daovoice.api_operations import SimpleAll, Save, Get


class Subscription(BaseService, SimpleAll, Save, Get):
    @property
    def resource_class(self):
        return models.Subscription

