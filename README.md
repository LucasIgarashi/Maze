# Proposta de trabalho – Métodos de busca para resolver um labirinto

**Autor** - Nome: Lucas Dantas Igarashi | Matrícula: 21203012 | Curso: Bacharelado em Ciência e Tecnologia

## Descrição

Este projeto visa resolver um labirinto de tamanho arbitrário utilizando dois algorítimos de busca:
- Breadth-First Search - BFS (Busca em largura)
- Depth First Seach - DFS (Busca em profundidade)


## How to: Instalação

1. Instalar o Python 3.9.11

2. Acessar a pasta do labirinto

    `cd .\Maze\`

3. Instalar o módulo virtualenv:

    `pip install virtualenv`

4. Criar o ambiente virtual:

    `python -m venv .venv`

5. Ativar o ambiente virtual:

  - Windows:

    `.venv\Scripts\activate`

  - macOS/Linux:

    `source .venv/bin/activate`
    
6. Instalar as dependências do script pelo arquivo requirements

    `pip install -r .\requirements.tx`

## How to: Execução

1. Iniciar a execução do script

    `python .\__init__.py`

2. A seguir, será imprimido no terminal o que deve ser feito para prosseguir com a execução do script. Comece atribuindo valores para a quantidade de linhas (largura) e colunas (altura) que você deseja que o labirinto tenha.
**Importante**: Os valores devem ser inteiros positivos, é recomendado que estejam entre 2 a 100, labirinto com dimensões superiores exigirão um tempo de processamento significativamente mais longos.

![tamanho labirinto](https://github.com/LucasIgarashi/Maze/blob/main/assets/l_x_c.png)

3. Escolha entre as opções:

![metodo](https://github.com/LucasIgarashi/Maze/blob/main/assets/possiveis_metodos.png)

## Resultados

Ao executar o script e insirir os dados requisitados no terminal, aparecerá um pop-up com a solução do labirinto em 2D.

- Amarelo: Método BFS
- Azul: Método DFS

![labirinto pop_up](https://github.com/LucasIgarashi/Maze/blob/main/assets/maze_10_x_10.png)

A quantidade de passos dados será imprimida no terminal.

![custo de passos](https://github.com/LucasIgarashi/Maze/blob/main/assets/custo_de_passos.png)
