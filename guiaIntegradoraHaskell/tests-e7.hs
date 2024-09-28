import E7

import Test.HUnit

import E6

run = runTestTT testsValoresCamino

tableroIguales = [

    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]
    ]

tableroVarios = [

    [1,3,19,0,17],
    [18,5,9,1,124],
    [11,1,67,1,115],
    [0,19,1,15,187],
    [1,21,24,151,9]
    ]

tableroMismasReps = [

    [1,3,19,0,17],
    [3,5,9,5,124],
    [3,1,16,5,115],
    [0,19,0,3,187],
    [1,21,24,151,9]
    ]

testsValoresCamino = test [

    "test una sola posicion" ~: valoresDeCamino tableroMismasReps [(1,2)] ~?= [3],

    "test ultima posicion" ~: valoresDeCamino tableroMismasReps [(5,5)] ~?= [9],

    "test fila entera" ~: valoresDeCamino tableroMismasReps [(2,1),(2,2),(2,3),(2,4),(2,5)] ~?= [3,5,9,5,124],

    "test columna entera" ~: valoresDeCamino tableroMismasReps [(1,3),(2,3),(3,3),(4,3),(5,3)] ~?= [19,9,16,0,24],

    "test camino largo por varias filas varias columnas" ~: valoresDeCamino tableroMismasReps [(2,1),(2,2),(3,2),(3,1),(4,1),(4,2),(4,3),(4,4),(5,4),(5,5)] ~?= [3,5,1,3,0,19,0,3,151,9] 
    ]


expectAny :: (Foldable t, Eq a, Show a, Show (t a)) => a -> t a -> Test
expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)