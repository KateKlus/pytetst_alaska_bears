from .Common import Common
import requests


class Api(Common):

    def create_bear(self, base_url, bear_json):
        """
        Creating bear

        Args:
            base_url: base url
            bear_json: data for creating bear in json
        Return:
            Api-response - bear id
        """
        response = requests.post(url=f'{base_url}/bear', json=bear_json)
        return response

    def get_all_bears(self, base_url):
        """
        Getting all bears info

        Args:
            base_url: base url
        Return:
            Api-response - all bears info
        """
        response = requests.get(url=f'{base_url}/bear')
        return response

    def get_bear_by_id(self, base_url, bear_id):
        """
        Getting bear info by id

        Args:
            base_url: base url
            bear_id: bear id
        Return:
            Api-response - bear info
        """
        response = requests.get(url=f'{base_url}/bear/{bear_id}')
        return response

    def update_bear_by_id(self, base_url, bear_id, bear_json):
        """
        Updating bear info by id

        Args:
            base_url: base url
            bear_id: bear id
            bear_json: new bear info
        Return:
            Api-response - status code
        """
        response = requests.put(url=f'{base_url}/bear/{bear_id}', json=bear_json)
        return response

    def delete_bear_by_id(self, base_url, bear_id):
        """
        Updating bear info by id

        Args:
            base_url: base url
            bear_id: bear id
        Return:
            Api-response - status code
        """
        response = requests.delete(url=f'{base_url}/bear/{bear_id}')
        return response

    def delete_all_bears(self, base_url):
        """
        Updating bear info by id

        Args:
            base_url: base url
        Return:
            Api-response - status code
        """
        response = requests.delete(url=f'{base_url}/bear')
        return response
