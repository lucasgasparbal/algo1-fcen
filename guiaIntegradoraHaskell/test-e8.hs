import Test.HUnit

import E8


run = runTestTT tests 


tests = test [
    "test con un numero y no coincide" ~: esCaminoFibo [7] 1 ~?= False,
    "test con un numero y coincide" ~: esCaminoFibo [3] 4 ~?= True,
    "test con varios numeros no coincide" ~: esCaminoFibo [1,1,12356,6345,12,32] 0 ~?= False,
    "test con varios numeros coincide con n=0" ~: esCaminoFibo [0,1,1,2,3,5,8,13] 0 ~?= True,
    "test con varios numeros coincide con n /= 0" ~: esCaminoFibo [8,13,21,34,55,89] 6 ~?= True,
    "test con varios numeros coincide al principio pero no al final" ~: esCaminoFibo [8,13,21,34,56,89] 6 ~?= False
    ]