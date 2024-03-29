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


class PriceQuote(object):
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
        'cost': 'Cost',
        'valid': 'bool',
        'reason': 'str'
    }

    attribute_map = {
        'cost': 'cost',
        'valid': 'valid',
        'reason': 'reason'
    }

    def __init__(self, cost=None, valid=None, reason=None, local_vars_configuration=None):  # noqa: E501
        """PriceQuote - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cost = None
        self._valid = None
        self._reason = None
        self.discriminator = None

        if cost is not None:
            self.cost = cost
        if valid is not None:
            self.valid = valid
        if reason is not None:
            self.reason = reason

    @property
    def cost(self):
        """Gets the cost of this PriceQuote.  # noqa: E501


        :return: The cost of this PriceQuote.  # noqa: E501
        :rtype: Cost
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this PriceQuote.


        :param cost: The cost of this PriceQuote.  # noqa: E501
        :type cost: Cost
        """

        self._cost = cost

    @property
    def valid(self):
        """Gets the valid of this PriceQuote.  # noqa: E501

        Whether the requested spec represents a valid configuration that could be launched  # noqa: E501

        :return: The valid of this PriceQuote.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this PriceQuote.

        Whether the requested spec represents a valid configuration that could be launched  # noqa: E501

        :param valid: The valid of this PriceQuote.  # noqa: E501
        :type valid: bool
        """

        self._valid = valid

    @property
    def reason(self):
        """Gets the reason of this PriceQuote.  # noqa: E501

        If the configuration is invalid this string will contain the reason why the configuration is not valid  # noqa: E501

        :return: The reason of this PriceQuote.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this PriceQuote.

        If the configuration is invalid this string will contain the reason why the configuration is not valid  # noqa: E501

        :param reason: The reason of this PriceQuote.  # noqa: E501
        :type reason: str
        """

        self._reason = reason

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
        if not isinstance(other, PriceQuote):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PriceQuote):
            return True

        return self.to_dict() != other.to_dict()
