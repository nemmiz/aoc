let generateData initial size =
    let rec loop (a: string) =
        if a.Length < size then
            let b = a |> Seq.rev |> Seq.map (fun c -> if c = '0' then "1" else "0") |> String.concat ""
            loop (a + "0" + b)
        else a.[..(size-1)]
    loop initial

let rec calculateChecksum (data: string) =
    if data.Length % 2 = 0 then
        Seq.chunkBySize 2 data
        |> Seq.map (fun p -> if p.[0] = p.[1] then "1" else "0")
        |> String.concat ""
        |> calculateChecksum
    else printfn "%s" data    

generateData "10111011111001111" 272 |> calculateChecksum
generateData "10111011111001111" 35651584 |> calculateChecksum
