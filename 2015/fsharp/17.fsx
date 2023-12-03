open System.IO

let containers =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/17.txt")
    |> File.ReadLines
    |> Seq.map int
    |> Seq.toList

let rec comb n l =
    match n, l with
    | 0, _ -> [[]]
    | _, [] -> []
    | k, (x::xs) -> List.map ((@) [x]) (comb (k-1) xs) @ comb k xs

let combs150 = 
    seq {
        for i in 1 .. containers.Length do
            for c in comb i containers do
                if (List.sum c) = 150 then
                    yield c.Length
    } |> Seq.toList

printfn "%d" combs150.Length
printfn "%d" (combs150 |> List.countBy id |> List.head |> snd)
