open System.IO

module Json =
    type Value =
        | Num of int
        | Str of string
        | Lst of List<Value>
        | Obj of Map<string, Value>

    let isDigit i = i >= (int '0') && i <= (int '9')

    let rec readFile (filename: string) =
        use stream = new StreamReader (filename)
        readJson stream

    and readJson (stream: StreamReader) =
        let c = char (stream.Peek())
        match c with
        | '[' -> readList stream
        | '{' -> readObject stream
        | '"' -> readString stream
        | '-' -> stream.Read() |> ignore; readNumber stream true
        | '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' -> readNumber stream false
        | _ -> failwith (sprintf "Invalid char: %c %s" c (stream.ReadLine()))
    
    and readList (stream: StreamReader) =
        stream.Read() |> ignore // Skip leading square bracket
        let theList =
            seq {
                while stream.Peek() <> (int ']') do
                    yield readJson stream
                    if stream.Peek() = (int ',') then
                        stream.Read() |> ignore // Skip comma
            } |> Seq.toList
        stream.Read() |> ignore // Skip trailing square bracket
        Lst theList
    
    and readObject (stream: StreamReader) =
        stream.Read() |> ignore // Skip leading curly brace
        let theMap = 
            seq {
                while stream.Peek() <> (int '}') do
                    let key = match readJson stream with
                              | Str x -> x
                              | _ -> failwith "Key must be a string!"
                    stream.Read() |> ignore // Skip colon
                    let value = readJson stream
                    yield key, value
                    if stream.Peek() = (int ',') then
                        stream.Read() |> ignore // Skip comma
            } |> Map.ofSeq
        stream.Read() |> ignore // Skip trailing curly brace
        Obj theMap
    
    and readString (stream: StreamReader) =
        stream.Read() |> ignore // Skip leading quote
        let s = seq { while stream.Peek() <> (int '"') do yield char (stream.Read()) }
                |> Seq.map string
                |> String.concat ""
        stream.Read() |> ignore // Skip trailing quote
        Str s
    
    and readNumber (stream: StreamReader) negative =
        seq { while isDigit (stream.Peek()) do yield stream.Read() - (int '0') }
        |> Seq.fold (fun total digit -> total * 10 + digit) 0
        |> (fun x -> if negative then Num -x else Num x)

let rec addNumbers data =
    match data with
    | Json.Num x -> x
    | Json.Str _ -> 0
    | Json.Lst x -> List.sumBy addNumbers x
    | Json.Obj x -> Map.fold (fun state _ value -> state + (addNumbers value)) 0 x

let isRed = function
            | Json.Str x -> x = "red"
            | _ -> false

let containsRedValue map =
    Map.exists (fun _ value -> isRed value) map

let rec addNumbersNoRed data =
    match data with
    | Json.Num x -> x
    | Json.Str _ -> 0
    | Json.Lst x -> List.sumBy addNumbersNoRed x
    | Json.Obj x when containsRedValue x -> 0
    | Json.Obj x -> Map.fold (fun state _ value -> state + (addNumbersNoRed value)) 0 x

let path = Path.Combine(__SOURCE_DIRECTORY__,"../input/12.txt")
let data = Json.readFile path

printfn "%d" (addNumbers data)
printfn "%d" (addNumbersNoRed data)
