# coding: utf-8

"""
    EPIC API

    REST API for interacting with EPIC (https://epic.zenotech.com) services. <br />                             Please note this API is in BETA and does not yet contain                             all EPIC functionality.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: support@zenotech.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from epiccore.configuration import Configuration


class EnvironmentVariable(object):
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
        'variable_name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'variable_name': 'variable_name',
        'value': 'value'
    }

    def __init__(self, variable_name=None, value=None, local_vars_configuration=None):  # noqa: E501
        """EnvironmentVariable - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._variable_name = None
        self._value = None
        self.discriminator = None

        self.variable_name = variable_name
        self.value = value

    @property
    def variable_name(self):
        """Gets the variable_name of this EnvironmentVariable.  # noqa: E501


        :return: The variable_name of this EnvironmentVariable.  # noqa: E501
        :rtype: str
        """
        return self._variable_name

    @variable_name.setter
    def variable_name(self, variable_name):
        """Sets the variable_name of this EnvironmentVariable.


        :param variable_name: The variable_name of this EnvironmentVariable.  # noqa: E501
        :type variable_name: str
        """
        if self.local_vars_configuration.client_side_validation and variable_name is None:  # noqa: E501
            raise ValueError("Invalid value for `variable_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                variable_name is not None and len(variable_name) > 300):
            raise ValueError("Invalid value for `variable_name`, length must be less than or equal to `300`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                variable_name is not None and len(variable_name) < 1):
            raise ValueError("Invalid value for `variable_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._variable_name = variable_name

    @property
    def value(self):
        """Gets the value of this EnvironmentVariable.  # noqa: E501


        :return: The value of this EnvironmentVariable.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this EnvironmentVariable.


        :param value: The value of this EnvironmentVariable.  # noqa: E501
        :type value: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                value is not None and len(value) > 300):
            raise ValueError("Invalid value for `value`, length must be less than or equal to `300`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                value is not None and len(value) < 1):
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, EnvironmentVariable):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnvironmentVariable):
            return True

        return self.to_dict() != other.to_dict()
