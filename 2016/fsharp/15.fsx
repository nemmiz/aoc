open System.IO

let solve (starts: int []) (nums: int []) =
    let n = starts.Length
    let rec tryFall startTime currentTime endTime =
        if currentTime >= endTime then true
        else
            let delta = (currentTime + 1) - startTime
            let disc = delta - 1
            let discPos = (starts.[disc] + (currentTime + 1)) % nums.[disc]
            if discPos <> 0 then false
            else tryFall startTime (currentTime + 1) endTime
    let rec loop i =
        if tryFall i i (i + n) then i
        else loop (i + 1)
    loop 0

let parse (line: string) =
    let tmp = line.Replace(".", "").Split()
    int tmp.[3], int tmp.[11]

let input =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/15.txt")
    |> File.ReadLines
    |> Seq.map parse
    |> Seq.toArray

let starts = Array.map snd input
let nums = Array.map fst input

solve starts nums |> printfn "%d"
solve (Array.append starts [|0|]) (Array.append nums [|11|]) |> printfn "%d"
