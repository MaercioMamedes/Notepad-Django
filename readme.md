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

### Diagrama da Matriz

![](https://github.com/MaercioMamedes/Notepad-Django/blob/master/docs/Matriz_de_Eisenhower.png?raw=true)

## Building

Esse projeto foi desenvolvido utilizando a versão 3.2.6 do interpretador Python. Todas as dependências
estão listadas no arquivo *requiments.txt*

### Como rodar ?

* realize o clone do repositório - `git clone https://github.com/MaercioMamedes/Notepad-Django.git`
* [crie um ambiente virtual dentro do diretório do projeto e instale todas as dependências](https://www.alura.com.br/artigos/ambientes-virtuais-em-python)

### Funcionalidades
* CRUD (Create , Read, Update e Delete) de usuário de notas de tarefas
* Listagem de notas agrupadas de acordo como o nível de prioridade classicado pela *matriz de Heisenhower*

### End points

|                  URI                   |    MÉTODO    |                     RECURSO                      |
|:--------------------------------------:|:------------:|:------------------------------------------------:|
|               /usuarios                |     GET      |               lista todos usuários               |
|               /usuarios                |     POST     |                Cria novo usuário                 |
|         /usuarios/{ user_id }          |     GET      |                 retorna usuário                  |
|         /usuarios/{ user_id }          | PUT ou PATCH |                 atualiza usuário                 |
|         /usuarios/{ user_id }          |    DELETE    |                  deleta usuário                  |
| /usuarios/{ user_id }/notas-atribuidas |     GET      |    lista todas as notas atribuídas ao usuário    |
|               /categoria               |     GET      |              lista todas categorias              |
|               /categoria               |     POST     |               cria nova categorias               |
|      /categoria/{ categoria_id }       |     GET      |                retorna categoria                 |
|      /categoria/{ categoria_id }       | PUT OU PATCH |                Atualiza categoria                |
|      /categoria/{ categoria_id }       |    DELETE    |                 deleta categoria                 |
|                 /notas                 |     GET      |               lista todas as notas               |
|                 /notas                 |     POST     |                cria uma nova nota                |
|           /notas/{ nota_id}            | PUT OU PATCH |                  atualiza nota                   |
|           /notas/{ nota_id }           |    DELETE    |                   deleta nota                    |
|              /atribuicao               |     GET      |         lista todas atribuições de notas         |
|              /atribuicao               |     POST     |         cria uma nova atribuição de nota         |
|        /atribuicao/{ attr_id }         |     GET      |            retorna atribuição de nota            |
|        /atribuicao/{ attr_id }         | PUT OU PATCH |           atualiza atribuição de nota            |
|        /atribuicao/{ attr_id }         |    DELETE    |            deleta atribuição de nota             |
|                 /fazer                 |     GET      | retorna todas as notas do 1ª quadrante da matriz |                
|                /agendar                |     GET      | retorna todas as notas do 2ª quadrante da matriz |
|                /delegar                |     GET      | retorna todas as notas do 3ª quadrante da matriz |
|               /eliminar                |     GET      | retorna todas as notas do 4ª quadrante da matriz |