/**
 * PowerliftingUtils
 * Copyright (c) 2018 Carter Hinsley
 * MIT License
 */

function FVP(inol, req) {
  // Calculate Fatigue-Variability Product from supplied microcycle total INOL and microcycle average REQ.
  return inol * req;
}

function INOL(intensity, reps) {
  // Calculate INOL from specified percent intensity (0.0 - 1.0) and repetition quantity.
  
  if (intensity > 0.96) {
    intensity = 0.96;
  }
  
  return reps / (100 - 100 * intensity)
}

function maxReps(intensity) {
  // Calculate maximal repetition quantity from a supplied percentage intensity using Brzycki formula.
  if (intensity == 1.0) {
    return 1.0;
  } else {
    return Math.floor(37 - intensity * 36);
  }
}

function oneRepMax(load, reps) {
  // Calculate one-rep maximum weight from supplied load used and quantity of reps performed, using Brzycki.
  return load * 36 / (37 - reps);
}

function repMax(reps, max) {
  // Calculate maximal weight that can be moved for supplied quantity of reps by a lifter with specified one rep max, using Brzycki formula.
  return max * (37 - reps) / 36;
}

function REQ(intensity, reps) {
  // Calculate the Repetition-Endurance Quotient for a set of an exercise at specified percentage intensity and repetition quantity.
  return reps / maxReps(intensity);
}

function VFI(volume, inol) {
  // Calculate Volume-Fatigue Index from supplied volume as percentage of one rep maximum and INOL.
  return volume / inol;
}
