#!/usr/bin/python3
"""
Module containing class FileStorage
"""
import json
import os


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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)

        self.__objects[key] = obj

    def save(self):
        """
        Public instance method : serializes __objects to the JSON file (path: __file_path)
        Args:
            self: first argument to instance methods
        returns: JSON representation of an object (string)
        """
        dict_obj = {}
        dict_obj_copy = self.__objects.copy()
        for key, value in dict_obj_copy.items():
            dict_obj[key] = value.to_dict()

        with open(self.__file_path, mode="w") as file:
            json.dump(dict_obj, file)

    def reload(self):
        """
        Public instance method : deserializes the JSON file to __objects
        Args:
            self: first argument to instance methods
        returns: an object (Python data structure) represented by a JSON string
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode="r") as file:
                self.__objects = json.load(file)
