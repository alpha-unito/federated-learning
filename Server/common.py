from enum import Enum

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
        return self.__type