from GraphReader import GraphReader
from average_degree import average_degree
import ugly_coder_converts as ucc

if __name__ == "__main__":

    # Task Num_3
    graph = ucc.convert_bg2gg(GraphReader("data.txt"))
    print(f"N:{len(graph)}| M:{round(average_degree(graph))}")