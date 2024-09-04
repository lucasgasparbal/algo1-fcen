type Coordenada3d = (Float, Float, Float)

absoluto :: Float -> Float

absoluto x | x >= 0 = x
           | otherwise = -x


distanciaManhattan :: Coordenada3d -> Coordenada3d -> Float

distanciaManhattan (x1,y1,z1) (x2,y2,z2) = absoluto (x1-x2) + absoluto (y1-y2)+ absoluto (z1-z2)