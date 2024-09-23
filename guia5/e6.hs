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

agregarContacto (nombreNuevo,numeroNuevo) ((nombre,numero):xs) 
    | nombreNuevo == nombre = (nombreNuevo,numeroNuevo):xs
    | otherwise = (nombre,numero) : (agregarContacto (nombreNuevo,numeroNuevo) xs)


eliminarContacto :: Nombre -> ContactosTel -> ContactosTel

eliminarContacto nombre ((contactoNombre, contactoNum):contactos)
    | not (enLosContactos nombre ((contactoNombre, contactoNum):contactos)) = (contactoNombre,contactoNum):contactos
    | nombre == contactoNombre = contactos
    | otherwise = (contactoNombre, contactoNum) : (eliminarContacto nombre contactos)