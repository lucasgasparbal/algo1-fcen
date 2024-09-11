sumaRacionales :: Integer -> Integer -> Float


sumaRacionales 1 q = sumaRacionalesInterna 1 q

sumaRacionales p q = sumaRacionalesInterna p q + sumaRacionales (p-1) q

sumaRacionalesInterna :: Integer -> Integer -> Float

sumaRacionalesInterna p 1 = fromInteger p
sumaRacionalesInterna p q = (fromInteger p/ fromInteger q) + sumaRacionalesInterna p (q-1)