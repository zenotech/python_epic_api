# coding: utf-8

"""
    EPIC API

    REST API for interacting with EPIC (https://epic.zenotech.com) services. <br />                             Please note this API is in BETA and does not yet contain                             all EPIC functionality.

    The version of the OpenAPI document: v2
    Contact: support@zenotech.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from epiccore.models.job_configuration import JobConfiguration
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class JobAppOptions(BaseModel):
    """
    JobAppOptions
    """ # noqa: E501
    app_options: Optional[Dict[str, Any]] = Field(description="Application specific options to update")
    config: JobConfiguration
    __properties: ClassVar[List[str]] = ["app_options", "config"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of JobAppOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        # set to None if app_options (nullable) is None
        # and model_fields_set contains the field
        if self.app_options is None and "app_options" in self.model_fields_set:
            _dict['app_options'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of JobAppOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app_options": obj.get("app_options"),
            "config": JobConfiguration.from_dict(obj.get("config")) if obj.get("config") is not None else None
        })
        return _obj


