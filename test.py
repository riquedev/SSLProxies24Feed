#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: rique_dev (rique_dev@hotmail.com)

from SSLProxies24.Feed import Feed
from SSLProxies24.Check import CheckProxy
import time
import gc

# Recupera a listagem
prx = Feed().PROXY_LIST

# Inicia classe
chk = CheckProxy()

# Começa validação
chk.validatelist(prx)

# Ativa garbage
gc.enable()

time.sleep(30)

# Contagem
print('Sucesso: '+str(chk.getsucesscount()))
print('Falhas: '+str(chk.getfailcount()))
print('Total de Proxys: '+str(chk.getproxycount()))
print('Restam: '+str(chk.getproxycount()-(chk.getsucesscount()+chk.getfailcount())))

# Lista de Proxys
print(chk.getproxylist())
del prx
del chk
print('Classes eliminadas.')
exit(0)