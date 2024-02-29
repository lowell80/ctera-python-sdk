from unittest import mock

from tests.ut import base_core_services


class BaseCoreServicesFilesDelete(base_core_services.BaseCoreServicesTest):

    def setUp(self):
        super().setUp()
        self._path = 'My Files/Documents'

    def test_delete(self):
        execute_response = 'Success'
        self._init_services(execute_response=execute_response)
        ret = self._services.files.delete(self._path)
        self._services.api.execute.assert_called_once_with('', 'deleteResources', mock.ANY)
        expected_param = self._create_delete_resource_param()
        actual_param = self._services.api.execute.call_args[0][2]
        self._assert_equal_objects(actual_param, expected_param)
        self.assertEqual(ret, execute_response)

    def _create_delete_resource_param(self):
        return self._create_action_resource_param([self._path])
