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
from epiccore.models.budget import Budget
from epiccore.models.job_auth import JobAuth
from epiccore.models.project import Project
from epiccore.models.team import Team
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Limit(BaseModel):
    """
    List of limits for all teams linked to the current user's billing profile
    """ # noqa: E501
    team: Optional[Team] = None
    budget: Optional[Budget] = None
    project: Optional[Project] = None
    jobauth: Optional[JobAuth] = None
    id: Annotated[int, Field(strict=True, ge=-1)] = Field(description="Team id for this limit. -1 signifies the user's limits")
    __properties: ClassVar[List[str]] = ["team", "budget", "project", "jobauth", "id"]

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
        """Create an instance of Limit from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of team
        if self.team:
            _dict['team'] = self.team.to_dict()
        # override the default output from pydantic by calling `to_dict()` of budget
        if self.budget:
            _dict['budget'] = self.budget.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of jobauth
        if self.jobauth:
            _dict['jobauth'] = self.jobauth.to_dict()
        # set to None if team (nullable) is None
        # and model_fields_set contains the field
        if self.team is None and "team" in self.model_fields_set:
            _dict['team'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Limit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "team": Team.from_dict(obj.get("team")) if obj.get("team") is not None else None,
            "budget": Budget.from_dict(obj.get("budget")) if obj.get("budget") is not None else None,
            "project": Project.from_dict(obj.get("project")) if obj.get("project") is not None else None,
            "jobauth": JobAuth.from_dict(obj.get("jobauth")) if obj.get("jobauth") is not None else None,
            "id": obj.get("id")
        })
        return _obj


