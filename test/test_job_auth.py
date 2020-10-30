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
from epiccore.models.job_auth import JobAuth  # noqa: E501
from epiccore.rest import ApiException

class TestJobAuth(unittest.TestCase):
    """JobAuth unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobAuth
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = epiccore.models.job_auth.JobAuth()  # noqa: E501
        if include_optional :
            return JobAuth(
                enabled = True, 
                all_jobs = True, 
                cost_threshold = '0', 
                description_str = '0'
            )
        else :
            return JobAuth(
        )

    def testJobAuth(self):
        """Test JobAuth"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
