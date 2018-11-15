# -*- coding: utf-8 -*-
"""
Training log utilities.
"""


from performance_utils.database import cursor as db
from typing import List

class LogItem():

    def __init__(self, log_id, log_item):
        self._log_id = log_id # There should be no setter method for log_id.

        self._datetime = log_item.datetime
        self._duration = log_item.duration
        self._item_id = log_item.item_id
        self._item_type = log_item.item_type
        self._parent_id = log_item.parent_id

    def delete(self):
        """
        Delete database entry for log item. Note that this does not destroy the
        Python object associated with the database entry, so once this method
        has been called, it is up to the caller to handle object discarding.
        """

        db.execute("""
            DELETE FROM log_{0} WHERE item_id=(?);
        """.format(self.log_id), (self.item_id))

    ### Properties to handle updating database fields in setters.

    @property
    def log_id(self):
        return self._log_id

    @property
    def datetime(self):
        return self._datetime
    
    @datetime.setter
    def datetime(self, value):
        db.execute("""
            UPDATE log_{0} SET datetime=(?) WHERE item_id=(?);
        """.format(self.log_id), (value, self.item_id))
        self._datetime = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        db.execute("""
            UPDATE log_{0} SET duration=(?) WHERE item_id=(?);
        """.format(self.log_id), (value, self.item_id))
        self._duration = value

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        db.execute("""
            UPDATE log_{0} SET item_id=(?) WHERE item_id=(?);
        """.format(self.log_id), (value, self.item_id))
        self._item_id = value

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        db.execute("""
            UPDATE log_{0} SET item_type=(?) WHERE item_id=(?);
        """.format(self.log_id), (value, self.item_id))
        self._item_type = value

    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, value):
        db.execute("""
            UPDATE log_{0} SET parent_id=(?) WHERE item_id=(?);
        """.format(self.log_id), (value, self.item_id))
        self._parent_id = value


class Log():

    items: List[LogItem]

    def __init__(self, log_id: int):
        """
        Initialize the object.

        Todo:
            * Make log_id an optional argument, with an autoincrement default
            feature, starting at zero.
        """
        self._log_id = log_id # There should be no setter method for log_id.

        # Create log table in database if it does not exist.
        db.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
        if "log_{0}".format(self.log_id) not in db.fetchall():
            db.execute("""
                CREATE TABLE log_{0} (
                    item_id INTEGER NOT NULL PRIMARY KEY,
                    parent_id INTEGER,
                    item_type TEXT,
                    datetime TEXT,
                    duration REAL
                );
            """.format(self.log_id))

        # Retrieve all log items from database table.
        db.execute("SELECT * FROM log_{0};".format(self.log_id))
        self.items = [LogItem(log_id, log_item) for log_item in db.fetchall()]

    def delete(self):
        """
        Delete database table for log. Note that this does not destroy the
        Python object associated with the database table, so once this method
        has been called, it is up to the caller to handle object discarding.
        """

        db.execute("""
            DROP TABLE log_{0};
        """.format(self.log_id))

    @property
    def log_id(self):
        return self._log_id
