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
from epic_api.models.user_name import UserName  # noqa: E501
from epic_api.rest import ApiException

class TestUserName(unittest.TestCase):
    """UserName unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserName
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = epic_api.models.user_name.UserName()  # noqa: E501
        if include_optional :
            return UserName(
                display_name = '0'
            )
        else :
            return UserName(
        )

    def testUserName(self):
        """Test UserName"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
