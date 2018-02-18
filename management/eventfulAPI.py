import hashlib
# import md5
import urllib

import httplib2
import simplejson


class APIError(Exception):
    pass


class API:
    def __init__(self, app_key, server='api.eventful.com', cache=None):
        """Create a new Eventful API client instance.
If you don't have an application key, you can request one:
    http://api.eventful.com/keys/"""
        self.app_key = app_key
        self.server = server
        self.http = httplib2.Http(cache)

    def call(self, method, **args):
        "Call the Eventful API's METHOD with ARGS."
        # Build up the request
        args['app_key'] = self.app_key
        if hasattr(self, 'user_key'):
            args['user'] = self.user
            args['user_key'] = self.user_key
        args = urllib.parse.urlencode(args)
        url = "http://%s/json/%s?%s" % (self.server, method, args)

        # Make the request
        response, content = self.http.request(url, "GET")

        # Handle the response
        status = int(response['status'])
        if status == 200:
            try:
                return simplejson.loads(content)
            except ValueError:
                raise APIError("Unable to parse API response!")
        elif status == 404:
            raise APIError("Method not found: %s" % method)
        else:
            raise APIError("Non-200 HTTP response status: %s" % response['status'])

    def login(self, user, password):
        "Login to the Eventful API as USER with PASSWORD."
        nonce = self.call('/users/login')['nonce']
        p = hashlib.md5(password.encode()).hexdigest()
        # h.update(password.encode('utf-8'))
        # p = h.hexdigest()
        print(nonce)
        p = nonce+':'+p
        print(p)
        res = hashlib.md5(p.encode()).hexdigest()
        # h2.update(p.encode())
        # res = h2.hexdigest()
        print(res)
        # response = hashlib.md5(nonce + ':'
        #                    + hashlib.md5().update(password.encode('utf-8')).hexdigest()).hexdigest()
        login = self.call('/users/login', user=user, nonce=nonce,
                          response=res)
        print(login)
        self.user_key = login['user_key']
        self.user = user
        return user
