from readbook.formats.standard import BaseReader, BaseWriter, BaseBook


class TxtReader(BaseReader):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.txt_book = self.load_file()

    def load_file(self):
        try:
            file_handler = open(self.file_name, 'r')
            txt_book = TxtBook(file_handler)
            return txt_book
        except OSError:
            print('[Error] Cannot open', self.file_name)

    def get_book_info(self):
        book_info = {'name': self.file_name, 'type': 'txt', 'file_size': ''}
        return book_info


class TxtWriter(BaseWriter):
    def __init__(self, ):
        super().__init__()


class TxtBook(BaseBook):
    def __init__(self, file_handler):
        super().__init__()
        self.file_handler = file_handler

    def get_plain_text(self, as_list=False):
        if as_list:
            return self.file_handler.readlines()
        else:
            return self.file_handler.read()

    def get_line(self, line_number):
        plain_list = self.get_plain_text(as_list=True)
        return plain_list[line_number]

    def get_info(self):
        pass
