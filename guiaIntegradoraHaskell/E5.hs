module E5 where

type Fila = [Integer]

type Tablero = [Fila]

type Posicion = (Integer, Integer)

type Camino = [Posicion]

maximo :: Tablero -> Integer

maximo [fila] = maximoDeFila fila

maximo (fila1:fila2:filas) | maximoDeFila fila1 > maximoDeFila fila2 = maximo (fila1:filas)
                    | otherwise = maximo (fila2:filas)


maximoDeFila :: Fila -> Integer

maximoDeFila [x] = x

maximoDeFila (x:y:xs) | y > x = maximoDeFila (y:xs)
                      | otherwise = maximoDeFila (x:xs)