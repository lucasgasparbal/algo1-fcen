import E2
import Test.HUnit

run = runTestTT tests


stock = [("tornillos",20),("clavos",60),("pituto",107)]
tests = test [

    "test tornillos devuelve numero de tornillos" ~: stockDeProducto stock "tornillos"  ~?= 20,
    "test algo que no esta devuelve 0" ~: stockDeProducto stock "inodoros"  ~?= 0
    ]