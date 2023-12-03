open System.Security.Cryptography
open System.Text
open System.Collections.Generic

let openChars = "bcdef" |> Set.ofSeq

let directions point (code: string) =
    use md5 = MD5.Create()
    let h = Encoding.ASCII.GetBytes code |> md5.ComputeHash |> Seq.map (fun x -> x.ToString("x2")) |> String.concat ""
    seq {
        let x, y = point
        if y > 0 && (openChars.Contains h.[0]) then yield 'U'
        if y < 3 && (openChars.Contains h.[1]) then yield 'D'
        if x > 0 && (openChars.Contains h.[2]) then yield 'L'
        if x < 3 && (openChars.Contains h.[3]) then yield 'R'
    }

let move pos direction =
    let x, y = pos
    match direction with
    | 'U' -> x, y - 1
    | 'D' -> x, y + 1
    | 'L' -> x - 1, y
    | 'R' -> x + 1, y
    | _ -> failwith "Invalid direction"

let findPath passcode =
    let start = 0, 0
    let goal = 3, 3
    let queue = new Queue<(int*int)*string>([(start, passcode)])
    while queue.Count > 0 do
        let pos, code = queue.Dequeue()
        if pos = goal then
            printfn "%s" (code.[passcode.Length..])
            queue.Clear()
        for d in (directions pos code) do
            queue.Enqueue (move pos d, sprintf "%s%c" code d)

let findLongest passcode =
    let start = (0, 0)
    let goal = (3, 3)
    let queue = new Queue<(int*int)*string>([(start, passcode)])
    let mutable longest = 0
    while queue.Count > 0 do
        let pos, code = queue.Dequeue()
        if pos = goal then
            longest <- max longest (code.Length - passcode.Length)
        else
            for d in (directions pos code) do
                queue.Enqueue (move pos d, sprintf "%s%c" code d)
    printfn "%d" longest

findPath "dmypynyp"
findLongest "dmypynyp"
