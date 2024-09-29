import Test.HUnit

import E9


run = runTestTT testsDivisoresPropios


testsDivisoresPropios = test [

    "divisores propios de 1 no tiene" ~: divisoresPropios 1 ~?= [],

    "divisores de numero primo solo 1" ~: divisoresPropios 19 ~?= [1],

    "divisores propios de 6" ~: divisoresPropios 6 ~?= [1,2,3],

    "divisoresPropios de 146" ~: divisoresPropios 146 ~?= [1,2,73],

    "divisores propios de 100" ~: divisoresPropios 100 ~?= [1,2,4,5,10,20,25,50]

    ]