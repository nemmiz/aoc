open System.IO

let uncompressedLength input recurse =
    let rec loop (data: string) =
        match data.IndexOf '(' with
        | -1 -> uint64 data.Length
        | i -> 
            let pend = data.IndexOf(')', i)
            let tmp = data.[(i + 1)..(pend - 1)].Split([|'x'|])
            let length = int tmp.[0]
            let repeat = uint64 tmp.[1]
            let chars = data.[(pend + 1)..(pend + length)]
            let subtotal = repeat * (if recurse then (uint64 (loop chars)) else (uint64 chars.Length))
            (uint64 i) + subtotal + (loop data.[(pend + length + 1)..])
    loop input

let input = Path.Combine(__SOURCE_DIRECTORY__,"../input/09.txt") |> File.ReadAllText
uncompressedLength input false |> printfn "%d"
uncompressedLength input true |> printfn "%d"
