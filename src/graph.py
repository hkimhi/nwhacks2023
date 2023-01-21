import os
import json
from collections import deque
from helpers import Helpers
from node import Node

class Graph:    
    def __init__(self) -> None:
        self.fwd = {} # course -> post-req
        self.back = {} # course -> pre-req
        self.nodes = {} # name -> course
    """ 
    Initializes the entire graph structure and 
    Assuming:
        - no duplicates in data
    """    
    @staticmethod
    def init_graph():
        FOLDER = "/home/chris/nwhacks2023/courses/"
        file_path = Helpers.get_files_from_folder(FOLDER)
        graph = Graph()
        # get all graph data
        for f in file_path:
            with open(f, "r") as file:
                data = json.load(file)
                Graph.populate(data, graph)
        return graph

    @staticmethod
    def populate(data, graph):
        for d in data:
            if d["name"] == "PHYS 157":
                print(d)
            name = d["name"]
            if name in graph.nodes:
                continue
            graph.fwd[name] = d["postreqs"] 
            graph.back[name] = d["prereqs"]
            graph.back[name].extend(d["coreqs"])
            graph.nodes[name] = Node(name, d["credits"], d["desc"])

    def bfs(self, src, tgt, pre=False, depth=-1) -> Node:
        que = deque()
        vis = set()
        que.append(src)
        i = 0
        print(que, vis)
        while que or (depth != -1 and i > depth):
            crs = que.popleft()
            print(crs)
            if crs in vis:
                continue
            vis.add(crs)
            if crs == tgt:
                return [self.nodes[name] for name in vis]
            if pre:
                que.extend(self.back[crs])
            else:
                que.extend(self.fwd[crs])
            i += 1
        return []

def main():
    graph = Graph.init_graph()
    print(graph.fwd["PHYS 157"])
    res = graph.bfs("PHYS 157", "PHYS 158")
    print(res)
    pass

if __name__ == "__main__":
    main()