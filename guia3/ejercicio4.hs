type Punto2D = (Float, Float)


prodInt :: Punto2D -> Punto2D -> Float

prodInt (v1, v2) (w1, w2) = v1*w1+v2*w2

todoMenor :: Punto2D -> Punto2D -> Bool

todoMenor (v1, v2) (w1, w2) = (v1 < w1) && (v2 < w2)


norma :: Punto2D -> Float

norma (x, y) = sqrt (x*x+y*y)

distanciaPuntos :: Punto2D -> Punto2D -> Float

distanciaPuntos (v1, v2) (w1, w2) = norma (v1-w1,v2-w2)


sumaTerna :: (Int,Int,Int)->Int

sumaTerna (v1,v2,v3) = v1+v2+v3

sumarSoloMultiplos :: (Int, Int, Int)-> Int -> Int

sumarSoloMultiplos (v1, v2, v3) n = numeroMultiplo v1 n + numeroMultiplo v2 n + numeroMultiplo v3 n

numeroMultiplo :: Int -> Int -> Int

numeroMultiplo x y | x `mod` y == 0 &&  y /= 0 = x
                   | otherwise = 0

posPrimerPar :: (Int, Int, Int) -> Int

posPrimerPar (v1,v2,v3) | even v1 = 1
                        | even v2 = 2
                        | even v3 = 3
                        | otherwise = 4

crearPar :: t1 -> t2 ->(t1,t2)

crearPar x y = (x,y)

invertirPar :: (t1,t2)->(t2,t1)

invertirPar (x,y) = (y,x)