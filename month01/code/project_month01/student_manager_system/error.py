class NameValueError(Exception):
    def __init__(self, message, name_value, id, code_line):
        self.message = message
        self.name_value = name_value
        self.id = id
        self.code_line = code_line


class AgeValueError(Exception):
    def __init__(self, message):
        self.message = message


class ScoreValueError(Exception):
    def __init__(self, message):
        self.message = message

