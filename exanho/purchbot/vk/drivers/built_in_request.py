from urllib import request, parse

from .i_vk_driver import IVkDriver

class BuildInDriver(IVkDriver):

    def get_response(self, *args, **kwargs):
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