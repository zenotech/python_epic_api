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


class ServiceCharge(object):
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
        'amount': 'float',
        'currency': 'str',
        'currency_symbol': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency',
        'currency_symbol': 'currency_symbol'
    }

    def __init__(self, amount=None, currency=None, currency_symbol=None, local_vars_configuration=None):  # noqa: E501
        """ServiceCharge - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._currency = None
        self._currency_symbol = None
        self.discriminator = None

        self.amount = amount
        self.currency = currency
        self.currency_symbol = currency_symbol

    @property
    def amount(self):
        """Gets the amount of this ServiceCharge.  # noqa: E501

        Amount of the currency  # noqa: E501

        :return: The amount of this ServiceCharge.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ServiceCharge.

        Amount of the currency  # noqa: E501

        :param amount: The amount of this ServiceCharge.  # noqa: E501
        :type amount: float
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this ServiceCharge.  # noqa: E501

        Type of currency  # noqa: E501

        :return: The currency of this ServiceCharge.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ServiceCharge.

        Type of currency  # noqa: E501

        :param currency: The currency of this ServiceCharge.  # noqa: E501
        :type currency: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def currency_symbol(self):
        """Gets the currency_symbol of this ServiceCharge.  # noqa: E501

        Symbol to be used for this currency  # noqa: E501

        :return: The currency_symbol of this ServiceCharge.  # noqa: E501
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """Sets the currency_symbol of this ServiceCharge.

        Symbol to be used for this currency  # noqa: E501

        :param currency_symbol: The currency_symbol of this ServiceCharge.  # noqa: E501
        :type currency_symbol: str
        """
        if self.local_vars_configuration.client_side_validation and currency_symbol is None:  # noqa: E501
            raise ValueError("Invalid value for `currency_symbol`, must not be `None`")  # noqa: E501

        self._currency_symbol = currency_symbol

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
        if not isinstance(other, ServiceCharge):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServiceCharge):
            return True

        return self.to_dict() != other.to_dict()
