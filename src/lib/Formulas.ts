/**
 * PerformanceUtils
 * Formulas.ts
 * Copyright (c) 2018 Performance Analytics
 * MIT License
**/


import * as T from "./DataTypes";


export interface Formula
{
    load(
        reps: T.Quantity,
        max: T.Load
        ): T.Load;

    max(
        reps: T.Quantity,
        load: T.Load
        ): T.Load;

    reps(
        intensity: T.Intensity
        ): T.PartialQuantity;
}


export class Brzycki
{
    public static load(
        reps: T.Quantity,
        max: T.Load
        ): T.Load
    {
        return max * (37 - reps) / 36;
    }

    public static max(
        reps: T.Quantity,
        load: T.Load
        ): T.Load
    {
        return load * 36 / (37 - reps);
    }

    public static reps(
        intensity: T.Intensity
        ): T.PartialQuantity
    {
        return 37 - intensity * 36;
    }
}
