-- ejercicio 1 a)

f :: Integer -> Integer

f 1 = 8
f 4 = 131
f 16 = 16

-- ejercicio 1 b)
-- Especificacion problema g(n:Z):Z{
-- 
-- requiere : {n = 8 v n= 16 v n= 131}
-- 
-- asegura: {((n = 8)->( resultado = 16)) ^ ((n = 16)-> resultado = 4) ^((n= 131)->(resultado = 1))}
--
-- }

g :: Integer -> Integer

g 8 = 16
g 16 = 4
g 131 = 1

-- ejercico 1 c)
h :: Integer -> Integer

h 8 = 16
h 16 = 131
h 131 = 8

k :: Integer -> Integer

k 1 = 16
k 4 = 1
k 16 = 4