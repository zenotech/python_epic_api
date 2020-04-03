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

import epic_api
from epic_api.api.catalog_api import CatalogApi  # noqa: E501
from epic_api.rest import ApiException


class TestCatalogApi(unittest.TestCase):
    """CatalogApi unit test stubs"""

    def setUp(self):
        self.api = epic_api.api.catalog_api.CatalogApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_catalog_applications_list(self):
        """Test case for catalog_applications_list

        """
        pass

    def test_catalog_applications_read(self):
        """Test case for catalog_applications_read

        """
        pass

    def test_catalog_viz_list(self):
        """Test case for catalog_viz_list

        """
        pass

    def test_catalog_viz_read(self):
        """Test case for catalog_viz_read

        """
        pass

    def test_catalog_viznodetype_read(self):
        """Test case for catalog_viznodetype_read

        """
        pass


if __name__ == '__main__':
    unittest.main()
