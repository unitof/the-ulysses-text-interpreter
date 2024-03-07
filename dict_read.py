# open a file for reading
dictionary_raw = open("readable_dictionary.txt", "r")

# read in all data as one long string
alldata = dictionary_raw.read()

# close the file
dictionary_raw.close()

#split data in to list of elements
for i in alldata:
    if ord(i) == 32:
        i = ''

wordsplit = alldata.split('\n')

noun_list = []
plural_list = []
verb_list = []
verb_intrans_list = []
verb_trans_list = []
pronoun_list = []
adj_list = []
interjection_list = []
adverb_list = []
conj_list = []
### swapped out "C" with "N" to create new conj list retroactively. If N needed,
#### change back! 
for word in wordsplit:
    if 'C' in word[word.find('.'):]:
    	conj_list.append(word[:word.find('.')])
##    if 'p' in word[word.find('.'):]:
##    	plural_list.append(word[:word.find('.')])
##    if 'V' in word[word.find('.'):]:
##    	verb_list.append(word[:word.find('.')])
##    if 'A' in word[word.find('.'):]:
##    	adj_list.append(word[:word.find('.')])
##    if '!' in word[word.find('.'):]:
##    	interjection_list.append(word[:word.find('.')])
##    if 'v' in word[word.find('.'):]:
##    	adverb_list.append(word[:word.find('.')])
##    if 't' in word[word.find('.'):]:
##    	verb_trans_list.append(word[:word.find('.')])
##    if 'i' in word[word.find('.'):]:
##    	verb_intrans_list.append(word[:word.find('.')])
##    if 'r' in word[word.find('.'):]:
##    	pronoun_list.append(word[:word.find('.')])
file_object = open('readable_conj.txt','w')
file_object.write(str(conj_list))
file_object.close()

##file_object = open('readable_plural.txt','w')
##file_object.write(str(plural_list))
##file_object.close()
##
##file_object = open('readable_verb.txt','w')
##file_object.write(str(verb_list))
##file_object.close()
##
##file_object = open('readable_intrans.txt','w')
##file_object.write(str(verb_intrans_list))
##file_object.close()
##
##file_object = open('readable_trans.txt','w')
##file_object.write(str(verb_trans_list))
##file_object.close()
##
##file_object = open('readable_pronoun.txt','w')
##file_object.write(str(pronoun_list))
##file_object.close()
##
##file_object = open('readable_adj.txt','w')
##file_object.write(str(adj_list))
##file_object.close()
##
##file_object = open('readable_interjection.txt','w')
##file_object.write(str(interjection_list))
##file_object.close()
##
##file_object = open('readable_adverb.txt','w')
##file_object.write(str(adverb_list))
##file_object.close()
