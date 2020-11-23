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


class DesktopNodeApplicationVersion(object):
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
        'id': 'int',
        'application_version': 'str',
        'connection_types': 'list[DesktopNodeConnectionType]'
    }

    attribute_map = {
        'id': 'id',
        'application_version': 'application_version',
        'connection_types': 'connection_types'
    }

    def __init__(self, id=None, application_version=None, connection_types=None, local_vars_configuration=None):  # noqa: E501
        """DesktopNodeApplicationVersion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._application_version = None
        self._connection_types = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.application_version = application_version
        if connection_types is not None:
            self.connection_types = connection_types

    @property
    def id(self):
        """Gets the id of this DesktopNodeApplicationVersion.  # noqa: E501

        ID for this application version. Use this in a DesktopNodeLaunchSpec.  # noqa: E501

        :return: The id of this DesktopNodeApplicationVersion.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DesktopNodeApplicationVersion.

        ID for this application version. Use this in a DesktopNodeLaunchSpec.  # noqa: E501

        :param id: The id of this DesktopNodeApplicationVersion.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def application_version(self):
        """Gets the application_version of this DesktopNodeApplicationVersion.  # noqa: E501

        Name of this application version  # noqa: E501

        :return: The application_version of this DesktopNodeApplicationVersion.  # noqa: E501
        :rtype: str
        """
        return self._application_version

    @application_version.setter
    def application_version(self, application_version):
        """Sets the application_version of this DesktopNodeApplicationVersion.

        Name of this application version  # noqa: E501

        :param application_version: The application_version of this DesktopNodeApplicationVersion.  # noqa: E501
        :type application_version: str
        """
        if self.local_vars_configuration.client_side_validation and application_version is None:  # noqa: E501
            raise ValueError("Invalid value for `application_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                application_version is not None and len(application_version) > 10):
            raise ValueError("Invalid value for `application_version`, length must be less than or equal to `10`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                application_version is not None and len(application_version) < 1):
            raise ValueError("Invalid value for `application_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._application_version = application_version

    @property
    def connection_types(self):
        """Gets the connection_types of this DesktopNodeApplicationVersion.  # noqa: E501

        List of connection types for this VizNodeApplicationVersion  # noqa: E501

        :return: The connection_types of this DesktopNodeApplicationVersion.  # noqa: E501
        :rtype: list[DesktopNodeConnectionType]
        """
        return self._connection_types

    @connection_types.setter
    def connection_types(self, connection_types):
        """Sets the connection_types of this DesktopNodeApplicationVersion.

        List of connection types for this VizNodeApplicationVersion  # noqa: E501

        :param connection_types: The connection_types of this DesktopNodeApplicationVersion.  # noqa: E501
        :type connection_types: list[DesktopNodeConnectionType]
        """

        self._connection_types = connection_types

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
        if not isinstance(other, DesktopNodeApplicationVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DesktopNodeApplicationVersion):
            return True

        return self.to_dict() != other.to_dict()
