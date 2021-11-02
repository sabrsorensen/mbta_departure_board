import requests


class MbtaHeaderAuth(requests.auth.AuthBase):
    '''
    Class to add MBTA API key header to jsonapi_request calls
    '''

    def __init__(self, api_key: str):
        self.api_key = api_key

    def __call__(self, request: requests.PreparedRequest):
        '''
        Add the MBTA API key to the header of all requests using this Auth handler
        '''
        request.headers['X-API-Key'] = self.api_key
        return request
