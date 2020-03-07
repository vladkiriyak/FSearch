
def get_message_type(request: dict):
    if "message" in request.keys():
        if "document" in request['message'].keys():
            return "document"
        elif "text" in request['message'].keys():
            return "text"
    else:
        return None

