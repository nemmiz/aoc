open System
open System.IO

type Command =
    | Move of int * int
    | SwapIndex of int * int
    | SwapLetter of char * char
    | RotateLeft of int
    | RotateRight of int
    | RotateBasedOnPos of char
    | Reverse of int * int

let parse (line: string) =
    match line.Split() with
    | [|"swap"; "position"; x; "with"; "position"; y|] -> SwapIndex (int x, int y)
    | [|"swap"; "letter"; x; "with"; "letter"; y|] -> SwapLetter (char x, char y)
    | [|"rotate"; "left"; x; _|] -> RotateLeft (int x)
    | [|"rotate"; "right"; x; _|] -> RotateRight (int x)
    | [|"rotate"; "based"; "on"; "position"; "of"; "letter"; x|] -> RotateBasedOnPos (char x)
    | [|"reverse"; "positions"; x; "through"; y|] -> Reverse (int x, int y)
    | [|"move"; "position"; src; "to"; "position"; dst|] -> Move (int src, int dst)
    | _ -> failwithf "Invalid instruction! %s" line

let ranges =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/21.txt")
    |> File.ReadLines
    |> Seq.map parse
    |> Seq.toList

let swapPositions (str: string) x y =
    let swapFun i c = if i = x then str.[y] elif i = y then str.[x] else c
    str |> Seq.mapi swapFun |> String.Concat

let swapLetters (str: string) (x: char) (y: char) =
    swapPositions str (str.IndexOf x) (str.IndexOf y)

let reverseInterval (str: string) x y =
    let inner i c =
        if i < x || i > y then c
        else str.[y - (i - x)]
    str |> Seq.mapi inner |> String.Concat

let rotateLeft str n =
    let rec rot (s: string) n =
        if n = 0 then s
        else rot (s.[1..] + s.[..0]) (n - 1)
    rot str n

let rotateRight str n =
    let rec rot (s: string) n =
        if n = 0 then s
        else rot (s.[(s.Length-1)..] + s.[..(s.Length-2)]) (n - 1)
    rot str n

let rotateBasedOnIndex (str: string) (x: char) =
    let i = str.IndexOf x
    let amount = 1 + i + (if i >= 4 then 1 else 0)
    rotateRight str amount

let unrotateBasedOnIndex (str: string) (x: char) =
    let rec loop s =
        if (rotateBasedOnIndex s x) = str then s
        else loop (rotateLeft s 1)
    loop str

let move (str: string) x y =
    let c = string str.[x]
    let n = str.Length
    let tmp = if x = 0 then str.[1..]
              elif x = (n-1) then str.[..n-2]
              else str.[..x-1] + str.[x+1..]
    if y = 0 then c + tmp
    elif y = (n-1) then tmp + c
    else tmp.[..y-1] + c + tmp.[y..]

let rec scramble operations str =
    match operations with
    | [] -> str
    | head :: tail ->
        match head with
        | Move (x, y) -> scramble tail (move str x y)
        | SwapIndex (x, y) -> scramble tail (swapPositions str x y)
        | SwapLetter (x, y) -> scramble tail (swapLetters str x y)
        | RotateLeft x -> scramble tail (rotateLeft str x)
        | RotateRight x -> scramble tail (rotateRight str x)
        | RotateBasedOnPos x -> scramble tail (rotateBasedOnIndex str x)
        | Reverse (x, y) -> scramble tail (reverseInterval str x y)

let rec unscramble operations str =
    match operations with
    | [] -> str
    | head :: tail ->
        match head with
        | Move (x, y) -> unscramble tail (move str y x)
        | SwapIndex (x, y) -> unscramble tail (swapPositions str x y)
        | SwapLetter (x, y) -> unscramble tail (swapLetters str x y)
        | RotateLeft x -> unscramble tail (rotateRight str x)
        | RotateRight x -> unscramble tail (rotateLeft str x)
        | RotateBasedOnPos x -> unscramble tail (unrotateBasedOnIndex str x)
        | Reverse (x, y) -> unscramble tail (reverseInterval str x y)

printfn "Scramble   : %s" (scramble ranges "abcdefgh")
printfn "Unscramble : %s" (unscramble (List.rev ranges) "fbgdceah")
