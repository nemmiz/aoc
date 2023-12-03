open System.IO

let lines =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/19.txt")
    |> File.ReadAllLines

let molecule = Array.last lines

let parseReplacement (r: string) =
    let parts = r.Split()
    (parts.[0], parts.[2])

let replacements =
    lines.[0 .. (lines.Length-3)]
    |> Array.map parseReplacement
    |> Array.toList

let getReplacements (molecule: string) (src: string) dst =
    seq {
        let mutable i = molecule.IndexOf src
        while i <> -1 do
            yield molecule.[0 .. (i - 1)] + dst + molecule.[(i + src.Length) .. ]
            if (i + 1) >= molecule.Length then i <- -1
            else i <- molecule.IndexOf(src, i + 1)
    }

let part1 molecule replacements =
    seq {
        for src, dst in replacements do
            yield! getReplacements molecule src dst
    } |> Seq.distinct |> Seq.length |> printfn "%d"

let part2 molecule (replacements: seq<string*string>) =
    let rec loop m n =
        match m with
        | "e" -> n
        | _ -> let src, dst = Seq.find (snd >> m.Contains) replacements
               let i = m.IndexOf dst
               loop (m.[0 .. (i - 1)] + src + m.[(i + dst.Length) .. ]) (n + 1)
    loop molecule 0 |> printfn "%d"

part1 molecule replacements
part2 molecule replacements
