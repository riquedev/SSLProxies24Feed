[![Build Status](https://travis-ci.org/riquedev/SSLProxies24Feed.svg?branch=master)](https://travis-ci.org/riquedev/SSLProxies24Feed) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/94104d284aa5420ca0d422defb0abd49)](https://www.codacy.com/app/rique_dev/SSLProxies24Feed?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=riquedev/SSLProxies24Feed&amp;utm_campaign=Badge_Grade) [![codecov](https://codecov.io/gh/riquedev/SSLProxies24Feed/branch/master/graph/badge.svg)](https://codecov.io/gh/riquedev/SSLProxies24Feed) [![Maintainability](https://api.codeclimate.com/v1/badges/550fedf5d605a680f698/maintainability)](https://codeclimate.com/repos/59bd9395ede9d502700015c6/maintainability)

SSL Proxies é um site onde é postado diariamente uma listagem de Proxys para serem utilizados, claro que nem todos funcionam perfeitamente, pensando nisso fiz esse pequeno código para possibilitar duas coisas.

* Obter os Proxys postados (diretamente do Feed)
* Testar um a um e só capturar os que realmente funcionam.

# Como funciona?

> A requisição é feita no site [SSL Proxies](http://www.sslproxies24.top/), para ser mais exato, em seu feed, onde é capturado o XML e então formatado para a captura dos Proxys postados.
> O que define um Proxy como válido? Bem, se a requisição feita com ele obteve sucesso. (dãh)

#### Requisitos:
* Python >=3.6
* Conexão com Internet moderada. (a velocidade de sua conexão influência na avaliação do Proxy)

#### Instalação
```bash
pip install sslproxies24
```
> Agora é só utilizar!
> Tutorial em: [https://github.com/riquedev/SSLProxies24Feed](https://github.com/riquedev/SSLProxies24Feed#como-utilizar)

### Agradecimentos
[SSL Proxies](http://www.sslproxies24.top/) por disponibilizar o serviço e o Feed.

##### Este projeto está sob licença **MIT**.
###### É isso pessoal, até a proxima 😆

## Gráfico Coverage
![Coverage](https://codecov.io/gh/riquedev/SSLProxies24Feed/branch/master/graphs/commits.svg)
