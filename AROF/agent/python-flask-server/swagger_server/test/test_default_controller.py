# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.arof_parameters import ArofParameters  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create_configuration(self):
        """Test case for create_configuration

        Create configuration
        """
        arof_pool = ArofParameters()
        response = self.client.open(
            '/api/arof',
            method='POST',
            data=json.dumps(arof_pool),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_configuration(self):
        """Test case for delete_configuration

        Delete configuration
        """
        response = self.client.open(
            '/api/arof',
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

    def test_update_configuration(self):
        """Test case for update_configuration

        Update configuration
        """
        arof_pool = ArofParameters()
        response = self.client.open(
            '/api/arof',
            method='PUT',
            data=json.dumps(arof_pool),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
