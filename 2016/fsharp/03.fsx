open System.IO

let parse (s: string) =
    s.Split(' ')
    |> Array.filter (fun tmp -> tmp <> "")
    |> Array.map int

let input =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/03.txt")
    |> File.ReadLines
    |> Seq.map parse
    |> Seq.toArray

let triangles1 = 
    input 
    |> Array.map (fun (a: int []) -> a.[0], a.[1], a.[2])
    |> Array.toList

let triangles2 =
    seq {
        for i in 0 .. 3 .. (input.Length - 1) do
            yield (input.[i].[0], input.[i+1].[0], input.[i+2].[0])
            yield (input.[i].[1], input.[i+1].[1], input.[i+2].[1])
            yield (input.[i].[2], input.[i+1].[2], input.[i+2].[2])
    } |> Seq.toList

let valid = function | a, b, c -> (a + b) > c && (a + c) > b && (b + c) > a

triangles1 |> List.filter valid |> List.length |> printfn "%d"
triangles2 |> List.filter valid |> List.length |> printfn "%d"
