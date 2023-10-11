#!/usr/bin/python3
"""
import modules
"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """
    parent class instance
    """
    def __init__(self, *args, **kwargs):
        """
        instantation
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.fromisoformat(value)
                        setattr(self, key, value)
                        if 'created_at' not in kwargs:
                            self.created_at = datetime.now()
                        if 'updated_at' not in kwargs:
                            self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storge.new(self)

    def save(self):
        """
        update public instance attribute updated at
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        return dictionary containing all keys/values of __dict__
        """
        class_name = self.__class__.__name__
        return {
                "__class__": class_name,
                "id": self.id,
                "created_at": self.created_at.isoformat(),
                "updated_at": self.updated_at.isoformat()
                }

    def __str__(self):
        """
        print function for string instances
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
