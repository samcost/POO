# Prática 2.2: Internet das Coisas (IoT)

No contexto de IoT (internet das coisas), um `Recurso` é um equipamento presente em uma casa automatizada, como uma *Impressora*, *Cafeteira*, *Máquina de lavar roupas*, *Bebedouro*, *Torradeira*, etc.

Estes recursos são gerenciados por um `GerenciadorRecursos`, que faz o papel de solicitar:
1. reserva do recurso para uso
2. liberação do recurso
3. processamento do recurso

Implemente o sistema de acordo com o que segue. Implemente também o diagrama de classes utilizando duas classes concretas quaisquer.
A classe `GerenciadorRecursos` é dada e não deve ser modificada.

Classe abstrata `Recurso`:

- _Atributos_: nome, número de tarefas que o recurso deve executar e uma variável booleana que indica se o recurso está ocupado. Esta classe tem um `get` para o seu `tipo` que já está implementado e não deve ser modificado.
- _Métodos_:
    - `__init__`: inicializa um recurso com nome passado como parâmetro
    - `reserva`: reserva um número de tarefas passado como parâmetro. Um recurso não deve ser reservado se ele estiver ocupado.
    - `processa` (abstrato): realiza uma tarefa no recurso (ex.: realiza uma impressão, prepara um café, etc.), caso o recurso tenha sido reservado anteriormente. Quando todas as tarefas reservadas para o recurso são realizadas, o recurso deve ser liberado para uso. O método deve retornar verdadeiro se uma tarefa foi processada ou falso caso contrário (este último caso acontece quando `processa` é chamado mas o recurso não havia sido reservado)
    - `libera`: libera um recurso para uso, independentemente das tarefas que ainda serão realizadas
    - `__repr__`: deve retornar uma versão em `str` do recurso contendo seu nome, número de tarefas e se ele está ocupado
    
Classes concretas `Impressora` e `Cafeteira`:

Estas classes devem herdar o comportamento da classe abstrata `Recurso` e devem:

- **Estender** o método abstrato `__repr__` com informação referente ao tipo específico do recurso.
Por exemplo, a classe `Impressora` deve conter `Tipo: Impressora` na string resultante.
- **Estender** o método abstrato `processa` para que seja impressa uma mensagem referente ao tipo específico do recurso. Por exemplo a classe `Impressora`, deve imprimir uma mensagem do tipo `'Realizando impressao... impressao feita com sucesso'` caso o método base retorne verdadeiro (ou seja, uma tarefa foi processada).

*Saída esperada para o programa:*

```
>>> Estado Inicial:
Recurso: cafeteira1, Tarefas: 0, Ocupado: False, Tipo: Cafeteira
==============================================
Recurso: cafeteira2, Tarefas: 0, Ocupado: False, Tipo: Cafeteira
==============================================
Recurso: impressora1, Tarefas: 0, Ocupado: False, Tipo: Impressora
==============================================
Recurso: impressora2, Tarefas: 0, Ocupado: False, Tipo: Impressora
==============================================

>Recurso cafeteira1 reservado
>Recurso impressora1 reservado

>>> Após reservar:
Recurso: cafeteira1, Tarefas: 1, Ocupado: True, Tipo: Cafeteira
==============================================
Recurso: cafeteira2, Tarefas: 0, Ocupado: False, Tipo: Cafeteira
==============================================
Recurso: impressora1, Tarefas: 1, Ocupado: True, Tipo: Impressora
==============================================
Recurso: impressora2, Tarefas: 0, Ocupado: False, Tipo: Impressora
==============================================

>Recurso cafeteira1 com processamento solicitado
>Tarefa processada
>Recurso cafeteira1 liberado
>Fazendo cafe
>Cafe feito com sucesso
>Recurso cafeteira2 com processamento solicitado
>Nao ha tarefas a serem processadas
>Cafeteira deve ser reservada previamente
>Recurso impressora1 com processamento solicitado
>Tarefa processada
>Recurso impressora1 liberado
>Realizando impressao
>Impressao realizada com sucesso
>Recurso impressora2 com processamento solicitado
>Nao ha tarefas a serem processadas
>Impressora deve ser reservada previamente

>>> Após processar tarefas:
Recurso: cafeteira1, Tarefas: 0, Ocupado: False, Tipo: Cafeteira
==============================================
Recurso: cafeteira2, Tarefas: 0, Ocupado: False, Tipo: Cafeteira
==============================================
Recurso: impressora1, Tarefas: 0, Ocupado: False, Tipo: Impressora
==============================================
Recurso: impressora2, Tarefas: 0, Ocupado: False, Tipo: Impressora
==============================================

>Recurso cafeteira1 reservado
>Recurso cafeteira2 reservado
>Recurso cafeteira1 com liberacao solicitada
>Recurso cafeteira1 liberado

>>> Após reservar e liberar:
Recurso: cafeteira1, Tarefas: 0, Ocupado: False, Tipo: Cafeteira
==============================================
Recurso: cafeteira2, Tarefas: 1, Ocupado: True, Tipo: Cafeteira
==============================================
Recurso: impressora1, Tarefas: 0, Ocupado: False, Tipo: Impressora
==============================================
Recurso: impressora2, Tarefas: 0, Ocupado: False, Tipo: Impressora
==============================================

```