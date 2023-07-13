#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4


class Base():
    def __init__(self):
        self.id = uuid4()
        self.updated_at = datetime.now()

class ChildBase(Base):
    def __init__(self):
        self.c_id = uuid4()

print("1 ==============================")
print(Base.ChildBase)
print("end of 1---------------------------")

print(datetime.now().isoformat())
print(datetime.today().isoformat(sep="T", timespec="microseconds"))

b1 = Base()
print(b1.__dict__)
print("type of object b1: {}".format(type(b1)))
print("type of id: {}".format(type(b1.id)))
print("type of updated_at: {}".format(type(b1.updated_at)))


print("--------------------------")
my_dict = {'a': 1, 'b': 2, 'c': 3}
temp_dict = {}
for obj in my_dict:
    temp_dict[obj] = my_dict[obj] * 2
print (my_dict)
print (temp_dict)