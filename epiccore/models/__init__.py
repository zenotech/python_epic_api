# coding: utf-8

# flake8: noqa
"""
    EPIC API

    REST API for interacting with EPIC (https://epic.zenotech.com) services. <br />                             Please note this API is in BETA and does not yet contain                             all EPIC functionality.  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@zenotech.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from epiccore.models.accelerator_config import AcceleratorConfig
from epiccore.models.application import Application
from epiccore.models.application_configuration_serialiser import ApplicationConfigurationSerialiser
from epiccore.models.batch_application_details import BatchApplicationDetails
from epiccore.models.batch_application_list import BatchApplicationList
from epiccore.models.batch_application_version_details import BatchApplicationVersionDetails
from epiccore.models.batch_queue_details import BatchQueueDetails
from epiccore.models.budget import Budget
from epiccore.models.cluster_node_config import ClusterNodeConfig
from epiccore.models.cost import Cost
from epiccore.models.cost_threshold import CostThreshold
from epiccore.models.current_spend import CurrentSpend
from epiccore.models.data_location import DataLocation
from epiccore.models.data_spec import DataSpec
from epiccore.models.desktop_instance import DesktopInstance
from epiccore.models.desktop_node_launch_spec import DesktopNodeLaunchSpec
from epiccore.models.desktop_node_quote import DesktopNodeQuote
from epiccore.models.desktop_node_type import DesktopNodeType
from epiccore.models.discount import Discount
from epiccore.models.env_var import EnvVar
from epiccore.models.env_var_template import EnvVarTemplate
from epiccore.models.environment_variable import EnvironmentVariable
from epiccore.models.file import File
from epiccore.models.file_details import FileDetails
from epiccore.models.folder import Folder
from epiccore.models.folder_details import FolderDetails
from epiccore.models.iaas_cost import IaasCost
from epiccore.models.inline_response200 import InlineResponse200
from epiccore.models.inline_response2001 import InlineResponse2001
from epiccore.models.inline_response20010 import InlineResponse20010
from epiccore.models.inline_response20011 import InlineResponse20011
from epiccore.models.inline_response2002 import InlineResponse2002
from epiccore.models.inline_response2003 import InlineResponse2003
from epiccore.models.inline_response2004 import InlineResponse2004
from epiccore.models.inline_response2005 import InlineResponse2005
from epiccore.models.inline_response2006 import InlineResponse2006
from epiccore.models.inline_response2007 import InlineResponse2007
from epiccore.models.inline_response2008 import InlineResponse2008
from epiccore.models.inline_response2009 import InlineResponse2009
from epiccore.models.job import Job
from epiccore.models.job_app_options import JobAppOptions
from epiccore.models.job_array_spec import JobArraySpec
from epiccore.models.job_auth import JobAuth
from epiccore.models.job_auth_status import JobAuthStatus
from epiccore.models.job_cluster_spec import JobClusterSpec
from epiccore.models.job_configuration import JobConfiguration
from epiccore.models.job_data_binding import JobDataBinding
from epiccore.models.job_log import JobLog
from epiccore.models.job_quote import JobQuote
from epiccore.models.job_residual import JobResidual
from epiccore.models.job_residual_data import JobResidualData
from epiccore.models.job_spec import JobSpec
from epiccore.models.job_step import JobStep
from epiccore.models.job_step_details import JobStepDetails
from epiccore.models.job_summary import JobSummary
from epiccore.models.job_task_spec import JobTaskSpec
from epiccore.models.jobstep_response_request import JobstepResponseRequest
from epiccore.models.license import License
from epiccore.models.license_template import LicenseTemplate
from epiccore.models.limit import Limit
from epiccore.models.limits import Limits
from epiccore.models.max_limit import MaxLimit
from epiccore.models.monthly_limit import MonthlyLimit
from epiccore.models.price_quote import PriceQuote
from epiccore.models.product_name import ProductName
from epiccore.models.profile_summary import ProfileSummary
from epiccore.models.project import Project
from epiccore.models.project_details import ProjectDetails
from epiccore.models.sla import SLA
from epiccore.models.service_charge import ServiceCharge
from epiccore.models.session_token import SessionToken
from epiccore.models.site_configuration_serialiser import SiteConfigurationSerialiser
from epiccore.models.software_cost import SoftwareCost
from epiccore.models.spend_limit import SpendLimit
from epiccore.models.task_quote import TaskQuote
from epiccore.models.tax import Tax
from epiccore.models.team import Team
from epiccore.models.team_details import TeamDetails
from epiccore.models.template import Template
from epiccore.models.total import Total
from epiccore.models.total1 import Total1
from epiccore.models.user_name import UserName
from epiccore.models.writable_license import WritableLicense
