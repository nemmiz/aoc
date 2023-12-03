
open System.IO

let removeQuotes (s: string) = s.[1 .. (s.Length-2)]

let stringLength s =
    let rec tmp n chars =
        match chars with
        | head :: tail when head = '\\' ->
            match tail.Head with
            | '\\' | '"' -> tmp (n + 1) tail.Tail
            | 'x' -> tmp (n + 1) tail.Tail.Tail.Tail
            | _ -> failwith "Invalid escape sequence!"
        | _ :: tail -> tmp (n + 1) tail
        | [] -> n
    s |> removeQuotes |> Seq.toList |> tmp 0

let stringValue1 (s: string) = s.Length - stringLength s

let escapeCharacter c =
    match c with
    | '\\' -> "\\\\"
    | '"' -> "\\\""
    | _ -> string c

let escapeString (s: string) = "\"" + (String.collect escapeCharacter s) + "\""

let stringValue2 (s: string) = (escapeString s).Length - s.Length

let lines = File.ReadAllLines (Path.Combine(__SOURCE_DIRECTORY__,"../input/08.txt"))

printfn "%d" (lines |> Seq.sumBy stringValue1)
printfn "%d" (lines |> Seq.sumBy stringValue2)
