from DPATrialClass import DPATrial

def generate_graph_DPA(n, m):
    DPAtrial = DPATrial(m)
    g_graph_2 = {}
    for i in range(m):
        g_graph_2[i] = set(range(i)) | set(range(i + 1, m))
    for i in range(m, n):
        g_graph_2[i] = DPAtrial.run_trial(m)
    return g_graph_2