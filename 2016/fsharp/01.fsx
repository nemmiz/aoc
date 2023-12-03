open System.IO

let input = Path.Combine(__SOURCE_DIRECTORY__,"../input/01.txt") |> File.ReadAllText
let directions = input.Replace(",", "").Split() |> Array.map (fun x -> x.[0], (int x.[1..])) |> Array.toList

let turn facing dir =
    match facing, dir with
    | 'U', 'L' | 'D', 'R' -> 'L'
    | 'D', 'L' | 'U', 'R' -> 'R'
    | 'L', 'L' | 'R', 'R' -> 'D'
    | 'R', 'L' | 'L', 'R' -> 'U'
    | _ -> failwith "Invalid direction!"

let velocity facing =
    match facing with
    | 'U' -> 0, -1
    | 'D' -> 0, 1
    | 'L' -> -1, 0
    | 'R' -> 1, 0
    | _ -> failwith "Invalid direction!"

let part1 directions =
    let rec loop x y facing dirs =
        match dirs with
        | [] -> (abs x) + (abs y)
        | head :: tail -> 
            match head with
            | dir, steps ->
                let newFacing = turn facing dir
                let vx, vy = velocity newFacing
                loop (x + vx * steps) (y + vy * steps) newFacing tail
    loop 0 0 'U' directions |> printfn "%d"

let part2 directions =
    let rec loop x y facing dirs (visited: Set<int*int>) =
        match dirs with
        | [] -> failwith "Did not visit any points twice!"
        | head :: tail ->
            match head with
            | dir, steps ->
                let newFacing = turn facing dir
                let vx, vy = velocity newFacing
                visit x y vx vy steps newFacing tail visited
    and visit x y vx vy steps facing dirs (visited: Set<int*int>) =
        let x2 = x + vx
        let y2 = y + vy
        if visited.Contains (x2, y2) then abs(x2) + abs(y2)
        elif steps > 1 then visit x2 y2 vx vy (steps - 1) facing dirs (visited.Add((x2, y2)))
        else loop x2 y2 facing dirs (visited.Add((x2, y2)))
    loop 0 0 'U' directions (Set.empty.Add((0, 0))) |> printfn "%d"

part1 directions
part2 directions
