import sys
import os
import multiprocessing
import nlp
from graph import Graph


def process_text((file, text)):
    tags = []

    [tags.append(x) for x in nlp.bigrams(text)]
    [tags.append(x) for x in nlp.trigrams(text)]
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

    for result in results:
        file, tags = result
        edges = [' '.join(tag) if not isinstance(tag, str) else tag for tag in tags]
        for tag in tags:
            if not isinstance(tag, str):
                name = ' '.join(tag)
            else:
                name = tag
            try:
                node = graph.getOrAddNode(name)
                node.addTag(file)
                for edge in edges:
                    graph.updateEdges(node,edge)
            except Exception as e:
                print e

    for node in  graph.getNodes():
        print node.name, node.getEdges(), node.getTags()


if __name__ == "__main__":
    main(sys.argv[1])