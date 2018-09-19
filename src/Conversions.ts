/**
 * PerformanceUtils
 * Conversions.ts
 * Copyright (c) 2018 Performance Analytics
 * MIT License
**/


import * as T from "./lib/DataTypes";


interface IFormula {

    load(reps: T.Quantity, max: T.Load): T.Load;

    max(reps: T.Quantity, load: T.Load): T.Load;

    reps(intensity: T.Intensity): T.PartialQuantity;

}


class Brzycki {

    public static load(reps: T.Quantity, max: T.Load): T.Load {

        return max * (37 - reps) / 36;

    }

    public static max(reps: T.Quantity, load: T.Load): T.Load {

        return load * 36 / (37 - reps);

    }

    public static reps(intensity: T.Intensity): T.PartialQuantity {

        return 37 - intensity * 36;

    }

}


// Calculate percentage intensity from supplied load used and one repetition
// maximum.
function intensity(load: T.Load, max: T.Load): T.Intensity {
    
    return load / max;
    
}


// Calculate maximal repetition quantity from a supplied percentage intensity
// using Brzycki formula.
function maxRepsFromIntensity(intensity: T.Intensity): T.Quantity {

    let formula: IFormula = Brzycki;

    return Math.floor(formula.reps(intensity));

}


// Calculate maximal repetition quantity from a supplied load to be used and one
// repetition maximum load.
function maxRepsFromLoads(load: T.Load, max: T.Load): T.Quantity {

    let formula: IFormula = Brzycki;

    return Math.floor(formula.reps(intensity(load, max)));

}


// Calculate one-rep maximum weight from supplied load used and quantity of reps
// performed, using Brzycki formula.
function oneRepMax(reps: T.Quantity, load: T.Load): T.Load {

    let formula: IFormula = Brzycki;

    return formula.max(reps, load);

}


// Calculate maximal weight that can be moved for supplied quantity of reps by a lifter with specified one rep max, using Brzycki formula.
function repMax(reps: T.Quantity, max: T.Load): T.Load {

    let formula: IFormula = Brzycki;

    return formula.load(reps, max);

}
