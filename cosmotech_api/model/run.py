"""
    Cosmo Tech Platform API

    Cosmo Tech Platform API  # noqa: E501

    The version of the OpenAPI document: 3.1.2-dev
    Contact: platform@cosmotech.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cosmotech_api.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from cosmotech_api.exceptions import ApiAttributeError


def lazy_import():
    from cosmotech_api.model.run_container import RunContainer
    from cosmotech_api.model.run_state import RunState
    from cosmotech_api.model.run_template_parameter_value import RunTemplateParameterValue
    globals()['RunContainer'] = RunContainer
    globals()['RunState'] = RunState
    globals()['RunTemplateParameterValue'] = RunTemplateParameterValue


class Run(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'state': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'organization_id': (str,),  # noqa: E501
            'workflow_id': (str,),  # noqa: E501
            'csm_simulation_run': (str,),  # noqa: E501
            'generate_name': (str,),  # noqa: E501
            'workflow_name': (str,),  # noqa: E501
            'owner_id': (str,),  # noqa: E501
            'workspace_id': (str,),  # noqa: E501
            'workspace_key': (str,),  # noqa: E501
            'runner_id': (str,),  # noqa: E501
            'solution_id': (str,),  # noqa: E501
            'run_template_id': (str,),  # noqa: E501
            'compute_size': (str,),  # noqa: E501
            'created_at': (str,),  # noqa: E501
            'dataset_list': ([str],),  # noqa: E501
            'parameters_values': ([RunTemplateParameterValue],),  # noqa: E501
            'node_label': (str,),  # noqa: E501
            'containers': ([RunContainer],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'state': 'state',  # noqa: E501
        'organization_id': 'organizationId',  # noqa: E501
        'workflow_id': 'workflowId',  # noqa: E501
        'csm_simulation_run': 'csmSimulationRun',  # noqa: E501
        'generate_name': 'generateName',  # noqa: E501
        'workflow_name': 'workflowName',  # noqa: E501
        'owner_id': 'ownerId',  # noqa: E501
        'workspace_id': 'workspaceId',  # noqa: E501
        'workspace_key': 'workspaceKey',  # noqa: E501
        'runner_id': 'runnerId',  # noqa: E501
        'solution_id': 'solutionId',  # noqa: E501
        'run_template_id': 'runTemplateId',  # noqa: E501
        'compute_size': 'computeSize',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'dataset_list': 'datasetList',  # noqa: E501
        'parameters_values': 'parametersValues',  # noqa: E501
        'node_label': 'nodeLabel',  # noqa: E501
        'containers': 'containers',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'csm_simulation_run',  # noqa: E501
        'owner_id',  # noqa: E501
        'workspace_id',  # noqa: E501
        'workspace_key',  # noqa: E501
        'runner_id',  # noqa: E501
        'solution_id',  # noqa: E501
        'run_template_id',  # noqa: E501
        'compute_size',  # noqa: E501
        'created_at',  # noqa: E501
        'dataset_list',  # noqa: E501
        'parameters_values',  # noqa: E501
        'node_label',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Run - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): the Run. [optional]  # noqa: E501
            state (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            organization_id (str): the Organization id. [optional]  # noqa: E501
            workflow_id (str): the Cosmo Tech compute cluster Argo Workflow Id to search. [optional]  # noqa: E501
            csm_simulation_run (str): the Cosmo Tech Simulation Run Id. [optional]  # noqa: E501
            generate_name (str): the base name for workflow name generation. [optional]  # noqa: E501
            workflow_name (str): the Cosmo Tech compute cluster Argo Workflow Name. [optional]  # noqa: E501
            owner_id (str): the user id which own this run. [optional]  # noqa: E501
            workspace_id (str): the Workspace Id. [optional]  # noqa: E501
            workspace_key (str): technical key for resource name convention and version grouping. Must be unique. [optional]  # noqa: E501
            runner_id (str): the Runner Id. [optional]  # noqa: E501
            solution_id (str): the Solution Id. [optional]  # noqa: E501
            run_template_id (str): the Solution Run Template id. [optional]  # noqa: E501
            compute_size (str): the compute size needed for this Analysis. Standard sizes are basic and highcpu. Default is basic. [optional]  # noqa: E501
            created_at (str): the Run creation date. [optional]  # noqa: E501
            dataset_list ([str]): the list of Dataset Id associated to this Run. [optional]  # noqa: E501
            parameters_values ([RunTemplateParameterValue]): the list of Run Template parameters values. [optional]  # noqa: E501
            node_label (str): the node label request. [optional]  # noqa: E501
            containers ([RunContainer]): the containers list. This information is not returned by the API.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Run - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): the Run. [optional]  # noqa: E501
            state (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            organization_id (str): the Organization id. [optional]  # noqa: E501
            workflow_id (str): the Cosmo Tech compute cluster Argo Workflow Id to search. [optional]  # noqa: E501
            csm_simulation_run (str): the Cosmo Tech Simulation Run Id. [optional]  # noqa: E501
            generate_name (str): the base name for workflow name generation. [optional]  # noqa: E501
            workflow_name (str): the Cosmo Tech compute cluster Argo Workflow Name. [optional]  # noqa: E501
            owner_id (str): the user id which own this run. [optional]  # noqa: E501
            workspace_id (str): the Workspace Id. [optional]  # noqa: E501
            workspace_key (str): technical key for resource name convention and version grouping. Must be unique. [optional]  # noqa: E501
            runner_id (str): the Runner Id. [optional]  # noqa: E501
            solution_id (str): the Solution Id. [optional]  # noqa: E501
            run_template_id (str): the Solution Run Template id. [optional]  # noqa: E501
            compute_size (str): the compute size needed for this Analysis. Standard sizes are basic and highcpu. Default is basic. [optional]  # noqa: E501
            created_at (str): the Run creation date. [optional]  # noqa: E501
            dataset_list ([str]): the list of Dataset Id associated to this Run. [optional]  # noqa: E501
            parameters_values ([RunTemplateParameterValue]): the list of Run Template parameters values. [optional]  # noqa: E501
            node_label (str): the node label request. [optional]  # noqa: E501
            containers ([RunContainer]): the containers list. This information is not returned by the API.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")