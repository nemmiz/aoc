open System.Security.Cryptography
open System.Text

let calculateHash (input: string) =
    use md5 = MD5.Create()
    input
    |> Encoding.ASCII.GetBytes
    |> md5.ComputeHash
    |> Seq.map (fun x -> x.ToString("x2"))
    |> Seq.reduce (+)

let rec findHash prefix key i =
    let hash = calculateHash (key + i.ToString())
    if hash.StartsWith prefix then i
    else findHash prefix key (i + 1)

printfn "%d" (findHash "00000" "ckczppom" 0)
printfn "%d" (findHash "000000" "ckczppom" 0)
