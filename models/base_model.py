#!/usr/bin/python3
"Modeule defining base class for all models"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """Base class on which all models are based"""

    def __init__(self, *args, **kwargs):
        """Initializes a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        else:
            attribute_mapping = {
                    'created_at': 'created_at',
                    'id': 'id',
                    'updated_at': 'updated_at'
            }

            for key, value in kwargs.items():
                if key in attribute_mapping:
                    attribute_name = attribute_mapping[key]
                    if key in ['created_at', 'updated_at']:
                        value = datetime.fromisoformat(value)
                    elif key == 'id':
                        value == str(value)
                    setattr(self, attribute_name, value)

    def __str__(self):
        """Returns the class represented as a string"""
        class_name = type(self).__name__

        return"[{}]({}) {}".format(class_name, self.id, self.__dict__)
