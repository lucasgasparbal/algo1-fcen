--1
pertenece :: (Eq t) => t -> [t] -> Bool

pertenece elem [] = False
pertenece elem (x:xs) | elem == x = True
                      | otherwise = pertenece elem xs

--2
todosIguales :: (Eq t) => [t] -> Bool

todosIguales (x:xs) | xs == [] = True
                    | x == head xs = todosIguales xs
                    | otherwise = False


--3
todosDistintos :: (Eq t) => [t] -> Bool

todosDistintos(x:xs) | xs == [] = True
                     | pertenece x xs = False
                     | otherwise = todosDistintos xs


--4
hayRepetidos :: (Eq t) => [t] -> Bool

hayRepetidos [] = False
hayRepetidos (x:xs) = pertenece x xs || hayRepetidos xs


--5
quitar :: (Eq t) => t -> [t] -> [t]

quitar x xs | xs == [] = xs
            | x == head xs = tail xs
            | otherwise = (head xs) : (quitar x (tail xs))


--6
quitarTodos :: (Eq t) =>  t ->  [t] -> [t]

quitarTodos x xs | xs == quitar x xs = xs
                 | otherwise = quitarTodos x (quitar x xs)



--7
eliminarRepetidos :: (Eq t) => [t] -> [t]

eliminarRepetidos [] = []

eliminarRepetidos (x:xs) | pertenece x xs = x : eliminarRepetidos (quitarTodos x xs)
                         | otherwise = x : eliminarRepetidos xs


--8

mismosElementos :: (Eq t) => [t] -> [t] -> Bool

mismosElementos lista1 lista2 = elementosEn lista1 lista2 && elementosEn lista2 lista1 


elementosEn :: (Eq t) => [t] -> [t] -> Bool

elementosEn [] lista2 = True

elementosEn (x1:xs1) lista2 = (pertenece x1 lista2) && (elementosEn xs1 lista2) 