let part1 puzzleInput =
    let count = puzzleInput / 10
    let arr = Array.create (count + 1) 10
    for i in 2 .. count do
        for j in i .. i .. count do
            arr.[j] <- arr.[j] + i * 10
    arr |> Array.findIndex (fun x -> x >= puzzleInput) |> printfn "%d"

let part2 puzzleInput =
    let count = puzzleInput / 11
    let arr = Array.create (count + 1) 0
    for i in 1 .. count do
        let last = min (i * 50) count
        for j in i .. i .. last do
            arr.[j] <- arr.[j] + i * 11
    arr |> Array.findIndex (fun x -> x >= puzzleInput) |> printfn "%d"

part1 29000000
part2 29000000
