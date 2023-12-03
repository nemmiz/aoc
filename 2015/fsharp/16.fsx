open System.IO

let facts = 
    Map.empty.
        Add("children", 3).
        Add("cats", 7).
        Add("samoyeds", 2).
        Add("pomeranians", 3).
        Add("akitas", 0).
        Add("vizslas", 0).
        Add("goldfish", 5).
        Add("trees", 3).
        Add("cars", 2).
        Add("perfumes", 1)

let parseLine (line: string) =
    let parts = line.Replace(":", "").Replace(",", "").Split()
    Map.empty.
        Add(parts.[2], int parts.[3]).
        Add(parts.[4], int parts.[5]).
        Add(parts.[6], int parts.[7])

let sues =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/16.txt")
    |> File.ReadLines
    |> Seq.map parseLine
    |> Seq.toList

let part1match sue =
    Map.forall (fun k v -> facts.[k] = v) sue

let part2match sue =
    let pred k v =
        match k with
        | "cats" | "trees" -> v > facts.[k]
        | "pomeranians" | "goldfish" -> v < facts.[k]
        | _ -> v = facts.[k]
    Map.forall pred sue

let findAunt aunts matchFun =
    match aunts |> List.tryFindIndex matchFun with
    | Some i -> i + 1
    | None -> failwith "Failed to find aunt!"

printfn "%d" (findAunt sues part1match)
printfn "%d" (findAunt sues part2match)
