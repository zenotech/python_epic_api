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


class ProductName(object):
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
        'name': 'str',
        'image': 'str',
        'description': 'str',
        'small_print': 'str'
    }

    attribute_map = {
        'name': 'name',
        'image': 'image',
        'description': 'description',
        'small_print': 'small_print'
    }

    def __init__(self, name=None, image=None, description=None, small_print=None, local_vars_configuration=None):  # noqa: E501
        """ProductName - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._image = None
        self._description = None
        self._small_print = None
        self.discriminator = None

        self.name = name
        if image is not None:
            self.image = image
        self.description = description
        self.small_print = small_print

    @property
    def name(self):
        """Gets the name of this ProductName.  # noqa: E501


        :return: The name of this ProductName.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductName.


        :param name: The name of this ProductName.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def image(self):
        """Gets the image of this ProductName.  # noqa: E501


        :return: The image of this ProductName.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ProductName.


        :param image: The image of this ProductName.  # noqa: E501
        :type image: str
        """

        self._image = image

    @property
    def description(self):
        """Gets the description of this ProductName.  # noqa: E501


        :return: The description of this ProductName.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProductName.


        :param description: The description of this ProductName.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1000):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")  # noqa: E501

        self._description = description

    @property
    def small_print(self):
        """Gets the small_print of this ProductName.  # noqa: E501


        :return: The small_print of this ProductName.  # noqa: E501
        :rtype: str
        """
        return self._small_print

    @small_print.setter
    def small_print(self, small_print):
        """Sets the small_print of this ProductName.


        :param small_print: The small_print of this ProductName.  # noqa: E501
        :type small_print: str
        """
        if (self.local_vars_configuration.client_side_validation and
                small_print is not None and len(small_print) > 1000):
            raise ValueError("Invalid value for `small_print`, length must be less than or equal to `1000`")  # noqa: E501

        self._small_print = small_print

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
        if not isinstance(other, ProductName):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProductName):
            return True

        return self.to_dict() != other.to_dict()
