#!/usr/bin/python3
""" base_model """
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
        return FileStorage.__objects

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        temp_dict = {}
        # >>> _objects = {'ob.11': obj1, 'ob.22': obj2,...}
        for obj in FileStorage.__objects:
            temp_dict[obj] = FileStorage.__objects[obj].to_dict()
            # >>> temp_dict = {'ob.11': {'id': 11, 'name': aa,...},
            # {'id': 11, 'name': aa,...},...}
        with open(FileStorage.__file_path, 'w') as db_f:
            json_text = json.dumps(temp_dict)
            db_f.write(json_text)
            # or we can use json.dumps(FileStorage.__objects, db_f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""
        temp_dict = {}
        try:
            with open(FileStorage.__file_path, 'r') as db_f:
                temp_dict = json.load(db_f)
                for dict_val in temp_dict.values():
                    # convert dict_val to object of class __class__
                    # since new(self, obj) method
                    # accepts obj as parrameter
                    FileStorage.new(eval(obj["__class__"])(**dict_val))
                    # delete __class__ key since we dont need it
                    # it will be generated every time we use to_dict()
                    del dict_val["__class__"]

        except Exception as e:
            # except FileNotFoundError:
            pass
