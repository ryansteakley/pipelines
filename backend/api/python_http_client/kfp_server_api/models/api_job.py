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


class ApiJob(object):
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
        'description': 'str',
        'pipeline_spec': 'ApiPipelineSpec',
        'resource_references': 'list[ApiResourceReference]',
        'service_account': 'str',
        'max_concurrency': 'str',
        'trigger': 'ApiTrigger',
        'mode': 'JobMode',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'status': 'str',
        'error': 'str',
        'enabled': 'bool',
        'no_catchup': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'pipeline_spec': 'pipeline_spec',
        'resource_references': 'resource_references',
        'service_account': 'service_account',
        'max_concurrency': 'max_concurrency',
        'trigger': 'trigger',
        'mode': 'mode',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'status': 'status',
        'error': 'error',
        'enabled': 'enabled',
        'no_catchup': 'no_catchup'
    }

    def __init__(self, id=None, name=None, description=None, pipeline_spec=None, resource_references=None, service_account=None, max_concurrency=None, trigger=None, mode=None, created_at=None, updated_at=None, status=None, error=None, enabled=None, no_catchup=None, local_vars_configuration=None):  # noqa: E501
        """ApiJob - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._pipeline_spec = None
        self._resource_references = None
        self._service_account = None
        self._max_concurrency = None
        self._trigger = None
        self._mode = None
        self._created_at = None
        self._updated_at = None
        self._status = None
        self._error = None
        self._enabled = None
        self._no_catchup = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if pipeline_spec is not None:
            self.pipeline_spec = pipeline_spec
        if resource_references is not None:
            self.resource_references = resource_references
        if service_account is not None:
            self.service_account = service_account
        if max_concurrency is not None:
            self.max_concurrency = max_concurrency
        if trigger is not None:
            self.trigger = trigger
        if mode is not None:
            self.mode = mode
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if status is not None:
            self.status = status
        if error is not None:
            self.error = error
        if enabled is not None:
            self.enabled = enabled
        if no_catchup is not None:
            self.no_catchup = no_catchup

    @property
    def id(self):
        """Gets the id of this ApiJob.  # noqa: E501

        Output. Unique run ID. Generated by API server.  # noqa: E501

        :return: The id of this ApiJob.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiJob.

        Output. Unique run ID. Generated by API server.  # noqa: E501

        :param id: The id of this ApiJob.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApiJob.  # noqa: E501

        Required input field. Job name provided by user. Not unique.  # noqa: E501

        :return: The name of this ApiJob.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiJob.

        Required input field. Job name provided by user. Not unique.  # noqa: E501

        :param name: The name of this ApiJob.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ApiJob.  # noqa: E501


        :return: The description of this ApiJob.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiJob.


        :param description: The description of this ApiJob.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def pipeline_spec(self):
        """Gets the pipeline_spec of this ApiJob.  # noqa: E501


        :return: The pipeline_spec of this ApiJob.  # noqa: E501
        :rtype: ApiPipelineSpec
        """
        return self._pipeline_spec

    @pipeline_spec.setter
    def pipeline_spec(self, pipeline_spec):
        """Sets the pipeline_spec of this ApiJob.


        :param pipeline_spec: The pipeline_spec of this ApiJob.  # noqa: E501
        :type: ApiPipelineSpec
        """

        self._pipeline_spec = pipeline_spec

    @property
    def resource_references(self):
        """Gets the resource_references of this ApiJob.  # noqa: E501

        Optional input field. Specify which resource this job belongs to.  # noqa: E501

        :return: The resource_references of this ApiJob.  # noqa: E501
        :rtype: list[ApiResourceReference]
        """
        return self._resource_references

    @resource_references.setter
    def resource_references(self, resource_references):
        """Sets the resource_references of this ApiJob.

        Optional input field. Specify which resource this job belongs to.  # noqa: E501

        :param resource_references: The resource_references of this ApiJob.  # noqa: E501
        :type: list[ApiResourceReference]
        """

        self._resource_references = resource_references

    @property
    def service_account(self):
        """Gets the service_account of this ApiJob.  # noqa: E501

        Optional input field. Specify which Kubernetes service account this job uses.  # noqa: E501

        :return: The service_account of this ApiJob.  # noqa: E501
        :rtype: str
        """
        return self._service_account

    @service_account.setter
    def service_account(self, service_account):
        """Sets the service_account of this ApiJob.

        Optional input field. Specify which Kubernetes service account this job uses.  # noqa: E501

        :param service_account: The service_account of this ApiJob.  # noqa: E501
        :type: str
        """

        self._service_account = service_account

    @property
    def max_concurrency(self):
        """Gets the max_concurrency of this ApiJob.  # noqa: E501


        :return: The max_concurrency of this ApiJob.  # noqa: E501
        :rtype: str
        """
        return self._max_concurrency

    @max_concurrency.setter
    def max_concurrency(self, max_concurrency):
        """Sets the max_concurrency of this ApiJob.


        :param max_concurrency: The max_concurrency of this ApiJob.  # noqa: E501
        :type: str
        """

        self._max_concurrency = max_concurrency

    @property
    def trigger(self):
        """Gets the trigger of this ApiJob.  # noqa: E501


        :return: The trigger of this ApiJob.  # noqa: E501
        :rtype: ApiTrigger
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this ApiJob.


        :param trigger: The trigger of this ApiJob.  # noqa: E501
        :type: ApiTrigger
        """

        self._trigger = trigger

    @property
    def mode(self):
        """Gets the mode of this ApiJob.  # noqa: E501


        :return: The mode of this ApiJob.  # noqa: E501
        :rtype: JobMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this ApiJob.


        :param mode: The mode of this ApiJob.  # noqa: E501
        :type: JobMode
        """

        self._mode = mode

    @property
    def created_at(self):
        """Gets the created_at of this ApiJob.  # noqa: E501

        Output. The time this job is created.  # noqa: E501

        :return: The created_at of this ApiJob.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiJob.

        Output. The time this job is created.  # noqa: E501

        :param created_at: The created_at of this ApiJob.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ApiJob.  # noqa: E501

        Output. The last time this job is updated.  # noqa: E501

        :return: The updated_at of this ApiJob.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ApiJob.

        Output. The last time this job is updated.  # noqa: E501

        :param updated_at: The updated_at of this ApiJob.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def status(self):
        """Gets the status of this ApiJob.  # noqa: E501


        :return: The status of this ApiJob.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiJob.


        :param status: The status of this ApiJob.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def error(self):
        """Gets the error of this ApiJob.  # noqa: E501

        In case any error happens retrieving a job field, only job ID and the error message is returned. Client has the flexibility of choosing how to handle error. This is especially useful during listing call.  # noqa: E501

        :return: The error of this ApiJob.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ApiJob.

        In case any error happens retrieving a job field, only job ID and the error message is returned. Client has the flexibility of choosing how to handle error. This is especially useful during listing call.  # noqa: E501

        :param error: The error of this ApiJob.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def enabled(self):
        """Gets the enabled of this ApiJob.  # noqa: E501

        Input. Whether the job is enabled or not.  # noqa: E501

        :return: The enabled of this ApiJob.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ApiJob.

        Input. Whether the job is enabled or not.  # noqa: E501

        :param enabled: The enabled of this ApiJob.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def no_catchup(self):
        """Gets the no_catchup of this ApiJob.  # noqa: E501

        Optional input field. Whether the job should catch up if behind schedule. If true, the job will only schedule the latest interval if behind schedule. If false, the job will catch up on each past interval.  # noqa: E501

        :return: The no_catchup of this ApiJob.  # noqa: E501
        :rtype: bool
        """
        return self._no_catchup

    @no_catchup.setter
    def no_catchup(self, no_catchup):
        """Sets the no_catchup of this ApiJob.

        Optional input field. Whether the job should catch up if behind schedule. If true, the job will only schedule the latest interval if behind schedule. If false, the job will catch up on each past interval.  # noqa: E501

        :param no_catchup: The no_catchup of this ApiJob.  # noqa: E501
        :type: bool
        """

        self._no_catchup = no_catchup

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
        if not isinstance(other, ApiJob):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiJob):
            return True

        return self.to_dict() != other.to_dict()
