open System.IO

let parseLine (line: string) =
    let parts = line.Split()
    let speed = int parts.[3]
    let flyTime = int parts.[6]
    let restTime = int parts.[13]
    (speed, flyTime, restTime)

let distanceTraveled time speed flyTime restTime =
    let rec fly remainingTime dist =
        let timeFlying = min flyTime remainingTime
        let d = speed * timeFlying
        rest (remainingTime - timeFlying) (dist + d)
    and rest remainingTime dist =
        if remainingTime <= restTime then dist
        else fly (remainingTime - restTime) dist
    fly time 0

let distances maxTime speed flyTime restTime =
    [for t in 1 .. maxTime do yield distanceTraveled t speed flyTime restTime]

let rec transpose m =
    match m with
    | (_::_)::_ -> List.map List.head m :: transpose (List.map List.tail m)
    | _ -> []

let reindeer =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/14.txt")
    |> File.ReadLines
    |> Seq.map parseLine
    |> Seq.toList

reindeer
|> List.map (fun r -> distanceTraveled 2503 <||| r)
|> List.max
|> printfn "%d"

let reindeerDistances = reindeer |> List.map (fun r -> distances 2503 <||| r)
let furthestDistances = reindeerDistances |> transpose |> List.map List.max

reindeerDistances
|> transpose
|> List.zip furthestDistances
|> List.map (fun p -> match p with best, dists -> List.map (fun x -> if x = best then 1 else 0) dists)
|> transpose
|> List.map List.sum
|> List.max
|> printfn "%d"        
