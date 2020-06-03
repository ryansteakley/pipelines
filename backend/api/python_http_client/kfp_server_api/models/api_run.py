# coding: utf-8

"""
    Kubeflow Pipelines API

    This file contains REST API specification for Kubeflow Pipelines. The file is autogenerated from the swagger definition.  # noqa: E501

    The version of the OpenAPI document: 1.0.0-dev.1
    Contact: kubeflow-pipelines@google.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kfp_server_api.configuration import Configuration


class ApiRun(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'name': 'str',
        'storage_state': 'RunStorageState',
        'description': 'str',
        'pipeline_spec': 'ApiPipelineSpec',
        'resource_references': 'list[ApiResourceReference]',
        'service_account': 'str',
        'created_at': 'datetime',
        'scheduled_at': 'datetime',
        'finished_at': 'datetime',
        'status': 'str',
        'error': 'str',
        'metrics': 'list[ApiRunMetric]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'storage_state': 'storage_state',
        'description': 'description',
        'pipeline_spec': 'pipeline_spec',
        'resource_references': 'resource_references',
        'service_account': 'service_account',
        'created_at': 'created_at',
        'scheduled_at': 'scheduled_at',
        'finished_at': 'finished_at',
        'status': 'status',
        'error': 'error',
        'metrics': 'metrics'
    }

    def __init__(self, id=None, name=None, storage_state=None, description=None, pipeline_spec=None, resource_references=None, service_account=None, created_at=None, scheduled_at=None, finished_at=None, status=None, error=None, metrics=None, local_vars_configuration=None):  # noqa: E501
        """ApiRun - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._storage_state = None
        self._description = None
        self._pipeline_spec = None
        self._resource_references = None
        self._service_account = None
        self._created_at = None
        self._scheduled_at = None
        self._finished_at = None
        self._status = None
        self._error = None
        self._metrics = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if storage_state is not None:
            self.storage_state = storage_state
        if description is not None:
            self.description = description
        if pipeline_spec is not None:
            self.pipeline_spec = pipeline_spec
        if resource_references is not None:
            self.resource_references = resource_references
        if service_account is not None:
            self.service_account = service_account
        if created_at is not None:
            self.created_at = created_at
        if scheduled_at is not None:
            self.scheduled_at = scheduled_at
        if finished_at is not None:
            self.finished_at = finished_at
        if status is not None:
            self.status = status
        if error is not None:
            self.error = error
        if metrics is not None:
            self.metrics = metrics

    @property
    def id(self):
        """Gets the id of this ApiRun.  # noqa: E501

        Output. Unique run ID. Generated by API server.  # noqa: E501

        :return: The id of this ApiRun.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiRun.

        Output. Unique run ID. Generated by API server.  # noqa: E501

        :param id: The id of this ApiRun.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApiRun.  # noqa: E501

        Required input field. Name provided by user, or auto generated if run is created by scheduled job. Not unique.  # noqa: E501

        :return: The name of this ApiRun.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiRun.

        Required input field. Name provided by user, or auto generated if run is created by scheduled job. Not unique.  # noqa: E501

        :param name: The name of this ApiRun.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def storage_state(self):
        """Gets the storage_state of this ApiRun.  # noqa: E501


        :return: The storage_state of this ApiRun.  # noqa: E501
        :rtype: RunStorageState
        """
        return self._storage_state

    @storage_state.setter
    def storage_state(self, storage_state):
        """Sets the storage_state of this ApiRun.


        :param storage_state: The storage_state of this ApiRun.  # noqa: E501
        :type: RunStorageState
        """

        self._storage_state = storage_state

    @property
    def description(self):
        """Gets the description of this ApiRun.  # noqa: E501


        :return: The description of this ApiRun.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiRun.


        :param description: The description of this ApiRun.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def pipeline_spec(self):
        """Gets the pipeline_spec of this ApiRun.  # noqa: E501


        :return: The pipeline_spec of this ApiRun.  # noqa: E501
        :rtype: ApiPipelineSpec
        """
        return self._pipeline_spec

    @pipeline_spec.setter
    def pipeline_spec(self, pipeline_spec):
        """Sets the pipeline_spec of this ApiRun.


        :param pipeline_spec: The pipeline_spec of this ApiRun.  # noqa: E501
        :type: ApiPipelineSpec
        """

        self._pipeline_spec = pipeline_spec

    @property
    def resource_references(self):
        """Gets the resource_references of this ApiRun.  # noqa: E501

        Optional input field. Specify which resource this run belongs to. When creating a run from a particular pipeline version, the pipeline version can be specified here.  # noqa: E501

        :return: The resource_references of this ApiRun.  # noqa: E501
        :rtype: list[ApiResourceReference]
        """
        return self._resource_references

    @resource_references.setter
    def resource_references(self, resource_references):
        """Sets the resource_references of this ApiRun.

        Optional input field. Specify which resource this run belongs to. When creating a run from a particular pipeline version, the pipeline version can be specified here.  # noqa: E501

        :param resource_references: The resource_references of this ApiRun.  # noqa: E501
        :type: list[ApiResourceReference]
        """

        self._resource_references = resource_references

    @property
    def service_account(self):
        """Gets the service_account of this ApiRun.  # noqa: E501

        Optional input field. Specify which Kubernetes service account this run uses.  # noqa: E501

        :return: The service_account of this ApiRun.  # noqa: E501
        :rtype: str
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        """Sets the service_account of this ApiRun.

        Optional input field. Specify which Kubernetes service account this run uses.  # noqa: E501

        :param service_account: The service_account of this ApiRun.  # noqa: E501
        :type: str
        """

        self._service_account = service_account

    @property
    def created_at(self):
        """Gets the created_at of this ApiRun.  # noqa: E501

        Output. The time that the run created.  # noqa: E501

        :return: The created_at of this ApiRun.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiRun.

        Output. The time that the run created.  # noqa: E501

        :param created_at: The created_at of this ApiRun.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def scheduled_at(self):
        """Gets the scheduled_at of this ApiRun.  # noqa: E501

        Output. When this run is scheduled to run. This could be different from created_at. For example, if a run is from a backfilling job that was supposed to run 2 month ago, the scheduled_at is 2 month ago, v.s. created_at is the current time.  # noqa: E501

        :return: The scheduled_at of this ApiRun.  # noqa: E501
        :rtype: datetime
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """Sets the scheduled_at of this ApiRun.

        Output. When this run is scheduled to run. This could be different from created_at. For example, if a run is from a backfilling job that was supposed to run 2 month ago, the scheduled_at is 2 month ago, v.s. created_at is the current time.  # noqa: E501

        :param scheduled_at: The scheduled_at of this ApiRun.  # noqa: E501
        :type: datetime
        """

        self._scheduled_at = scheduled_at

    @property
    def finished_at(self):
        """Gets the finished_at of this ApiRun.  # noqa: E501

        Output. The time this run is finished.  # noqa: E501

        :return: The finished_at of this ApiRun.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this ApiRun.

        Output. The time this run is finished.  # noqa: E501

        :param finished_at: The finished_at of this ApiRun.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def status(self):
        """Gets the status of this ApiRun.  # noqa: E501


        :return: The status of this ApiRun.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiRun.


        :param status: The status of this ApiRun.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def error(self):
        """Gets the error of this ApiRun.  # noqa: E501

        In case any error happens retrieving a run field, only run ID and the error message is returned. Client has the flexibility of choosing how to handle error. This is especially useful during listing call.  # noqa: E501

        :return: The error of this ApiRun.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ApiRun.

        In case any error happens retrieving a run field, only run ID and the error message is returned. Client has the flexibility of choosing how to handle error. This is especially useful during listing call.  # noqa: E501

        :param error: The error of this ApiRun.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def metrics(self):
        """Gets the metrics of this ApiRun.  # noqa: E501

        Output. The metrics of the run. The metrics are reported by ReportMetrics API.  # noqa: E501

        :return: The metrics of this ApiRun.  # noqa: E501
        :rtype: list[ApiRunMetric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ApiRun.

        Output. The metrics of the run. The metrics are reported by ReportMetrics API.  # noqa: E501

        :param metrics: The metrics of this ApiRun.  # noqa: E501
        :type: list[ApiRunMetric]
        """

        self._metrics = metrics

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiRun):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiRun):
            return True

        return self.to_dict() != other.to_dict()
