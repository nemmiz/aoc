open System.IO

let lines =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/06.txt")
    |> File.ReadLines
    |> Seq.toList

let counts =
    seq {
        for i = 0 to lines.Head.Length - 1 do
            yield lines |> Seq.countBy (fun ln -> ln.[i]) |> Seq.toList
    }

counts |> Seq.map ((fun lst -> lst |> Seq.maxBy snd) >> fst >> string) |> String.concat "" |> printfn "%s"
counts |> Seq.map ((fun lst -> lst |> Seq.minBy snd) >> fst >> string) |> String.concat "" |> printfn "%s"
