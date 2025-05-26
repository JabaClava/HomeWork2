from Alg_ER import ER
from GraphPlot import graphPlot
from GraphReader import GraphReader
from IncomingDegrees import incomingDegrees
from Rationing import rationing
from average_degree import average_degree
import ugly_coder_converts as ucc
from average_in_degs import average_in_degs
from generate_graph_DPA import generate_graph_DPA

# main code for tasks num_1 - num_5
if __name__ == "__main__":


    # Task Num_1
    print("Start Task 1:")
    G = GraphReader("data.txt")
    in_deg = rationing(incomingDegrees(G), len(G))
    graphPlot(in_deg)

    # Task Num_2
    print("Start Task 2:")
    N = 10
    arr_in_deg = []
    for i in range(N):
        G_new = ER(1000, 352807 / (1000 ** 2))
        in_deg_2 = rationing(incomingDegrees(G_new), len(G_new))
        print("iteration:", i + 1)
        arr_in_deg.append(in_deg_2)
    graphPlot(average_in_degs(arr_in_deg))

    # Task Num_3
    print("Start Task 3:")
    graph = ucc.convert_bg2gg(G)
    n, m = len(graph), round(average_degree(graph))
    print(f"N:{n}| M:{m}")

    # Task Num_4
    print("Start Task 4:")
    g_graph_2 = ucc.convert_gg2bg(generate_graph_DPA(n, m))
    in_deg_3 = rationing(incomingDegrees(G), len(G))
    graphPlot(in_deg_3)