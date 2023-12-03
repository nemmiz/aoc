open System
open System.Collections.Generic

let isOpen x y =
    let tmp = x*x + 3*x + 2*x*y + y + y*y + 1364
    (Convert.ToString (tmp, 2) |> Seq.filter ((=) '1') |> Seq.length) % 2 = 0

let neighbors point =
    seq {
        let x, y = point
        if y > 0 && isOpen x (y - 1) then yield x, (y - 1)
        if x > 0 && isOpen (x - 1) y then yield (x - 1), y
        if isOpen x (y + 1) then yield x, (y + 1)
        if isOpen (x + 1) y then yield (x + 1), y
    }

let findPath start goal =
    let queue = new Queue<(int*int)*int>([start, 0])
    let mutable visited = Set.ofList [start]
    while queue.Count > 0 && not (visited.Contains goal) do
        let pos, cost = queue.Dequeue()
        for neighbor in neighbors pos do
            if not (visited.Contains neighbor) then
                visited <- visited.Add neighbor
                queue.Enqueue (neighbor, (cost + 1))
                if neighbor = goal then
                    printfn "%d" (cost + 1)

let findReachablePoints start maxSteps =
    let queue = new Queue<(int*int)*int>([start, 0])
    let mutable visited = Set.ofList [start]
    while queue.Count > 0 do
        let pos, cost = queue.Dequeue()
        if cost <= maxSteps then
            visited <- visited.Add pos
            for neighbor in neighbors pos do
                if not (visited.Contains neighbor) then
                    queue.Enqueue (neighbor, (cost + 1))
    printfn "%d" visited.Count

findPath (1,1) (31,39)
findReachablePoints (1,1) 50
