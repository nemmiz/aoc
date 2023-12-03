open System.IO

type Bot =
    | OneValue of int
    | TwoValues of int * int

// Give value to a bot that has 0 or 1 value(s)
// Fails if the bot already has 2 values
// Returns the updated bot map
let give value bot (bots: Map<int,Bot>) =
    match bots.TryFind bot with
    | Some x ->
        match x with
        | OneValue a -> bots.Add (bot, TwoValues (min a value, max a value))
        | TwoValues _ -> failwith "Cannot receive more values!"
    | None -> bots.Add (bot, OneValue value)

// Tries fetching both values of a bot
// Returns Some lo, hi if the bot has two values
// otherwise returns None
let tryFetch bot (bots: Map<int,Bot>) =
    match bots.TryFind bot with
    | Some x ->
        match x with
        | OneValue _ -> None
        | TwoValues (a, b) -> Some (a, b)
    | None -> None

let simulate lines =
    let rec loop (commands: string [] list) remaining bots (outputs: Map<int,int>) =
        match commands with
        | [] ->
            match remaining with
            | [] -> bots, outputs
            | _ -> loop (List.rev remaining) [] bots outputs
        | head :: tail when head.[0] = "value" ->
            loop tail remaining (give (int head.[1]) (int head.[5]) bots) outputs
        | head :: tail when head.[0] = "bot" ->
            match tryFetch (int head.[1]) bots with
            | None -> loop tail (head :: remaining) bots outputs
            | Some (lo, hi) ->
                match head.[5], int head.[6], head.[10], int head.[11] with
                | "bot", a, "bot", b -> loop tail remaining (give lo a (give hi b bots)) outputs
                | "output", a, "bot", b -> loop tail remaining (give hi b bots) (outputs.Add (a, lo))
                | "output", a, "output", b -> loop tail remaining bots (outputs.Add(a, lo).Add(b, hi))
                | _ -> failwith "Unhandled case"
        | _ -> failwith "Unhandled case"
    loop lines [] Map.empty Map.empty

let bots, outputs =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/10.txt")
    |> File.ReadLines
    |> Seq.map (fun line -> line.Split())
    |> Seq.toList
    |> simulate

// Part 1
Map.iter (fun k v -> if v = TwoValues(17,61) then printfn "%d" k) bots

// Part 2
printfn "%d" (outputs.[0] * outputs.[1] * outputs.[2])
