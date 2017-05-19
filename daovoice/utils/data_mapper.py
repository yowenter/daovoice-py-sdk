# -*-encoding:utf-8 -*-

import logging
import six
import importlib

LOG = logging.getLogger(__name__)


def get_cls_by_name(name):
    names = name.rsplit(".")
    if len(names) >= 2:
        module_names = names[:-1]
        cls_name = names[-1]
        module_name = '.'.join(module_names)
        module = importlib.import_module(module_name)
        LOG.debug("Get class by name :`%s`, find module `%s`, cls_name `%s`", name, module, cls_name)
        return getattr(module, cls_name)
    else:
        cls = globals().get(name)
        LOG.debug("Get class by name in globals `%s` ,`%s`", name, cls)
        return cls


class MappingMode:
    strict = "strict"


class DataMapperBase(object):
    '''
    For data model convert

    '''
    mapper = dict()

    def __init__(self, src_data, mode=None):
        assert isinstance(src_data, dict), "Src data is not dict `%s` " % str(src_data)
        self.src_data = src_data
        self.map_mode = mode

    def map_key(self, key):
        target = self.mapper.get(key)
        LOG.debug("DataMapper mapping from `%s` to `%s`", key, target)
        if target is None:
            if self.map_mode == MappingMode.strict:
                return None
            else:
                return key, self.src_data[key]

        if isinstance(target, list):
            assert len(target) == 2, "mapper target list `%s` length is not 2 " % str(target)
            target_key, target_cls_name = target
            target_cls = get_cls_by_name(target_cls_name)
            assert target_cls is not None, "Unknown DataMapper cls `%s`" % str(
                target_cls)
            value = self.src_data[key]
            if isinstance(value, dict):
                return target_key, target_cls(self.src_data[key])
            else:
                return target_key, [target_cls(v) for v in value]
        else:
            target_key = target
            assert isinstance(target_key, six.string_types), "Target key `%s` is not string" % str(target_key)
            return target_key, self.src_data[key]

    def __iter__(self):

        for k in self.src_data.keys():
            key_value = self.map_key(k)
            if key_value is None:
                LOG.info("Key `%s` has no target", k)
                continue
            new_key, value = key_value
            yield new_key, value


if __name__ == '__main__':
    data_1_mapper = {
        "a": "A",
        "o": ["O", "UpperData2Mapper"]
    }
    data_2_mapper = {
        "p": "P",
        "q": "Q",
        "r": ["R", "UpperData3Mapper"]
    }

    data_3_mapper = {
        'x': "X"
    }


    class UpperData1Mapper(DataMapperBase):
        mapper = data_1_mapper


    class UpperData2Mapper(DataMapperBase):
        mapper = data_2_mapper


    class UpperData3Mapper(DataMapperBase):
        mapper = data_3_mapper


    example_data = {
        "a": "1",
        "b": "2",
        "c": "3",
        "o":
            {
                "p": "1",
                "q": "2",
                "r": {"x": 1}
            }

    }
    for i, v in iter(UpperData1Mapper(example_data, mode=MappingMode.strict)):
        print i, v
