import requests

from io import BufferedIOBase
from uuid import uuid4

from .i_vk_driver import IVkDriver

class RequestsDriver(IVkDriver):

    def get(self, *args, **kwargs):
        url = args[0]
        assert isinstance(url, str)

        params = kwargs.get('params', None)
        resp = requests.get(url, params=params)        
        return resp.text

    def post(self, *args, **kwargs):
        url = args[0]
        assert isinstance(url, str)

        params = kwargs.get('params', None)

        resp = requests.post(url, data=params)
        return resp.text

    def upload_file(self, *args, **kwargs):
        upload_url = args[0]
        assert isinstance(upload_url, str)

        filename = kwargs.get('filename', str(uuid4()))
        file_obj:BufferedIOBase = kwargs['file']
        content_type = kwargs.get('content_type', 'multipart/form-data')

        files = {'file': (filename, file_obj, content_type)}
        resp = requests.post(upload_url, files=files)
        return resp.text
