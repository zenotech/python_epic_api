# coding: utf-8

"""
    EPIC API

    REST API for interacting with EPIC (https://epic.zenotech.com) services. <br />                             Used by the EPIC CLI (https://github.com/zenotech/epic-cli).                             Please note this API is in BETA and does not yet contain                             all EPIC functionality.  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@zenotech.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from epiccore.configuration import Configuration


class License(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'teams': 'str',
        'license_type': 'str',
        'id': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'teams': 'teams',
        'license_type': 'license_type',
        'id': 'id',
        'display_name': 'display_name'
    }

    def __init__(self, teams=None, license_type=None, id=None, display_name=None, local_vars_configuration=None):  # noqa: E501
        """License - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._teams = None
        self._license_type = None
        self._id = None
        self._display_name = None
        self.discriminator = None

        if teams is not None:
            self.teams = teams
        self.license_type = license_type
        if id is not None:
            self.id = id
        self.display_name = display_name

    @property
    def teams(self):
        """Gets the teams of this License.  # noqa: E501


        :return: The teams of this License.  # noqa: E501
        :rtype: str
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this License.


        :param teams: The teams of this License.  # noqa: E501
        :type teams: str
        """

        self._teams = teams

    @property
    def license_type(self):
        """Gets the license_type of this License.  # noqa: E501


        :return: The license_type of this License.  # noqa: E501
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """Sets the license_type of this License.


        :param license_type: The license_type of this License.  # noqa: E501
        :type license_type: str
        """
        if self.local_vars_configuration.client_side_validation and license_type is None:  # noqa: E501
            raise ValueError("Invalid value for `license_type`, must not be `None`")  # noqa: E501
        allowed_values = ["zenotech_zcfd", "zenotech_zcad", "ansys"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and license_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `license_type` ({0}), must be one of {1}"  # noqa: E501
                .format(license_type, allowed_values)
            )

        self._license_type = license_type

    @property
    def id(self):
        """Gets the id of this License.  # noqa: E501


        :return: The id of this License.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this License.


        :param id: The id of this License.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this License.  # noqa: E501


        :return: The display_name of this License.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this License.


        :param display_name: The display_name of this License.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 30):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `30`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, License):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, License):
            return True

        return self.to_dict() != other.to_dict()
