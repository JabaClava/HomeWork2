from Alg_ER import ER
from DistributionPlot import distributionPlot
from GraphPlot import graphPlot
from GraphReader import GraphReader
from IncomingDegrees import incomingDegrees
from Probability import probability
from Rationing import rationing
from average_degree import average_degree
import ugly_coder_converts as ucc
from average_in_degs import average_in_degs
from generate_graph_DPA import generate_graph_DPA
import matplotlib.pyplot as plt

# main code for tasks num_1 - num_5
if __name__ == "__main__":


    # Task Num_1
    print("Start Task 1:")
    G = GraphReader("data.txt")
    in_deg = rationing(incomingDegrees(G), len(G))
    graphPlot(in_deg, "Input Graph")
    # основанием логарифма была выбрана 2

    # Task Num_2
    print("Start Task 2:")
    N = 10
    arr_in_deg = []
    n = 27770
    p = probability(G) # вероятность добавления ребра для ER - алгоритма
    for i in range(N):
        G_new = ER(n, p)
        in_deg_2 = rationing(incomingDegrees(G_new), len(G_new))
        print("iteration:", i + 1)
        arr_in_deg.append(in_deg_2)
    graphPlot(average_in_degs(arr_in_deg), "Random Graph 1")
    distributionPlot(n, p, "Distribution")
    # Ответы на вопросы для подзадачи 2:
    # 1) График для случайного графа выглядит одинаково с графиком распределения,
    #    так как способ генерации случайный
    # 2) График для случайного и реального графа сильно отличаются из-за способа
    #    генерации, он распределяет ребра примерно одинаково и граф получается более связный
    # 3) Сходств у случайного и реального графа мало, только большое количество
    #    вершин с маленькой входящей степенью

    # Task Num_3
    print("Start Task 3:")
    graph = ucc.convert_bg2gg(G)
    n, m = len(graph), round(average_degree(graph))
    print(f"N:{n}| M:{m}")
    # n = 27770; m = 13

    # Task Num_4
    print("Start Task 4:")
    g_graph_2 = ucc.convert_gg2bg(generate_graph_DPA(n, m))
    in_deg_3 = rationing(incomingDegrees(g_graph_2), len(g_graph_2))
    graphPlot(in_deg_3, "Random Graph 2")

    # Task Num_5
    # 1) Графики для случайного графа и реального графа похожи своим поведениям,
    # но немного отличаются значениями
    # 2) Алгоритм DPA подражает феномену иерархической структуры сетей, так как
    # есть начальный кластер вершин, из него появляются ребра в другие вершины,
    # и вокруг них начинают образовываться свои кластеры вершин и так далее
    # 3) Феномен иерархической структуры сетей объясняет структуру графа цитирований,
    # потому что из большой группы авторов статей явно есть группа наиболее
    # авторитетных, на кого из них ссылаются группы менее авторитетных авторов
    # и так далее, так и получается данная структура

    plt.legend()
    plt.show()