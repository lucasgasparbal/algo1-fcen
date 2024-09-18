--ej2

pertenece :: (Eq t) => t -> [t] -> Bool

pertenece elem [] = False
pertenece elem (x:xs) | elem == x = True
                      | otherwise = pertenece elem xs

todosIguales :: (Eq t) => [t] -> Bool

todosIguales (x:xs) | xs == [] = True
                    | x == head xs = todosIguales xs
                    | otherwise = False

todosDistintos :: (Eq t) => [t] -> Bool

todosDistintos(x:xs) | xs == [] = True
                     | pertenece x xs = False
                     | otherwise = todosDistintos xs

quitar :: (Eq t) => t -> [t] -> [t]

quitar x xs | xs == [] = xs
            | x == head xs = tail xs
            | otherwise = (head xs) : (quitar x (tail xs))


quitarTodos :: (Eq t) =>  t ->  [t] -> [t]

quitarTodos x xs | xs == quitar x xs = xs
                 | otherwise = quitarTodos x (quitar x xs)


--ej3.3

maximo :: [Integer] -> Integer

maximo [x] = x

maximo (x:xs) | x > maximo xs = x
                 | otherwise = maximo xs


ordenar :: [Integer] -> [Integer]

ordenar [] = []

ordenar xs = (ordenar (quitar (maximo xs) xs)) ++ [maximo xs]


--ej6

type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]


--a

enLosContactos :: Nombre -> ContactosTel -> Bool

enLosContactos nombre [] = False

enLosContactos nombre ((contactoNombre, contactoNumero):xs) | nombre == contactoNombre = True
                                                            | otherwise = enLosContactos nombre xs


agregarContacto :: Contacto -> ContactosTel -> ContactosTel


agregarContacto contacto [] = [contacto]

agregarContacto (nombreNuevo,numeroNuevo) ((nombre,numero):xs) | nombreNuevo == nombre = (nombreNuevo,numeroNuevo):xs
                                                               | otherwise = (nombre,numero) : (agregarContacto (nombreNuevo,numeroNuevo) xs)