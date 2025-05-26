from GraphPlot import graphPlot
from GraphReader import GraphReader
from IncomingDegrees import incomingDegrees
from Rationing import rationing
from average_degree import average_degree
import ugly_coder_converts as ucc

if __name__ == "__main__":

    # Task Num_1
    G = GraphReader("data.txt")
    in_deg = rationing(incomingDegrees(G), len(G))
    graphPlot(in_deg)

    # Task Num_3
    graph = ucc.convert_bg2gg(G)
    print(f"N:{len(graph)}| M:{round(average_degree(graph))}")