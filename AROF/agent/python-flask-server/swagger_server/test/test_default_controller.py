# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.operation import Operation  # noqa: E501
from swagger_server.models.operations import Operations  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create_configuration_by_id(self):
        """Test case for create_configuration_by_id

        Create configuration by ID
        """
        data = dict(enable=true)
        response = self.client.open(
            '/api/arof/{arof_id}'.format(arof_id=56),
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_configuration_by_id(self):
        """Test case for delete_configuration_by_id

        Delete configuration by ID
        """
        response = self.client.open(
            '/api/arof/{arof_id}'.format(arof_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_configuration(self):
        """Test case for retrieve_configuration

        Retrieve configuration
        """
        response = self.client.open(
            '/api/arof',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_arof_by_id(self):
        """Test case for update_arof_by_id

        Update configuration by ID
        """
        data = dict(enable=true)
        response = self.client.open(
            '/api/arof/{arof_id}'.format(arof_id=56),
            method='PUT',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
