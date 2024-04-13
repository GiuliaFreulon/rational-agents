from agents.rational_agent import RationalAgent
import random

# O agente baseado em modelos/estados tem um mapa interno por onde já passou e evita repetir os mesmos caminhos
# caso encontre um item ele o pega e o coloca na posição inicial
class StateAgent(RationalAgent):
    def __init__(self, map, limit):
        super().__init__(map, limit)
        self.internMap = set()

    def move(self):
        randomDirections = []
        directions = []

        if self.position[0] > 0:
            randomDirections.append("U")
            if (self.position[0] - 1, self.position[1]) not in self.internMap:
                directions.append("U")

        if self.position[0] < self.map.size - 1:
            randomDirections.append("D")
            if (self.position[0] + 1, self.position[1]) not in self.internMap:
                directions.append("D")

        if self.position[1] > 0:
            randomDirections.append("L")
            if (self.position[0], self.position[1] - 1) not in self.internMap:
                directions.append("L")

        if self.position[1] < self.map.size - 1:
            randomDirections.append("R")
            if (self.position[0], self.position[1] + 1) not in self.internMap:
                directions.append("R")

        if directions:
            direction = random.choice(directions)
        else:
            direction = random.choice(randomDirections) # Caso ele já tenha passado por todas as direções possiveis

        if(direction == "U"):
            self.up()
            return
        if(direction == "D"):
            self.down()
            return
        if(direction == "L"):
            self.left()
            return
        if(direction == "R"):
            self.right()
            return

    def search_item(self):
        while True:
            if self.countItems != self.limit:
                if self.position_content == ' ':
                    self.internMap.add(self.position)
                    self.move()
                else:
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
                return