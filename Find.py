import spacy


comand = input()#$ python ./constitution_helper.py find "The republic of Armenia"


def read_constitution(comand):
    comand = comand.split()
    if comand[0] == '$' and comand[1] == 'python' and comand[2] == './constitution_helper.py' and comand[3] == 'find':
        search_text = comand [4:]
        search_text [0] = search_text [0][1:]
        search_text [-1] = search_text [-1][:-1]
        return search_text
    raise RuntimeError('Invalid Input')

search_text = read_constitution(comand)

def constitution_helper():

    text = open("Constitution.txt", encoding="utf8")
    text = text.read()
    text = text.replace("\n"," ")
    return text

text = constitution_helper()

def search_similar_words(text, search_text):
    # load the model
    nlp = spacy.load("en_core_web_lg")
    # internal information extraction
    doc = nlp(text)
    similar_words = set()
    for token in doc:
        for word in search_text:
            similarity = token.similarity(nlp(word))
            if similarity > 0.6:  # Adjust the threshold as needed
                similar_words.add(token.text)
    return similar_words

similar_words = search_similar_words(text,search_text)


def split_into_sentences(text) :

    text = text.replace(".","<stop>")
    sentences = text.split("<stop>")
    sentences = [s.strip() for s in sentences]
    if sentences and not sentences[-1]:
         sentences = sentences[:-1]
    return sentences

text = split_into_sentences(text)

matching_sentences = []
len = len(search_text)
enumerate_Sentences = []

def enumerateSentences(len):

    for sentnece in text:
        count = 0
        for word in similar_words:
            if word in sentnece:
                count += 1
        if count > 0:
            matching_sentences.append((count,sentnece))
    
    count = 1
    
    for sentence in matching_sentences:
        for y in matching_sentences:
            if y[0] == len:
                enumerate_Sentences.append((count,y))
                count += 1
        if len == 1:
            break
        len -= 1



enumerateSentences(len)

print(enumerate_Sentences)

        