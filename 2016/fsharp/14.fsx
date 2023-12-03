open System.Security.Cryptography
open System.Text
open System.Collections.Generic

let calculateHash n salt stretch =
    use md5 = MD5.Create()
    let rec loop (input: string) times =
        match times with
        | 0 -> input
        | _ ->
            let nextHash =
                Encoding.ASCII.GetBytes input
                |> md5.ComputeHash
                |> Seq.map (fun x -> x.ToString("x2"))
                |> String.concat ""
            loop nextHash (times - 1)
    loop (sprintf "%s%d" salt n) (if stretch then 2017 else 1)

let calculateKeys salt stretch =
    let cache = new Dictionary<int,string>()

    let getHash i =
        if not (cache.ContainsKey i) then
            cache.Add (i, (calculateHash i salt stretch))
        cache.[i]

    let rec findQuint i j quint =
        if j > (i + 1000) then false
        elif (getHash j).Contains quint then printf "."; true
        else findQuint i (j + 1) quint

    let rec loop i foundQuints =
        if foundQuints = 64 then i - 1
        else
            let h = getHash i
            match Seq.windowed 3 h |> Seq.tryFindIndex (fun x -> x.[0] = x.[1] && x.[0] = x.[2]) with
            | None ->
                loop (i + 1) foundQuints
            | Some x ->
                let quint = String.replicate 5 (string h.[x])
                if findQuint i (i + 1) quint then
                    loop (i + 1) (foundQuints + 1)
                else loop (i + 1) foundQuints

    let result = loop 0 0
    printfn ""
    printfn "%d" result

calculateKeys "zpqevtbw" false
calculateKeys "zpqevtbw" true
