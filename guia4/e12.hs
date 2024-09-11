raizDe2Aprox :: Integer -> Float

raizDe2Aprox n = sucesionMitades n - 1

sucesionMitades :: Integer -> Float

sucesionMitades 1 = 2
sucesionMitades n = 2 + (1 / sucesionMitades (n-1))