# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.operation import Operation  # noqa: E501
from swagger_server.models.operations import Operations  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create_configuration(self):
        """Test case for create_configuration

        Create configuration
        """
        body = Operations()
        response = self.client.open(
            '/api/obfn',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_configuration(self):
        """Test case for delete_configuration

        Delete configuration
        """
        response = self.client.open(
            '/api/obfn',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_configuration(self):
        """Test case for retrieve_configuration

        Retrieve configuration
        """
        response = self.client.open(
            '/api/obfn',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_configuration_by_id(self):
        """Test case for update_configuration_by_id

        Update configuration by ID
        """
        query_string = [('x_offset_angle', 8.14),
                        ('y_offset_angle', 8.14),
                        ('wavelength', 8.14)]
        response = self.client.open(
            '/api/obfn/{beam_id}'.format(beam_id=56),
            method='PUT',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
