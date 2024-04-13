from agents.rational_agent import RationalAgent

# O agente baseado em utilidade sabe onde os itens estão no mapa
# ele move-se em direção aos itens que estão mais perto no menor caminho possível
# ele prioriza os itens de maior valor primeiro
class UtilityAgent(RationalAgent):
    def __init__(self, map, limit):
        super().__init__(map, limit)

    def move(self, goal): # Se move no menor percurso possível para chegar no item
        current_x, current_y = self.position
        goal_x, goal_y = goal

        while current_x != goal_x:
            if current_x < goal_x:
                self.down()
                current_x += 1
            else:
                self.up()
                current_x -= 1

        while current_y != goal_y:
            if current_y < goal_y:
                self.right()
                current_y += 1
            else:
                self.left()
                current_y -= 1

    def read_map(self): # Lê o mapa e retorna as coordenadas dos itens em ordem de valor de pontos
        items1 = []
        items2 = []

        for i in range(self.map.size):
            for j in range(self.map.size):
                if self.map.grid[i][j] != ' ':
                    if self.map.grid[i][j] == '1':
                        items1.append((i, j))
                    if self.map.grid[i][j] == '2':
                        items2.append((i, j))

        # Retorna as coordenadas dos itens em ordem de distância
        items1 = sorted(items1, key=sum)
        items2 = sorted(items2, key=sum)

        return items2 + items1

    def search_item(self):
        goals = self.read_map()
        loop = True

        while loop:
                for goal in goals:
                    if self.countItems != self.limit:
                        self.move(goal)
                        self.grab_item(self.position_content)
                        print("Item encontrado! Voltando para a posição inicial...")
                        self.back_initial_position()
                        self.drop_item()
                        self.countPoints()
                        print("Pontos: {}\n".format(self.points))
                        self.map.print_map()
                        print("")
                    else:
                        self.noOp()
                        loop = False