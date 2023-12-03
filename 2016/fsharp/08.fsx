open System.IO

type Command =
    | Rect of int * int
    | Row of int * int
    | Col of int * int

let parse (line: string) =
    if line.StartsWith "rect" then
        let parts = line.Replace('x', ' ').Split()
        Rect(int parts.[1], int parts.[2])
    elif line.StartsWith "rotate row" then
        let parts = line.Replace('=', ' ').Split()
        Row(int parts.[3], int parts.[5])
    elif line.StartsWith "rotate column" then
        let parts = line.Replace('=', ' ').Split()
        Col(int parts.[3], int parts.[5])
    else
        failwith "Failed to parse row!"

let solve commands =
    let screen = Array2D.create 6 50 ' '
    for command in commands do
        match command with
        | Rect (w, h) ->
            for y = 0 to (h - 1) do
                for x = 0 to (w - 1) do
                    screen.[y, x] <- '#'
        | Row (y, amount) ->
            let row = screen.[y, *]
            let action i value = screen.[y, (amount + i) % 50] <- value
            Array.iteri action row
        | Col (x, amount) ->
            let col = screen.[*, x]
            let action i value = screen.[(amount + i) % 6, x] <- value
            Array.iteri action col
    screen |> Seq.cast<char> |> Seq.filter (fun c -> c = '#') |> Seq.length |> printfn "%d"
    screen |> Array2D.iteri (fun y x value -> if x = 49 then printfn "%c" value else printf "%c" value)

Path.Combine(__SOURCE_DIRECTORY__,"../input/08.txt")
|> File.ReadLines
|> Seq.map parse
|> Seq.toList
|> solve
