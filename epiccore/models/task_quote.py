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


class TaskQuote(object):
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
        'reference': 'str',
        'queue_id': 'int',
        'iaas_cost': 'IaasCost',
        'software_cost': 'SoftwareCost',
        'service_charge': 'ServiceCharge',
        'discount': 'Discount',
        'tax': 'Tax',
        'total': 'Total1'
    }

    attribute_map = {
        'reference': 'reference',
        'queue_id': 'queue_id',
        'iaas_cost': 'iaas_cost',
        'software_cost': 'software_cost',
        'service_charge': 'service_charge',
        'discount': 'discount',
        'tax': 'tax',
        'total': 'total'
    }

    def __init__(self, reference=None, queue_id=None, iaas_cost=None, software_cost=None, service_charge=None, discount=None, tax=None, total=None, local_vars_configuration=None):  # noqa: E501
        """TaskQuote - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._reference = None
        self._queue_id = None
        self._iaas_cost = None
        self._software_cost = None
        self._service_charge = None
        self._discount = None
        self._tax = None
        self._total = None
        self.discriminator = None

        if reference is not None:
            self.reference = reference
        if queue_id is not None:
            self.queue_id = queue_id
        if iaas_cost is not None:
            self.iaas_cost = iaas_cost
        if software_cost is not None:
            self.software_cost = software_cost
        if service_charge is not None:
            self.service_charge = service_charge
        if discount is not None:
            self.discount = discount
        if tax is not None:
            self.tax = tax
        if total is not None:
            self.total = total

    @property
    def reference(self):
        """Gets the reference of this TaskQuote.  # noqa: E501

        The reference given in the quote request, to help you identify this task.  # noqa: E501

        :return: The reference of this TaskQuote.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this TaskQuote.

        The reference given in the quote request, to help you identify this task.  # noqa: E501

        :param reference: The reference of this TaskQuote.  # noqa: E501
        :type reference: str
        """
        if (self.local_vars_configuration.client_side_validation and
                reference is not None and len(reference) > 25):
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `25`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                reference is not None and len(reference) < 1):
            raise ValueError("Invalid value for `reference`, length must be greater than or equal to `1`")  # noqa: E501

        self._reference = reference

    @property
    def queue_id(self):
        """Gets the queue_id of this TaskQuote.  # noqa: E501

        The ID of the queue for this quote  # noqa: E501

        :return: The queue_id of this TaskQuote.  # noqa: E501
        :rtype: int
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """Sets the queue_id of this TaskQuote.

        The ID of the queue for this quote  # noqa: E501

        :param queue_id: The queue_id of this TaskQuote.  # noqa: E501
        :type queue_id: int
        """
        if (self.local_vars_configuration.client_side_validation and
                queue_id is not None and queue_id < -1):  # noqa: E501
            raise ValueError("Invalid value for `queue_id`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._queue_id = queue_id

    @property
    def iaas_cost(self):
        """Gets the iaas_cost of this TaskQuote.  # noqa: E501


        :return: The iaas_cost of this TaskQuote.  # noqa: E501
        :rtype: IaasCost
        """
        return self._iaas_cost

    @iaas_cost.setter
    def iaas_cost(self, iaas_cost):
        """Sets the iaas_cost of this TaskQuote.


        :param iaas_cost: The iaas_cost of this TaskQuote.  # noqa: E501
        :type iaas_cost: IaasCost
        """

        self._iaas_cost = iaas_cost

    @property
    def software_cost(self):
        """Gets the software_cost of this TaskQuote.  # noqa: E501


        :return: The software_cost of this TaskQuote.  # noqa: E501
        :rtype: SoftwareCost
        """
        return self._software_cost

    @software_cost.setter
    def software_cost(self, software_cost):
        """Sets the software_cost of this TaskQuote.


        :param software_cost: The software_cost of this TaskQuote.  # noqa: E501
        :type software_cost: SoftwareCost
        """

        self._software_cost = software_cost

    @property
    def service_charge(self):
        """Gets the service_charge of this TaskQuote.  # noqa: E501


        :return: The service_charge of this TaskQuote.  # noqa: E501
        :rtype: ServiceCharge
        """
        return self._service_charge

    @service_charge.setter
    def service_charge(self, service_charge):
        """Sets the service_charge of this TaskQuote.


        :param service_charge: The service_charge of this TaskQuote.  # noqa: E501
        :type service_charge: ServiceCharge
        """

        self._service_charge = service_charge

    @property
    def discount(self):
        """Gets the discount of this TaskQuote.  # noqa: E501


        :return: The discount of this TaskQuote.  # noqa: E501
        :rtype: Discount
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this TaskQuote.


        :param discount: The discount of this TaskQuote.  # noqa: E501
        :type discount: Discount
        """

        self._discount = discount

    @property
    def tax(self):
        """Gets the tax of this TaskQuote.  # noqa: E501


        :return: The tax of this TaskQuote.  # noqa: E501
        :rtype: Tax
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this TaskQuote.


        :param tax: The tax of this TaskQuote.  # noqa: E501
        :type tax: Tax
        """

        self._tax = tax

    @property
    def total(self):
        """Gets the total of this TaskQuote.  # noqa: E501


        :return: The total of this TaskQuote.  # noqa: E501
        :rtype: Total1
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this TaskQuote.


        :param total: The total of this TaskQuote.  # noqa: E501
        :type total: Total1
        """

        self._total = total

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
        if not isinstance(other, TaskQuote):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaskQuote):
            return True

        return self.to_dict() != other.to_dict()
