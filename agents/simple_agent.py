from agents.rational_agent import RationalAgent
import random

# O agente simples anda em direções aleatórias
# caso encontre um item ele o pega e o coloca na posição inicial
class SimpleAgent(RationalAgent):
    def __init__(self, map, limit):
        super().__init__(map, limit)

    def move(self):
        directions = []
        if self.position[0] > 0:  # Verifica se não está na borda superior
            directions.append("U")
        if self.position[0] < self.map.size - 1:  # Verifica se não está na borda inferior
            directions.append("D")
        if self.position[1] > 0:  # Verifica se não está na borda esquerda
            directions.append("L")
        if self.position[1] < self.map.size - 1:  # Verifica se não está na borda direita
            directions.append("R")
        if directions:
            direction = random.choice(directions)
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
                if self.position_content == ' ': # Verifica se há um item na posição atual
                    self.move()
                else:
                    self.grab_item(self.position_content)  # Pega o item
                    print("Item encontrado! Voltando para a posição inicial...")
                    self.back_initial_position()  # Retorna para a posição inicial
                    self.drop_item() # Solta o item na posição inicial
                    self.countPoints()
                    print("Pontos: {}\n".format(self.points))
                    self.map.print_map()
                    print("")
            else:
                self.noOp()
                return