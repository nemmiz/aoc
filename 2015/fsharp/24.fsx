open System.IO

let packages =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/24.txt")
    |> File.ReadLines
    |> Seq.map int64
    |> Seq.toList

let rec comb n l =
    match n, l with
    | 0, _ -> [[]]
    | _, [] -> []
    | k, (x::xs) -> List.map ((@) [x]) (comb (k-1) xs) @ comb k xs

let solve packages groups =
    let totalWeight = List.sum packages
    let groupWeight = totalWeight / groups
    let rec loop i =
        if i >= packages.Length then failwith "No candidates!"
        let c = List.filter (fun x -> (List.sum x) = groupWeight) (comb i packages)
        if c.Length > 0 then c else loop (i + 1)
    printfn "%d" (loop 1 |> Seq.map (List.reduce (*)) |> Seq.min)

solve packages 3L
solve packages 4L
