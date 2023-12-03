let nextChar c = 
    match c with
    | 'z' -> 'a'
    | 'h' | 'n' | 'k' -> char ((int c) + 2)
    | _ -> char ((int c) + 1)

let nextPassword (pwd: string) =
    let rec loop p p2 step =
        match p with
        | [] -> String.concat "" (Seq.map string p2)
        | head :: tail ->
            if step then
                let next = nextChar head
                loop tail (next :: p2) (next = 'a')
            else loop tail (head :: p2) false
    loop (pwd |> Seq.toList |> List.rev) [] true

let hasIncStraight window =
    let nums = Array.map int window
    (nums.[1] = (nums.[0] + 1)) && (nums.[2] = (nums.[0] + 2))

let rec countPairs password n =
    match password with
    | [] -> n
    | head1 :: tail1 ->
        match tail1 with
        | [] -> n
        | head2 :: tail2 ->
            if head1 = head2 then countPairs tail2 (n + 1)
            else countPairs tail1 n

let isValid (password: string) =
    (password |> Seq.windowed 3 |> Seq.exists hasIncStraight) &&
    (countPairs (Seq.toList password) 0) >= 2

let rec nextValidPassword password =
    let next = nextPassword password
    if isValid next then next
    else nextValidPassword next

let password1 = nextValidPassword "cqjxjnds"
let password2 = nextValidPassword password1

printfn "%s" password1
printfn "%s" password2
