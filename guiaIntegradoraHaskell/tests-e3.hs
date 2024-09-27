import E3
import Test.HUnit

run = runTestTT tests


stockTodos = [("tornillos",20),("clavos",60),("pituto",10)]

stockAlgunos = [("pituto",5),("tornillos",10)]
precios = [("tornillos",1.0),("clavos",0.5),("pituto",3.0)]
tests = test [

    "test todos los productos en stock" ~: dineroEnStock stockTodos precios ~?= 80, 

    "test algunos productos en stock"  ~: dineroEnStock stockAlgunos precios ~?= 25
    ]

