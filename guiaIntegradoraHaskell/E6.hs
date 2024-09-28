module E6 where

type Fila = [Integer]

type Tablero = [Fila]

type Posicion = (Integer, Integer)

type Camino = [Posicion]

type NumeroOcurrencia = (Integer, Integer)

masRepetido :: Tablero -> Integer

masRepetido tablero = conseguirMasRepetido ( numerosYOcurrenciasDelTablero tablero)


conseguirMasRepetido :: [NumeroOcurrencia] -> Integer

conseguirMasRepetido [(numero,ocurrencia)] = numero

conseguirMasRepetido ((numero1,ocurrencia1):(numero2,ocurrencia2):numerosOcurrencias) | ocurrencia2 > ocurrencia1 = conseguirMasRepetido ((numero2,ocurrencia2):numerosOcurrencias)
                                                                                      | otherwise = conseguirMasRepetido ((numero1,ocurrencia1):numerosOcurrencias)




numerosYOcurrenciasDelTablero :: Tablero -> [NumeroOcurrencia]

numerosYOcurrenciasDelTablero [fila] = numeroOcurrenciasDeFila fila
numerosYOcurrenciasDelTablero (fila:filas) = combinarNumeroOcurrencias (numeroOcurrenciasDeFila fila) (numerosYOcurrenciasDelTablero filas)


combinarNumeroOcurrencias :: [NumeroOcurrencia] -> [NumeroOcurrencia] -> [NumeroOcurrencia]

combinarNumeroOcurrencias [x] lista2 = agregarNumeroOcurrencia x lista2

combinarNumeroOcurrencias (x:xs) lista2 = agregarNumeroOcurrencia x (combinarNumeroOcurrencias xs lista2)
 

agregarNumeroOcurrencia :: NumeroOcurrencia -> [NumeroOcurrencia] -> [NumeroOcurrencia]

agregarNumeroOcurrencia (numero,ocurrencia) [] = [(numero,ocurrencia)]

agregarNumeroOcurrencia (numero1,ocurrencia1) ((numero2,ocurrencia2):numerosOcurrencias) | numero1 == numero2 = (numero1,ocurrencia1+ocurrencia2) : numerosOcurrencias
                                                         | otherwise = (numero2,ocurrencia2) : agregarNumeroOcurrencia (numero1,ocurrencia1) numerosOcurrencias


numeroOcurrenciasDeFila :: Fila -> [NumeroOcurrencia]

numeroOcurrenciasDeFila [] = []

numeroOcurrenciasDeFila (x:xs)  = agregarNumero x (numeroOcurrenciasDeFila xs)

agregarNumero :: Integer -> [NumeroOcurrencia] -> [NumeroOcurrencia]

agregarNumero n [] = [(n,1)]

agregarNumero n ((numero,ocurrencia):numerosOcurrencias) | n == numero = (numero,ocurrencia+1): numerosOcurrencias
                                                         | otherwise = (numero,ocurrencia): agregarNumero n numerosOcurrencias