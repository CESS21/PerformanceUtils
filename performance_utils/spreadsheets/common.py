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
import typing


class Worksheet(ABC):
    """
    Abstract base class for worksheet interfaces.

    Attributes:
        name: Title of the worksheet.

    Todo:
        * Write the C & D parts of CRUD interface.
    """

    name: str

    @abstractmethod
    def __init__(self: Worksheet, name: str) -> None:
        """
        Initializes `Worksheet` object.

        Implementation needs to ensure that if the actual worksheet does not
        exist, it should be created.

        Args:
            name: Title of the worksheet.
        """

        self.name = name

    @abstractmethod
    def retrieve(self: Worksheet, row: int, column: int) -> str:
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
    def update(
        self: Worksheet,
        row: int,
        column: int,
        data: str
        ) -> None:
        """
        Updates the content of a worksheet cell.

        Args:
            row: Index of the row to update cell content in.
            column: Index of the column to update cell content in.
        """

        pass


class Workbook(ABC):
    """
    Abstract base class for spreadsheet workbook interfaces.
    
    Attributes:
        name: Title of the spreadsheet workbook.
        sheets: List of worksheets within the workbook.

    Todo:
        * Write the C & D parts of CRUD interface.
    """
    
    name: str
    sheets: typing.List[Worksheet]

    @abstractmethod
    def __init__(self: Workbook, name: str) -> None:
        """
        Initializes `Workbook` object.

        Implementation needs to ensure that if the actual workbook does not
        exist, it should be created.
        
        Args:
            name: Title of the spreadsheet workbook.
        """

        self.name = name
        self.sheets = []
