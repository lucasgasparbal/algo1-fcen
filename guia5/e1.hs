longitud :: [t] -> Integer

longitud [] = 0
longitud lista = 1 + longitud (tail lista)

ultimo :: [t] -> t

ultimo lista | longitud lista == 1 = head lista
             | otherwise = ultimo (tail lista)

principio :: [t] -> [t]

principio lista | longitud lista == 1 = []
                | otherwise = head lista : principio (tail lista) 


reverso :: [t]->[t]

reverso [] = []
reverso lista = ultimo lista : reverso (principio lista)