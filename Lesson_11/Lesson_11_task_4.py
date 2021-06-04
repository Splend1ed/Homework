import json


class CustomException(Exception):
    Lesson_11 = False

    def __init__(self, msg):
        self.msg = msg
        if self.Lesson_11 is not False:
            with open('logs.txt', 'w+') as logs_doc:
                json.dump(self.msg, logs_doc)


try:
    CustomException.Lesson_11 = 'hsdfgjh'
    raise CustomException
except:
    massage = CustomException('Tu dyrak? Peredelai')
