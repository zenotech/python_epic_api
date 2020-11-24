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


class DesktopNodeLaunchSpec(object):
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
        'application_version': 'int',
        'node_type': 'int',
        'connection_type': 'int',
        'runtime': 'int',
        'secure_ip': 'bool',
        'ip_address': 'str',
        'invoice_reference': 'str',
        'data_path': 'DataSpec',
        'mount_type': 'str',
        'project': 'int'
    }

    attribute_map = {
        'application_version': 'application_version',
        'node_type': 'node_type',
        'connection_type': 'connection_type',
        'runtime': 'runtime',
        'secure_ip': 'secure_ip',
        'ip_address': 'ip_address',
        'invoice_reference': 'invoice_reference',
        'data_path': 'data_path',
        'mount_type': 'mount_type',
        'project': 'project'
    }

    def __init__(self, application_version=None, node_type=None, connection_type=None, runtime=None, secure_ip=False, ip_address=None, invoice_reference=None, data_path=None, mount_type=None, project=None, local_vars_configuration=None):  # noqa: E501
        """DesktopNodeLaunchSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._application_version = None
        self._node_type = None
        self._connection_type = None
        self._runtime = None
        self._secure_ip = None
        self._ip_address = None
        self._invoice_reference = None
        self._data_path = None
        self._mount_type = None
        self._project = None
        self.discriminator = None

        self.application_version = application_version
        self.node_type = node_type
        self.connection_type = connection_type
        self.runtime = runtime
        if secure_ip is not None:
            self.secure_ip = secure_ip
        if ip_address is not None:
            self.ip_address = ip_address
        if invoice_reference is not None:
            self.invoice_reference = invoice_reference
        self.data_path = data_path
        self.mount_type = mount_type
        if project is not None:
            self.project = project

    @property
    def application_version(self):
        """Gets the application_version of this DesktopNodeLaunchSpec.  # noqa: E501

        ID of the application_version to launch. Valid values are obtained from the catalog/desktop/ endpoint  # noqa: E501

        :return: The application_version of this DesktopNodeLaunchSpec.  # noqa: E501
        :rtype: int
        """
        return self._application_version

    @application_version.setter
    def application_version(self, application_version):
        """Sets the application_version of this DesktopNodeLaunchSpec.

        ID of the application_version to launch. Valid values are obtained from the catalog/desktop/ endpoint  # noqa: E501

        :param application_version: The application_version of this DesktopNodeLaunchSpec.  # noqa: E501
        :type application_version: int
        """
        if self.local_vars_configuration.client_side_validation and application_version is None:  # noqa: E501
            raise ValueError("Invalid value for `application_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                application_version is not None and application_version < 1):  # noqa: E501
            raise ValueError("Invalid value for `application_version`, must be a value greater than or equal to `1`")  # noqa: E501

        self._application_version = application_version

    @property
    def node_type(self):
        """Gets the node_type of this DesktopNodeLaunchSpec.  # noqa: E501

        ID of the node_type. Valid values are obtained from the catalog/desktop/ endpoint  # noqa: E501

        :return: The node_type of this DesktopNodeLaunchSpec.  # noqa: E501
        :rtype: int
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this DesktopNodeLaunchSpec.

        ID of the node_type. Valid values are obtained from the catalog/desktop/ endpoint  # noqa: E501

        :param node_type: The node_type of this DesktopNodeLaunchSpec.  # noqa: E501
        :type node_type: int
        """
        if self.local_vars_configuration.client_side_validation and node_type is None:  # noqa: E501
            raise ValueError("Invalid value for `node_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                node_type is not None and node_type < 1):  # noqa: E501
            raise ValueError("Invalid value for `node_type`, must be a value greater than or equal to `1`")  # noqa: E501

        self._node_type = node_type

    @property
    def connection_type(self):
        """Gets the connection_type of this DesktopNodeLaunchSpec.  # noqa: E501

        The connection type to use for the Desktop  # noqa: E501

        :return: The connection_type of this DesktopNodeLaunchSpec.  # noqa: E501
        :rtype: int
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this DesktopNodeLaunchSpec.

        The connection type to use for the Desktop  # noqa: E501

        :param connection_type: The connection_type of this DesktopNodeLaunchSpec.  # noqa: E501
        :type connection_type: int
        """
        if self.local_vars_configuration.client_side_validation and connection_type is None:  # noqa: E501
            raise ValueError("Invalid value for `connection_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                connection_type is not None and connection_type < 1):  # noqa: E501
            raise ValueError("Invalid value for `connection_type`, must be a value greater than or equal to `1`")  # noqa: E501

        self._connection_type = connection_type

    @property
    def runtime(self):
        """Gets the runtime of this DesktopNodeLaunchSpec.  # noqa: E501

        Runtime in hours to run this desktop node for. This is the maximum runtime as the viz node can be stopped earlier and you will only be charged for the elapsed time  # noqa: E501

        :return: The runtime of this DesktopNodeLaunchSpec.  # noqa: E501
        :rtype: int
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this DesktopNodeLaunchSpec.

        Runtime in hours to run this desktop node for. This is the maximum runtime as the viz node can be stopped earlier and you will only be charged for the elapsed time  # noqa: E501

        :param runtime: The runtime of this DesktopNodeLaunchSpec.  # noqa: E501
        :type runtime: int
        """
        if self.local_vars_configuration.client_side_validation and runtime is None:  # noqa: E501
            raise ValueError("Invalid value for `runtime`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                runtime is not None and runtime < 1):  # noqa: E501
            raise ValueError("Invalid value for `runtime`, must be a value greater than or equal to `1`")  # noqa: E501

        self._runtime = runtime

    @property
    def secure_ip(self):
        """Gets the secure_ip of this DesktopNodeLaunchSpec.  # noqa: E501

        Should we restrict which IPs can connect to this node?  # noqa: E501

        :return: The secure_ip of this DesktopNodeLaunchSpec.  # noqa: E501
        :rtype: bool
        """
        return self._secure_ip

    @secure_ip.setter
    def secure_ip(self, secure_ip):
        """Sets the secure_ip of this DesktopNodeLaunchSpec.

        Should we restrict which IPs can connect to this node?  # noqa: E501

        :param secure_ip: The secure_ip of this DesktopNodeLaunchSpec.  # noqa: E501
        :type secure_ip: bool
        """

        self._secure_ip = secure_ip

    @property
    def ip_address(self):
        """Gets the ip_address of this DesktopNodeLaunchSpec.  # noqa: E501

        IPv4 Address to restrict connections to this node from  # noqa: E501

        :return: The ip_address of this DesktopNodeLaunchSpec.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this DesktopNodeLaunchSpec.

        IPv4 Address to restrict connections to this node from  # noqa: E501

        :param ip_address: The ip_address of this DesktopNodeLaunchSpec.  # noqa: E501
        :type ip_address: str
        """
        if (self.local_vars_configuration.client_side_validation and
                ip_address is not None and len(ip_address) < 1):
            raise ValueError("Invalid value for `ip_address`, length must be greater than or equal to `1`")  # noqa: E501

        self._ip_address = ip_address

    @property
    def invoice_reference(self):
        """Gets the invoice_reference of this DesktopNodeLaunchSpec.  # noqa: E501

        Invoice reference - this text will appear on the monthly invoice against this nodes charges  # noqa: E501

        :return: The invoice_reference of this DesktopNodeLaunchSpec.  # noqa: E501
        :rtype: str
        """
        return self._invoice_reference

    @invoice_reference.setter
    def invoice_reference(self, invoice_reference):
        """Sets the invoice_reference of this DesktopNodeLaunchSpec.

        Invoice reference - this text will appear on the monthly invoice against this nodes charges  # noqa: E501

        :param invoice_reference: The invoice_reference of this DesktopNodeLaunchSpec.  # noqa: E501
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
    def data_path(self):
        """Gets the data_path of this DesktopNodeLaunchSpec.  # noqa: E501


        :return: The data_path of this DesktopNodeLaunchSpec.  # noqa: E501
        :rtype: DataSpec
        """
        return self._data_path

    @data_path.setter
    def data_path(self, data_path):
        """Sets the data_path of this DesktopNodeLaunchSpec.


        :param data_path: The data_path of this DesktopNodeLaunchSpec.  # noqa: E501
        :type data_path: DataSpec
        """
        if self.local_vars_configuration.client_side_validation and data_path is None:  # noqa: E501
            raise ValueError("Invalid value for `data_path`, must not be `None`")  # noqa: E501

        self._data_path = data_path

    @property
    def mount_type(self):
        """Gets the mount_type of this DesktopNodeLaunchSpec.  # noqa: E501

        How should the data folder be mounted to the desktop. Offline takes a copy of the data and will not be automatically synced back to the data store.  # noqa: E501

        :return: The mount_type of this DesktopNodeLaunchSpec.  # noqa: E501
        :rtype: str
        """
        return self._mount_type

    @mount_type.setter
    def mount_type(self, mount_type):
        """Sets the mount_type of this DesktopNodeLaunchSpec.

        How should the data folder be mounted to the desktop. Offline takes a copy of the data and will not be automatically synced back to the data store.  # noqa: E501

        :param mount_type: The mount_type of this DesktopNodeLaunchSpec.  # noqa: E501
        :type mount_type: str
        """
        if self.local_vars_configuration.client_side_validation and mount_type is None:  # noqa: E501
            raise ValueError("Invalid value for `mount_type`, must not be `None`")  # noqa: E501
        allowed_values = ["online", "offline"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mount_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mount_type` ({0}), must be one of {1}"  # noqa: E501
                .format(mount_type, allowed_values)
            )

        self._mount_type = mount_type

    @property
    def project(self):
        """Gets the project of this DesktopNodeLaunchSpec.  # noqa: E501

        Project ID to bill this desktop node against  # noqa: E501

        :return: The project of this DesktopNodeLaunchSpec.  # noqa: E501
        :rtype: int
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this DesktopNodeLaunchSpec.

        Project ID to bill this desktop node against  # noqa: E501

        :param project: The project of this DesktopNodeLaunchSpec.  # noqa: E501
        :type project: int
        """
        if (self.local_vars_configuration.client_side_validation and
                project is not None and project < -1):  # noqa: E501
            raise ValueError("Invalid value for `project`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._project = project

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
        if not isinstance(other, DesktopNodeLaunchSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DesktopNodeLaunchSpec):
            return True

        return self.to_dict() != other.to_dict()
