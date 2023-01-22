import os
import json
from collections import deque
from helpers import Helpers
from node import Node
from copy import copy

class Graph:    
    def __init__(self) -> None:
        self.fwd = {} # course -> post-req
        self.back = {} # course -> pre-req
        self.nodes = {} # name -> course

    @staticmethod
    def init_graph():
        """Initializes the Graph structure

        Returns:
            Graph: graph consisting of all courses
        """
        file_path = "/home/chris/nwhacks2023/courses.json"
        graph = Graph()
        # get all graph data
        with open(file_path, "r") as file:
            data = json.load(file)
            Graph.populate(data, graph)
        return graph

    @staticmethod
    def populate(data, graph):
        """Populates the graph with courses

        Args:
            data (Any): object representing data from a json file
            graph (Graph): Graph to populate data onto
        """
        for d in data:
            name = d["name"]
            if name in graph.nodes:
                continue
            graph.fwd[name] = set(d["postreqs"])
            graph.back[name] = set(d["prereqs"])
            graph.back[name].update(d["coreqs"])
            graph.nodes[name] = Node(name, d["credits"], d["desc"])

    def bfs(self, src, tgt, pre=True, depth=-1):
        que = deque()
        vis = set()
        que.append(src)
        i = 0
        while que or (depth != -1 and i > depth):
            crs = que.popleft()
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
        
    def findAllPaths(self, src, tgt, pre=False):
        """Finds all paths between the source and target courses.

        Args:
            src (str): name of course to start traversal
            tgt (str): name of course to reach through traversal
            pre (bool, optional): True if traversal goes backwawrds (i.e. towards pre-reqs). Defaults to False.

        Returns:
            set[tuple[str, str]]: A set of tuples of two course codes, representing an edge, that is visited throughout traversal.
        """        
        valid_paths = set()
        self.__findAllPathsInner(src, tgt, [], set(), valid_paths, pre)
        return valid_paths

    def __findAllPathsInner(self, src, tgt, curr_path, curr_path_set, valid_paths, pre=False):
        # base
        if src == tgt:
            valid_paths.update(copy(curr_path))
            return
        if src not in self.nodes:
            courses = set()
        else:
            courses = self.back[src] if pre else self.fwd[src]
        curr_path_set.add(src)
        for crs in courses:
            curr_path.append((src,crs))
            if crs not in curr_path_set:
                self.findAllPathsInner(crs, tgt, curr_path, curr_path_set, valid_paths, pre)
                del curr_path[-1]

def main():
    graph = Graph.init_graph()
    # src = "MATH 100"
    # tgt = "CPSC 221"
    tgt = "MATH 100"
    src = "CPSC 221"
    res = graph.findAllPaths(src, tgt, pre=True)
    print("\n")
    print(res)
    pass

if __name__ == "__main__":
    main() 