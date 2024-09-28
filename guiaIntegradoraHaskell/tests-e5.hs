import Test.HUnit

import E5

run = runTestTT testsMaximo

tableroIguales = [

    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]
    ]

tableroVarios = [

    [1,3,19,0,17],
    [18,5,9,31,124],
    [11,23,67,1,115],
    [0,19,124,15,187],
    [1,21,24,151,9]
    ]

testsMaximo = test [

    "test 1 fila sola 1 valor" ~: maximo [[1,1,1]] ~?= 1,

    "test 1 fila sola con varios valores" ~: maximo [[1,2,10,8,74,9,54,12]] ~?= 74,

    "test varias filas con 1 valor" ~: maximo tableroIguales ~?= 1,

    "test varias filas con varios valores" ~: maximo tableroVarios ~?= 187

    ]