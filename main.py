import copy, time

from environment.map import Map

from agents.simple_agent import SimpleAgent
from agents.state_agent import StateAgent
from agents.goal_agent import GoalAgent
from agents.utility_agent import UtilityAgent

def main():
    print("\n--- AGENTES RACIONAIS ---\n")

    # Variáveis
    size = 20
    items1 = 5
    items2 = 5
    limit = 5

    # Gerando mapa e itens
    map = Map(size)
    map.generate_items(items1, items2)

    print("\n- Agente Reativo Simples - \n")
    map_copy = copy.deepcopy(map)
    print("Mapa inicial:")
    map.print_map()
    print()
    agent1 = SimpleAgent(map_copy, limit)
    begin_agent1 = time.time()
    agent1.search_item()
    end_agent1 = time.time()
    time_agent1 = end_agent1 - begin_agent1
    print("- Fim Agente Reativo Simples - \n")

    print("\n- Agente Reativo Baseado em Modelos - \n")
    map_copy = copy.deepcopy(map)
    print("Mapa inicial:")
    map.print_map()
    print()
    agent2 = StateAgent(map_copy, limit)
    begin_agent2 = time.time()
    agent2.search_item()
    end_agent2 = time.time()
    time_agent2 = end_agent2 - begin_agent2
    print("- Fim Agente Reativo Baseado em Modelos - \n")

    print("\n- Agente Reativo Baseado em Objetivos - \n")
    map_copy = copy.deepcopy(map)
    print("Mapa inicial:")
    map.print_map()
    print()
    agent3 = GoalAgent(map_copy, limit)
    begin_agent3 = time.time()
    agent3.search_item()
    end_agent3 = time.time()
    time_agent3 = end_agent3 - begin_agent3
    print("- Fim Agente Reativo Baseado em Objetivos - \n")

    print("\n- Agente Reativo Baseado em Utilidade - \n")
    map_copy = copy.deepcopy(map)
    print("Mapa inicial:")
    map.print_map()
    print()
    agent4 = UtilityAgent(map_copy, limit)
    begin_agent4 = time.time()
    agent4.search_item()
    end_agent4 = time.time()
    time_agent4 = end_agent4 - begin_agent4
    print("- Fim Agente Reativo Baseado em Utilidade - \n")

    print("\n- Agente Reativo Simples -")
    print("Tempo gasto: {:.6f} segundos".format(time_agent1))
    print("Pontos: {}\n".format(agent1.points))

    print("- Agente Reativo Baseado em Modelos -")
    print("Tempo gasto: {:.6f} segundos".format(time_agent2))
    print("Pontos: {}\n".format(agent2.points))

    print("- Agente Reativo Baseado em Objetivos -")
    print("Tempo gasto: {:.6f} segundos".format(time_agent3))
    print("Pontos: {}\n".format(agent3.points))

    print("- Agente Reativo Baseado em Utilidade -")
    print("Tempo gasto: {:.6f} segundos".format(time_agent4))
    print("Pontos: {}\n".format(agent4.points))

if __name__ == "__main__":
    main()