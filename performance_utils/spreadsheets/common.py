# -*- coding: utf-8 -*-
"""
Worksheet utilities.

This module provides abstract base classes for manipulating spreadsheets in
various programs and file formats.

Todo:
    * Allow non-string types in data manipulation.
    * Write retrieval and update utilities for ranges of cells.
"""


from abc import ABC, abstractmethod
from typing import Any, List


class AbstractCRUDWorksheet(ABC):
    """
    Abstract base class for worksheet interfaces.

    Attributes:
        name: Title of the worksheet.
        _IR: Internal representation of worksheet.
        _workbook: Workbook object the worksheet is contained in.

    Todo:
        * Write the C part of CRUD interface.
    """

    name: str
    _IR: Any
    _workbook: "AbstractCRUDWorkbook"

    @abstractmethod
    def __init__(self,
                 workbook: "AbstractCRUDWorkbook",
                 name: str,
                 index: int = None
                 ) -> None:
        """
        Initializes `AbstractCRUDWorksheet` object.

        ***Needs to be executed by subclass.***

        Subclass needs to ensure that if the actual worksheet does not exist, it
        is created.

        Args:
            workbook: Workbook to open/create sheet in.
            name: Title of the worksheet.
            index: Position to insert new sheet in list. If None, appends to
                sheet list. Unnecessary if sheet already exists in workbook.
        """

        self.name = name
        self._IR = None
        self._workbook = workbook

    @abstractmethod
    def delete(self) -> None:
        """Destroys worksheet."""

        pass

    @abstractmethod
    def read(self, row: int, column: int) -> str:
        """
        Retrieves the content of a worksheet cell.

        Args:
            row: Index of the row to retrieve cell content from.
            column: Index of the column to retrieve cell content from.

        Returns:
            Cell contents.
        """

        pass

    @abstractmethod
    def update(self, row: int, column: int, data: str) -> None:
        """
        Updates the content of a worksheet cell.

        Args:
            row: Index of the row to update cell content in.
            column: Index of the column to update cell content in.
            data: Data to update the cell content with.
        """

        pass


class AbstractCRUDWorkbook(ABC): #pylint: disable=too-few-public-methods
    """
    Abstract base class for spreadsheet workbook interfaces.

    Use `with` keyword to create and use instances of subclasses.

    Attributes:
        name: Title of the spreadsheet workbook.
        _sheets: List of worksheets within the workbook.
        _IR: Internal representation of workbook.
    """

    name: str
    _sheets: List[AbstractCRUDWorksheet]
    _IR: Any

    @abstractmethod
    def __init__(self, name: str) -> None:
        """
        Initializes `AbstractCRUDWorkbook` object.

        ***Needs to be executed by subclass.***

        Subclass needs to ensure that if the actual workbook does not exist, it
        is created.

        Args:
            name: Title of the spreadsheet workbook.
        """

        self.name = name
        self._sheets = []
        self._IR = None
    
    @abstractmethod
    def __enter__(self):
        """
        Called upon `with` block entry.

        ***Needs to be executed by subclass. Make sure to return `self`.***
        """

        self.create()

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        """
        Called upon `with` block exit.

        ***Needs to be executed by subclass.***
        """

        self.save()

    @abstractmethod
    def create(self) -> None:
        """Opens a workbook or creates a new one."""

        pass

    @abstractmethod
    def delete(self) -> None:
        """Destroys workbook."""

        pass

    @abstractmethod
    def sheet(self, sheet_name: str, index: None) -> AbstractCRUDWorksheet:
        """
        Opens a worksheet by name if it exists or creates a new one.

        Args:
            sheet_name: Title of worksheet.
            index: Position to insert new sheet in list. If None, appends to
                sheet list. Unnecessary if sheet already exists.

        Returns:
            Worksheet wrapped in `Worksheet` object.
        """

        pass

    @abstractmethod
    def save(self) -> None:
        """Saves the workbook to storage."""

        pass
