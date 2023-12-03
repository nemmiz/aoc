open System.IO

let lines =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/04.txt")
    |> File.ReadLines
    |> Seq.toList

let sectorID (s: string) =
    let lastDash = s.LastIndexOf '-'
    let charCount =
        s.[..(lastDash - 1)].Replace("-", "")
        |> Seq.countBy id
        |> Seq.map (fun p -> 100 - (snd p), fst p)
        |> Seq.sort
        |> Seq.toList
    let calculatedChecksum = charCount.[0..4] |> List.map (snd >> string) |> String.concat ""
    let x = s.[(lastDash + 1)..].Split([|'['; ']'|])
    (if calculatedChecksum = x.[1] then int x.[0] else 0)

let decode (s: string) =
    let lastDash = s.LastIndexOf '-'
    let bracket = s.IndexOf '['
    let name = s.[..(lastDash - 1)]
    let sector = int s.[(lastDash + 1)..(bracket - 1)]
    let decodeChar c =
        if c = '-' then " "
        else let i = (int c) - (int 'a')
             ((i + sector) % 26) + (int 'a') |> char |> string
    name |> Seq.map decodeChar |> String.concat "", sector

lines |> List.sumBy sectorID |> printfn "%d"
lines |> Seq.map decode |> Seq.find (fun p -> (fst p).Contains "northpole") |> snd |> printfn "%d"
