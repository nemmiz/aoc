let simulate hardMode =
    let mutable best = 999999
    let rec turn playerHP playerMP shdCnt psnCnt rchCnt bossHP spent isPlayersTurn =
        if spent < best then
            let bhp = if psnCnt > 0 then bossHP - 3 else bossHP
            let mp = if rchCnt > 0 then playerMP + 101 else playerMP
            let hp = if hardMode && isPlayersTurn then playerHP - 1 else playerHP
            let a = shdCnt - 1
            let b = psnCnt - 1
            let c = rchCnt - 1

            // Check if the boss is dead
            if hp > 0 && bhp <= 0 then
                best <- spent

            if hp > 0 && mp >= 53 && bhp > 0 then
                if isPlayersTurn then
                    // Try casting magic missile
                    if mp >= 53 then
                        turn hp (mp - 53) a b c (bhp - 4) (spent + 53) false

                    // Try casting drain
                    if mp >= 73 then
                        turn (hp + 2) (mp - 73) a b c (bhp - 2) (spent + 73) false
    
                    // Try casting shield
                    if mp >= 113 && a <= 0 then
                        turn hp (mp - 113) 6 b c bhp (spent + 113) false

                    // Try casting poison
                    if mp >= 173 && b <= 0 then
                        turn hp (mp - 173) a 6 c bhp (spent + 173) false

                    // Try casting recharge
                    if mp >= 229 && c <= 0 then
                        turn hp (mp - 229) a b 5 bhp (spent + 229) false

                else
                    // Attack the player
                    let dmg = 8 - (if shdCnt > 0 then 7 else 0)
                    if dmg < hp then
                        turn (hp - dmg) mp a b c bhp spent true

    turn 50 500 0 0 0 55 0 true
    printfn "%d" best

simulate false
simulate true
