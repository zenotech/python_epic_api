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


class BatchApplicationList(object):
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
        'product': 'ProductName',
        'versions': 'list[BatchApplicationVersionDetails]',
        'permission_to_use': 'bool',
        'supports_cases': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'product': 'product',
        'versions': 'versions',
        'permission_to_use': 'permission_to_use',
        'supports_cases': 'supports_cases'
    }

    def __init__(self, id=None, product=None, versions=None, permission_to_use=None, supports_cases=None, local_vars_configuration=None):  # noqa: E501
        """BatchApplicationList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._product = None
        self._versions = None
        self._permission_to_use = None
        self._supports_cases = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.product = product
        if versions is not None:
            self.versions = versions
        if permission_to_use is not None:
            self.permission_to_use = permission_to_use
        if supports_cases is not None:
            self.supports_cases = supports_cases

    @property
    def id(self):
        """Gets the id of this BatchApplicationList.  # noqa: E501


        :return: The id of this BatchApplicationList.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchApplicationList.


        :param id: The id of this BatchApplicationList.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def product(self):
        """Gets the product of this BatchApplicationList.  # noqa: E501


        :return: The product of this BatchApplicationList.  # noqa: E501
        :rtype: ProductName
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this BatchApplicationList.


        :param product: The product of this BatchApplicationList.  # noqa: E501
        :type product: ProductName
        """
        if self.local_vars_configuration.client_side_validation and product is None:  # noqa: E501
            raise ValueError("Invalid value for `product`, must not be `None`")  # noqa: E501

        self._product = product

    @property
    def versions(self):
        """Gets the versions of this BatchApplicationList.  # noqa: E501


        :return: The versions of this BatchApplicationList.  # noqa: E501
        :rtype: list[BatchApplicationVersionDetails]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this BatchApplicationList.


        :param versions: The versions of this BatchApplicationList.  # noqa: E501
        :type versions: list[BatchApplicationVersionDetails]
        """

        self._versions = versions

    @property
    def permission_to_use(self):
        """Gets the permission_to_use of this BatchApplicationList.  # noqa: E501

        Does your account have permission to use this application?  # noqa: E501

        :return: The permission_to_use of this BatchApplicationList.  # noqa: E501
        :rtype: bool
        """
        return self._permission_to_use

    @permission_to_use.setter
    def permission_to_use(self, permission_to_use):
        """Sets the permission_to_use of this BatchApplicationList.

        Does your account have permission to use this application?  # noqa: E501

        :param permission_to_use: The permission_to_use of this BatchApplicationList.  # noqa: E501
        :type permission_to_use: bool
        """

        self._permission_to_use = permission_to_use

    @property
    def supports_cases(self):
        """Gets the supports_cases of this BatchApplicationList.  # noqa: E501


        :return: The supports_cases of this BatchApplicationList.  # noqa: E501
        :rtype: bool
        """
        return self._supports_cases

    @supports_cases.setter
    def supports_cases(self, supports_cases):
        """Sets the supports_cases of this BatchApplicationList.


        :param supports_cases: The supports_cases of this BatchApplicationList.  # noqa: E501
        :type supports_cases: bool
        """

        self._supports_cases = supports_cases

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
        if not isinstance(other, BatchApplicationList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchApplicationList):
            return True

        return self.to_dict() != other.to_dict()
