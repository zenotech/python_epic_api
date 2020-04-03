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

import epic_api
from epic_api.models.batch_job_spec import BatchJobSpec  # noqa: E501
from epic_api.rest import ApiException

class TestBatchJobSpec(unittest.TestCase):
    """BatchJobSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BatchJobSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = epic_api.models.batch_job_spec.BatchJobSpec()  # noqa: E501
        if include_optional :
            return BatchJobSpec(
                application_version = 1, 
                project = -1, 
                tasks = [
                    epic_api.models.batch_job_task_spec.BatchJobTaskSpec(
                        reference = '0', 
                        partitions = 1, 
                        runtime = 1, 
                        task_distribution = 'core', 
                        hyperthreading = True, )
                    ]
            )
        else :
            return BatchJobSpec(
                application_version = 1,
                tasks = [
                    epic_api.models.batch_job_task_spec.BatchJobTaskSpec(
                        reference = '0', 
                        partitions = 1, 
                        runtime = 1, 
                        task_distribution = 'core', 
                        hyperthreading = True, )
                    ],
        )

    def testBatchJobSpec(self):
        """Test BatchJobSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
