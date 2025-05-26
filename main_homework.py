from GraphReader import GraphReader
from average_degree import average_degree
import ugly_coder_converts as ucc
from generate_graph_DPA import generate_graph_DPA

if __name__ == "__main__":

    # Task Num_3
    graph = ucc.convert_bg2gg(GraphReader("data.txt"))
    n, m = len(graph), round(average_degree(graph))
    print(f"N:{n}| M:{m}")

    # Task Num_4
    g_graph_2 = ucc.convert_gg2bg(generate_graph_DPA(n, m))
