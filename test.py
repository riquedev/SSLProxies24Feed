#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: rique_dev (rique_dev@hotmail.com)

from SSLProxies24.Feed import Feed
from SSLProxies24.Check import CheckProxy
import time
import os
import gc

# Recupera a listagem
prx = Feed().PROXY_LIST

# Inicia classe
chk = CheckProxy()

# Começa validação
chk.validatelist(prx)

# Ativa garbage
gc.enable()
while True:

    # Limpa tela
    os.system('cls || clear')

    # Garbage
    if gc.isenabled():
        print('O Garbage Collector está ativo!')

    # Contagem
    print('Sucesso: '+str(chk.getsucesscount()))
    print('Falhas: '+str(chk.getfailcount()))
    print('Total de Proxys: '+str(chk.getproxycount()))
    print('Restam: '+str(chk.getproxycount()-(chk.getsucesscount()+chk.getfailcount())))

    # Lista de Proxys
    print(chk.getproxylist())

    # Aguarda 5 segundos para atualizar dados
    time.sleep(5)

    break
