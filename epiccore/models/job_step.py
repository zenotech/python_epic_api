# coding: utf-8

"""
    EPIC API

    REST API for interacting with EPIC (https://epic.zenotech.com) services. <br />                             Used by the EPIC CLI (https://github.com/zenotech/epic-cli).                             Please note this API is in BETA and does not yet contain                             all EPIC functionality.  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@zenotech.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from epiccore.configuration import Configuration


class JobStep(object):
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
        'run_if_previous_step_fails': 'bool',
        'step_name': 'str',
        'node_count': 'int',
        'num_tasks': 'int',
        'tasks_per_node': 'int',
        'threads_per_task': 'int',
        'max_runtime': 'int',
        'status': 'str',
        'exit_code': 'int',
        'start': 'datetime',
        'end': 'datetime',
        'wallclock': 'str'
    }

    attribute_map = {
        'id': 'id',
        'run_if_previous_step_fails': 'run_if_previous_step_fails',
        'step_name': 'step_name',
        'node_count': 'node_count',
        'num_tasks': 'num_tasks',
        'tasks_per_node': 'tasks_per_node',
        'threads_per_task': 'threads_per_task',
        'max_runtime': 'max_runtime',
        'status': 'status',
        'exit_code': 'exit_code',
        'start': 'start',
        'end': 'end',
        'wallclock': 'wallclock'
    }

    def __init__(self, id=None, run_if_previous_step_fails=None, step_name=None, node_count=None, num_tasks=None, tasks_per_node=None, threads_per_task=None, max_runtime=None, status=None, exit_code=None, start=None, end=None, wallclock=None, local_vars_configuration=None):  # noqa: E501
        """JobStep - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._run_if_previous_step_fails = None
        self._step_name = None
        self._node_count = None
        self._num_tasks = None
        self._tasks_per_node = None
        self._threads_per_task = None
        self._max_runtime = None
        self._status = None
        self._exit_code = None
        self._start = None
        self._end = None
        self._wallclock = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if run_if_previous_step_fails is not None:
            self.run_if_previous_step_fails = run_if_previous_step_fails
        self.step_name = step_name
        if node_count is not None:
            self.node_count = node_count
        if num_tasks is not None:
            self.num_tasks = num_tasks
        if tasks_per_node is not None:
            self.tasks_per_node = tasks_per_node
        if threads_per_task is not None:
            self.threads_per_task = threads_per_task
        if max_runtime is not None:
            self.max_runtime = max_runtime
        self.status = status
        self.exit_code = exit_code
        self.start = start
        self.end = end
        self.wallclock = wallclock

    @property
    def id(self):
        """Gets the id of this JobStep.  # noqa: E501

        jobstep id  # noqa: E501

        :return: The id of this JobStep.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobStep.

        jobstep id  # noqa: E501

        :param id: The id of this JobStep.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def run_if_previous_step_fails(self):
        """Gets the run_if_previous_step_fails of this JobStep.  # noqa: E501

        Whether this job step will run if the previous step fails  # noqa: E501

        :return: The run_if_previous_step_fails of this JobStep.  # noqa: E501
        :rtype: bool
        """
        return self._run_if_previous_step_fails

    @run_if_previous_step_fails.setter
    def run_if_previous_step_fails(self, run_if_previous_step_fails):
        """Sets the run_if_previous_step_fails of this JobStep.

        Whether this job step will run if the previous step fails  # noqa: E501

        :param run_if_previous_step_fails: The run_if_previous_step_fails of this JobStep.  # noqa: E501
        :type run_if_previous_step_fails: bool
        """

        self._run_if_previous_step_fails = run_if_previous_step_fails

    @property
    def step_name(self):
        """Gets the step_name of this JobStep.  # noqa: E501

        The name of this job step  # noqa: E501

        :return: The step_name of this JobStep.  # noqa: E501
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """Sets the step_name of this JobStep.

        The name of this job step  # noqa: E501

        :param step_name: The step_name of this JobStep.  # noqa: E501
        :type step_name: str
        """
        if self.local_vars_configuration.client_side_validation and step_name is None:  # noqa: E501
            raise ValueError("Invalid value for `step_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                step_name is not None and len(step_name) > 30):
            raise ValueError("Invalid value for `step_name`, length must be less than or equal to `30`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                step_name is not None and len(step_name) < 1):
            raise ValueError("Invalid value for `step_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._step_name = step_name

    @property
    def node_count(self):
        """Gets the node_count of this JobStep.  # noqa: E501

        Number of nodes this job step will run on  # noqa: E501

        :return: The node_count of this JobStep.  # noqa: E501
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """Sets the node_count of this JobStep.

        Number of nodes this job step will run on  # noqa: E501

        :param node_count: The node_count of this JobStep.  # noqa: E501
        :type node_count: int
        """
        if (self.local_vars_configuration.client_side_validation and
                node_count is not None and node_count > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `node_count`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                node_count is not None and node_count < 1):  # noqa: E501
            raise ValueError("Invalid value for `node_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._node_count = node_count

    @property
    def num_tasks(self):
        """Gets the num_tasks of this JobStep.  # noqa: E501

        Number of tasks that will run for this job step  # noqa: E501

        :return: The num_tasks of this JobStep.  # noqa: E501
        :rtype: int
        """
        return self._num_tasks

    @num_tasks.setter
    def num_tasks(self, num_tasks):
        """Sets the num_tasks of this JobStep.

        Number of tasks that will run for this job step  # noqa: E501

        :param num_tasks: The num_tasks of this JobStep.  # noqa: E501
        :type num_tasks: int
        """
        if (self.local_vars_configuration.client_side_validation and
                num_tasks is not None and num_tasks > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `num_tasks`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                num_tasks is not None and num_tasks < 1):  # noqa: E501
            raise ValueError("Invalid value for `num_tasks`, must be a value greater than or equal to `1`")  # noqa: E501

        self._num_tasks = num_tasks

    @property
    def tasks_per_node(self):
        """Gets the tasks_per_node of this JobStep.  # noqa: E501

        Number of tasks that will run on each node  # noqa: E501

        :return: The tasks_per_node of this JobStep.  # noqa: E501
        :rtype: int
        """
        return self._tasks_per_node

    @tasks_per_node.setter
    def tasks_per_node(self, tasks_per_node):
        """Sets the tasks_per_node of this JobStep.

        Number of tasks that will run on each node  # noqa: E501

        :param tasks_per_node: The tasks_per_node of this JobStep.  # noqa: E501
        :type tasks_per_node: int
        """
        if (self.local_vars_configuration.client_side_validation and
                tasks_per_node is not None and tasks_per_node > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `tasks_per_node`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tasks_per_node is not None and tasks_per_node < 1):  # noqa: E501
            raise ValueError("Invalid value for `tasks_per_node`, must be a value greater than or equal to `1`")  # noqa: E501

        self._tasks_per_node = tasks_per_node

    @property
    def threads_per_task(self):
        """Gets the threads_per_task of this JobStep.  # noqa: E501

        Number of threads assigned to each task  # noqa: E501

        :return: The threads_per_task of this JobStep.  # noqa: E501
        :rtype: int
        """
        return self._threads_per_task

    @threads_per_task.setter
    def threads_per_task(self, threads_per_task):
        """Sets the threads_per_task of this JobStep.

        Number of threads assigned to each task  # noqa: E501

        :param threads_per_task: The threads_per_task of this JobStep.  # noqa: E501
        :type threads_per_task: int
        """
        if (self.local_vars_configuration.client_side_validation and
                threads_per_task is not None and threads_per_task > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `threads_per_task`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                threads_per_task is not None and threads_per_task < 1):  # noqa: E501
            raise ValueError("Invalid value for `threads_per_task`, must be a value greater than or equal to `1`")  # noqa: E501

        self._threads_per_task = threads_per_task

    @property
    def max_runtime(self):
        """Gets the max_runtime of this JobStep.  # noqa: E501

        Maximum runtime in hours that this job step will run for  # noqa: E501

        :return: The max_runtime of this JobStep.  # noqa: E501
        :rtype: int
        """
        return self._max_runtime

    @max_runtime.setter
    def max_runtime(self, max_runtime):
        """Sets the max_runtime of this JobStep.

        Maximum runtime in hours that this job step will run for  # noqa: E501

        :param max_runtime: The max_runtime of this JobStep.  # noqa: E501
        :type max_runtime: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_runtime is not None and max_runtime > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `max_runtime`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_runtime is not None and max_runtime < 1):  # noqa: E501
            raise ValueError("Invalid value for `max_runtime`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_runtime = max_runtime

    @property
    def status(self):
        """Gets the status of this JobStep.  # noqa: E501

        Status of this jobstep  # noqa: E501

        :return: The status of this JobStep.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobStep.

        Status of this jobstep  # noqa: E501

        :param status: The status of this JobStep.  # noqa: E501
        :type status: str
        """
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) > 50):
            raise ValueError("Invalid value for `status`, length must be less than or equal to `50`")  # noqa: E501

        self._status = status

    @property
    def exit_code(self):
        """Gets the exit_code of this JobStep.  # noqa: E501

        Unix exit code for this job step  # noqa: E501

        :return: The exit_code of this JobStep.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this JobStep.

        Unix exit code for this job step  # noqa: E501

        :param exit_code: The exit_code of this JobStep.  # noqa: E501
        :type exit_code: int
        """
        if (self.local_vars_configuration.client_side_validation and
                exit_code is not None and exit_code > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `exit_code`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                exit_code is not None and exit_code < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `exit_code`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._exit_code = exit_code

    @property
    def start(self):
        """Gets the start of this JobStep.  # noqa: E501

        Time this job step started running  # noqa: E501

        :return: The start of this JobStep.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this JobStep.

        Time this job step started running  # noqa: E501

        :param start: The start of this JobStep.  # noqa: E501
        :type start: datetime
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this JobStep.  # noqa: E501

        Time this job step finished running  # noqa: E501

        :return: The end of this JobStep.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this JobStep.

        Time this job step finished running  # noqa: E501

        :param end: The end of this JobStep.  # noqa: E501
        :type end: datetime
        """

        self._end = end

    @property
    def wallclock(self):
        """Gets the wallclock of this JobStep.  # noqa: E501


        :return: The wallclock of this JobStep.  # noqa: E501
        :rtype: str
        """
        return self._wallclock

    @wallclock.setter
    def wallclock(self, wallclock):
        """Sets the wallclock of this JobStep.


        :param wallclock: The wallclock of this JobStep.  # noqa: E501
        :type wallclock: str
        """

        self._wallclock = wallclock

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
        if not isinstance(other, JobStep):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JobStep):
            return True

        return self.to_dict() != other.to_dict()
