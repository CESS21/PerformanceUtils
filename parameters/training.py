# -*- coding: utf-8 -*-
#pylint: disable=redefined-outer-name
"""
Training parameter conversions.

This module provides functions to calculate various training parameters.
"""

import PerformanceUtils.datatypes as T


def fvp(inol: T.INOL, req: T.REQ) -> T.FVP:
    """
    Calculate Fatigue-Variability Product.

    Args:
        inol: Intensity * Number Of Lifts.
        req: Repetition-Endurance Quotient.

    Returns:
        Fatigue-Variability Product.
    """

    return inol * req


def inol(intensity: T.Intensity, reps: T.Quantity) -> T.INOL:
    """
    Calculate Intensity * Number Of Lifts.

    INOL is calculated as Hristov uses it.

    Args:
        intensity: Intensity used.
        reps: Number of repetitions performed.

    Returns:
        Intensity * Number Of Lifts.
    """

    return reps / ((1 - intensity) * 100)


def req(reps: T.Quantity, max_reps: T.Quantity) -> T.REQ:
    """
    Calculate Repetition-Endurance Quotient.

    Args:
        reps: Number of repetitions performed.
        max_reps: Number of repetitions that *could* be performed. For instance,
            if the lifter could performed 6 repetitions, but would be able to
            perform two more, this value would be 8.

    Returns:
        Repetition-Endurance Quotient.
    """

    return reps / max_reps


def vfi(volume: T.RelativeVolume, inol: T.INOL) -> T.VFI:
    """
    Calculate Volume-Fatigue Index.

    Args:
        volume: Relative Volume performed.
        inol: Intensity * Number Of Lifts.

    Returns:
        Volume-Fatigue Index.
    """

    return volume / inol
