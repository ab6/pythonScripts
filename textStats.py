#Requires nltk and several nltk.data downloads which can be done by import nltk and then 
#nltk.download()
from __future__ import division
import nltk
import argparse
import nltk.data
import spellCheck
from spellCheck import correct

parser = argparse.ArgumentParser(description='Provide basic text statistics.')
parser.add_argument('inputFile', help='Plain text input file path.')

args = parser.parse_args()

inputFile = args.inputFile

text = open(inputFile, 'r').read()
words = text.split()

#Total words
totalWords = len(words)
print("Total words - " + str(totalWords))

#Total tokens
tokens = nltk.word_tokenize(text)
print("Total tokens - " + str(len(tokens)))

#Numbers of unique words
uniqueWords = len(set(words))
print("Unique words - " + str(uniqueWords))

#Ratio of unique words to total words
ratio = uniqueWords/totalWords
print("Ratio of unique words to total words - " + str(ratio))

#Average word length
avgWord = 0
for word in words:
	avgWord += len(word)
print ("Average word length - " + str(avgWord/len(words)) + " characters")

#Numbers of sentences
sent_det = nltk.data.load('tokenizers/punkt/english.pickle')
sentences = sent_det.tokenize(text.strip())
print ("Sentences - " + str(len(sentences)))

#Average length of sentences
avgSent = 0
for sentence in sentences:
	avgSent += len(sentence.split())
print ("Average sentence length - " + str(avgSent/len(sentences)) + " words")

#Number of misspelled words
misspells = 0
listUnique = list(set(words))
for word in listUnique[0:5]:
    if cmp(word, correct(word)) is not 0:
        misspells += 1
        print (word + " " + correct(word))
print ("Number of misspelled words: " + str(misspells))
print ("Percent misspelled: " + str(misspells/len(words)*100) + "%")

#Entities
def extract_entity_names(t):
    entity_names = []
    
    if hasattr(t, 'node') and t.node:
        if t.node == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
                
    return entity_names

#tagged = nltk.pos_tag(tokens)
#entities = nltk.chunk.ne_chunk(tagged)
# tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
# tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
# chunked_sentences = nltk.batch_ne_chunk(tagged_sentences, binary=True)
# entity_names = []
# for tree in chunked_sentences:
# 	entity_names.extend(extract_entity_names(tree))
# print ("Unique Entities - " + str(len(set(entity_names))))
# print ("Total Entities - " + str(len(entity_names)))
# print (set(entity_names))

