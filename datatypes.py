# -*- coding: utf-8 -*-
"""
Training-related type aliases.

This module provides type aliases for analysis-related primitive types.

Todo:
    * Write Bounded abstract base class. Will be used for runtime data
    validation.
    * Write Percentage class. Temporarily aliased to `float`.
"""

Percentage = float

# Fatigue-Variability Product.
FVP = float
# Intensity * Number Of Lifts.
INOL = float
Intensity = Percentage
Load = float
PartialQuantity = float
Quantity = int
RelativeVolume = float
# Relative Volume.
RV = RelativeVolume
RelativeVolumePercent = Percentage
# Relative Volume: Percent.
RVPercent = RelativeVolumePercent
# Repetition-Endurance Quotient.
REQ = Percentage
# Volume-Fatigue Index.
VFI = float
