#!/usr/bin/python3
"""
initialize the models package to
create a unique FileStorage instance
for the applciation
"""

from models.engine.file_storage import FileStorage

#task 5
storage = FileStorage()
storage.reload()
