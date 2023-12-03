open System.Security.Cryptography
open System.Text

let calculateHash (input: string) =
    use md5 = MD5.Create()
    input
    |> Encoding.ASCII.GetBytes
    |> md5.ComputeHash
    |> Seq.map (fun x -> x.ToString("x2"))
    |> Seq.reduce (+)

let hashes doorID =
    seq {
        let mutable i = 0
        while true do
            let hash = calculateHash (doorID + (string i))
            if hash.StartsWith "00000" then yield hash
            i <- i + 1
    }

hashes "ugkcyxxp"
|> Seq.take 8
|> Seq.map (fun h -> string h.[5])
|> String.concat ""
|> printfn "%s"

hashes "ugkcyxxp"
|> Seq.filter (fun h -> "01234567".Contains (string h.[5]))
|> Seq.distinctBy (fun h -> string h.[5])
|> Seq.take 8
|> Seq.map (fun h -> int h.[5], string h.[6])
|> Seq.sort
|> Seq.map snd
|> String.concat ""
|> printfn "%s"
