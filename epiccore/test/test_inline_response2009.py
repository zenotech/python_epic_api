# coding: utf-8

"""
    EPIC API

    REST API for interacting with EPIC (https://epic.zenotech.com) services. <br />                             Used by the EPIC CLI (https://github.com/zenotech/epic-cli).                             Please note this API is in BETA and does not yet contain                             all EPIC functionality.  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@zenotech.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import epiccore
from epiccore.models.inline_response2009 import InlineResponse2009  # noqa: E501
from epiccore.rest import ApiException

class TestInlineResponse2009(unittest.TestCase):
    """InlineResponse2009 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2009
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = epiccore.models.inline_response2009.InlineResponse2009()  # noqa: E501
        if include_optional :
            return InlineResponse2009(
                count = 56, 
                next = '0', 
                previous = '0', 
                results = [
                    epiccore.models.job_auth_status.JobAuthStatus(
                        required = True, 
                        state = '0', 
                        job = epiccore.models.job.Job(
                            id = 56, 
                            name = '0', 
                            app = '0', 
                            app_options = epiccore.models.app_options.App options(), 
                            application_version = 1, 
                            cost = '0', 
                            status = '0', 
                            submitted_by = '0', 
                            submitted_at = '0', 
                            finished = True, 
                            resource = epiccore.models.batch_queue_details.BatchQueueDetails(
                                id = 56, 
                                display_name = '0', 
                                display_description = '0', 
                                max_runtime = 0, 
                                max_allocation = 0, 
                                reported_avail_tasks = 0, 
                                reported_max_tasks = 0, 
                                sla = epiccore.models.sla.SLA(
                                    name = '0', 
                                    description = '0', ), 
                                maintenance_mode = True, 
                                resource_config = '0', ), 
                            project = 1, 
                            invoice_reference = '0', 
                            config = epiccore.models.job_configuration.JobConfiguration(
                                upload = [
                                    'complete'
                                    ], 
                                overwrite_existing = True, 
                                data_sync_interval = 0, ), ), 
                        user_profile = epiccore.models.user_name.UserName(
                            display_name = '0', ), 
                        permissions = '0', )
                    ]
            )
        else :
            return InlineResponse2009(
                count = 56,
                results = [
                    epiccore.models.job_auth_status.JobAuthStatus(
                        required = True, 
                        state = '0', 
                        job = epiccore.models.job.Job(
                            id = 56, 
                            name = '0', 
                            app = '0', 
                            app_options = epiccore.models.app_options.App options(), 
                            application_version = 1, 
                            cost = '0', 
                            status = '0', 
                            submitted_by = '0', 
                            submitted_at = '0', 
                            finished = True, 
                            resource = epiccore.models.batch_queue_details.BatchQueueDetails(
                                id = 56, 
                                display_name = '0', 
                                display_description = '0', 
                                max_runtime = 0, 
                                max_allocation = 0, 
                                reported_avail_tasks = 0, 
                                reported_max_tasks = 0, 
                                sla = epiccore.models.sla.SLA(
                                    name = '0', 
                                    description = '0', ), 
                                maintenance_mode = True, 
                                resource_config = '0', ), 
                            project = 1, 
                            invoice_reference = '0', 
                            config = epiccore.models.job_configuration.JobConfiguration(
                                upload = [
                                    'complete'
                                    ], 
                                overwrite_existing = True, 
                                data_sync_interval = 0, ), ), 
                        user_profile = epiccore.models.user_name.UserName(
                            display_name = '0', ), 
                        permissions = '0', )
                    ],
        )

    def testInlineResponse2009(self):
        """Test InlineResponse2009"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
