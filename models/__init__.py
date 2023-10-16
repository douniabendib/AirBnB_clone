#!/usr/bin/python3
"""Init storage file"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
