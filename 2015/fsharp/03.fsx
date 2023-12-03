open System.IO

let next point dir =
    let (x, y) = point
    match dir with
    | '^' -> (x, y - 1)
    | 'v' -> (x, y + 1)
    | '<' -> (x - 1, y)
    | '>' -> (x + 1, y)
    | _ -> failwith "Invalid direction!"

let rec move point directions (houses : Set<int*int>) =
    match directions with
    | [] -> houses.Count
    | head :: tail -> let tmp = next point head
                      move tmp tail (houses.Add tmp)

let rec move2 point1 point2 directions (houses : Set<int*int>) =
    match directions with
    | [] -> houses.Count
    | head :: tail -> let tmp = next point1 head
                      move2 point2 tmp tail (houses.Add tmp)

let path = Path.Combine(__SOURCE_DIRECTORY__,"../input/03.txt")
let input = Seq.toList (File.ReadAllText path)

let origo = (0, 0)
printfn "%d" (move origo input (Set.empty.Add origo))
printfn "%d" (move2 origo origo input (Set.empty.Add origo))
