 Esta é uma API criada com o objetivo de estudar o framework Flask e demonstrar como servir um modelo de machine learning treinado.

### Funcionalidades

#### Análise de Sentimento de Frases:

Rota:``` /sentimento/<frase> ```


Descrição: Esta rota permite analisar o sentimento de uma determinada frase. 
Utiliza a biblioteca TextBlob para traduzir a frase para o inglês (caso necessário) e calcular a polaridade do sentimento. 

Ex: GET /sentimento/Odio

Saída: A polaridade da frase é: -0.8




#### Previsão de Preços de Imóveis:


Rota: ``` /cotacao/ ```

Método: POST

Descrição: Esta rota permite fazer previsões de preços de imóveis com base nos dados de entrada fornecidos.
Os dados de entrada necessários são o tamanho do imóvel, o ano de construção e o número de garagens. Utiliza um modelo de regressão linear previamente treinado.


Ex:

Entrada:
```
{
  "tamanho": 150,
  "ano": 2005,
  "garagem": 2
}
```
Saída:
```
{
  "preco": 250000
}
```
