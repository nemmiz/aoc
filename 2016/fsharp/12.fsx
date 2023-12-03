open System.IO

type Instruction =
    | Cpy of int * int
    | Set of int * int
    | Inc of int
    | Dec of int
    | Jmp of int
    | Jnz of int * int

let regIndex = Map.ofList ["a", 0; "b", 1; "c", 2; "d", 3]

let parse (line: string) =
    match line.Split() with
    | [|"cpy"; src; dst|] ->
        match System.Int32.TryParse src with
        | true, x -> Set (x, regIndex.[dst])
        | false, _ -> Cpy (regIndex.[src], regIndex.[dst])
    | [|"inc"; reg|] -> Inc (regIndex.[reg])
    | [|"dec"; reg|] -> Dec (regIndex.[reg])
    | [|"jnz"; reg; off|] ->
        match System.Int32.TryParse reg with
        | true, x -> Jmp (int off)
        | false, _ -> Jnz (regIndex.[reg], int off)
    | _ -> failwith "Invalid instruction"

let run (instructions: Instruction []) (regs: int []) =
    let mutable pc = 0
    while pc < instructions.Length do
        match instructions.[pc] with
        | Cpy (a, b) -> regs.[b] <- regs.[a]
        | Set (x, b) -> regs.[b] <- x
        | Inc (a) -> regs.[a] <- regs.[a] + 1
        | Dec (a) -> regs.[a] <- regs.[a] - 1
        | Jmp (a) -> pc <- pc + a - 1
        | Jnz (a, b) -> if regs.[a] <> 0 then pc <- pc + b - 1
        pc <- pc + 1
    printfn "%d" regs.[0]

let input =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/12.txt")
    |> File.ReadLines
    |> Seq.map parse
    |> Seq.toArray

run input [|0; 0; 0; 0|]
run input [|0; 0; 1; 0|]
