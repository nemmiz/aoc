open System.IO
open System.Collections.Generic

type Node = { x: int; y: int; size: int; used: int }

let parse (line: string) =
    let parts = line.Replace("-x", " ").Replace("-y", " ").Split() |> Array.filter ((<>) "")
    let x, y = int parts.[1], int parts.[2]
    let size = int (parts.[3].TrimEnd [|'T'|])
    let used = int (parts.[4].TrimEnd [|'T'|])
    { x = x; y = y; size = size; used = used }

let nodes =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/22.txt")
    |> File.ReadLines
    |> Seq.skip 2
    |> Seq.map parse
    |> Seq.toList

let part1 nodes =
    seq { for a in nodes do for b in nodes do if a <> b then yield a, b }
    |> Seq.filter (fun p -> (fst p).used > 0 && ((fst p).used <= (snd p).size - (snd p).used))
    |> Seq.length
    |> printfn "%d"

let part2 (nodes: Node list) =
    let hugeSize = nodes.Head.size * 2
    let allowedPositions = nodes |> Seq.filter (fun x -> x.size < hugeSize) |> Seq.map (fun x -> x.x, x.y) |> Set.ofSeq
    let emptyPos = nodes |> Seq.find (fun x -> x.used = 0) |> (fun x -> x.x, x.y)
    let initialState = (fst emptyPos), (snd emptyPos), nodes |> Seq.map (fun x -> x.x) |> Seq.max, 0
    let queue = new Queue<int*int*int*int>([initialState])
    let visited = new Dictionary<int*int*int*int,int>()
    visited.Add(initialState, 0)

    while queue.Count > 0 do
        let state = queue.Dequeue()
        match state with
        | _, _, 0, 0 ->
            queue.Clear()
            printfn "%d" visited.[state]
        | ex, ey, dx, dy ->
            for ox, oy in [0, -1; 0, 1; -1, 0; 1, 0] do
                let nx = ex + ox
                let ny = ey + oy
                if allowedPositions.Contains (nx, ny) then
                    let newState = if nx = dx && ny = dy then nx, ny, ex, ey else nx, ny, dx, dy
                    if not (visited.ContainsKey newState) then
                        visited.Add(newState, (visited.[state] + 1))
                        queue.Enqueue newState

part1 nodes
part2 nodes
