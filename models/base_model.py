#!/usr/bin/python3
"Modeule defining base class for all models"""
from datetime import datetime, date
from uuid import uuid4
import models


class BaseModel:
    """Base class on which all models are based"""

    def __init__(self, *args, **kwargs):
        """Initializes a new model"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            # attribute_mapping = {
            #       'created_at': 'created_at',
            #      'id': 'id',
            #       'updated_at': 'updated_at'
            # }

            for key, value in kwargs.items():
                if key == "__clas_s_":
                    continue
                elif key in ['created_at', 'updated_at']:
                    setattr(self, key,  datetime.fromisoformat(value))
                    # elif key == 'id':
                    # value = str(value)
                else:
                    setattr(self, attribute_name, value)
                # elif key == "__class__":
                    # continue

    def __str__(self):
        """Returns the class represented as a string"""
        class_name = type(self).__name__

        return "[{}]({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """returns class represented as dictionary"""
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary

    def save(self):
        """updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()
