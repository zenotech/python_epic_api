# coding: utf-8

"""
    EPIC API

    REST API for interacting with EPIC (https://epic.zenotech.com) services. <br />                             Used by the EPIC CLI (https://github.com/zenotech/epic-cli).                             Please note this API is in BETA and does not yet contain                             all EPIC functionality.  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@zenotech.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import epiccore
from epiccore.model.data_spec import DataSpec
from epiccore.model.job_configuration import JobConfiguration
from epiccore.model.job_data_binding import JobDataBinding
globals()['DataSpec'] = DataSpec
globals()['JobConfiguration'] = JobConfiguration
globals()['JobDataBinding'] = JobDataBinding
from epiccore.model.job_array_spec import JobArraySpec


class TestJobArraySpec(unittest.TestCase):
    """JobArraySpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJobArraySpec(self):
        """Test JobArraySpec"""
        # FIXME: construct object with mandatory attributes with example values
        # model = JobArraySpec()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
