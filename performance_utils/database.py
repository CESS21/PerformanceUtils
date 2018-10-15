# -*- coding: utf-8 -*-
"""
Database utilities.
"""


import sqlite3


db = sqlite3.connect("pu.db")

cursor = db.cursor()
