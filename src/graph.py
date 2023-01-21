import os
import json
from collections import deque
from helpers import Helpers
from node import Node

class Graph:    
    def __init__(self) -> None:
        self.fwd = {} # course -> post-req
        self.back = {} # course -> pre-req
        nodes = {} # name -> course

    """ 
    Initializes the entire graph structure and 
    Assuming:
        - no duplicates in data
    """    
    @staticmethod
    def init_graph():
        FOLDER = ""
        file_path = Helpers.get_files_from_folder(FOLDER)
        graph = Graph()
        # get all graph data
        for f in file_path:
            with open(f, "r") as file:
                data = json.load(file)
                Graph.populate(data, graph)
    
    @staticmethod
    def populate(data, graph):
        for d in data:
            name = d["name"]
            if name in graph.nodes:
                continue
            graph.fwd[name] = d["postreqs"] 
            graph.back[name] = d["prereqs"]
            graph.back[name].extend(d["coreqs"])
            graph.nodes[name] = Node(name, d["cred"], d["desc"])

    def bfs(self, src, tgt, pre=False, depth=-1) -> Node:
        que = deque(src)
        vis = set(src)
        i = 0
        while not que or (depth != -1 and i > depth):
            crs = que.popleft()
            if crs in vis:
                continue
            if crs == tgt:
                return [self.nodes[name] for name in vis]
            if pre:
                que.extend(self.back[crs])
            else:
                que.extend(self.fwd[crs])
            i += 1
        return []
