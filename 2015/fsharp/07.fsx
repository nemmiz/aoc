open System.IO
open System.Collections.Generic

let parse (line: string) = line.Split()
let commands = 
    File.ReadLines (Path.Combine(__SOURCE_DIRECTORY__,"../input/07.txt"))
    |> Seq.map parse
    |> Seq.toList

let getValue input (wires: Dictionary<string,int>) =
    match System.Int32.TryParse input with
    | true, x -> x
    | false, _ -> wires.[input]

let getValue2 input1 input2 (wires: Dictionary<string,int>) =
    (getValue input1 wires, getValue input2 wires)

let processCommands (commands: string[] list) (overrides: Map<string,int>) =
    let cmdQueue = new Queue<string[]>(commands)
    let wires = new Dictionary<string, int>()
    while cmdQueue.Count > 0 do
        let command = cmdQueue.Dequeue()
        for entry in overrides do
            wires.[entry.Key] <- entry.Value
        try
            match command with
            | [|value; "->"; a|] -> wires.[a] <- getValue value wires
            | [|"NOT"; a; "->"; b|] -> wires.[b] <- ~~~(getValue a wires) &&& 0xffff
            | [|a; "AND"; b; "->"; c|] ->
                let (x, y) = getValue2 a b wires
                wires.[c] <- x &&& y
            | [|a; "OR"; b; "->"; c|] ->
                let (x, y) = getValue2 a b wires
                wires.[c] <- x ||| y
            | [|a; "LSHIFT"; b; "->"; c|] ->
                let (x, y) = getValue2 a b wires
                wires.[c] <- (x <<< y) &&& 0xffff
            | [|a; "RSHIFT"; b; "->"; c|] ->
                let (x, y) = getValue2 a b wires
                wires.[c] <- (x >>> y) &&& 0xffff
            | _ -> failwith "Invalid command!"
        with
            | :? KeyNotFoundException as ex ->
                cmdQueue.Enqueue command
    wires.["a"]

let part1result = processCommands commands Map.empty
let part2result = processCommands commands (Map.empty.Add("b", part1result))

printfn "%d" part1result
printfn "%d" part2result
