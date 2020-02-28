import xml.etree.ElementTree as ET
import zipfile

from readbook.formats.standard import BaseReader, BaseBook


class EPUBReader(BaseReader):
    def __init__(self, file_name):
        super().__init__(file_name)
        self._zip_file_handler = None
        self._epub_book = self.load_file()

    def load_file(self):
        try:
            if not zipfile.is_zipfile(self._file_name):
                raise zipfile.BadZipFile()

            self._zip_file_handler = zipfile.ZipFile(self._file_name, mode='r')
            epub_book = EPUBBook(self._zip_file_handler)

            if not self._check_mimetype():
                pass

            root_file = self._get_root_file_path()

            return epub_book

        except zipfile.BadZipFile:
            print('[Error]', self._file_name, 'is not compressed properly')
        except OSError:
            print('[Error] Cannot open', self._file_name)

    def _check_mimetype(self):
        with self._zip_file_handler.open('mimetype') as mimetype:
            if mimetype.readline() is 'application/epub+zip':
                return True
            else:
                return False

    def _get_root_file_path(self):
        with self._zip_file_handler.open('META-INF/container.xml') as container:
            xml_text = container.read()
            root = ET.fromstring(xml_text).getroot()
            namespace = '{urn:oasis:names:tc:opendocument:xmlns:container}'

            for root_file in root.findall(namespace + '(rootfiles)'):
                full_path = root_file.attrib['full-path']
                media_type = root_file.attrib['media-type']
            if media_type is 'application/oebps-package+xml':
                return full_path
            else:
                return None

    def _parse_root_file(self):
        pass

    def get_book_info(self):
        pass


class EPUBBook(BaseBook):
    def __init__(self, file_handler):
        super().__init__()
        self._file_handler = file_handler

    def get_plain_text(self):
        pass

    def get_info(self):
        pass
