open System.IO

let mergeRanges (ranges: (int64 * int64) list) =
    let rec loop curr (rns: (int64 * int64) list) (res: (int64 * int64) list) =
        match rns with
        | [] -> List.rev (if curr = (0L, 0L) then res else curr :: res)
        | head :: tail ->
            let s1, e1 = curr
            let s2, e2 = head
            if (s2 - e1) <= 1L then loop ((min s1 s2), (max e1 e2)) tail res
            elif curr = (0L, 0L) then loop head tail res
            else loop head tail (curr :: res)
    loop (0L, 0L) ranges []

let parse (line: string) =
    let tmp = line.Split([|'-'|])
    int64 tmp.[0], int64 tmp.[1]

let ranges =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/20.txt")
    |> File.ReadLines
    |> Seq.map parse
    |> Seq.sort
    |> Seq.toList
    |> mergeRanges

let countAllowed (ranges: (int64 * int64) list) =
    let leading = fst ranges.Head
    let trailing = 4294967295L - (ranges |> Seq.last |> snd)
    let others = ranges |> Seq.pairwise |> Seq.sumBy (fun p -> ((p |> snd |> fst) - (p |> fst |> snd) - 1L))
    others + leading + trailing
    
printfn "%d" ((snd ranges.Head) + 1L)
printfn "%d" (countAllowed ranges)
