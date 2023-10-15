#!/usr/bin/python3
<<<<<<< HEAD
'''
This is a base model that defines all common attributes and methods of other classes
'''
=======
"""
BaseModel class defining common attributes and methods
"""
>>>>>>> 29b57553be073c535d074890dd0479434db3d083
from datetime import datetime
import uuid


class BaseModel:
<<<<<<< HEAD
    '''
    Represents the base model class of AirBnB console
    '''

    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
=======
    """
    BaseModel for the AirBnB console

    """

    def __init__(self, *args, **kwargs):
        """
        constructor indicators
        """

>>>>>>> 29b57553be073c535d074890dd0479434db3d083
        from models import storage
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            date_format = '%Y-%m-%dT%H:%M:%S.%f'
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'], date_format)
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], date_format)

            for a, b in kwargs.items():
                if "__class__" not in a:
                    setattr(self, a, b)

    def __str__(self):
        """String repr of the Base Model Class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
<<<<<<< HEAD
        Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        Dict = dict(self.__dict__)
        Dict['__class__'] = type(self).__name__
        Dict['created_at'] = self.created_at.isoformat()
        Dict['updated_at'] = self.updated_at.isoformat()
        return Dict

=======
            Return a dictionary with instance attributes and metadata.
        """
        bModelDict = dict(self.__dict__)
        bModelDict['__class__'] = type(self).__name__
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
>>>>>>> 29b57553be073c535d074890dd0479434db3d083
