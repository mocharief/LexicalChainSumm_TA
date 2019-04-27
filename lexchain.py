def build_chains():

def build_segment_chain():

def components_relatedtoword(components, word):

def merge_components(components):

def split_interpretation(word, interp):

max_active_interpretations = 10

def interpretation_score(interp):
    # 10 if they are synonyms;
    # 8 if they are offsprings;
    # 7 if they are antonyms;
    # 4 if they are meronyms;
    # 2 if they are siblings.
    # reiteration dan sinonim sebesar 10, antonim sebesar 7, hiponim dan hipernim sebesar 4.
def merge_segment_chains(segments_chains):

