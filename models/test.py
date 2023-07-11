#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4

print(datetime.now().isoformat())
print(datetime.today().isoformat(sep="T", timespec="microseconds"))
