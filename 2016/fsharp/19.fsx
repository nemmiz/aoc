open System.Collections.Generic


let part1 n =
    let queue = new Queue<int>([for i = 1 to n do yield i])

    while queue.Count > 0 do
        let elf = queue.Dequeue()

        if queue.Count > 0 then
            queue.Dequeue() |> ignore
            queue.Enqueue(elf)
        else
            printfn "Elf %d wins" elf


let part2 n =
    let queue1 = new LinkedList<int>([for i = 1 to n / 2 do yield i])
    let queue2 = new Queue<int>([for i = n / 2 + 1 to n do yield i])

    while queue1.Count > 0 do
        let elf = queue1.First.Value
        queue1.RemoveFirst()

        if queue2.Count > 0 then
            if queue1.Count >= queue2.Count then
                queue1.RemoveLast()
            else
                queue2.Dequeue() |> ignore

            queue2.Enqueue(elf)
            queue1.AddLast(queue2.Dequeue()) |> ignore
        else
            printfn "Elf %d wins" elf


part1 3017957
part2 3017957
