### GeoTiff's Information API

Calculates vegetation cover and some geographical information for a given file in the server (preexisting).

A imagem 319567_2331703_2016-12-07_0c0b-20161207T151953Z.tif é uma imagem de 
satélite multiespectral georreferenciada em formato GeoTIFF obtida pelo microsssatélite ID 0c0b da constelação PlanetScope em 7 de dezembro de 2016, às 15h19m53s UTC.

Ela possui as seguintes bandas:

| ÍNDICE | BANDA   |   ALCANCE ESPECTRAL (nm) |
|--------|---------|--------------------------|
|1       |  Blue   | 455 - 515                |
|2       |  Green  | 500 - 590                |
|3       |  Red    | 590 - 670                |
|5       |  NIR    | 780 - 860                |

Sua missão é calcular o seguinte: 

- Percentual de área desta imagem que está coberto por algum tipo de vegetação
- Centróide geográfico da cena
- Área em quilômetros quadrados da cena
- Horário local da captura

Esse cálculo deverá ser fornecido através de um endpoint HTTP em formato JSON.
O arquivo swagger_api.yml contém a especificação exata do formato de retorno
e do nome do endpoint.

O servidor que serve o endpoint deve ser feito em Python/Flask.

### Desenvolvimento da API

:pushpin: API fornece um endpoint /vegetation-cover onde os cálculos e informações solicitados na
descrição do desafio são feitos através do arquivo localizado em **sources/analytic.tif**

Para executar o projeto na sua máquina o projeto necessita que seja instalada as
seguintes bibliotecas e nas suas respectivas versões:

- Python 3+
- Flask 1.1.1
- rasterio 1.1.2
- numpy 1.18.1
- affine 2.3.0
- proj 0.1.0
- Transform 0.0.1
- connexion 2.5.1
- pyproj 2.4.2.post1

Após a instalação, basta que execute o seguinte comando na raíz do projeto:

- python api.py

Tudo certo? :+1:

Ahh.. :bulb: já ia me esquecendo! :grimacing: Foram desenvolvidos alguns testes para garantir que a API funcione como o esperado
e também para validar o deploy da mesma no Heroku. A execução dos testes é feita através do comando:

- pytest

Para executar apenas o teste da API no Heroku, execute:

- pytest test_api_heroku.py

**Agora sim! Tudo pronto!** :raised_hands: O acesso a API pode ser feito através de duas formas:

- http://localhost:5000 :house:
- https://alaor-strdr.herokuapp.com/ :cloud:
