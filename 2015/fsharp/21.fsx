let weapons = [
    Some (8, 4, 0);
    Some (10, 5, 0);
    Some (25, 6, 0);
    Some (40, 7, 0);
    Some (74, 8, 0);
]

let armors = [
    None;
    Some (13, 0, 1)
    Some (31, 0, 2);
    Some (53, 0, 3);
    Some (75, 0, 4);
    Some (102, 0, 5);
]

let rings = [
    None;
    Some (25, 1, 0);
    Some (50, 2, 0);
    Some (100, 3, 0);
    Some (20, 0, 1);
    Some (40, 0, 2);
    Some (80, 0, 3);
]

let fight playerDamage playerArmor =
    let rec playerTurn playerHP bossHP =
        let bossArmor = 2
        let dmg = max 1 (playerDamage - bossArmor)
        if dmg >= bossHP then true
        else bossTurn playerHP (bossHP - dmg)
    and bossTurn playerHP bossHP =
        let bossDamage = 9
        let dmg = max 1 (bossDamage - playerArmor)
        if dmg >= playerHP then false
        else playerTurn (playerHP - dmg) bossHP
    playerTurn 100 103

let equipmentTotal equipment =
    let addParts b a =
        match b with
        | None -> a
        | Some (b1, b2, b3) ->
            let a1, a2, a3 = a
            (a1 + b1, a2 + b2, a3 + b3)
    let wep, arm, rn1, rn2 = equipment
    (0, 0, 0) |> addParts wep |> addParts arm |> addParts rn1 |> addParts rn2

let inventories =
    seq {
        for wep in weapons do
            for arm in armors do
                for rn1 in rings do
                    for rn2 in rings do
                        if rn1.IsNone || rn2.IsNone || rn1.Value <> rn2.Value then
                            yield wep, arm, rn1, rn2
    } |> Seq.map equipmentTotal |> Seq.toList

let results =
    seq {
        for cost, damage, armor in inventories do
            yield cost, fight damage armor
    } |> Seq.toList

printfn "%d" (results |> Seq.filter snd |> Seq.map fst |> Seq.min)
printfn "%d" (results |> Seq.filter (snd >> not) |> Seq.map fst |> Seq.max)
