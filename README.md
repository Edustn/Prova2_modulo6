# Perguntas:
## 2.1. 

O método escolhido foi o HAAR Cacade. Se trata de um algoritmo de detecção de objetos e faces, que utiliza uma série de características simples, Hear-like features, calculadas rapidamente por meio da imagem integarl, a qual é baseada em 3 componetes principais: imagem integral, seleção de características e casacade de classificadores.

## 2.2 A ordem seria: 

HAAR Cascade

NN Linear

CNN

Filtros de correlação cruzada

Essa ordem foi escolihda principalmente pelo poder de processemanto de cada um, pois para esse caso em específico não se faz necessário ter grandes opções para diferentes análsies. Nesse setido, por exemplo se o filtro de correlação curzada fosse escolhido só estaria sendo utilizado uma ferramenta muito poderosa para um problema "pequeno", assim disperdiçando armazenamento e poder computacional.

Ademais, o HAAR Cascade é de suma importância, pois é um algoritmo mais leve e de fácil implementação com uma ótimo autonomia de tempo para o caso indicado.

Já o CNN lienar e Filtros de convolução cruzada são algorotmos mais robostudos com mais camadas de comparação se comparado com o Haar Casacde e NN Linear. Assim, resultando em uma análise mais profunda e demorada. 

## 2.3 

A nova ordem do item seria: 

CNN

Filtros de correlação cruzada

HAAR Cascade

NN Linear


Essa nova ordem se daria pelo fato de ser necessário abordagens mais profundas agora do que somente analisar uma face, ou seja, essa nova disposição dos algoritmos teria que analisar de uma maneira masis profunda cada rosto e cada sutileza que se faz na expressão de cada rosto.

## 2.4 
Sim, todos os algoritmos listados podem considerar variação de um frame para outro se devidamente treinados.


Obs: Artigo utilizado para pegar a base de dados para analisar as emoções das pessoas: https://www.aprendizartificial.com/deteccao-de-emocoes-em-video-com-python-e-deep-learning/



# Execução do programa:
1 - Clone esse repositório, com o seguinte comando `git clone 'https://github.com/Edustn/Prova2_modulo6.git'`

2 - Baixe o Python e a biblioteca CV2.

3 - Execute o comando `python3 main.py`
