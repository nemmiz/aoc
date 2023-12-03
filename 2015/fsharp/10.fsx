let rle (input: char seq) =
    let rec newchar (s: char list) = countchar s.Tail s.Head 1
    and countchar s c n =
        seq {
            match s with
            | head :: tail when head = c -> yield! countchar tail c (n + 1)
            | [] -> yield! (string n)
                    yield c
            | _ -> yield! (string n)
                   yield c
                   yield! newchar s
        }
    newchar (input |> Seq.toList)

let calculate input n =
    let rec loop input n result =
        match n with
        | 0 -> List.rev result
        | _ ->
            let tmp = rle input
            let length = rle input |> Seq.length
            loop tmp (n - 1) (length :: result)
    loop input n []

let results = calculate "1321131112" 50
printfn "%d" results.[39]
printfn "%d" results.[49]
