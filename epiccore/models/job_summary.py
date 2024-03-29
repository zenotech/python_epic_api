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


class JobSummary(object):
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
        'app': 'str',
        'cost': 'str',
        'submitted_by': 'str',
        'submitted_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'app': 'app',
        'cost': 'cost',
        'submitted_by': 'submitted_by',
        'submitted_at': 'submitted_at'
    }

    def __init__(self, id=None, name=None, app=None, cost=None, submitted_by=None, submitted_at=None, local_vars_configuration=None):  # noqa: E501
        """JobSummary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._app = None
        self._cost = None
        self._submitted_by = None
        self._submitted_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if app is not None:
            self.app = app
        if cost is not None:
            self.cost = cost
        if submitted_by is not None:
            self.submitted_by = submitted_by
        if submitted_at is not None:
            self.submitted_at = submitted_at

    @property
    def id(self):
        """Gets the id of this JobSummary.  # noqa: E501

        The ID for this job  # noqa: E501

        :return: The id of this JobSummary.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobSummary.

        The ID for this job  # noqa: E501

        :param id: The id of this JobSummary.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this JobSummary.  # noqa: E501

        Name of this job  # noqa: E501

        :return: The name of this JobSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobSummary.

        Name of this job  # noqa: E501

        :param name: The name of this JobSummary.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def app(self):
        """Gets the app of this JobSummary.  # noqa: E501

        Name of the application that this job uses  # noqa: E501

        :return: The app of this JobSummary.  # noqa: E501
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this JobSummary.

        Name of the application that this job uses  # noqa: E501

        :param app: The app of this JobSummary.  # noqa: E501
        :type app: str
        """
        if (self.local_vars_configuration.client_side_validation and
                app is not None and len(app) > 30):
            raise ValueError("Invalid value for `app`, length must be less than or equal to `30`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                app is not None and len(app) < 1):
            raise ValueError("Invalid value for `app`, length must be greater than or equal to `1`")  # noqa: E501

        self._app = app

    @property
    def cost(self):
        """Gets the cost of this JobSummary.  # noqa: E501

        Maximum cost for running this job  # noqa: E501

        :return: The cost of this JobSummary.  # noqa: E501
        :rtype: str
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this JobSummary.

        Maximum cost for running this job  # noqa: E501

        :param cost: The cost of this JobSummary.  # noqa: E501
        :type cost: str
        """
        if (self.local_vars_configuration.client_side_validation and
                cost is not None and len(cost) > 30):
            raise ValueError("Invalid value for `cost`, length must be less than or equal to `30`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cost is not None and len(cost) < 1):
            raise ValueError("Invalid value for `cost`, length must be greater than or equal to `1`")  # noqa: E501

        self._cost = cost

    @property
    def submitted_by(self):
        """Gets the submitted_by of this JobSummary.  # noqa: E501

        Name of the user who submitted this job  # noqa: E501

        :return: The submitted_by of this JobSummary.  # noqa: E501
        :rtype: str
        """
        return self._submitted_by

    @submitted_by.setter
    def submitted_by(self, submitted_by):
        """Sets the submitted_by of this JobSummary.

        Name of the user who submitted this job  # noqa: E501

        :param submitted_by: The submitted_by of this JobSummary.  # noqa: E501
        :type submitted_by: str
        """

        self._submitted_by = submitted_by

    @property
    def submitted_at(self):
        """Gets the submitted_at of this JobSummary.  # noqa: E501

        Date at which this job was submitted  # noqa: E501

        :return: The submitted_at of this JobSummary.  # noqa: E501
        :rtype: str
        """
        return self._submitted_at

    @submitted_at.setter
    def submitted_at(self, submitted_at):
        """Sets the submitted_at of this JobSummary.

        Date at which this job was submitted  # noqa: E501

        :param submitted_at: The submitted_at of this JobSummary.  # noqa: E501
        :type submitted_at: str
        """

        self._submitted_at = submitted_at

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
        if not isinstance(other, JobSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobSummary):
            return True

        return self.to_dict() != other.to_dict()
