import sys
import os
import json
import multiprocessing
import SimpleHTTPServer
import SocketServer
import nlp
from graph import Graph


def process_text((file, text)):
    tags = []

    #[tags.append(x) for x in nlp.bigrams(text)]
    #[tags.append(x) for x in nlp.trigrams(text)]
    [tags.append(x) for x in nlp.extract_named_entities(text)]

    return (file, tags)

def main(dir):
    print "yolo"

    pool = multiprocessing.Pool(processes=4)

    jobs = []

    graph = Graph()

    for (root, directories, files) in os.walk(dir):
        for file in files:
            print file

            text = open(os.path.join(root, file), 'r').read()

            jobs.append((file, text))

    results = pool.map(process_text, jobs)

    pool.terminate()

    for result in results:
        file, tags = result
        edges = [' '.join(tag) if not isinstance(tag, str) else tag for tag in tags]
        for name in edges:
            try:
                node = graph.getOrAddNode(name)
                graph.updateEdges(node, file)
            except Exception as e:
                print e

    for node in graph.getNodes():
        print node.name, node.getEdges()

    nodes = []
    edges = []

    for node in graph.getNodes():
        nodes.append({'name':node.getName(),'id':graph.getNodeIndex(node)})
        for k, v in node.getEdges().items():
            edges.append({'source':graph.getNodeIndex(node),'target':k, 'weight':v})

    out = open('data.json','w')
    data = json.dumps({'nodes':nodes,'links':edges})
    out.write(data)
    out.close()

    print "http://127.0.0.1:8000"

    port = 8000
    handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", port), handler)
    httpd.serve_forever()


if __name__ == "__main__":
    main(sys.argv[1])