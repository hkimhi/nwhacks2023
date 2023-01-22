import json

with open("courses.json", "r") as infile:
    all_courses = json.load(infile)
    nodes = []
    edges = []

    for course in all_courses:
        node_dict = {
            'id': course['name'],
            'title': course['title'],
            'credits': course['credits'],
            'desc': course['desc']
        }
        nodes.append(node_dict)

        for prereq in course['prereqs']:
            edge_dict = {
                'source': prereq,
                'target': course['name']
            }
            edges.append(edge_dict)

        for coreq in course['coreqs']:
            edge_dict = {
                'source': coreq,
                'target': course['name']
            }
            edges.append(edge_dict)

    graph = [nodes, edges]
    # Serializing json
    graph_json = json.dumps(graph, indent=4)
    # Writing to sample.json
    with open("graph.json", "w") as outfile:
        outfile.write(graph_json)