
function executeAggregation() {
   
    var pipeline = [
        {
            $lookup: {
                from: "Montadoras",
                localField: "Montadora",
                foreignField: "Montadora",
                as: "Montadoras"
            }
        },
        {
            $unwind: "$Montadoras"
        },
        {
            $group: {
                _id: "$Montadoras.País",
                Carros: {
                    $push: {
                        Carro: "$Carro",
                        Cor: "$Cor"
                    }
                }
            }
        }
    ];

    
    var result = db.Carros.aggregate(pipeline);

    
    result.forEach(function(doc) {
        printjson(doc);
    });
}


executeAggregation();

