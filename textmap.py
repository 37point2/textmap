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

    return {file: tags}

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
        print result
        for file,tags in result:
            print file, tags
            for tag in tags:
                try:
                    node = graph.getOrAddNode(tag)
                    node.addTag(file)
                    graph.updateEdges(node,tag)
                except Exception as e:
                    print e

    print graph.getNodes()


if __name__ == "__main__":
    main(sys.argv[1])