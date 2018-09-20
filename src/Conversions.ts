/**
 * PerformanceUtils
 * Conversions.ts
 * Copyright (c) 2018 Performance Analytics
 * MIT License
**/


import * as T from "./lib/DataTypes";
import * as Formulas from "./lib/Formulas";


let default_formula : Formulas.Formula = Formulas.Brzycki;


// Calculate percentage intensity from supplied load used and one repetition
// maximum.
function intensity(
    load: T.Load,
    max: T.Load
    ): T.Intensity
{
    return load / max;
}


// Calculate maximal repetition quantity from a supplied percentage intensity.
function maxRepsFromIntensity(
    intensity: T.Intensity,
    formula: Formulas.Formula = default_formula
    ): T.Quantity
{
    return Math.floor(formula.reps(intensity));
}


// Calculate maximal repetition quantity from a supplied load to be used and one
// repetition maximum load.
function maxRepsFromLoads(
    load: T.Load,
    max: T.Load,
    formula: Formulas.Formula = default_formula
    ): T.Quantity
{
    return Math.floor(formula.reps(intensity(load, max)));
}


// Calculate one-rep maximum weight from supplied load used and quantity of reps
// performed.
function oneRepMax(
    reps: T.Quantity,
    load: T.Load,
    formula: Formulas.Formula = default_formula
    ): T.Load
{
    return formula.max(reps, load);
}


// Calculate maximal weight that can be moved for supplied quantity of reps by a
// lifter with specified one rep max.
function repMax(
    reps: T.Quantity,
    max: T.Load,
    formula: Formulas.Formula = default_formula
    ): T.Load
{
    return formula.load(reps, max);
}
