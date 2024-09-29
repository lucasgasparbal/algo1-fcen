import Test.HUnit

import E10


run = runTestTT testsAmigos


testsAmigos = test [
    "test 220 y 284" ~: sonAmigos 220 284 ~?= True,

    "no importa el orden" ~: sonAmigos 284 220 ~?= True,

    "8 y 10 no son amigos" ~: sonAmigos 8 10 ~?= False,

    "numero perfecto es amigo de si mismo" ~: sonAmigos 6 6 ~?= True
    ]