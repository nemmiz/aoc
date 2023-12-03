open System.IO

let vowels = ['a';'e';'i';'o';'u']
let isVowel c = List.contains c vowels
let countVowels = String.filter isVowel >> String.length

let bad = ["ab"; "cd"; "pq"; "xy"]
let containsBad (str: string) = List.exists str.Contains bad

let part1filter input =
    countVowels input >= 3 &&
    not (containsBad input) &&
    input |> Seq.pairwise |> Seq.exists (fun (a, b) -> a = b)

let findPair pair chars =
    chars |> Seq.pairwise |> Seq.exists (fun p -> p = pair)

let rec hasRepeatingPairs chars =
    match chars with
    | [] -> false
    | head1 :: tail1 ->
        match tail1 with
        | [] -> false
        | head2 :: tail2 ->
            findPair (head1, head2) tail2 || hasRepeatingPairs tail1

let part2filter input =
    input |> Seq.windowed 3 |> Seq.exists (fun a -> a.[0] = a.[2]) &&
    hasRepeatingPairs (Seq.toList input)

let strings = 
    File.ReadLines (Path.Combine(__SOURCE_DIRECTORY__,"../input/05.txt"))
    |> Seq.toList

printfn "%d" (strings |> List.filter part1filter |> List.length)
printfn "%d" (strings |> List.filter part2filter |> List.length)
