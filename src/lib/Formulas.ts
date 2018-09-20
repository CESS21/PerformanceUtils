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


export class Epley
{
    public static load(
        reps: T.Quantity,
        max: T.Load
    ): T.Load
    {
        return max / (1 + reps / 30);
    }

    public static max(
        reps: T.Quantity,
        load: T.Load
    ): T.Load
    {
        return load * (1 + reps / 30);
    }

    public static reps(
        intensity: T.Intensity
    ): T.PartialQuantity
    {
        return 30 * (1 / intensity - 1);
    }
}


export class McGlothin
{
    public static load(
        reps: T.Quantity,
        max: T.Load
    ): T.Load
    {
        return max * (101.3 - 2.67123 * reps) / 100;
    }

    public static max(
        reps: T.Quantity,
        load: T.Load
    ): T.Load
    {
        return 100 * load / (101.3 - 2.67123 * reps);
    }

    public static reps(
        intensity: T.Intensity
    ): T.PartialQuantity
    {
        return (101.3 - 100 * intensity) / 2.67123;
    }
}
