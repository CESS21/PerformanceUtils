# -*- coding: utf-8 -*-
#pylint: disable=redefined-outer-name
"""
Training log utilities.
"""


from datetime import datetime
from typing import Callable, Dict, List
import json

LogItem = Dict[str, any]
Log = List[LogItem]
# Accessor address type; allows specifying location of an object in a deeply
# nested structure.
Trace = List[any]

def datetime_from_iso_format(dtstr: str) -> datetime:
    """
    A workaround for `datetime.datetime.fromisoformat()` not being present in
    Python versions earlier than 3.7.
    """

    try:
        return datetime.strptime(dtstr, "%Y-%m-%d")
    except ValueError:
        return datetime.strptime(dtstr, "%Y-%m-%d %H:%M:%S")


class LogUtils():
    """Utilities for dealing with `Log` and related objects."""

    @staticmethod
    def trace_access(log: Log, trace: Trace) -> any:
        """
        Accesses an element of a `Log` tree using a `Trace` object to locate
        it.
        """

        item = log
        for key in trace:
            item = item[key]
        return item

    @staticmethod
    def filter(function: Callable[[LogItem], bool], log: Log) -> List[Trace]:
        """
        Filters through a log to obtain trace addresses
        """

        # Helper generator.
        def helper(trace: Trace):
            # Descend to current level of recursion.
            level = LogUtils.trace_access(log, trace)

            for index, log_item in enumerate(level):
                current_trace = trace + [index]

                # Filter log item.
                if function(log_item):
                    yield current_trace

                # Recurse down the tree.
                try:
                    yield from helper(current_trace + ["contents"])
                except KeyError:
                    pass

        return list(helper([]))


log: Log = json.load(open("performance_utils/example_log.json"))

def my_filter(item: LogItem) -> bool:
    """Simple example filter."""
    return item["item_id"] == 12

for trace in LogUtils.filter(my_filter, log):
    print(datetime_from_iso_format(LogUtils.trace_access(log, trace)["time"]))
