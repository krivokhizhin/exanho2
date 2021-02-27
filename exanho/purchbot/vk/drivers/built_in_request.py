from io import BufferedIOBase
from urllib import request, parse

from .i_vk_driver import IVkDriver

class BuildInDriver(IVkDriver):

    def get(self, *args, **kwargs):
        url = args[0]
        assert isinstance(url, str)

        params = kwargs.get('params', None)

        if params:
            querystring = parse.urlencode(params)
            if '?' in url:
                url += '&'+querystring
            else:
                url += '?'+querystring
        
        resp = request.urlopen(url)
        return resp.read().decode('utf-8')

    def post(self, *args, **kwargs):
        url = args[0]
        assert isinstance(url, str)

        params = kwargs['params']
        headers = kwargs.get('headers', None)

        data = parse.urlencode(params).encode('utf-8')
        req = request.Request(url, data)
        if headers and isinstance(headers, dict):
            for key, value in headers.items():
                req.add_header(key, value)
        with request.urlopen(req) as response:
            return response.read().decode('utf-8')

    def upload_file(self, *args, **kwargs):
        upload_url = args[0]
        assert isinstance(upload_url, str)

        file_obj:BufferedIOBase = kwargs['file']
        content_type = kwargs.get('content_type', 'multipart/form-data')

        params = {'file': file_obj.read()}
        headers = {'Content-Type': content_type, 'Content-Length': len(params['file'])}

        data = parse.urlencode(params).encode('utf-8')
        req = request.Request(upload_url, data=data, headers=headers)
        with request.urlopen(req) as response:
            return response.read().decode('utf-8')