#!/usr/bin/python3
"""
BaseModel class defining common attributes and methods
"""
from datetime import datetime
#from models import storage
import uuid


class BaseModel:
    """
    BaseModel for the AirBnB console

    """

    def _init_(self, *args, **kwargs):
        """
        constructor indicators
        """

        from models import storage
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            for a, b in kwargs.items():
                if "_class_" not in a:
                    setattr(self, a, b)

    def _str_(self):
        """String repr of the Base Model Class"""
        return f"[{self._class.name}] ({self.id}) {self.dict_}"

    def to_dict(self):
        """
            Return a dictionary with instance attributes and metadata.
        """
        bModelDict = dict(self._dict_)
        bModelDict['_class'] = type(self).name_
        bModelDict['created_at'] = self.created_at.isoformat()
        bModelDict['updated_at'] = self.updated_at.isoformat()
        return bModelDict

    def save(self):
        """
        Update 'updated_at' and save the instance.

        """
        from models import storage

        self.updated_at = datetime.now()
        storage.save()
