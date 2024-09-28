from pyamaze import maze, agent, COLOR
from collections import deque

def Maze(m, method):
    start = (m.rows, m.cols)
    goal = (1, 1)

    def test(cell):
        return cell == goal #verifica se a célula atual é a saída

    def BFSSuccessor(cell, visited):
        queue = deque([cell]) #fila com as coordenadas
        path = {} #
        while len(queue) > 0:
            curr_cell = queue.popleft() #acessa os valores da fila (First in Fisrt Out)
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
            curr_cell = stack.pop() #acessa os valores da pilha (Last In First Out)
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
        path, step = BFS(start)
    elif method == 'DFS':
        path, step = DFS(start)
    return path, step

if __name__=='__main__':
    r = int(input('Insira a quantidade desejada de linhas: '))
    c = int(input('Insira a quantidade desejada de colunas: '))

    print('------------------------------------------------------------------------------')

    choose=int(input('Qual método deseja utilizar para resolver o labirinto?\n1 - BFS\n2 - DFS\n3 - Ambos\n4 - Nenhum\nR: '))

    print('------------------------------------------------------------------------------')

    if choose == 1:
        m = maze(r, c)
        m.CreateMaze(loopPercent=15)
        path, step = Maze(m, 'BFS')
        a = agent(m, footprints=True, color=COLOR.blue)

        m.tracePath({a: path})
        print(f'Custo de passos: {step}')
        m.run()

    elif choose == 2:
        m = maze(r, c)
        m.CreateMaze(loopPercent=15)
        path, step = Maze(m, 'DFS')
        a = agent(m, footprints=True, color=COLOR.yellow)

        m.tracePath({a: path})
        print(f'Custo de passos: {step}')
        m.run()

    elif choose == 3:
        m = maze(r, c)
        m.CreateMaze(loopPercent=15)
        path_bfs, step_bfs = Maze(m, 'BFS')
        path_dfs, step_dfs = Maze(m, 'DFS')
        a = agent(m, footprints=True, color=COLOR.blue)
        b = agent(m, footprints=True, color=COLOR.yellow)

        m.tracePath({a: path_bfs})
        m.tracePath({b: path_dfs})
        print(f'\nCusto de passos pela BFS: {step_bfs}\nCusto de passos pela DFS: {step_dfs}')
        m.run()

    elif choose == 4:
        print('Saindo...')
        quit