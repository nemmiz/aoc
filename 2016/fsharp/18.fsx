open System.IO

let nextRow (row: string) =
    let getChar left center right =
        match left, center, right with
        | true, true, false -> '^'
        | false, true, true -> '^'
        | true, false, false -> '^'
        | false, false, true -> '^'
        | _ -> '.'
    let getTriple i c =
        if i = 0 then
            getChar false (row.[0] = '^') (row.[1] = '^')
        elif i = (row.Length - 1) then
            getChar (row.[i-1] = '^') (row.[i] = '^') false
        else
            getChar (row.[i-1] = '^') (row.[i] = '^') (row.[i+1] = '^')
    String.mapi getTriple row

let countSafeTiles row n =
    let rec loop r remaining total =
        if remaining > 0 then
            let numSafe = (Seq.filter (fun c -> c = '.') r |> Seq.length)
            loop (nextRow r) (remaining - 1) (total + numSafe)
        else total
    loop row n 0 |> printfn "%d"

let input = File.ReadAllText (Path.Combine(__SOURCE_DIRECTORY__,"../input/18.txt"))

countSafeTiles input 40
countSafeTiles input 400000
