let rec solve x y code =
    let nextCode = (code * 252533L) % 33554393L
    match x, y with
    | 3029, 2947 -> code
    | _, 1 -> solve 1 (x + 1) nextCode
    | _, _ -> solve (x + 1) (y - 1) nextCode

printfn "%d" (solve 1 1 20151125L)
