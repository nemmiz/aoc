open System.IO

let parse (line: string) =
    let strings = line.Replace('[', ' ').Replace(']', ' ').Split()
    let outside = [for i in 0 .. 2 .. (strings.Length - 1) do yield strings.[i]]
    let inside = [for i in 1 .. 2 .. (strings.Length - 1) do yield strings.[i]]
    outside, inside

let lines =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/07.txt")
    |> File.ReadLines
    |> Seq.map parse
    |> Seq.toList

let supportsTLS line =
    let hasAbba str =
        str
        |> Seq.windowed 4
        |> Seq.exists (fun arr -> arr.[0] = arr.[3] && arr.[1] = arr.[2] && arr.[0] <> arr.[1])
    let outside, inside = line
    List.exists hasAbba outside && not (List.exists hasAbba inside)

let supportsSSL line =
    let outside, inside = line
    let babs =
        seq {
            for string in outside do
                yield! string
                       |> Seq.windowed 3
                       |> Seq.filter (fun arr -> arr.[0] = arr.[2] && arr.[0] <> arr.[1])
                       |> Seq.map (fun arr -> sprintf "%c%c%c" arr.[1] arr.[0] arr.[1])
        } |> Set.ofSeq
    babs |> Seq.exists (fun bab -> inside |> Seq.exists (fun (ins: string) -> ins.Contains(bab)))

lines |> Seq.filter supportsTLS |> Seq.length |> printfn "%d"
lines |> Seq.filter supportsSSL |> Seq.length |> printfn "%d"
