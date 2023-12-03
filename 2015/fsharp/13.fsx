open System.IO

let parseLine (line: string) =
    let parts = line.Split()
    let name = parts.[0]
    let gain = parts.[2] = "gain"
    let amount = int parts.[3]
    let neighbor = parts.[10].TrimEnd('.')
    ((name, neighbor), if gain then amount else -amount)

let effects =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/13.txt")
    |> File.ReadLines
    |> Seq.map parseLine
    |> Map.ofSeq

let people =
    effects
    |> Map.toSeq
    |> Seq.map (fun t -> match t with | ((x, _), _) -> x)
    |> Seq.distinct
    |> Seq.toList

let peopleIncludingMe = people @ ["Myself"]

let effectsIncludingMe =
    seq {
        for p in people do
            yield (("Myself", p), 0)
            yield ((p, "Myself"), 0)
    }
    |> Map.ofSeq
    |> Map.fold (fun acc k v -> Map.add k v acc) effects

let happiness order (effects: Map<(string*string),int>) =
    order @ [order.Head]
    |> List.toSeq
    |> Seq.pairwise
    |> Seq.sumBy (fun p -> match p with a, b -> effects.[a,b] + effects.[b,a])

let optimalHappiness people (effects: Map<(string*string),int>) =
    let rec stuff people order =
        let length = List.length people
        if length = 0 then
            order @ [order.Head]
            |> List.toSeq
            |> Seq.pairwise
            |> Seq.sumBy (fun p -> match p with a, b -> effects.[a,b] + effects.[b,a])
        else 
            seq {
                for i in 0 .. (length - 1) do
                    let perm = List.permute (fun index -> (index + i) % length) people
                    yield stuff perm.Tail (perm.Head :: order)
            } |> Seq.max
    stuff people []

printfn "%d" (optimalHappiness people effects)
printfn "%d" (optimalHappiness peopleIncludingMe effectsIncludingMe)
