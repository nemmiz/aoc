open System.IO
open System.Collections.Generic

let calculateValidStates n =
    let valid (arr: int []) (generatorsOnFloors: int []) =
        let rec loop a b =
            if a = arr.Length then true
            elif arr.[a] <> arr.[b] && generatorsOnFloors.[arr.[b]] > 0 then false
            else loop (a + 2) (b + 2)
        loop 0 1    
    let rec inner (arr: int []) n (generatorsOnFloors: int []) =
        seq {
            for a = 0 to 3 do
                for b = 0 to 3 do
                    if a = b || generatorsOnFloors.[b] = 0 then
                        arr.[n - 2] <- a
                        arr.[n - 1] <- b
                        generatorsOnFloors.[a] <- generatorsOnFloors.[a] + 1
                        if n > 2 then
                            yield! (inner arr (n - 2) generatorsOnFloors)
                        elif valid arr generatorsOnFloors then
                            yield Array.map string arr |> String.concat ""
                        generatorsOnFloors.[a] <- generatorsOnFloors.[a] - 1
        } |> Set.ofSeq
    let x = Array.init n id
    let y = Array.zeroCreate n
    inner x n y

let rec comb l =
    seq {
        match l with
        | [] -> ()
        | (x::xs) ->
            for b in xs do
                yield x, b
            yield! comb xs
    }

let solve initial =
    let queue = new Queue<string*int*int>([(initial,0,0)])
    let validStates = calculateValidStates initial.Length
    let endState = [for _ in initial -> "3"] |> String.concat ""
    let states = [|
        new Dictionary<string,int>();
        new Dictionary<string,int>();
        new Dictionary<string,int>();
        new Dictionary<string,int>()
    |]

    while queue.Count > 0 do
        let state, steps, floor = queue.Dequeue()

        if not (states.[floor].ContainsKey state) then
            states.[floor].Add (state, steps)

            if state = endState then
                queue.Clear()
            else
                let itemsHere = 
                    state
                    |> Seq.mapi (fun i item -> i, (int item) - 48)
                    |> Seq.filter (fun p -> snd p = floor)
                    |> Seq.map fst
                    |> Seq.toList

                for nextFloor in [floor - 1; floor + 1] do
                    if nextFloor >= 0 && nextFloor <= 3 then
                        let rep = char (nextFloor + 48)
                    
                        for a in itemsHere do
                            let newState = String.mapi (fun i c -> if i = a then rep else c) state
                            if validStates.Contains newState then
                                if not (states.[nextFloor].ContainsKey newState) then
                                    queue.Enqueue (newState, steps + 1, nextFloor)

                        for a, b in comb itemsHere do
                            let newState = String.mapi (fun i c -> if i = a || i = b then rep else c) state
                            if validStates.Contains newState then
                                if not (states.[nextFloor].ContainsKey newState) then
                                    queue.Enqueue (newState, steps + 1, nextFloor)
        
    printfn "%d" states.[3].[endState]

let parse floor (line: string) =
    line.Replace(",", "").Replace(".", "").Split()
    |> Seq.windowed 2
    |> Seq.filter (fun p -> p.[1] = "generator" || p.[1] = "microchip")
    |> Seq.map (fun p -> p.[0].[..1] + p.[1].[..0], floor)
    |> Seq.toList

let initialState =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/11.txt")
    |> File.ReadLines
    |> Seq.mapi parse
    |> Seq.reduce (@)
    |> Seq.toList
    |> List.sort
    |> List.map (snd >> string)
    |> String.concat ""

solve initialState
solve (initialState + "0000")
