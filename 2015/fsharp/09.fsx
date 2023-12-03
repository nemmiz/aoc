open System.IO

let parse (line: string) =
    seq {
        let parts = line.Split()
        yield ((parts.[0], parts.[2]), int parts.[4])
        yield ((parts.[2], parts.[0]), int parts.[4])
    }

let distances =
    File.ReadLines (Path.Combine(__SOURCE_DIRECTORY__,"../input/09.txt"))
    |> Seq.collect parse
    |> Map

let places =
    distances
    |> Map.toSeq
    |> Seq.map (fun t -> match t with | ((x, _), _) -> x)
    |> Seq.distinct
    |> Seq.toList

let findDistances places (distances: Map<(string*string),int>) =
    let mutable minDist = 9999999
    let mutable maxDist = 0
    let rec stuff places order =
        let length = List.length places
        if length = 0 then
            let dist = order |> List.toSeq |> Seq.pairwise |> Seq.sumBy (fun p -> distances.[p])
            minDist <- min minDist dist
            maxDist <- max maxDist dist
        else
            for i in 0 .. (length - 1) do
                let perm = List.permute (fun index -> (index + i) % length) places
                stuff perm.Tail (perm.Head :: order)
    stuff places []
    printfn "%d" minDist
    printfn "%d" maxDist

findDistances places distances
