open System.IO

let parseLine (line: string) =
    let parts = line.Split()
    let capacity = int (parts.[2].TrimEnd(','))
    let durability = int (parts.[4].TrimEnd(','))
    let flavor = int (parts.[6].TrimEnd(','))
    let texture = int (parts.[8].TrimEnd(','))
    let calories = int parts.[10]
    (capacity, durability, flavor, texture, calories)

let ingredients =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/15.txt")
    |> File.ReadLines
    |> Seq.map parseLine
    |> Seq.toList

let rec transpose m =
    match m with
    | (_::_)::_ -> List.map List.head m :: transpose (List.map List.tail m)
    | _ -> []

let score ingredients amounts =
    ingredients
    |> List.zip amounts
    |> List.map (fun p -> match p with (a, (c, d, f, t, _)) -> [a*c; a*d; a*f; a*t])
    |> transpose
    |> List.map (List.reduce (+) >> max 0)
    |> List.reduce (*)

let scoreOnly500cal ingredients amounts =
    let calories =
        ingredients
        |> List.zip amounts
        |> List.sumBy (fun p -> match p with (a, (_, _, _, _, c)) -> a*c)
    if calories = 500 then score ingredients amounts else 0

let findBestCookie ingredients scoreFun =
    let rec loop n remaining amounts =
        match n with
        | 1 -> scoreFun ingredients (remaining :: amounts)
        | _ -> seq {
                   for i in 0 .. remaining do
                       yield loop (n - 1) (remaining - i) (i :: amounts)
               } |> Seq.max
    loop (List.length ingredients) 100 []

printfn "%d" (findBestCookie ingredients score)
printfn "%d" (findBestCookie ingredients scoreOnly500cal)
