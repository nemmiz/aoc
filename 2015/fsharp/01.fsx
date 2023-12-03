open System.IO

let rec part1 input floor =
    match input with
    | [] -> floor
    | head :: tail when head = '(' -> part1 tail (floor + 1)
    | head :: tail when head = ')' -> part1 tail (floor - 1)
    | _ -> failwith "Bad input!"

let rec part2 input floor n =
    if floor < 0 then n
    else match input with
         | head :: tail when head = '(' -> part2 tail (floor + 1) (n + 1)
         | head :: tail when head = ')' -> part2 tail (floor - 1) (n + 1)
         | _ -> failwith "Bad input!"

let path = Path.Combine(__SOURCE_DIRECTORY__,"../input/01.txt")
let input = Seq.toList (File.ReadAllText path)

printfn "%d" (part1 input 0)
printfn "%d" (part2 input 0 0)
