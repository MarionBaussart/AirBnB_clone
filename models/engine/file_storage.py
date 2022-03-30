#!/usr/bin/python3
import json

"""
Module containing class FileStorage
"""

class FileStorage:
    """
    Class FileStorage: serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Public instance method : returns the dictionary __objects
        Args:
            self: first argument to instance methods
        returns: dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Public instance method : sets in __objects the obj with key <obj class name>.id
        Args:
            self: first argument to instance methods
        returns: no return
        """
        key = "<{}>.{}".format(obj.__class__.__name__, obj.id)
        setattr(self, key, obj)

    def save(self):
        """
        Public instance method : serializes __objects to the JSON file (path: __file_path)
        Args:
            self: first argument to instance methods
        returns: JSON representation of an object (string)
        """
        dict_json = {}
        for key, value in self.__objects.items():
            dict_json[key] = value.to_dict()
        with open(self.__file_path, mode="w") as file:
            json.dump(dict_json, file)

    def reload(self):
        """
        Public instance method : deserializes the JSON file to __objects
        Args:
            self: first argument to instance methods
        returns: an object (Python data structure) represented by a JSON string
        """
        with open(FileStorage.__file_path, mode="r") as file:
            self.__objects = json.load(file)


