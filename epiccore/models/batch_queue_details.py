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


class BatchQueueDetails(object):
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
        'queue_code': 'str',
        'name': 'str',
        'description': 'str',
        'cluster_name': 'str',
        'max_runtime': 'int',
        'max_allocation': 'int',
        'reported_avail_tasks': 'int',
        'reported_max_tasks': 'int',
        'sla': 'SLA',
        'maintenance_mode': 'bool',
        'resource_config': 'ClusterNodeConfig'
    }

    attribute_map = {
        'queue_code': 'queue_code',
        'name': 'name',
        'description': 'description',
        'cluster_name': 'cluster_name',
        'max_runtime': 'max_runtime',
        'max_allocation': 'max_allocation',
        'reported_avail_tasks': 'reported_avail_tasks',
        'reported_max_tasks': 'reported_max_tasks',
        'sla': 'sla',
        'maintenance_mode': 'maintenance_mode',
        'resource_config': 'resource_config'
    }

    def __init__(self, queue_code=None, name=None, description=None, cluster_name=None, max_runtime=None, max_allocation=None, reported_avail_tasks=None, reported_max_tasks=None, sla=None, maintenance_mode=None, resource_config=None, local_vars_configuration=None):  # noqa: E501
        """BatchQueueDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._queue_code = None
        self._name = None
        self._description = None
        self._cluster_name = None
        self._max_runtime = None
        self._max_allocation = None
        self._reported_avail_tasks = None
        self._reported_max_tasks = None
        self._sla = None
        self._maintenance_mode = None
        self._resource_config = None
        self.discriminator = None

        self.queue_code = queue_code
        if name is not None:
            self.name = name
        self.description = description
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if max_runtime is not None:
            self.max_runtime = max_runtime
        if max_allocation is not None:
            self.max_allocation = max_allocation
        self.reported_avail_tasks = reported_avail_tasks
        self.reported_max_tasks = reported_max_tasks
        self.sla = sla
        if maintenance_mode is not None:
            self.maintenance_mode = maintenance_mode
        self.resource_config = resource_config

    @property
    def queue_code(self):
        """Gets the queue_code of this BatchQueueDetails.  # noqa: E501


        :return: The queue_code of this BatchQueueDetails.  # noqa: E501
        :rtype: str
        """
        return self._queue_code

    @queue_code.setter
    def queue_code(self, queue_code):
        """Sets the queue_code of this BatchQueueDetails.


        :param queue_code: The queue_code of this BatchQueueDetails.  # noqa: E501
        :type queue_code: str
        """
        if self.local_vars_configuration.client_side_validation and queue_code is None:  # noqa: E501
            raise ValueError("Invalid value for `queue_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                queue_code is not None and len(queue_code) > 100):
            raise ValueError("Invalid value for `queue_code`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                queue_code is not None and len(queue_code) < 1):
            raise ValueError("Invalid value for `queue_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._queue_code = queue_code

    @property
    def name(self):
        """Gets the name of this BatchQueueDetails.  # noqa: E501


        :return: The name of this BatchQueueDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BatchQueueDetails.


        :param name: The name of this BatchQueueDetails.  # noqa: E501
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
        """Gets the description of this BatchQueueDetails.  # noqa: E501


        :return: The description of this BatchQueueDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BatchQueueDetails.


        :param description: The description of this BatchQueueDetails.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1000):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")  # noqa: E501

        self._description = description

    @property
    def cluster_name(self):
        """Gets the cluster_name of this BatchQueueDetails.  # noqa: E501


        :return: The cluster_name of this BatchQueueDetails.  # noqa: E501
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this BatchQueueDetails.


        :param cluster_name: The cluster_name of this BatchQueueDetails.  # noqa: E501
        :type cluster_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                cluster_name is not None and len(cluster_name) > 100):
            raise ValueError("Invalid value for `cluster_name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cluster_name is not None and len(cluster_name) < 1):
            raise ValueError("Invalid value for `cluster_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._cluster_name = cluster_name

    @property
    def max_runtime(self):
        """Gets the max_runtime of this BatchQueueDetails.  # noqa: E501


        :return: The max_runtime of this BatchQueueDetails.  # noqa: E501
        :rtype: int
        """
        return self._max_runtime

    @max_runtime.setter
    def max_runtime(self, max_runtime):
        """Sets the max_runtime of this BatchQueueDetails.


        :param max_runtime: The max_runtime of this BatchQueueDetails.  # noqa: E501
        :type max_runtime: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_runtime is not None and max_runtime > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `max_runtime`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_runtime is not None and max_runtime < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_runtime`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_runtime = max_runtime

    @property
    def max_allocation(self):
        """Gets the max_allocation of this BatchQueueDetails.  # noqa: E501


        :return: The max_allocation of this BatchQueueDetails.  # noqa: E501
        :rtype: int
        """
        return self._max_allocation

    @max_allocation.setter
    def max_allocation(self, max_allocation):
        """Sets the max_allocation of this BatchQueueDetails.


        :param max_allocation: The max_allocation of this BatchQueueDetails.  # noqa: E501
        :type max_allocation: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_allocation is not None and max_allocation > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `max_allocation`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_allocation is not None and max_allocation < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_allocation`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_allocation = max_allocation

    @property
    def reported_avail_tasks(self):
        """Gets the reported_avail_tasks of this BatchQueueDetails.  # noqa: E501


        :return: The reported_avail_tasks of this BatchQueueDetails.  # noqa: E501
        :rtype: int
        """
        return self._reported_avail_tasks

    @reported_avail_tasks.setter
    def reported_avail_tasks(self, reported_avail_tasks):
        """Sets the reported_avail_tasks of this BatchQueueDetails.


        :param reported_avail_tasks: The reported_avail_tasks of this BatchQueueDetails.  # noqa: E501
        :type reported_avail_tasks: int
        """
        if (self.local_vars_configuration.client_side_validation and
                reported_avail_tasks is not None and reported_avail_tasks > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `reported_avail_tasks`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                reported_avail_tasks is not None and reported_avail_tasks < 0):  # noqa: E501
            raise ValueError("Invalid value for `reported_avail_tasks`, must be a value greater than or equal to `0`")  # noqa: E501

        self._reported_avail_tasks = reported_avail_tasks

    @property
    def reported_max_tasks(self):
        """Gets the reported_max_tasks of this BatchQueueDetails.  # noqa: E501


        :return: The reported_max_tasks of this BatchQueueDetails.  # noqa: E501
        :rtype: int
        """
        return self._reported_max_tasks

    @reported_max_tasks.setter
    def reported_max_tasks(self, reported_max_tasks):
        """Sets the reported_max_tasks of this BatchQueueDetails.


        :param reported_max_tasks: The reported_max_tasks of this BatchQueueDetails.  # noqa: E501
        :type reported_max_tasks: int
        """
        if (self.local_vars_configuration.client_side_validation and
                reported_max_tasks is not None and reported_max_tasks > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `reported_max_tasks`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                reported_max_tasks is not None and reported_max_tasks < 0):  # noqa: E501
            raise ValueError("Invalid value for `reported_max_tasks`, must be a value greater than or equal to `0`")  # noqa: E501

        self._reported_max_tasks = reported_max_tasks

    @property
    def sla(self):
        """Gets the sla of this BatchQueueDetails.  # noqa: E501


        :return: The sla of this BatchQueueDetails.  # noqa: E501
        :rtype: SLA
        """
        return self._sla

    @sla.setter
    def sla(self, sla):
        """Sets the sla of this BatchQueueDetails.


        :param sla: The sla of this BatchQueueDetails.  # noqa: E501
        :type sla: SLA
        """
        if self.local_vars_configuration.client_side_validation and sla is None:  # noqa: E501
            raise ValueError("Invalid value for `sla`, must not be `None`")  # noqa: E501

        self._sla = sla

    @property
    def maintenance_mode(self):
        """Gets the maintenance_mode of this BatchQueueDetails.  # noqa: E501


        :return: The maintenance_mode of this BatchQueueDetails.  # noqa: E501
        :rtype: bool
        """
        return self._maintenance_mode

    @maintenance_mode.setter
    def maintenance_mode(self, maintenance_mode):
        """Sets the maintenance_mode of this BatchQueueDetails.


        :param maintenance_mode: The maintenance_mode of this BatchQueueDetails.  # noqa: E501
        :type maintenance_mode: bool
        """

        self._maintenance_mode = maintenance_mode

    @property
    def resource_config(self):
        """Gets the resource_config of this BatchQueueDetails.  # noqa: E501


        :return: The resource_config of this BatchQueueDetails.  # noqa: E501
        :rtype: ClusterNodeConfig
        """
        return self._resource_config

    @resource_config.setter
    def resource_config(self, resource_config):
        """Sets the resource_config of this BatchQueueDetails.


        :param resource_config: The resource_config of this BatchQueueDetails.  # noqa: E501
        :type resource_config: ClusterNodeConfig
        """
        if self.local_vars_configuration.client_side_validation and resource_config is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_config`, must not be `None`")  # noqa: E501

        self._resource_config = resource_config

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
        if not isinstance(other, BatchQueueDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchQueueDetails):
            return True

        return self.to_dict() != other.to_dict()
