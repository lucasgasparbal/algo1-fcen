import Test.HUnit

import E6

run = runTestTT testsMaximo

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

testsMaximo = test [

    "test un valor solo" ~: masRepetido [[1]] ~?= 1,
    "test 1 fila 1 valor" ~: masRepetido [[1,1,1,1,1,1]] ~?= 1,
    "test 1 fila varios valores" ~: masRepetido [[1,3,4,5,67,8,1,2,3,3,3,1,4,5,6,1,7,109]] ~?= 1,
    "test tablero 1 valor" ~: masRepetido tableroIguales ~?= 1,
    "test tablero varios valores 1 valor mas repetido" ~: masRepetido tableroVarios ~?= 1,
    "test 1 fila 2 numeros con mismas repeticiones" ~: expectAny (masRepetido [[1,0]]) [1,0],
    "test tablero varios numeros con mismas repeticiones"~: expectAny (masRepetido tableroMismasReps) [1,0,3,5]

    ]


expectAny :: (Foldable t, Eq a, Show a, Show (t a)) => a -> t a -> Test
expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)