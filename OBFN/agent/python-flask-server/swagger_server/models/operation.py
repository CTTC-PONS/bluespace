# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Operation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, wavelength: float=None, beam_id: int=None, x_offset_angle: float=None, y_offset_angle: float=None):  # noqa: E501
        """Operation - a model defined in Swagger

        :param wavelength: The wavelength of this Operation.  # noqa: E501
        :type wavelength: float
        :param beam_id: The beam_id of this Operation.  # noqa: E501
        :type beam_id: int
        :param x_offset_angle: The x_offset_angle of this Operation.  # noqa: E501
        :type x_offset_angle: float
        :param y_offset_angle: The y_offset_angle of this Operation.  # noqa: E501
        :type y_offset_angle: float
        """
        self.swagger_types = {
            'wavelength': float,
            'beam_id': int,
            'x_offset_angle': float,
            'y_offset_angle': float
        }

        self.attribute_map = {
            'wavelength': 'wavelength',
            'beam_id': 'beam_id',
            'x_offset_angle': 'X_offset_angle',
            'y_offset_angle': 'Y_offset_angle'
        }

        self._wavelength = wavelength
        self._beam_id = beam_id
        self._x_offset_angle = x_offset_angle
        self._y_offset_angle = y_offset_angle

    @classmethod
    def from_dict(cls, dikt) -> 'Operation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Operation of this Operation.  # noqa: E501
        :rtype: Operation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def wavelength(self) -> float:
        """Gets the wavelength of this Operation.


        :return: The wavelength of this Operation.
        :rtype: float
        """
        return self._wavelength

    @wavelength.setter
    def wavelength(self, wavelength: float):
        """Sets the wavelength of this Operation.


        :param wavelength: The wavelength of this Operation.
        :type wavelength: float
        """

        self._wavelength = wavelength

    @property
    def beam_id(self) -> int:
        """Gets the beam_id of this Operation.


        :return: The beam_id of this Operation.
        :rtype: int
        """
        return self._beam_id

    @beam_id.setter
    def beam_id(self, beam_id: int):
        """Sets the beam_id of this Operation.


        :param beam_id: The beam_id of this Operation.
        :type beam_id: int
        """

        self._beam_id = beam_id

    @property
    def x_offset_angle(self) -> float:
        """Gets the x_offset_angle of this Operation.


        :return: The x_offset_angle of this Operation.
        :rtype: float
        """
        return self._x_offset_angle

    @x_offset_angle.setter
    def x_offset_angle(self, x_offset_angle: float):
        """Sets the x_offset_angle of this Operation.


        :param x_offset_angle: The x_offset_angle of this Operation.
        :type x_offset_angle: float
        """

        self._x_offset_angle = x_offset_angle

    @property
    def y_offset_angle(self) -> float:
        """Gets the y_offset_angle of this Operation.


        :return: The y_offset_angle of this Operation.
        :rtype: float
        """
        return self._y_offset_angle

    @y_offset_angle.setter
    def y_offset_angle(self, y_offset_angle: float):
        """Sets the y_offset_angle of this Operation.


        :param y_offset_angle: The y_offset_angle of this Operation.
        :type y_offset_angle: float
        """

        self._y_offset_angle = y_offset_angle
