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


class DesktopNodeType(object):
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
        'name': 'str',
        'description': 'str',
        'cores': 'int',
        'gpus': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'cores': 'cores',
        'gpus': 'gpus'
    }

    def __init__(self, id=None, name=None, description=None, cores=None, gpus=None, local_vars_configuration=None):  # noqa: E501
        """DesktopNodeType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._cores = None
        self._gpus = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if cores is not None:
            self.cores = cores
        if gpus is not None:
            self.gpus = gpus

    @property
    def id(self):
        """Gets the id of this DesktopNodeType.  # noqa: E501

        ID for this node_type to be used in DesktopNodeLaunchSpec  # noqa: E501

        :return: The id of this DesktopNodeType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DesktopNodeType.

        ID for this node_type to be used in DesktopNodeLaunchSpec  # noqa: E501

        :param id: The id of this DesktopNodeType.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DesktopNodeType.  # noqa: E501

        This provides the name of this node type  # noqa: E501

        :return: The name of this DesktopNodeType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DesktopNodeType.

        This provides the name of this node type  # noqa: E501

        :param name: The name of this DesktopNodeType.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this DesktopNodeType.  # noqa: E501

        This provides a detailed description of this node type  # noqa: E501

        :return: The description of this DesktopNodeType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DesktopNodeType.

        This provides a detailed description of this node type  # noqa: E501

        :param description: The description of this DesktopNodeType.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 100):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def cores(self):
        """Gets the cores of this DesktopNodeType.  # noqa: E501

        Number of cores that this desktop node has  # noqa: E501

        :return: The cores of this DesktopNodeType.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this DesktopNodeType.

        Number of cores that this desktop node has  # noqa: E501

        :param cores: The cores of this DesktopNodeType.  # noqa: E501
        :type cores: int
        """
        if (self.local_vars_configuration.client_side_validation and
                cores is not None and cores < 0):  # noqa: E501
            raise ValueError("Invalid value for `cores`, must be a value greater than or equal to `0`")  # noqa: E501

        self._cores = cores

    @property
    def gpus(self):
        """Gets the gpus of this DesktopNodeType.  # noqa: E501

        Number of gpus that this desktop node has  # noqa: E501

        :return: The gpus of this DesktopNodeType.  # noqa: E501
        :rtype: int
        """
        return self._gpus

    @gpus.setter
    def gpus(self, gpus):
        """Sets the gpus of this DesktopNodeType.

        Number of gpus that this desktop node has  # noqa: E501

        :param gpus: The gpus of this DesktopNodeType.  # noqa: E501
        :type gpus: int
        """
        if (self.local_vars_configuration.client_side_validation and
                gpus is not None and gpus < 0):  # noqa: E501
            raise ValueError("Invalid value for `gpus`, must be a value greater than or equal to `0`")  # noqa: E501

        self._gpus = gpus

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
        if not isinstance(other, DesktopNodeType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DesktopNodeType):
            return True

        return self.to_dict() != other.to_dict()
