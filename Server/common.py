from enum import Enum

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MsgType(Enum):
    DEVICE = 1
    AGGREGATION = 2
    GREETINGS = 3
    DEVICES_REQUEST = 4


class Message(object):
  
    def __init__(self, msg_type: MsgType, body):
        self.__type = msg_type
        self.__body = body

    def get_type(self):
        return self.__type

    def get_body(self):
        return self.__body


class Device(object):
  
    def __init__(self, id, dataset):
        self.__id = id
        self.__dataset = dataset

    def get_id(self):
        return self.__id

    def get_dataset(self):
        return self.__dataset