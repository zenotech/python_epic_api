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


class JobstepResponseRequest(object):
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
        'job_step': 'int',
        'response_recieved': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'job_step': 'job_step',
        'response_recieved': 'response_recieved'
    }

    def __init__(self, id=None, job_step=None, response_recieved=None, local_vars_configuration=None):  # noqa: E501
        """JobstepResponseRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._job_step = None
        self._response_recieved = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.job_step = job_step
        if response_recieved is not None:
            self.response_recieved = response_recieved

    @property
    def id(self):
        """Gets the id of this JobstepResponseRequest.  # noqa: E501

        The ID for this refresh request  # noqa: E501

        :return: The id of this JobstepResponseRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobstepResponseRequest.

        The ID for this refresh request  # noqa: E501

        :param id: The id of this JobstepResponseRequest.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def job_step(self):
        """Gets the job_step of this JobstepResponseRequest.  # noqa: E501

        The ID of the running job step to refresh  # noqa: E501

        :return: The job_step of this JobstepResponseRequest.  # noqa: E501
        :rtype: int
        """
        return self._job_step

    @job_step.setter
    def job_step(self, job_step):
        """Sets the job_step of this JobstepResponseRequest.

        The ID of the running job step to refresh  # noqa: E501

        :param job_step: The job_step of this JobstepResponseRequest.  # noqa: E501
        :type job_step: int
        """
        if self.local_vars_configuration.client_side_validation and job_step is None:  # noqa: E501
            raise ValueError("Invalid value for `job_step`, must not be `None`")  # noqa: E501

        self._job_step = job_step

    @property
    def response_recieved(self):
        """Gets the response_recieved of this JobstepResponseRequest.  # noqa: E501

        Has the refresh completed?  # noqa: E501

        :return: The response_recieved of this JobstepResponseRequest.  # noqa: E501
        :rtype: bool
        """
        return self._response_recieved

    @response_recieved.setter
    def response_recieved(self, response_recieved):
        """Sets the response_recieved of this JobstepResponseRequest.

        Has the refresh completed?  # noqa: E501

        :param response_recieved: The response_recieved of this JobstepResponseRequest.  # noqa: E501
        :type response_recieved: bool
        """

        self._response_recieved = response_recieved

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
        if not isinstance(other, JobstepResponseRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobstepResponseRequest):
            return True

        return self.to_dict() != other.to_dict()
