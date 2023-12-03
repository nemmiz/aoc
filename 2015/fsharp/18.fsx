open System.IO

let data =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/18.txt")
    |> File.ReadLines
    |> Seq.map Seq.toList
    |> Seq.toList
    |> array2D

let countNeighbors (arr: char[,]) x y =
    let minx = max (x - 1) 0
    let miny = max (y - 1) 0
    let maxx = min (x + 1) 99
    let maxy = min (y + 1) 99
    let mutable total = 0
    for yy in miny .. maxy do
        for xx in minx .. maxx do
            if (xx <> x || yy <> y) && arr.[xx, yy] = '#' then
                total <- (total + 1)
    total

let nextState state =
    let mapping x y value =
        let n = countNeighbors state x y
        match value, n with
        | '#', 2 -> '#'
        | '#', 3 -> '#'
        | '#', _ -> '.'
        | '.', 3 -> '#'
        | '.', _ -> '.'
        | _, _ -> failwith "Illegal state!"
    Array2D.mapi mapping state

let countLights data =
    data |> Seq.cast<char> |> Seq.filter (fun c -> c = '#') |> Seq.length

let part1 data =
    let rec loop data n =
        if n = 0 then countLights data
        else loop (nextState data) (n - 1)
    loop data 100 |> printfn "%d"

let part2 data =
    let rec loop (data: char [,]) n =
        data.[0, 0] <- '#'
        data.[0, 99] <- '#'
        data.[99, 0] <- '#'
        data.[99, 99] <- '#'
        if n = 0 then countLights data
        else loop (nextState data) (n - 1)
    loop (Array2D.copy data) 100 |> printfn "%d"

part1 data
part2 data
