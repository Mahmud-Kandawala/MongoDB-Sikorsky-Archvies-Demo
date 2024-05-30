



db['16mm_Films'].aggregate([{ $match: { aircraftModel: "S-76" } }]).pretty();
