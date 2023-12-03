open System.IO

let doSet value (grid: int [,]) x y = grid.[y,x] <- value
let toggle (grid: int [,]) x y = grid.[y,x] <- if grid.[y,x] = 0 then 1 else 0
let inc value (grid: int [,]) x y = grid.[y,x] <- grid.[y,x] + value
let dec (grid: int [,]) x y = grid.[y,x] <- max 0 (grid.[y,x] - 1)

let mapArea (grid: int [,]) sx sy ex ey f =
    for y in sy .. ey do
        for x in sx .. ex do
            f grid x y

let runCommands commands onOn onOff onToggle =
    let grid = Array2D.zeroCreate<int> 1000 1000
    for command in commands do
        match command with
        | ("on", sx, sy, ex, ey) -> mapArea grid sx sy ex ey onOn
        | ("off", sx, sy, ex, ey) -> mapArea grid sx sy ex ey onOff
        | ("toggle", sx, sy, ex, ey) -> mapArea grid sx sy ex ey onToggle
        | _ -> failwith "Unknown command!"
    seq { 
        for y in 0 .. 999 do
            for x in 0 .. 999 -> grid.[y,x]
        }
    |> Seq.sum
    |> printfn "%d"

let parse (line: string) =
    let parts = line.Replace(",", " ").Split()
    match parts with
    | [|"turn"; op; sx; sy; "through"; ex; ey|] -> (op, int sx, int sy, int ex, int ey)
    | [|"toggle"; sx; sy; "through"; ex; ey|] -> ("toggle", int sx, int sy, int ex, int ey)
    | _ -> failwith "Invalid input!"

let commands = 
    File.ReadLines (Path.Combine(__SOURCE_DIRECTORY__,"../input/06.txt"))
    |> Seq.map parse
    |> Seq.toList

runCommands commands (doSet 1) (doSet 0) toggle
runCommands commands (inc 1) dec (inc 2)