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
        
        u = request.urlopen(url)
        return u.read().decode('utf-8')

    def post(self, *args, **kwargs):
        url = args[0]
        assert isinstance(url, str)

        params = kwargs.get('params', None)

        data = parse.urlencode(params).encode('utf-8')
        req = request.Request(url, data)
        with request.urlopen(req) as response:
            return response.read().decode('utf-8')