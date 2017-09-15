# SSLProxies24Feed

SSL Proxies é um site onde é postado diariamente uma listagem de Proxys para serem utilizados, claro que nem todos funcionam perfeitamente, pensando nisso fiz esse pequeno código para possibilitar duas coisas.

* Obter os Proxys postados (diretamente do Feed)
* Testar um a um e só capturar os que realmente funcionam.

# Como funciona?

> A requisição é feita no site [SSL Proxies](http://www.sslproxies24.top/), para ser mais exato, em seu feed, onde é capturado o XML e então formatado para a captura dos Proxys postados.
> O que define um Proxy como válido? Bem, se a requisição feita com ele obteve sucesso. (dãh)

#### Requisitos:
* Python >=3.6
* Conexão com Internet moderada. (a velocidade de sua conexão influência na avaliação do Proxy)

#### Como Utilizar
* Coloque a pasta **SSLProxies24** em seu projeto e siga o script abaixo:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Autor: rique_dev (rique_dev@hotmail.com)

from SSLProxies24.Feed import Feed
from SSLProxies24.Check import CheckProxy

# Recupera a listagem
prx = Feed().PROXY_LIST

# Inicia classe
chk = CheckProxy()

# Começa validação
chk.validatelist(prx)

# A partir de agora os Proxys já estão sendo validados dentro de uma Thread, para obter os dados você poderá utilizar:

# Contagem de sucesso:
print(str(chk.getsucesscount()))

# Contagem de Falhas:
print(str(chk.getfailcount())))

# Total de Proxys (geral)
print(str(chk.getproxycount()))

# Listagem de Proxys já avaliados e liberados com sucesso
print(chk.getproxylist())
```

### Agradecimentos
[SSL Proxies](http://www.sslproxies24.top/) por disponibilizar o serviço e o Feed.

##### Este projeto está sob licença **MIT**.
###### É isso pessoal, até a proxima 😆
