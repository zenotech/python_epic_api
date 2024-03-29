# coding: utf-8

"""
    EPIC API

    REST API for interacting with EPIC (https://epic.zenotech.com) services. <br />                             Please note this API is in BETA and does not yet contain                             all EPIC functionality.  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@zenotech.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from epiccore.configuration import Configuration


class LicenseTemplate(object):
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
        'id': 'str',
        'application': 'Application',
        'environment': 'list[EnvVarTemplate]'
    }

    attribute_map = {
        'id': 'id',
        'application': 'application',
        'environment': 'environment'
    }

    def __init__(self, id=None, application=None, environment=None, local_vars_configuration=None):  # noqa: E501
        """LicenseTemplate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._application = None
        self._environment = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if application is not None:
            self.application = application
        if environment is not None:
            self.environment = environment

    @property
    def id(self):
        """Gets the id of this LicenseTemplate.  # noqa: E501


        :return: The id of this LicenseTemplate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LicenseTemplate.


        :param id: The id of this LicenseTemplate.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def application(self):
        """Gets the application of this LicenseTemplate.  # noqa: E501


        :return: The application of this LicenseTemplate.  # noqa: E501
        :rtype: Application
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this LicenseTemplate.


        :param application: The application of this LicenseTemplate.  # noqa: E501
        :type application: Application
        """

        self._application = application

    @property
    def environment(self):
        """Gets the environment of this LicenseTemplate.  # noqa: E501


        :return: The environment of this LicenseTemplate.  # noqa: E501
        :rtype: list[EnvVarTemplate]
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this LicenseTemplate.


        :param environment: The environment of this LicenseTemplate.  # noqa: E501
        :type environment: list[EnvVarTemplate]
        """

        self._environment = environment

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
        if not isinstance(other, LicenseTemplate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LicenseTemplate):
            return True

        return self.to_dict() != other.to_dict()
