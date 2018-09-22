# -*- coding: utf-8 -*-
"""
One-Rep Maximum Formulas.

This module provides classes for estimating one-rep maximum loads and related
metrics using different formulas.
"""

from abc import ABC, abstractmethod
import math

import PerformanceUtils.datatypes as T


class Formula(ABC):
    """Abstract base class for one-repetition maximal load estimator classes."""

    @staticmethod
    @abstractmethod
    def one_rep_max(reps: T.Quantity, rep_max: T.Load) -> T.Load:
        """
        Estimate one-repetition maximum load.

        Args:
            reps: Repetitions performed.
            rep_max: Maximum load that can be performed for ``reps``
                repetitions.

        Returns:
            Estimated one-rep maximum load.
        """

        pass

    @staticmethod
    @abstractmethod
    def rep_max(reps: T.Quantity, one_rep_max: T.Load) -> T.Load:
        """
        Estimate maximal load that can be performed for a supplied number of
        repetitions.

        Args:
            reps: Repetitions to estimate a maximal load for.
            one_rep_max: One-repetition maximal load.

        Returns:
            Maximal load that can be performed for the supplied number of
            repetitions.
        """

        pass

    @staticmethod
    @abstractmethod
    def reps(intensity: T.Intensity) -> T.PartialQuantity:
        """
        Estimate maximum number of repetitions that can be performed at a
        supplied intensity.

        Args:
            intensity: Intensity as coefficient of one-repetition maximal load.

        Returns:
            Maximal (real / float) number of repetitions that can be performed
            at the supplied intensity.
        """

        pass


class Brzycki(Formula):
    """
    One-repetition maximal load estimator using Brzycki formula.

    https://en.wikipedia.org/wiki/One-repetition_maximum#Brzycki
    """

    @staticmethod
    def one_rep_max(reps: T.Quantity, rep_max: T.Load) -> T.Load:
        return rep_max * 36 / (37 - reps)

    @staticmethod
    def rep_max(reps: T.Quantity, one_rep_max: T.Load) -> T.Load:
        return one_rep_max * (37 - reps) / 36

    @staticmethod
    def reps(intensity: T.Intensity) -> T.PartialQuantity:
        return 37 - intensity * 36


class Epley(Formula):
    """
    One-repetition maximal load estimator using Epley formula.

    https://en.wikipedia.org/wiki/One-repetition_maximum#Epley_formula
    """

    @staticmethod
    def one_rep_max(reps: T.Quantity, rep_max: T.Load) -> T.Load:
        return rep_max * (1 + reps / 30)

    @staticmethod
    def rep_max(reps: T.Quantity, one_rep_max: T.Load) -> T.Load:
        return one_rep_max / (1 + reps / 30)

    @staticmethod
    def reps(intensity: T.Intensity) -> T.PartialQuantity:
        return 30 * (1 / intensity - 1)


class McGlothin(Formula):
    """
    One-repetition maximal load estimator using McGlothin formula.

    https://en.wikipedia.org/wiki/One-repetition_maximum#McGlothin
    """

    @staticmethod
    def one_rep_max(reps: T.Quantity, rep_max: T.Load) -> T.Load:
        return 100 * rep_max / (101.3 - 2.67123 * reps)

    @staticmethod
    def rep_max(reps: T.Quantity, one_rep_max: T.Load) -> T.Load:
        return one_rep_max * (101.3 - 2.67123 * reps) / 100

    @staticmethod
    def reps(intensity: T.Intensity) -> T.PartialQuantity:
        return (101.3 - 100 * intensity) / 2.67123


class Lombardi(Formula):
    """
    One-repetition maximal load estimator using Lombardi formula.

    https://en.wikipedia.org/wiki/One-repetition_maximum#Lombardi
    """

    @staticmethod
    def one_rep_max(reps: T.Quantity, rep_max: T.Load) -> T.Load:
        return reps ** 0.1 * rep_max

    @staticmethod
    def rep_max(reps: T.Quantity, one_rep_max: T.Load) -> T.Load:
        return one_rep_max / (reps ** 0.1)

    @staticmethod
    def reps(intensity: T.Intensity) -> T.PartialQuantity:
        return intensity ** -10


class Mayhew(Formula):
    """
    One-repetition maximal load estimator using Mayhew et al. formula.

    https://en.wikipedia.org/wiki/One-repetition_maximum#Mayhew_et_al.
    """

    @staticmethod
    def one_rep_max(reps: T.Quantity, rep_max: T.Load) -> T.Load:
        return 100 * rep_max / (52.2 + 41.9 * (math.e ** (-0.055 * reps)))

    @staticmethod
    def rep_max(reps: T.Quantity, one_rep_max: T.Load) -> T.Load:
        return one_rep_max * (52.2 + 41.9 * (math.e ** (-0.055 * reps))) / 100

    @staticmethod
    def reps(intensity: T.Intensity) -> T.PartialQuantity:
        return 200 / 11 * math.log(419 / (2 * (500 * intensity - 261)))


class OConner(Formula):
    """
    One-repetition maximal load estimator using O'Conner formula.

    https://en.wikipedia.org/wiki/One-repetition_maximum#O'Conner_et_al.
    """

    @staticmethod
    def one_rep_max(reps: T.Quantity, rep_max: T.Load) -> T.Load:
        return rep_max * (1 + reps / 40)

    @staticmethod
    def rep_max(reps: T.Quantity, one_rep_max: T.Load) -> T.Load:
        return one_rep_max / (1 + reps / 40)

    @staticmethod
    def reps(intensity: T.Intensity) -> T.PartialQuantity:
        return 40 * (1 / intensity - 1)


class Wathan(Formula):
    """
    One-repetition maximal load estimator using Wathan formula.

    https://en.wikipedia.org/wiki/One-repetition_maximum#Wathan
    """

    @staticmethod
    def one_rep_max(reps: T.Quantity, rep_max: T.Load) -> T.Load:
        return 100 * rep_max / (48.8 + 53.8 * (math.e ** (-0.075 * reps)))

    @staticmethod
    def rep_max(reps: T.Quantity, one_rep_max: T.Load) -> T.Load:
        return one_rep_max * (48.8 + 53.8 * (math.e ** (-0.075 * reps))) / 100

    @staticmethod
    def reps(intensity: T.Intensity) -> T.PartialQuantity:
        return 40 / 3 * math.log(269 / (500 * intensity - 244))
