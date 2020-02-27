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
        book_info = {'name': self.file_name, 'type': 'txt', 'file_size': '',
                     'page_numbers': self.txt_book.get_page_numbers(),
                     'word_counts': self.txt_book.get_word_counts(),
                     'read_time': self.txt_book.get_read_time()}
        return book_info


class TxtWriter(BaseWriter):
    def __init__(self, ):
        super().__init__()


class TxtBook(BaseBook):
    def __init__(self, file_handler):
        super().__init__()
        self.file_handler = file_handler
        self.plain_list = self.get_plain_text(as_list=True)
        self.word_counts = -1

    def get_plain_text(self, as_list=False):
        if as_list:
            if not self.plain_list:
                self.plain_list = self.file_handler.readlines()
            return self.plain_list
        else:
            return self.file_handler.read()

    def get_line(self, line_number):
        if line_number < len(self.plain_list):
            return self.plain_list[line_number]
        else:
            return None

    def get_word_counts(self):
        if self.word_counts == -1:
            for line in self.plain_list:
                self.word_counts += len(line.split())
            self.word_counts += 1
        return self.word_counts

    def get_read_time(self):
        return self.get_word_counts() / 265

    def get_page_numbers(self):
        return len(self.plain_list) / 25

    def get_info(self):
        pass
