import requests_mock
from page_loader.loader import download
from tests.helpers import read_file
import tempfile
import requests


def test_download():
    mock_url = 'https://test_page.com/first_page'
    with requests_mock.Mocker() as mock:
        mock.get(mock_url, text="test-page")
        with tempfile.TemporaryDirectory() as tempdir:
            file_path = download(mock_url, tempdir)
            assert 'test-page-com-first-page.html' == file_path.split('/')[-1]
            page = requests.get('https://test_page.com/first_page')
            assert read_file(file_path) == page.text
