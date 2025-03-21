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
from typing_extensions import Annotated
from epiccore.models.data_spec import DataSpec
from epiccore.models.job_configuration import JobConfiguration
from epiccore.models.job_data_binding import JobDataBinding
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class JobArraySpec(BaseModel):
    """
    JobArraySpec
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = Field(default='Job Array', description="Name of job array - only required for more than one job")
    config: JobConfiguration
    jobs: List[JobDataBinding] = Field(description="List of job specs to launch")
    common_data: Optional[DataSpec] = None
    __properties: ClassVar[List[str]] = ["name", "config", "jobs", "common_data"]

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
        """Create an instance of JobArraySpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in jobs (list)
        _items = []
        if self.jobs:
            for _item in self.jobs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['jobs'] = _items
        # override the default output from pydantic by calling `to_dict()` of common_data
        if self.common_data:
            _dict['common_data'] = self.common_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of JobArraySpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name") if obj.get("name") is not None else 'Job Array',
            "config": JobConfiguration.from_dict(obj.get("config")) if obj.get("config") is not None else None,
            "jobs": [JobDataBinding.from_dict(_item) for _item in obj.get("jobs")] if obj.get("jobs") is not None else None,
            "common_data": DataSpec.from_dict(obj.get("common_data")) if obj.get("common_data") is not None else None
        })
        return _obj


