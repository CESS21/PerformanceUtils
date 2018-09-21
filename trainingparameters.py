# PerformanceUtils
# trainingparameters.py
# Copyright (c) 2018 Performance Analytics
# License: MIT


# TODO: Rename this module "parameters.training".


import datatypes as T


def fvp(inol: T.INOL, req: T.REQ) -> T.FVP:
    return inol * req


def inol(intensity: T.Intensity, reps: T.Quantity) -> T.INOL:
    return reps / ((1 - intensity) * 100)


def req(reps: T.Quantity, max_reps: T.Quantity) -> T.REQ:
    return reps / max_reps


def vfi(volume: T.RelativeVolume, inol: T.INOL) -> T.VFI:
    return volume / inol
