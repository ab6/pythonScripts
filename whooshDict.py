from whoosh import spelling
from whoosh.filedb.filestore import FileStorage

wordfile = open("/Users/amckenzie/Documents/data/scowl-7.1/final/english-words.60")

# Use a Storage object to get a file to write the graph into 
st = FileStorage("/Users/amckenzie/Tools/pythonScripts") 
f = st.create_file("wordgraph") 

# Write a graph of the words into the file 
spelling.wordlist_to_graph_file(wordfile, f) 

# Create a graph reader from the file and wrap it with a corrector 
f = st.open_file("wordgraph") 
gr = fst.GraphReader(f) 
cor = spelling.GraphCorrector(gr) 

# See docs for whoosh.spelling.Corrector.suggest() 
cor.suggest("aple")