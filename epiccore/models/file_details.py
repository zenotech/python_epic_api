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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FileDetails(BaseModel):
    """
    FileDetails
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID for this folder")
    meta_data: Optional[Dict[str, Any]] = Field(default=None, description="File meta-data")
    created: Optional[datetime] = Field(default=None, description="Creation time")
    modified: Optional[datetime] = None
    name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="File name")
    obj_key: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="S3 key reference")
    size: Optional[Annotated[int, Field(le=9223372036854775807, strict=True, ge=-9223372036854775808)]] = None
    last_modified: Optional[datetime] = Field(default=None, description="Last modified time")
    folder: Optional[StrictInt] = Field(default=None, description="Folder name")
    __properties: ClassVar[List[str]] = ["id", "meta_data", "created", "modified", "name", "obj_key", "size", "last_modified", "folder"]

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
        """Create an instance of FileDetails from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
                "meta_data",
                "created",
                "modified",
                "name",
                "obj_key",
                "last_modified",
                "folder",
            },
            exclude_none=True,
        )
        # set to None if last_modified (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified is None and "last_modified" in self.model_fields_set:
            _dict['last_modified'] = None

        # set to None if folder (nullable) is None
        # and model_fields_set contains the field
        if self.folder is None and "folder" in self.model_fields_set:
            _dict['folder'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FileDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "meta_data": obj.get("meta_data"),
            "created": obj.get("created"),
            "modified": obj.get("modified"),
            "name": obj.get("name"),
            "obj_key": obj.get("obj_key"),
            "size": obj.get("size"),
            "last_modified": obj.get("last_modified"),
            "folder": obj.get("folder")
        })
        return _obj


