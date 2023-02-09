# Projeto Notepad
## Uma API que gerencia lembretes/tarefas de uma execução de projeto

Esse gerenciador se baseia no princípio da matriz de Eisenhower, que tem como o objetivo,
classificar tarefas a serem executadas, de forma mais eficiente. Essa matriz é dividada em 
quatro quadrante, cada um deles determina o nível prioridade da tarefa a ser executada. O
agrupamento de tarefa, dentro da matriz, é definido a partir da combinação de dois atributos básicos da tarefa,
urgente e importante, esses atributos podem assumir apenas valores lógicos de verdadeiro ou falso.

### Tabela

| Quadrante | Importante |  Urgente   |     prioridade      |
|:---------:|:----------:|:----------:|:-------------------:|
|    1º     | Verdadeiro | Verdadeiro | Fazer imediatamente |
|    2º     | Verdadeiro |   Falso    |       Agendar       |
|    3º     |   Falso    | Verdadeiro |       Delegar       |
|    4º     |   Falso    |   Falso    |      Eliminar       |



