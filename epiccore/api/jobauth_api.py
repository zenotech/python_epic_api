# coding: utf-8

"""
    EPIC API

    REST API for interacting with EPIC (https://epic.zenotech.com) services. <br />                             Please note this API is in BETA and does not yet contain                             all EPIC functionality.  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@zenotech.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from epiccore.api_client import ApiClient
from epiccore.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class JobauthApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def jobauth_list(self, **kwargs):  # noqa: E501
        """jobauth_list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.jobauth_list(async_req=True)
        >>> result = thread.get()

        :param limit: Number of results to return per page.
        :type limit: int
        :param offset: The initial index from which to return the results.
        :type offset: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InlineResponse2007
        """
        kwargs['_return_http_data_only'] = True
        return self.jobauth_list_with_http_info(**kwargs)  # noqa: E501

    def jobauth_list_with_http_info(self, **kwargs):  # noqa: E501
        """jobauth_list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.jobauth_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param limit: Number of results to return per page.
        :type limit: int
        :param offset: The initial index from which to return the results.
        :type offset: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(InlineResponse2007, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'limit',
            'offset'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method jobauth_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/jobauth/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2007',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def jobauth_read(self, job, **kwargs):  # noqa: E501
        """jobauth_read  # noqa: E501

        Get the authorisation status for job with ID {id}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.jobauth_read(job, async_req=True)
        >>> result = thread.get()

        :param job: A unique value identifying this job authorisation. (required)
        :type job: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: JobAuthStatus
        """
        kwargs['_return_http_data_only'] = True
        return self.jobauth_read_with_http_info(job, **kwargs)  # noqa: E501

    def jobauth_read_with_http_info(self, job, **kwargs):  # noqa: E501
        """jobauth_read  # noqa: E501

        Get the authorisation status for job with ID {id}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.jobauth_read_with_http_info(job, async_req=True)
        >>> result = thread.get()

        :param job: A unique value identifying this job authorisation. (required)
        :type job: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(JobAuthStatus, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'job'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method jobauth_read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'job' is set
        if self.api_client.client_side_validation and ('job' not in local_var_params or  # noqa: E501
                                                        local_var_params['job'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `job` when calling `jobauth_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job' in local_var_params:
            path_params['job'] = local_var_params['job']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/jobauth/{job}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JobAuthStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def jobauth_update(self, job, data, **kwargs):  # noqa: E501
        """jobauth_update  # noqa: E501

        Update the authorisation status for job  with ID {id}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.jobauth_update(job, data, async_req=True)
        >>> result = thread.get()

        :param job: A unique value identifying this job authorisation. (required)
        :type job: str
        :param data: (required)
        :type data: JobAuthStatus
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: JobAuthStatus
        """
        kwargs['_return_http_data_only'] = True
        return self.jobauth_update_with_http_info(job, data, **kwargs)  # noqa: E501

    def jobauth_update_with_http_info(self, job, data, **kwargs):  # noqa: E501
        """jobauth_update  # noqa: E501

        Update the authorisation status for job  with ID {id}  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.jobauth_update_with_http_info(job, data, async_req=True)
        >>> result = thread.get()

        :param job: A unique value identifying this job authorisation. (required)
        :type job: str
        :param data: (required)
        :type data: JobAuthStatus
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(JobAuthStatus, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'job',
            'data'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method jobauth_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'job' is set
        if self.api_client.client_side_validation and ('job' not in local_var_params or  # noqa: E501
                                                        local_var_params['job'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `job` when calling `jobauth_update`")  # noqa: E501
        # verify the required parameter 'data' is set
        if self.api_client.client_side_validation and ('data' not in local_var_params or  # noqa: E501
                                                        local_var_params['data'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `data` when calling `jobauth_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job' in local_var_params:
            path_params['job'] = local_var_params['job']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in local_var_params:
            body_params = local_var_params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/jobauth/{job}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JobAuthStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
