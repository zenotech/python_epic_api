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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class JobSummary(BaseModel):
    """
    JobSummary
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The ID for this job")
    name: Optional[StrictStr] = Field(default=None, description="Name of this job")
    app: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=30)]] = Field(default=None, description="Name of the application that this job uses")
    cost: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=30)]] = Field(default=None, description="Maximum cost for running this job")
    submitted_by: Optional[StrictStr] = Field(default=None, description="Name of the user who submitted this job")
    submitted_at: Optional[StrictStr] = Field(default=None, description="Date at which this job was submitted")
    __properties: ClassVar[List[str]] = ["id", "name", "app", "cost", "submitted_by", "submitted_at"]

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
        """Create an instance of JobSummary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
                "name",
                "app",
                "cost",
                "submitted_by",
                "submitted_at",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of JobSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "app": obj.get("app"),
            "cost": obj.get("cost"),
            "submitted_by": obj.get("submitted_by"),
            "submitted_at": obj.get("submitted_at")
        })
        return _obj


