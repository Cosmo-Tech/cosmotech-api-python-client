"""
    Cosmo Tech Plaform API

    Cosmo Tech Platform API  # noqa: E501

    The version of the OpenAPI document: 0.0.4-SNAPSHOT
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
)

def lazy_import():
    from cosmotech_api.model.scenario_last_run import ScenarioLastRun
    from cosmotech_api.model.scenario_run_template_parameter_value import ScenarioRunTemplateParameterValue
    from cosmotech_api.model.scenario_user import ScenarioUser
    globals()['ScenarioLastRun'] = ScenarioLastRun
    globals()['ScenarioRunTemplateParameterValue'] = ScenarioRunTemplateParameterValue
    globals()['ScenarioUser'] = ScenarioUser


class Scenario(ModelNormal):
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
        ('state',): {
            'CREATED': "Created",
            'RUNNING': "Running",
            'SUCCESSFUL': "Successful",
            'FAILED': "Failed",
        },
    }

    validations = {
    }

    additional_properties_type = None

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
            'name': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'tags': ([str],),  # noqa: E501
            'parent_id': (str,),  # noqa: E501
            'owner_id': (str,),  # noqa: E501
            'solution_id': (str,),  # noqa: E501
            'run_template_id': (str,),  # noqa: E501
            'workspace_id': (str,),  # noqa: E501
            'users': ([ScenarioUser],),  # noqa: E501
            'state': (str,),  # noqa: E501
            'creation_date': (datetime,),  # noqa: E501
            'last_update': (datetime,),  # noqa: E501
            'owner_name': (str,),  # noqa: E501
            'solution_name': (str,),  # noqa: E501
            'run_template_name': (str,),  # noqa: E501
            'dataset_list': ([str],),  # noqa: E501
            'parameters_values': ([ScenarioRunTemplateParameterValue],),  # noqa: E501
            'last_run': (ScenarioLastRun,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'description': 'description',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'parent_id': 'parentId',  # noqa: E501
        'owner_id': 'ownerId',  # noqa: E501
        'solution_id': 'solutionId',  # noqa: E501
        'run_template_id': 'runTemplateId',  # noqa: E501
        'workspace_id': 'workspaceId',  # noqa: E501
        'users': 'users',  # noqa: E501
        'state': 'state',  # noqa: E501
        'creation_date': 'creationDate',  # noqa: E501
        'last_update': 'lastUpdate',  # noqa: E501
        'owner_name': 'ownerName',  # noqa: E501
        'solution_name': 'solutionName',  # noqa: E501
        'run_template_name': 'runTemplateName',  # noqa: E501
        'dataset_list': 'datasetList',  # noqa: E501
        'parameters_values': 'parametersValues',  # noqa: E501
        'last_run': 'lastRun',  # noqa: E501
    }

    _composed_schemas = {}

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
        """Scenario - a model defined in OpenAPI

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
            id (str): the Scenario unique identifier. [optional]  # noqa: E501
            name (str): the Scenario name. [optional]  # noqa: E501
            description (str): the Scenario description. [optional]  # noqa: E501
            tags ([str]): the list of tags. [optional]  # noqa: E501
            parent_id (str): the Scenario parent id. [optional]  # noqa: E501
            owner_id (str): the user id which own this Scenario. [optional]  # noqa: E501
            solution_id (str): the Solution Id associated with this Scenario. [optional]  # noqa: E501
            run_template_id (str): the Solution Run Template Id associated with this Scenario. [optional]  # noqa: E501
            workspace_id (str): the associated Workspace Id. [optional]  # noqa: E501
            users ([ScenarioUser]): the list of users Id with their role. [optional]  # noqa: E501
            state (str): the Scenario state. [optional]  # noqa: E501
            creation_date (datetime): the Scenario creation date. [optional]  # noqa: E501
            last_update (datetime): the last time a Scenario was updated. [optional]  # noqa: E501
            owner_name (str): the name of the owner. [optional]  # noqa: E501
            solution_name (str): the Solution name. [optional]  # noqa: E501
            run_template_name (str): the Solution Run Template name associated with this Scenario. [optional]  # noqa: E501
            dataset_list ([str]): the list of Dataset Id associated to this Scenario Run Template. [optional]  # noqa: E501
            parameters_values ([ScenarioRunTemplateParameterValue]): the list of Solution Run Template parameters values. [optional]  # noqa: E501
            last_run (ScenarioLastRun): [optional]  # noqa: E501
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