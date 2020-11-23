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


class Job(object):
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
        'app_options': 'object',
        'application_version': 'int',
        'cost': 'str',
        'status': 'str',
        'submitted_by': 'str',
        'submitted_at': 'str',
        'finished': 'bool',
        'resource': 'BatchQueueDetails',
        'project': 'int',
        'invoice_reference': 'str',
        'config': 'JobConfiguration',
        'job_steps': 'list[JobStep]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'app': 'app',
        'app_options': 'app_options',
        'application_version': 'application_version',
        'cost': 'cost',
        'status': 'status',
        'submitted_by': 'submitted_by',
        'submitted_at': 'submitted_at',
        'finished': 'finished',
        'resource': 'resource',
        'project': 'project',
        'invoice_reference': 'invoice_reference',
        'config': 'config',
        'job_steps': 'job_steps'
    }

    def __init__(self, id=None, name=None, app=None, app_options=None, application_version=None, cost=None, status=None, submitted_by=None, submitted_at=None, finished=None, resource=None, project=None, invoice_reference=None, config=None, job_steps=None, local_vars_configuration=None):  # noqa: E501
        """Job - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._app = None
        self._app_options = None
        self._application_version = None
        self._cost = None
        self._status = None
        self._submitted_by = None
        self._submitted_at = None
        self._finished = None
        self._resource = None
        self._project = None
        self._invoice_reference = None
        self._config = None
        self._job_steps = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if app is not None:
            self.app = app
        if app_options is not None:
            self.app_options = app_options
        if application_version is not None:
            self.application_version = application_version
        if cost is not None:
            self.cost = cost
        if status is not None:
            self.status = status
        if submitted_by is not None:
            self.submitted_by = submitted_by
        if submitted_at is not None:
            self.submitted_at = submitted_at
        if finished is not None:
            self.finished = finished
        if resource is not None:
            self.resource = resource
        if project is not None:
            self.project = project
        if invoice_reference is not None:
            self.invoice_reference = invoice_reference
        if config is not None:
            self.config = config
        if job_steps is not None:
            self.job_steps = job_steps

    @property
    def id(self):
        """Gets the id of this Job.  # noqa: E501

        The ID for this job  # noqa: E501

        :return: The id of this Job.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Job.

        The ID for this job  # noqa: E501

        :param id: The id of this Job.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Job.  # noqa: E501

        Name of this job  # noqa: E501

        :return: The name of this Job.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Job.

        Name of this job  # noqa: E501

        :param name: The name of this Job.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def app(self):
        """Gets the app of this Job.  # noqa: E501

        Name of the application that this job uses  # noqa: E501

        :return: The app of this Job.  # noqa: E501
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this Job.

        Name of the application that this job uses  # noqa: E501

        :param app: The app of this Job.  # noqa: E501
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
    def app_options(self):
        """Gets the app_options of this Job.  # noqa: E501

        Job app options  # noqa: E501

        :return: The app_options of this Job.  # noqa: E501
        :rtype: object
        """
        return self._app_options

    @app_options.setter
    def app_options(self, app_options):
        """Sets the app_options of this Job.

        Job app options  # noqa: E501

        :param app_options: The app_options of this Job.  # noqa: E501
        :type app_options: object
        """

        self._app_options = app_options

    @property
    def application_version(self):
        """Gets the application_version of this Job.  # noqa: E501

        Application version ID  # noqa: E501

        :return: The application_version of this Job.  # noqa: E501
        :rtype: int
        """
        return self._application_version

    @application_version.setter
    def application_version(self, application_version):
        """Sets the application_version of this Job.

        Application version ID  # noqa: E501

        :param application_version: The application_version of this Job.  # noqa: E501
        :type application_version: int
        """
        if (self.local_vars_configuration.client_side_validation and
                application_version is not None and application_version < 1):  # noqa: E501
            raise ValueError("Invalid value for `application_version`, must be a value greater than or equal to `1`")  # noqa: E501

        self._application_version = application_version

    @property
    def cost(self):
        """Gets the cost of this Job.  # noqa: E501

        Maximum cost for running this job  # noqa: E501

        :return: The cost of this Job.  # noqa: E501
        :rtype: str
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """Sets the cost of this Job.

        Maximum cost for running this job  # noqa: E501

        :param cost: The cost of this Job.  # noqa: E501
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
    def status(self):
        """Gets the status of this Job.  # noqa: E501

        Current status of this job  # noqa: E501

        :return: The status of this Job.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Job.

        Current status of this job  # noqa: E501

        :param status: The status of this Job.  # noqa: E501
        :type status: str
        """
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) > 100):
            raise ValueError("Invalid value for `status`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) < 1):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

    @property
    def submitted_by(self):
        """Gets the submitted_by of this Job.  # noqa: E501

        Name of the user who submitted this job  # noqa: E501

        :return: The submitted_by of this Job.  # noqa: E501
        :rtype: str
        """
        return self._submitted_by

    @submitted_by.setter
    def submitted_by(self, submitted_by):
        """Sets the submitted_by of this Job.

        Name of the user who submitted this job  # noqa: E501

        :param submitted_by: The submitted_by of this Job.  # noqa: E501
        :type submitted_by: str
        """

        self._submitted_by = submitted_by

    @property
    def submitted_at(self):
        """Gets the submitted_at of this Job.  # noqa: E501

        Date at which this job was submitted  # noqa: E501

        :return: The submitted_at of this Job.  # noqa: E501
        :rtype: str
        """
        return self._submitted_at

    @submitted_at.setter
    def submitted_at(self, submitted_at):
        """Sets the submitted_at of this Job.

        Date at which this job was submitted  # noqa: E501

        :param submitted_at: The submitted_at of this Job.  # noqa: E501
        :type submitted_at: str
        """

        self._submitted_at = submitted_at

    @property
    def finished(self):
        """Gets the finished of this Job.  # noqa: E501

        Has this job finished?  # noqa: E501

        :return: The finished of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        """Sets the finished of this Job.

        Has this job finished?  # noqa: E501

        :param finished: The finished of this Job.  # noqa: E501
        :type finished: bool
        """

        self._finished = finished

    @property
    def resource(self):
        """Gets the resource of this Job.  # noqa: E501


        :return: The resource of this Job.  # noqa: E501
        :rtype: BatchQueueDetails
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Job.


        :param resource: The resource of this Job.  # noqa: E501
        :type resource: BatchQueueDetails
        """

        self._resource = resource

    @property
    def project(self):
        """Gets the project of this Job.  # noqa: E501

        Project ID to bill this job against  # noqa: E501

        :return: The project of this Job.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Job.

        Project ID to bill this job against  # noqa: E501

        :param project: The project of this Job.  # noqa: E501
        :type project: int
        """
        if (self.local_vars_configuration.client_side_validation and
                project is not None and project < 1):  # noqa: E501
            raise ValueError("Invalid value for `project`, must be a value greater than or equal to `1`")  # noqa: E501

        self._project = project

    @property
    def invoice_reference(self):
        """Gets the invoice_reference of this Job.  # noqa: E501

        Invoice reference - this text will appear on the monthly invoice against this jobs charges  # noqa: E501

        :return: The invoice_reference of this Job.  # noqa: E501
        :rtype: str
        """
        return self._invoice_reference

    @invoice_reference.setter
    def invoice_reference(self, invoice_reference):
        """Sets the invoice_reference of this Job.

        Invoice reference - this text will appear on the monthly invoice against this jobs charges  # noqa: E501

        :param invoice_reference: The invoice_reference of this Job.  # noqa: E501
        :type invoice_reference: str
        """
        if (self.local_vars_configuration.client_side_validation and
                invoice_reference is not None and len(invoice_reference) > 100):
            raise ValueError("Invalid value for `invoice_reference`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                invoice_reference is not None and len(invoice_reference) < 1):
            raise ValueError("Invalid value for `invoice_reference`, length must be greater than or equal to `1`")  # noqa: E501

        self._invoice_reference = invoice_reference

    @property
    def config(self):
        """Gets the config of this Job.  # noqa: E501


        :return: The config of this Job.  # noqa: E501
        :rtype: JobConfiguration
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Job.


        :param config: The config of this Job.  # noqa: E501
        :type config: JobConfiguration
        """

        self._config = config

    @property
    def job_steps(self):
        """Gets the job_steps of this Job.  # noqa: E501

        The job steps associated with this Job  # noqa: E501

        :return: The job_steps of this Job.  # noqa: E501
        :rtype: list[JobStep]
        """
        return self._job_steps

    @job_steps.setter
    def job_steps(self, job_steps):
        """Sets the job_steps of this Job.

        The job steps associated with this Job  # noqa: E501

        :param job_steps: The job_steps of this Job.  # noqa: E501
        :type job_steps: list[JobStep]
        """

        self._job_steps = job_steps

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
        if not isinstance(other, Job):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Job):
            return True

        return self.to_dict() != other.to_dict()
