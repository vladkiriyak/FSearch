from abc import ABC, abstractmethod


def get_message_type(request: dict):
    if "message" in request.keys():
        if "document" in request['message'].keys():
            return "document"
        elif "text" in request['message'].keys():
            return "text"
    else:
        return None


def create_message(request_info: dict):
    message_type = get_message_type(request_info)

    if message_type == "text":
        return TextMessage(request_info)
    elif message_type == "document":
        return DocumentMessage(request_info)


class Message(ABC):

    @abstractmethod
    def processing(self):
        pass


class DocumentMessage(Message):

    def processing(self):
        pass

    def __init__(self, request_info: dict):
        pass


class TextMessage(Message):

    def __init__(self, request_info: dict):
        pass

    def processing(self):
        pass
