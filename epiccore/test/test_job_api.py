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

import epiccore
from epiccore.api.job_api import JobApi  # noqa: E501
from epiccore.rest import ApiException


class TestJobApi(unittest.TestCase):
    """JobApi unit test stubs"""

    def setUp(self):
        self.api = epiccore.api.job_api.JobApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_job_auth_read(self):
        """Test case for job_auth_read

        """
        pass

    def test_job_auth_update(self):
        """Test case for job_auth_update

        """
        pass

    def test_job_cancel(self):
        """Test case for job_cancel

        """
        pass

    def test_job_create(self):
        """Test case for job_create

        """
        pass

    def test_job_list(self):
        """Test case for job_list

        """
        pass

    def test_job_partial_update(self):
        """Test case for job_partial_update

        """
        pass

    def test_job_quote(self):
        """Test case for job_quote

        """
        pass

    def test_job_read(self):
        """Test case for job_read

        """
        pass


if __name__ == '__main__':
    unittest.main()
