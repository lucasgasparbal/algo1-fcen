import Test.HUnit

import E12

run = runTestTT testsListaDeAmigos

testsListaDeAmigos = test [

    "lista vacia devuelve lista vacia" ~: listaDeAmigos [] ~?= [],

    "lista de 1 numero devuelve vacia" ~: listaDeAmigos [6] ~?= [],

    "lista 2 numeros no amigos devuelve vacia" ~: listaDeAmigos [3,5] ~?= [],
    
    "lista con varios numeros ningunos amigos devuelve vacia" ~: listaDeAmigos [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16] ~?= [],

    "lista con 2 amigos devuelve tupla de los 2" ~: listaDeAmigos [220,284] ~?= [(220,284)],

    "lista con 2 amigos y mas numeros devuelve la tupla de 2 amigos" ~: listaDeAmigos[1,2,9,76,220,234,260,283,284] ~?= [(220,284)],

    "lista con varios pares de amigos devuelve los pares" ~: listaDeAmigos[220,234,260,284,560,780,910,1184,1210,2620,2736,2924,4560,4928,5020,5564] ~?= [(220,284),(1184, 1210),(2620, 2924),(5020, 5564)]

    ]