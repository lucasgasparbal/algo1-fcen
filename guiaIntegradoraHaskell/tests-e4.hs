import E4
import Test.HUnit

run = runTestTT tests


stockTodosOferta = [("tornillos",20),("clavos",60),("pituto",40)]
stockNingunoOferta = [("clavos",2),("pituto",4),("tornillos",9)]

stockAlgunosOferta = [("pituto",5),("tornillos",11),("clavos",10)]
precios = [("tornillos",10.0),("clavos",5.0),("pituto",20.0)]
tests = test [

    "test todos los productos en oferta" ~: aplicarOferta stockTodosOferta precios ~?= [("tornillos",8.0),("clavos",4.0),("pituto",16.0)], 

    "test algunos productos en oferta"  ~: aplicarOferta stockAlgunosOferta precios ~?= [("tornillos",8.0),("clavos",5.0),("pituto",20.0)],
    
    "test ningun producto en oferta"  ~: aplicarOferta stockNingunoOferta precios ~?= precios
    ]