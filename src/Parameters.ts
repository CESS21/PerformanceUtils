/**
 * PerformanceUtils
 * Parameters.ts
 * Copyright (c) 2018 Performance Analytics
 * MIT License
**/


import * as T from "./lib/DataTypes";


// Calculate Fatigue-Variability Product from supplied microcycle total INOL and
// microcycle average REQ.
function FVP(inol: T.INOL, req: T.REQ): T.FVP {
    
    return inol * req;

}


// Calculate INOL from specified percent intensity (0.0 - 1.0) and repetition
// quantity.
function INOL(intensity: T.Intensity, reps: T.Quantity): T.INOL {

    return reps / ((1 - intensity) * 100);

}


// Calculate the Repetition-Endurance Quotient for a set of an exercise at
// specified percentage intensity and repetition quantity.
function REQ(reps: T.Quantity, maxReps: T.Quantity): T.REQ {
  
    return reps / maxReps;

}


// Calculate Volume-Fatigue Index from supplied volume as percentage of one rep
// maximum and INOL.
function VFI(volume: T.RelativeVolume, inol: T.INOL): T.VFI {

    return volume / inol;

}
