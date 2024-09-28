module E7 where


type Fila = [Integer]

type Tablero = [Fila]

type Posicion = (Integer, Integer)

type Camino = [Posicion]


valoresDeCamino :: Tablero -> Camino -> [Integer]

valoresDeCamino tablero [x] = [obtenerNumeroEnPos tablero x]

valoresDeCamino tablero (x:xs) = obtenerNumeroEnPos tablero x : valoresDeCamino tablero xs


obtenerNumeroEnPos :: Tablero -> Posicion -> Integer

obtenerNumeroEnPos (fila:filas) (posFila,posColumna) | posFila == 1 = obtenerNumeroDeFila fila posColumna
                                                     | otherwise = obtenerNumeroEnPos filas (posFila-1,posColumna) 

obtenerNumeroDeFila :: Fila -> Integer -> Integer

obtenerNumeroDeFila (x:xs) 1 = x
obtenerNumeroDeFila  (x:xs) n = obtenerNumeroDeFila xs (n-1)


