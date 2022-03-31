#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage

"""
Module containing class BaseModel
"""


class BaseModel:
    """
    Class BaseModel: defines all common attributes/methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """ Initialize the attributes
        Args:
            self: first argument to instance methods
            args: list of arguments - no-keyworded arguments
            kwargs: double pointer to a dictionary: key/value
            (keyworded arguments)
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

        for key, value in kwargs.items():
            if key in ['created_at', 'updated_at']:
                value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            if key != '__class__':
                setattr(self, key, value)
        if not kwargs:
            storage.new(self)

    def __str__(self):
        """
        Public instance method
        Args:
            self: first argument to instance methods
        returns: a printable string: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(BaseModel.__name__, self.id, self.__dict__)

    def save(self):
        """
        Public instance method, updates the public instance attribute
        updated_at with the current datetime.
        Args:
            self: first argument to instance methods
        return: no return
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Public instance method
        Args:
            self: first argument to instance methods
        return: dictionary containing all keys/values of __dict__
        of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary
