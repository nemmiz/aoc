open System.IO

let paperNeeded present =
    let (l, w, h) = present
    let sides = [l*w; w*h; h*l]
    (List.fold (fun acc x -> acc + x*2) 0 sides) + (Seq.min sides)

let ribbonNeeded present =
    let (l, w, h) = present
    let perims = [l+l+w+w; w+w+h+h; h+h+l+l]
    (Seq.min perims) + l*w*h

let parsePresent (present : string) =
    let p = Array.map int (present.Split 'x')
    (p.[0], p.[1], p.[2])

let presents = 
    File.ReadLines (Path.Combine(__SOURCE_DIRECTORY__,"../input/02.txt"))
    |> Seq.map parsePresent
    |> Seq.toList

printfn "%d" (presents |> Seq.fold (fun acc x -> acc + (paperNeeded x)) 0)
printfn "%d" (presents |> Seq.fold (fun acc x -> acc + (ribbonNeeded x)) 0)
