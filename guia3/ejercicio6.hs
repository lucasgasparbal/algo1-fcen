type Anio = Integer
type EsBisiesto = Bool

bisiesto :: Anio -> EsBisiesto

bisiesto anio = not ((anio `mod` 4 /= 0 ) || (anio `mod` 100 == 0 && ((anio `mod` 400) /= 0)))