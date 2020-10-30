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
from epiccore.models.desktop_node_application_version import DesktopNodeApplicationVersion  # noqa: E501
from epiccore.rest import ApiException

class TestDesktopNodeApplicationVersion(unittest.TestCase):
    """DesktopNodeApplicationVersion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DesktopNodeApplicationVersion
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = epiccore.models.desktop_node_application_version.DesktopNodeApplicationVersion()  # noqa: E501
        if include_optional :
            return DesktopNodeApplicationVersion(
                id = 56, 
                application_version = '0', 
                connection_types = [
                    epiccore.models.desktop_node_connection_type.DesktopNodeConnectionType(
                        id = 56, 
                        name = '0', 
                        description = '0', )
                    ]
            )
        else :
            return DesktopNodeApplicationVersion(
                application_version = '0',
        )

    def testDesktopNodeApplicationVersion(self):
        """Test DesktopNodeApplicationVersion"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
