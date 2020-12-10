import networkx as nx

def main():

    input = open("input", "r")
    luggage_list = input.read().splitlines()

    partOne(luggage_list)
    
def partOne(luggage_list):
    G = nx.DiGraph()
    for luggage in luggage_list:
        #get the bag and a string of the contains
        bag,contains = luggage.strip().rstrip(".").split(" bags contain ")
        print(bag)
        print(contains)

        #this is a single bag, likely a solo node or the end of the graph
        if contains == "no other bags":
            continue

        for other in contains.split(", "):
            count = int(other[0])
            other = other[2:].rstrip("bags").strip()
            G.add_edge(bag, other, count=count)
    # stole this from reddit, im not smart enough for graphs.
    print("Part 1:", len(list(nx.dfs_postorder_nodes(G.reverse(), "shiny gold"))) - 1)
    for node in nx.dfs_postorder_nodes(G, "shiny gold"):
        G.nodes[node]["count"] = sum((G.nodes[n]["count"] + 1) * v["count"] for (n, v) in G[node].items())

    print("Part 2:", G.nodes["shiny gold"]["count"])


class LuggageNode:
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    main()
