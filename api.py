
import json
import requests


class PetFriends:
    """API библиотека к веб приложению Pet Friends"""

    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru/'

    def get_api_key(self, email: str, password: str) -> json:
        """This method allows to get API key which should be used for other API methods."""

        headers = {
            'email': email,
            'password': password,
        }
        res = requests.get(self.base_url +'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


    def get_list_of_pets(self, auth_key: str, filter: str ='my_pets') -> json:
        """This method allows to get the list of pets."""

        headers = {
            'auth_key': auth_key,
            'filter': filter,
        }
        res = requests.get(self.base_url + 'api/pets', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


    def post_add_new_pet(self, auth_key: str, name: str, animal_type: str, age: int, pet_photo: str) -> json:
        """This method allows to add information about new pet."""

        headers = {
            'auth_key': auth_key,
        }
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
            'pet_photo': pet_photo,
        }
        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


    def delete_pet(self, auth_key: str, pet_id: str) -> json:
        """This method allows to delete information about pet from database."""

        headers = {
            'auth_key': auth_key,
        }
        res = requests.delete(self.base_url + 'api/pets' + pet_id, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result


    def put_update_pet_info(self, auth_key: str, pet_id: str, name: str = "", animal_type: str = "", age: int = 0) -> json:
        """This method allows to update information about pet."""

        headers = {
            'auth_key': auth_key,
        }
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        res = requests.put(self.base_url + 'api/pets' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
