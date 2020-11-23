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


class BatchApplicationVersionDetails(object):
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
        'version': 'str',
        'queue_ids': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'queue_ids': 'queue_ids'
    }

    def __init__(self, id=None, version=None, queue_ids=None, local_vars_configuration=None):  # noqa: E501
        """BatchApplicationVersionDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._version = None
        self._queue_ids = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.version = version
        if queue_ids is not None:
            self.queue_ids = queue_ids

    @property
    def id(self):
        """Gets the id of this BatchApplicationVersionDetails.  # noqa: E501


        :return: The id of this BatchApplicationVersionDetails.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchApplicationVersionDetails.


        :param id: The id of this BatchApplicationVersionDetails.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def version(self):
        """Gets the version of this BatchApplicationVersionDetails.  # noqa: E501


        :return: The version of this BatchApplicationVersionDetails.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this BatchApplicationVersionDetails.


        :param version: The version of this BatchApplicationVersionDetails.  # noqa: E501
        :type version: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) > 100):
            raise ValueError("Invalid value for `version`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) < 1):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501

        self._version = version

    @property
    def queue_ids(self):
        """Gets the queue_ids of this BatchApplicationVersionDetails.  # noqa: E501

        List of the batch cluster queues with the application available  # noqa: E501

        :return: The queue_ids of this BatchApplicationVersionDetails.  # noqa: E501
        :rtype: list[int]
        """
        return self._queue_ids

    @queue_ids.setter
    def queue_ids(self, queue_ids):
        """Sets the queue_ids of this BatchApplicationVersionDetails.

        List of the batch cluster queues with the application available  # noqa: E501

        :param queue_ids: The queue_ids of this BatchApplicationVersionDetails.  # noqa: E501
        :type queue_ids: list[int]
        """

        self._queue_ids = queue_ids

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
        if not isinstance(other, BatchApplicationVersionDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchApplicationVersionDetails):
            return True

        return self.to_dict() != other.to_dict()
