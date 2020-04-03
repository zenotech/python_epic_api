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
from epic_api.models.inline_response2001 import InlineResponse2001  # noqa: E501
from epic_api.rest import ApiException

class TestInlineResponse2001(unittest.TestCase):
    """InlineResponse2001 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2001
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = epic_api.models.inline_response2001.InlineResponse2001()  # noqa: E501
        if include_optional :
            return InlineResponse2001(
                count = 56, 
                next = '0', 
                previous = '0', 
                results = [
                    epic_api.models.viz_node_app.VizNodeApp(
                        name = '0', 
                        description = '0', 
                        versions = [
                            epic_api.models.viz_node_application_version.VizNodeApplicationVersion(
                                id = 56, 
                                application_version = '0', 
                                connection_types = [
                                    epic_api.models.viz_node_connection_type.VizNodeConnectionType(
                                        id = 56, 
                                        name = '0', 
                                        description = '0', )
                                    ], )
                            ], 
                        image = '0', )
                    ]
            )
        else :
            return InlineResponse2001(
                count = 56,
                results = [
                    epic_api.models.viz_node_app.VizNodeApp(
                        name = '0', 
                        description = '0', 
                        versions = [
                            epic_api.models.viz_node_application_version.VizNodeApplicationVersion(
                                id = 56, 
                                application_version = '0', 
                                connection_types = [
                                    epic_api.models.viz_node_connection_type.VizNodeConnectionType(
                                        id = 56, 
                                        name = '0', 
                                        description = '0', )
                                    ], )
                            ], 
                        image = '0', )
                    ],
        )

    def testInlineResponse2001(self):
        """Test InlineResponse2001"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
