from pyamaze import maze, agent, COLOR, textLabel
from collections import deque

def Maze(m, method):
    start = (m.rows, m.cols)
    goal = (1, 1)

    def test(cell):
        return cell == goal #verifica se a célula atual é a saída

    def BFSSuccessor(cell, visited):
        queue = deque([cell]) #fila com as coordenadas
        path = {}
        while queue:
            curr_cell = queue.popleft() #acessa os da fila (First in Fisrt Out)
            if test(curr_cell):
                print('Saída Encontrada!!!')
                break
            for d in 'ESNW': #ordem de verificação da direção: W -> N -> S -> E
                if m.maze_map[curr_cell][d] == True:
                    if d == 'E': child_cell = (curr_cell[0], curr_cell[1] + 1)
                    elif d == 'W': child_cell = (curr_cell[0], curr_cell[1] - 1)
                    elif d == 'N': child_cell = (curr_cell[0] - 1, curr_cell[1])
                    elif d == 'S': child_cell = (curr_cell[0] + 1, curr_cell[1])
                    if child_cell in visited: continue
                    visited.append(child_cell)
                    queue.append(child_cell)
                    path[child_cell] = curr_cell
        return path


    def BFS(cell):
        visited = [cell]
        path = BFSSuccessor(cell, visited)
        inverted_path = {}
        node = goal
        steps = 1
        while node != start:
            inverted_path[path[node]] = node
            node = path[node]
            steps += 1
        return inverted_path, steps


    def DFSSuccessor(cell, visited):
        stack = [cell] #pilha com as coordenadas
        path = {}
        while len(stack) > 0:
            curr_cell = stack.pop() #Acessa os valores da pilha (Last In First Out)
            if test(curr_cell):
                print('Saída Encontrada!!!')
                break
            for d in 'ESNW': #ordem de verificação da direção: W -> N -> S -> E
                if m.maze_map[curr_cell][d] == True:
                    if d == 'E': child_cell = (curr_cell[0], curr_cell[1] + 1)
                    elif d == 'W': child_cell = (curr_cell[0], curr_cell[1] - 1)
                    elif d == 'N': child_cell = (curr_cell[0] - 1, curr_cell[1])
                    elif d == 'S': child_cell = (curr_cell[0] + 1, curr_cell[1])
                    if child_cell in visited: continue
                    visited.append(child_cell)
                    stack.append(child_cell)
                    path[child_cell] = curr_cell
        return path


    def DFS(cell):
        visited=[cell]
        node = goal
        path = DFSSuccessor(cell, visited)
        inverted_path = {}
        steps = 1
        while node != start:
            inverted_path[path[node]] = node
            node = path[node]
            steps += 1
        return inverted_path, steps


    if method == 'BFS':
        path, _ = BFS(start)
    elif method == 'DFS':
        path, _ = DFS(start)
    return path




if __name__=='__main__':
    r = int(input('Insira a quantidade desejada de linhas: '))
    c = int(input('Insira a quantidade desejada de colunas: '))

    print('------------------------------------------------------------------------------')

    choose=int(input('Qual método deseja utilizar para resolver o labirinto?\n1 - BFS\n2 - DFS\n3 - Ambos\n4 - Nenhum\nR: '))

    print('------------------------------------------------------------------------------')

    if choose == 1:
        m = maze(r, c)
        m.CreateMaze(loopPercent=20)
        path = Maze(m, 'BFS')
        a = agent(m, footprints=True, color=COLOR.blue)
        print('------------------------------------------------------------------------------')
        m.tracePath({a: path})
        l=textLabel(m, 'O menor caminho dado pelo método DFS é: ', len(path)+1)
        m.run()

    elif choose == 2:
        m = maze(r, c)
        m.CreateMaze(loopPercent=20)
        path = Maze(m, 'DFS')
        a = agent(m, footprints=True, color=COLOR.yellow)
        print('------------------------------------------------------------------------------')
        m.tracePath({a: path})
        l=textLabel(m, 'O menor caminho dado pelo método DFS é: ', len(path)+1)
        m.run()

    elif choose == 3:
        m = maze(r, c)
        m.CreateMaze(loopPercent=20)
        path_bfs = Maze(m, 'BFS')
        path_dfs = Maze(m, 'DFS')
        a = agent(m, footprints=True, color=COLOR.blue)
        b = agent(m, footprints=True, color=COLOR.yellow)

        print('------------------------------------------------------------------------------')
        m.tracePath({a: path_bfs})
        m.tracePath({b: path_dfs})
        l_bfs = textLabel(m, 'BFS - AZUL\nO menor caminho dado pelo método BFS é: ', len(path_bfs) + 1)
        l_dfs = textLabel(m, 'DFS - AMARELO\nO menor caminho dado pelo método DFS é: ', len(path_dfs) + 1)
        m.run()

    elif choose == 4:
        print('Saindo...')
        quit