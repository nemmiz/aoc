open System.IO

let input =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/02.txt")
    |> File.ReadLines
    |> Seq.map Seq.toList
    |> Seq.toList

let velocity dir =
    match dir with
    | 'U' -> 0, -1
    | 'D' -> 0, 1
    | 'L' -> -1, 0
    | 'R' -> 1, 0
    | _ -> failwith "Invalid direction!"

let solve lines (keypad: Map<int*int,char>) startPos =
    let rec code line pos =
        match line with
        | [] -> keypad.[pos]
        | head :: tail ->
            let vx, vy = velocity head
            let nextPos = ((fst pos) + vx), ((snd pos) + vy)
            code tail (if keypad.ContainsKey nextPos then nextPos else pos)
    lines |> List.iter (fun line -> printf "%c" (code line startPos))
    printfn ""

let keypad1 = [for i in 0..8 do yield ((i%3, i/3), (char (i + 49)))] |> Map.ofList
let keypad2 = [((2, 0), '1'); ((1, 1), '2'); ((2, 1), '3'); ((3, 1), '4');
               ((0, 2), '5'); ((1, 2), '6'); ((2, 2), '7'); ((3, 2), '8');
               ((4, 2), '9'); ((1, 3), 'A'); ((2, 3), 'B'); ((3, 3), 'C');
               ((2, 4), 'D');] |> Map.ofList

solve input keypad1 (1, 1)
solve input keypad2 (2, 2)
