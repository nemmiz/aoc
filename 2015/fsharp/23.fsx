open System.IO

let instructions =
    Path.Combine(__SOURCE_DIRECTORY__,"../input/23.txt")
    |> File.ReadLines
    |> Seq.map (fun s -> s.Replace(",", "").Split())
    |> Seq.toArray

let run (instructions: string [] []) initialRegs =
    let rec loop (regs: Map<string,int64>) pc =
        if pc >= instructions.Length then regs
        else match instructions.[pc] with
             | [|"hlf"; r|] -> loop (regs.Add(r, regs.[r] / 2L)) (pc + 1)
             | [|"tpl"; r|] -> loop (regs.Add(r, regs.[r] * 3L)) (pc + 1)
             | [|"inc"; r|] -> loop (regs.Add(r, regs.[r] + 1L)) (pc + 1)
             | [|"jmp"; o|] -> loop regs (pc + (int o))
             | [|"jie"; r; o|] -> loop regs (if regs.[r] % 2L = 0L then (pc + (int o)) else (pc + 1))
             | [|"jio"; r; o|] -> loop regs (if regs.[r] = 1L then (pc + (int o)) else (pc + 1))
             | _ -> failwith "Invalid instruction!"
    loop initialRegs 0 |> Map.find "b" |> printfn "%d"

run instructions (Map.empty.Add("a", 0L).Add("b", 0L))
run instructions (Map.empty.Add("a", 1L).Add("b", 0L))
