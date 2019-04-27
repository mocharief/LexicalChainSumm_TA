from nltk.corpus import wordnet as wn
from neo4jrestclient.client import GraphDatabase
# from py2neo import Graph, Node

# graph = Graph(host="localhost")
# graph.delete_all()
# w = Node("Lexical", word="person")
# graph.create(w)

db = GraphDatabase("http://localhost:7474", username="boyan", password="boy123")
#
# create some nodes with labels
word = db.labels.create("Word")
w1 = db.nodes.create(word="Mr.")
w2 = db.nodes.create(word="person")
w3 = db.nodes.create(word="machine")
w4 = db.nodes.create(word="microcomputer")
w5 = db.nodes.create(word="device")
w6 = db.nodes.create(word="pump")
w7 = db.nodes.create(word="Mr.")
word.add(w1, w2, w3, w4, w5, w6,w7)

# Relation
# w1.relationships.create("medium-strong", w2)
# w3.relationships.create("strong", w4)
# w3.relationships.create("strong", w5)
# w3.relationships.create("strong", w6)
# w4.relationships.create("strong", w5)
# w4.relationships.create("strong", w6)
# w5.relationships.create("strong", w6)

w1.Synonim(w2)
w1.Hypo_hyper(w3)