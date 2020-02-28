from abc import ABC


class BaseReader(ABC):
    def __init__(self, file_name):
        self._file_name = file_name

    def load_file(self):
        pass

    def get_book_info(self):
        pass


class BaseWriter(ABC):
    def __init__(self):
        pass


class BaseBook(ABC):
    def get_plain_text(self):
        pass

    def get_info(self):
        pass
