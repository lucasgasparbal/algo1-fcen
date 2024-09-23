{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Redundant bracket" #-}
import Test.HUnit

lockers = [(100,(False,"ZD39I")),(101,(True,"JAH3I")),(103,(True,"IQSA9")),(105,(True,"QOTSA")),(109,(False,"893JJ")),(110,(False,"99292"))]
type Texto = [Char]
type Identificacion = Integer
type Ubicacion = Texto
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
type Disponibilidad = Bool


existeElLocker :: Identificacion -> MapaDeLockers -> Bool

existeElLocker _  [] = False

existeElLocker identificador((lockerId,_):lockers) = (identificador == lockerId) || existeElLocker identificador lockers


ubicacionDelLocker :: Identificacion -> MapaDeLockers -> Ubicacion

ubicacionDelLocker _ [] = ""

ubicacionDelLocker identificacion ((lockerId,(_,lockerUbicacion)):lockers)
    | identificacion == lockerId = lockerUbicacion
    | otherwise = ubicacionDelLocker identificacion lockers



estaDisponibleLocker :: Identificacion -> MapaDeLockers -> Disponibilidad

estaDisponibleLocker _ [] = False

estaDisponibleLocker identificacion ((lockerId,(lockerDisponibilidad,_)):lockers)
    | identificacion == lockerId = lockerDisponibilidad
    | otherwise = estaDisponibleLocker identificacion lockers

ocuparLocker :: Identificacion -> MapaDeLockers -> MapaDeLockers

ocuparLocker _ [] = []
ocuparLocker id  ((lockerId, (lockerDisponibilidad,lockerUbicacion)):lockers)
 | id == lockerId = (id,(False,lockerUbicacion)):lockers
 | otherwise = (lockerId, (lockerDisponibilidad,lockerUbicacion)): (ocuparLocker id lockers)




testSuiteUbicacionDelLocker = test [
 "caso1" ~: (ubicacionDelLocker 100 lockers ) ~?= "ZD39I",
 "caso2" ~: (ubicacionDelLocker 105 lockers) ~?= "QOTSA"] 

testSuiteEstaDisponibleLocker = test [
 "casoFalse" ~: (estaDisponibleLocker 100 lockers ) ~?= False,
 "casoTrue" ~: (estaDisponibleLocker 101 lockers ) ~?= True]