#klasa logger do zapisu logów
class Logger:
    def __init__(self, file_name):
        self.file_name = file_name

    def log (self, message):
        with open(self.file_name, 'a', encoding='UTF-8') as f:
            f.write(message +'\n')
