/**
 * PerformanceUtils
 * Conversions.ts
 * Copyright (c) 2018 Performance Analytics
 * MIT License
**/


import * as T from "./lib/DataTypes";


// Calculate maximal repetition quantity from a supplied percentage intensity
// using Brzycki formula.
function maxReps(intensity: T.Intensity): T.Quantity {
    return Math.floor(37 - intensity * 36);
}


// Calculate one-rep maximum weight from supplied load used and quantity of reps
// performed, using Brzycki formula.
function oneRepMax(load: T.Load, reps: T.Quantity): T.Load {
    return load * 36 / (37 - reps);
}


// Calculate maximal weight that can be moved for supplied quantity of reps by a lifter with specified one rep max, using Brzycki formula.
function repMax(reps: T.Quantity, max: T.Load): T.Load {
    return max * (37 - reps) / 36;
}
