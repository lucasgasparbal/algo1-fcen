import Test.HUnit
import Clase5funciones


runFib = runTestTT testsFib

testsFib = test [
    "casoBase n=0" ~: fib 0 ~?= 0,
    "casoBase n=1" ~: fib 1 ~?= 1,
    "pasoRecursivo n=5" ~: fib 5 ~?= 5,
    "pasoRecursivo n=10" ~: fib 10 ~?= 55,
    "pasoRecursivo n=3" ~: fib 3 ~?= 2,
    "testParaFallo" ~: fib 1 ~?= 0
    ]

runPares = runTestTT testsPares

testsPares = test [

    "lista Vacia Devuelve Lista Vacia" ~: pares [] ~?= [],
    "lista Sin Pares Devuelve Vacia" ~: pares [1,3,5] ~?= [],
    "lista De 1 Solo Par Devuelve La Misma Lista" ~: pares [2] ~?= [2],
    "lista con varios Pares devuelve una permutacion" ~: (esPermutacion (pares [2,4,6,8]) [2,4,6,8]) ~?= True,
    "lista con elementos pares e impares" ~: (esPermutacion (pares [1,3,4,2,6,7,8,10,19,24]) [2,4,6,8,10,24]) ~?= True,
    "lista con elementos pares e impares distinto orden" ~: (esPermutacion (pares [1,3,4,2,6,7,8,10,19,24]) [6,8,4,2,24,10]) ~?= True,
    "lista con pares repetidos no los incluye" ~: (esPermutacion (pares [1,2,3,4,4,5,6]) [2,4,6]) ~?= True

    ]

esPermutacion :: (Eq t) => [t] -> [t] -> Bool

esPermutacion [] [] = True

esPermutacion (x:xs) lista2 = length (x:xs) == length lista2 && pertenece x lista2 && (esPermutacion xs (quitar x lista2))

quitar :: (Eq t) => t -> [t] -> [t]

quitar _ [] = []

quitar elem (x:xs) | elem == x = xs
                   | otherwise = x : quitar elem xs


-- hacer funciones generar stock

