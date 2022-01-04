# PROVA 1
    A atividade consiste em desenvolver um "SistemaMultiRobos" de acordo com as definições fornecidas:
## Classe ``Robo``
*Atributos:*

- ``nome``: str encapsulada com get/set estilo Python (com ``@property``)
- ``posicao``: ``list`` com as coordenadas  x,y  que denota a posição no mundo do robô. Possui apenas get (com ``@property``)
- ``em_op``: ``bool`` público que informa se o robô está em operação ou não

*Métodos:*

- ``__init__``: recebe como parâmetro o nome do robô. Todo robô é inicializado nas coordenadas  0,0 .
- ``__str__``: retorna uma ``str`` que representa um robô. Observe a execução abaixo para visualizar o formato.
- ``distancia``: calcula a distância entre a posição atual do robô e uma posição (``list`` ou ``tuple``) passada como parâmetro. Sendo  xr,yr  a posição do robô e  x,y  uma posição qualquer, a distância é calculada por $\sqrt{(x_r - x)^2 + (y_r - y)^2}$
- `move`: faz o robô ir até a posição passada como parâmetro. Na abstração em questão, apenas atribui a nova posição do robô

## Classe `SistemaMultiRobos`

*Atributos:*

- `robos`: composição de objetos da classe `Robo`. Você pode implementar esta relação entre classes como agregação, desde que modifique também o código de testes fornecido. Este atributo não deve possuir get/set

*Métodos:*

- `__init__`: deve receber como parâmetro a quantidade de robôs que faz parte da composição (assuma que sempre será dado um número maior que 0). Caso implemente a relação como agregação, modifique este método para que a classe funcione com a agregação, mantendo a mesma multiplicidade.
- `_acha_robo_ocioso`: método privado que percorre a lista de robôs armazenada internamente e retorna o primeiro robô que encontra-se ocioso (`em_op` com valor `False`)
- `imprime_robos`: imprime todos os robôs do sistema. Observe a execução abaixo para visualizar o formato.
- `despacha`: método principal da classe. Recebe como parâmetro uma `list` ou `tuple` contendo as coordenadas para onde um robô deve ser despachado. Acha o primeiro robô ocioso da lista e o move até a posição alvo. Ao ser chamado, faz com que um robô entre em operação e imprime a distância entre o robô despachado e a posição alvo (observe a execução abaixo).

## Saída esperada do programa: 

```
-----------------
Robôs do sistema:
Robô: Robo0, ocioso em [0.0, 0.0]
Robô: Robo1, ocioso em [1.0, 0.0]
Robô: Robo2, ocioso em [2.0, 0.0]
-----------------
Robô Robo0 livre
Despachando Robo0 para (5.0, 5.0).
Distancia até o alvo: 7.0710678118654755
-----------------
Robôs do sistema:
Robô: Robo0, operando em [5.0, 5.0]
Robô: Robo1, ocioso em [1.0, 0.0]
Robô: Robo2, ocioso em [2.0, 0.0]
-----------------
Robô Robo1 livre
Despachando Robo1 para (-5.0, -5.0).
Distancia até o alvo: 7.810249675906654
-----------------
Robôs do sistema:
Robô: Robo0, operando em [5.0, 5.0]
Robô: Robo1, operando em [-5.0, -5.0]
Robô: Robo2, ocioso em [2.0, 0.0]
-----------------
Robô Robo2 livre
Despachando Robo2 para (0.0, -10.0).
Distancia até o alvo: 10.198039027185569
-----------------
Robôs do sistema:
Robô: Robo0, operando em [5.0, 5.0]
Robô: Robo1, operando em [-5.0, -5.0]
Robô: Robo2, operando em [0.0, -10.0]
-----------------
Todos os robôs ocupados
-----------------
Robôs do sistema:
Robô: Robo0, operando em [5.0, 5.0]
Robô: Robo1, operando em [-5.0, -5.0]
Robô: Robo2, operando em [0.0, -10.0]
-----------------
```