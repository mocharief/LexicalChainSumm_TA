import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet as wn
import codecs
from neo4jrestclient.client import GraphDatabase

# //-----------------------------------------------Global variable-------------------------------------------------------\\
db = GraphDatabase("http://localhost:7474", username="boyan", password="boy123")
wn_lemmas = set(wn.all_lemma_names()) # untuk pengecekkan kata apabila tidak ada pada wordnet

# //-----------------------------------------------Function-------------------------------------------------------\\
def open_file(text) :
    with codecs.open(text, 'r', encoding='utf8') as f:
        source_text = f.read()
        # print(source_text)
        return source_text

def sentences(source_text) :
    # if source_text == None
    #     print("File not found")
    #     exit()
    # else
        sentence_list = sent_tokenize(source_text)
        # print(sentence_list)
        return sentence_list

def candidate_set(source_text) :
    # if source_text == None
    #     print("File not found")
    #     exit()
    # else
        list_postag = nltk.pos_tag(word_tokenize(source_text))
        #print(list_postag)
        nouns = [token for token, pos in list_postag if pos.startswith('N')]
        return nouns
        #print('Candidate Set : \n', nouns)

# print(sentences(open_file('source.txt')))
# print(word_tokenize(open_file('source.txt')))
# print(candidate_set(open_file('source.txt')))

# -------------Penambahan informasi letak kalimat dengan kata yang ada di anggota candidate set----------------------
# sent_list = sentences(open_file('source.txt'))
# nouns = [[], []]
# for idx, sentence in enumerate(sent_list):
#     for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
#         if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
#             nouns[0].append(word)
#             nouns[1].append(idx)

# for idx, val in enumerate(nouns[0]):
#     print('kata', '"', nouns[0][idx], '"', 'terdapat pada kalimat : ', sent_list[nouns[1][idx]] )
# print(nouns[0][1], nouns[1][1], sent_list[1])

# //-----------------------------------------------SENSE_KATA-------------------------------------------------------\\

# candidate = candidate_set(open_file('source2.txt'))
# print(candidate)
# i = 0
# list_sense = {}
# while i < len(nouns):
#     for ss in wn.synsets(nouns[i], pos='n'):
#         list_sense = {
#             "noun": nouns[i],
#             "synset": ss.name(),
#             "lemma": ss.lemma_names(),
#             "definition": ss.definition(),
#             "hypernyms": ss.hypernyms()
#         }
#         print(list_sense)
#     i += 1

# //------------------- PENGECEKKAN KATA YANG ADA PADA LEMMA SYNSET

def identifikasiSyn(word, word1): # Output berupa boolean apakah dua kata tersebut terikat synonim atau tidak
    # if word in wn_lemmas:
    #     if word1 in wn_lemmas:
    for ss in wn.synsets(word, pos='n'): #pos='n' untuk mengambil synset yang merupakan noun (karena ada dua yaitu noun dan verb)
        lemmas = ss.lemmas()
        for l in lemmas:
            if l.name() == word1:
                return True
    # else:
    #     return False

def identifikasiHip(word, word1): # Output berupa nilai terbesar dari semua nilai hipernim dari dua kata
    value = []
    # if word in wn_lemmas:
    #     if word1 in wn_lemmas:
    for s1 in wn.synsets(word, pos='n'):
        # print(s1)
        for s2 in wn.synsets(word1, pos='n'):
            # print(s2)
            similarity = wn.path_similarity(s1, s2)
            value.append(similarity)
            # print('value', s1, 'and', s2, '=', similarity)
    return max(value)
    # else:
    #     return 0

# //------------------- CARA AMBIL MERONIM/HOLONIM
# car = wn.synset('car.n.01')
# cc = car.part_meronyms()
# # print(cc)
# for synset in cc:
#     print(synset.name().split('.')[0])

# //------------------- MENGIDENTIFIKASI SHORTEST PATH DAN INTERSECTION DARI SYNSET DEFINITIOIN
#person = wn.synset('person.n.01')
#machine = wn.synset('machine.n.02')
#tax_dis = person.shortest_path_distance(machine)
#comm_lemmas = len(set(person.lemma_names()).intersection(set(machine.definition())))

# //--------------------------------------------- MAIN_FUNCTION -----------------------------------------------------\\

candidate = ['Mr.', 'person', 'machine', 'device', 'individual', 'car']
# print(identifikasiHip('Kenny', 'python'))
# print(candidate)

# //---------------------- Node dibuat berdasarkan anggota candidate set
# word = db.labels.create("Word")
# for noun in candidate:
#     if noun in wn_lemmas:
        # print(noun)
        # word.add(db.nodes.create(word=noun))
# Node dibuat berdasarkan anggota candidate set ----------------------\\


# //---------------------- Pengecekkan Relasi antar 2 kata dan add ke graph
# i = 0
# j = 0
# simiprev = 0
# while i < (len(candidate)):
#     j = i + 1
#     while j < len(candidate):
#         if identifikasiSyn(candidate[i], candidate[j]) == True:
#             for p in word.get(word=candidate[i]):
#                 for w2 in word.get(word=candidate[j]):
#                     p.Syno(w2)
#                     print('add syno success')
#             # print(candidate[i], 'to', candidate[j], 'is Synonim adding Succes')
#         elif 0 < identifikasiHip(candidate[i], candidate[j]) <= 1:
#             similarity = identifikasiHip(candidate[i], candidate[j])
#             # if similarity != 0:
#             if simiprev <= similarity:
#                 for p in word.get(word=candidate[i]):
#                     for w2 in word.get(word=candidate[j]):
#                         p.Hypo_Hype(w2)
#                         w2.Hypo_Hype(p)
#                         print('add hypo_hype success')
#                         simiprev = similarity
#             # print(candidate[i], 'to', candidate[j], 'is Hipernim', '[value = ', similarity, '] adding Succes')
#         j += 1
#     i += 1
# Pengecekkan Relasi antar 2 kata dan add ke graph ----------------------\\
