from readbook.formats.standard import BaseReader, BaseBook


class TxtReader(BaseReader):
    def __init__(self, file_name):
        super().__init__(file_name)
        self._txt_book = self.load_file()

    def load_file(self):
        try:
            file_handler = open(self._file_name, 'r')
            txt_book = _TxtBook(file_handler)
            return txt_book
        except OSError:
            print('[Error] Cannot open', self._file_name)

    def get_book_info(self):
        book_info = {'name': self._file_name, 'type': 'text/plain', 'file_size': '',
                     'page_numbers': self._txt_book.get_page_numbers(),
                     'word_counts': self._txt_book.get_word_counts(),
                     'read_time': self._txt_book.get_read_time()}
        return book_info


class _TxtBook(BaseBook):
    def __init__(self, file_handler):
        self._file_handler = file_handler
        self._word_counts = -1
        self._plain_list = self.get_plain_text(as_list=True)
        self._file_handler.close()

    def get_plain_text(self, as_list=False):
        if as_list:
            plain_list = self._file_handler.readlines()
            return plain_list
        else:
            return "".join(self._plain_list)

    def get_line(self, line_number):
        if line_number < len(self._plain_list):
            return self._plain_list[line_number]
        else:
            return None

    def get_word_counts(self):
        if self._word_counts == -1:
            for line in self._plain_list:
                self._word_counts += len(line.split())
            self._word_counts += 1
        return self._word_counts

    def get_read_time(self):
        return self.get_word_counts() / 265

    def get_page_numbers(self):
        return len(self._plain_list) / 25

    def get_info(self):
        pass
