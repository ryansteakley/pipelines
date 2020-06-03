# coding: utf-8

"""
    Kubeflow Pipelines API

    This file contains REST API specification for Kubeflow Pipelines. The file is autogenerated from the swagger definition.  # noqa: E501

    The version of the OpenAPI document: 1.0.0-dev.1
    Contact: kubeflow-pipelines@google.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kfp_server_api
from kfp_server_api.models.api_report_run_metrics_response import ApiReportRunMetricsResponse  # noqa: E501
from kfp_server_api.rest import ApiException

class TestApiReportRunMetricsResponse(unittest.TestCase):
    """ApiReportRunMetricsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiReportRunMetricsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kfp_server_api.models.api_report_run_metrics_response.ApiReportRunMetricsResponse()  # noqa: E501
        if include_optional :
            return ApiReportRunMetricsResponse(
                results = [
                    kfp_server_api.models.report_run_metrics_response_report_run_metric_result.ReportRunMetricsResponseReportRunMetricResult(
                        metric_name = '0', 
                        metric_node_id = '0', 
                        status = 'UNSPECIFIED', 
                        message = '0', )
                    ]
            )
        else :
            return ApiReportRunMetricsResponse(
        )

    def testApiReportRunMetricsResponse(self):
        """Test ApiReportRunMetricsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
