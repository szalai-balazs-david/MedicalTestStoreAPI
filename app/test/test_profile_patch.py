import json

from app.test.base_test_class import BaseTestClass, basic_auth_header, advanced_auth_header


class GetTestsTestCase(BaseTestClass):

    def test_patch_profile_endpoint_with_basic_level_authorization_updates_user_info(self):
        patch_data = {'name': 'newName'}

        res = self.client().get('/profile', headers=basic_auth_header())
        data = json.loads(res.data)
        message = self.check_if_operation_was_successful_and_get_payload(data)
        self.assertFalse(message['name'] == patch_data['name'])

        res = self.client().patch('/profile', json=patch_data, headers=basic_auth_header(True))
        data = json.loads(res.data)
        self.check_if_operation_was_successful_and_get_payload(data)

        res = self.client().get('/profile', headers=basic_auth_header())
        data = json.loads(res.data)
        message = self.check_if_operation_was_successful_and_get_payload(data)
        self.assertTrue(message['name'] == patch_data['name'])

    def test_patch_profile_endpoint_with_basic_level_authorization_without_name_in_payload_returns_422(self):
        patch_data = {}

        res = self.client().patch('/profile', json=patch_data, headers=basic_auth_header(True))
        data = json.loads(res.data)
        self.check_if_operation_failed_with_error_code(data, 422)

    def test_patch_profile_endpoint_with_advanced_level_authorization_updates_user_info(self):
        patch_data = {'name': 'newName'}

        res = self.client().get('/profile', headers=advanced_auth_header())
        data = json.loads(res.data)
        message = self.check_if_operation_was_successful_and_get_payload(data)
        self.assertFalse(message['name'] == patch_data['name'])

        res = self.client().patch('/profile', json=patch_data, headers=advanced_auth_header(True))
        data = json.loads(res.data)
        self.check_if_operation_was_successful_and_get_payload(data)

        res = self.client().get('/profile', headers=advanced_auth_header())
        data = json.loads(res.data)
        message = self.check_if_operation_was_successful_and_get_payload(data)
        self.assertTrue(message['name'] == patch_data['name'])

    def test_patch_profile_endpoint_with_advanced_level_authorization_without_name_in_payload_returns_422(self):
        patch_data = {}

        res = self.client().patch('/profile', json=patch_data, headers=advanced_auth_header(True))
        data = json.loads(res.data)
        self.check_if_operation_failed_with_error_code(data, 422)

    def test_patch_profile_endpoint_with_no_authorization_returns_401(self):
        patch_data = {'name': 'newName'}

        res = self.client().patch('/profile', json=patch_data)
        data = json.loads(res.data)
        self.check_if_operation_failed_with_error_code(data, 401)
