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


class ProfileSummary(object):
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
        'display_currency': 'str',
        'display_currency_symbol': 'str'
    }

    attribute_map = {
        'id': 'id',
        'display_currency': 'display_currency',
        'display_currency_symbol': 'display_currency_symbol'
    }

    def __init__(self, id=None, display_currency=None, display_currency_symbol=None, local_vars_configuration=None):  # noqa: E501
        """ProfileSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._display_currency = None
        self._display_currency_symbol = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if display_currency is not None:
            self.display_currency = display_currency
        if display_currency_symbol is not None:
            self.display_currency_symbol = display_currency_symbol

    @property
    def id(self):
        """Gets the id of this ProfileSummary.  # noqa: E501


        :return: The id of this ProfileSummary.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProfileSummary.


        :param id: The id of this ProfileSummary.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def display_currency(self):
        """Gets the display_currency of this ProfileSummary.  # noqa: E501


        :return: The display_currency of this ProfileSummary.  # noqa: E501
        :rtype: str
        """
        return self._display_currency

    @display_currency.setter
    def display_currency(self, display_currency):
        """Sets the display_currency of this ProfileSummary.


        :param display_currency: The display_currency of this ProfileSummary.  # noqa: E501
        :type display_currency: str
        """
        allowed_values = ["EUR", "GBP", "USD"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and display_currency not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `display_currency` ({0}), must be one of {1}"  # noqa: E501
                .format(display_currency, allowed_values)
            )

        self._display_currency = display_currency

    @property
    def display_currency_symbol(self):
        """Gets the display_currency_symbol of this ProfileSummary.  # noqa: E501


        :return: The display_currency_symbol of this ProfileSummary.  # noqa: E501
        :rtype: str
        """
        return self._display_currency_symbol

    @display_currency_symbol.setter
    def display_currency_symbol(self, display_currency_symbol):
        """Sets the display_currency_symbol of this ProfileSummary.


        :param display_currency_symbol: The display_currency_symbol of this ProfileSummary.  # noqa: E501
        :type display_currency_symbol: str
        """

        self._display_currency_symbol = display_currency_symbol

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
        if not isinstance(other, ProfileSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProfileSummary):
            return True

        return self.to_dict() != other.to_dict()
