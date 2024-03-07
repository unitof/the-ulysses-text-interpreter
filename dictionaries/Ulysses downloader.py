# (U)lysses (T)ext (I)nterperator

import urllib.request, random

def downloader():
    url = 'http://www.gutenberg.org/cache/epub/4300/pg4300.txt'

    response = urllib.request.urlopen(url)

    charactersdata = response.read().decode('utf-8')

    file_object = open('ulysses.txt','')
    for i in charactersdata:
        try:
                file_object.write(i)
        except:
                file_object.write('')

    file_object.close()

def chapter_creator(number):
    myvar = open('ulysses.txt', 'r')

    full_text = myvar.read()

    myvar.close()
    
    start = '[ '+str(number)+' ]'
    end = '[ '+str(number+1)+' ]'
    chapter_slice = full_text[full_text.find(start):full_text.find(end)]
    return chapter_slice

# import custom libraries:

myvar = open('readable_adj.txt', 'r')

adj_master = myvar.read()
adj_master = adj_master.replace("'",'')
adj_master = adj_master.replace(" ",'').lower()
adj_master = adj_master.split(',')

myvar.close()

myvar = open('readable_adverb.txt', 'r')

adverb_master = myvar.read()
adverb_master = adverb_master.replace("'",'')
adverb_master = adverb_master.replace(" ",'').lower()
adverb_master = adverb_master.split(',')

myvar.close()

myvar = open('readable_conj.txt', 'r')

conj_master = myvar.read()
conj_master = conj_master.replace("'",'')
conj_master = conj_master.replace(" ",'').lower()
conj_master = conj_master.split(',')


myvar.close()


myvar = open('readable_interjection.txt', 'r')

interjection_master = myvar.read()
interjection_master = interjection_master.replace("'",'')
interjection_master = interjection_master.replace(" ",'').lower()
interjection_master = interjection_master.split(',')


myvar.close()

myvar = open('readable_intrans.txt', 'r')

intrans_master = myvar.read()
intrans_master = intrans_master.replace("'",'')
intrans_master = intrans_master.replace(" ",'').lower()
intrans_master = intrans_master.split(',')

myvar.close()

myvar = open('readable_noun.txt', 'r')

noun_master = myvar.read()
noun_master = noun_master.replace("'",'')
noun_master = noun_master.replace(" ",'').lower()
noun_master = noun_master.split(',')

myvar.close()
myvar = open('readable_plural.txt', 'r')

plural_master = myvar.read()
plural_master = plural_master.replace("'",'')
plural_master = plural_master.replace(" ",'').lower()
plural_master = plural_master.split(',')

myvar.close()
myvar = open('readable_pronoun.txt', 'r')

pronoun_master = myvar.read()
pronoun_master = pronoun_master.replace("'",'')
pronoun_master = pronoun_master.replace(" ",'').lower()
pronoun_master = pronoun_master.split(',')

myvar.close()
myvar = open('readable_trans.txt', 'r')

trans_master = myvar.read()
trans_master = trans_master.replace("'",'')
trans_master = trans_master.replace(" ",'').lower()
trans_master = trans_master.split(',')

myvar.close()
myvar = open('readable_verb.txt', 'r')

verb_master = myvar.read()
verb_master = verb_master.replace("'",'')
verb_master = verb_master.replace(" ",'').lower()
verb_master = verb_master.split(',')

myvar.close()

def occ_gen(lst):
    dic = {}
    while len(lst) > 1:
        if lst[0] not in dic:
            dic[lst[0]]=1
        else:
            dic[lst[0]]+=1
        cleanup = lst.pop(0)
    ordered = []
    for key, value in dic.items():
        tup = (value, key)
        ordered.append(tup)
    ordered.sort()
    ordered.reverse()
    return ordered
# accepts chapter, returns list of words not sorted
def not_in(chapterX_split):
    not_words = []
    for i in chapterX_split:
        if i not in adj_master and i not in adverb_master and i not in interjection_master and i not in intrans_master and i not in trans_master and i not in noun_master and i not in plural_master and i not in pronoun_master and i not in verb_master:
            not_words.append(i)
    return not_words

##def occ_clean(lst):
##    for i in range(len(lst)):
##        v = lst[i]
##        if v[0] > 



#LETS GET STARTED!!

# Chapter 1

chapter1 = chapter_creator(1)
chapter1 = chapter1.replace(',','')
chapter1 = chapter1.replace('.','').lower()
chapter1 = chapter1.replace('-','')

chapter1_split = chapter1.split()

adj_1 = []
adverb_1 = []
interjection_1 = []
intrans_1 = []
noun_1 = []
plural_1 = []
pronoun_1 = []
trans_1 = []
verb_1 = []
conj_1 = []

for i in chapter1_split:
    if i in adj_master:
        adj_1.append(i)
    if i in adverb_master:
        adverb_1.append(i)
    if i in interjection_master:
        interjection_1.append(i)
    if i in intrans_master:
        intrans_1.append(i)
    if i in noun_master:
        noun_1.append(i)
    if i in plural_master:
        plural_1.append(i)
    if i in pronoun_master:
        pronoun_1.append(i)
    if i in trans_master:
        trans_1.append(i)
    if i in verb_master:
        verb_1.append(i)
    if i in conj_master:
        conj_1.append(i)
     

# Chapter 4

chapter4 = chapter_creator(4)
chapter4 = chapter4.replace(',','')
chapter4 = chapter4.replace('.','').lower()
chapter4 = chapter4.replace('-','')

chapter4_split = chapter4.split()

adj_4 = []
adverb_4 = []
interjection_4 = []
intrans_4 = []
noun_4 = []
plural_4 = []
pronoun_4 = []
trans_4 = []
verb_4 = []
conj_4 = []

for i in chapter4_split:
    if i in adj_master:
        adj_4.append(i)
    if i in adverb_master:
        adverb_4.append(i)
    if i in interjection_master:
        interjection_4.append(i)
    if i in intrans_master:
        intrans_4.append(i)
    if i in noun_master:
        noun_4.append(i)
    if i in plural_master:
        plural_4.append(i)
    if i in pronoun_master:
        pronoun_4.append(i)
    if i in trans_master:
        trans_4.append(i)
    if i in verb_master:
        verb_4.append(i)
    if i in conj_master:
        conj_4.append(i)





# Chapter 15

chapter15 = chapter_creator(15)
chapter15 = chapter15.replace(',','')
chapter15 = chapter15.replace('.','').lower()
chapter15 = chapter15.replace('-','')

chapter15_split = chapter15.split()

adj_15 = []
adverb_15 = []
interjection_15 = []
intrans_15 = []
noun_15 = []
plural_15 = []
pronoun_15 = []
trans_15 = []
verb_15 = []
conj_15 = []

for i in chapter15_split:
    if i in adj_master:
        adj_15.append(i)
    if i in adverb_master:
        adverb_15.append(i)
    if i in interjection_master:
        interjection_15.append(i)
    if i in intrans_master:
        intrans_15.append(i)
    if i in noun_master:
        noun_15.append(i)
    if i in plural_master:
        plural_15.append(i)
    if i in pronoun_master:
        pronoun_15.append(i)
    if i in trans_master:
        trans_15.append(i)
    if i in verb_master:
        verb_15.append(i)
    if i in conj_master:
        conj_1.append(i)



# Chapter 18

chapter18 = chapter_creator(18)
chapter18 = chapter18.replace(',','')
chapter18 = chapter18.replace('.','').lower()
chapter18 = chapter18.replace('-','')

chapter18_split = chapter18.split()

adj_18 = []
adverb_18 = []
interjection_18 = []
intrans_18 = []
noun_18 = []
plural_18 = []
pronoun_18 = []
trans_18 = []
verb_18 = []


for i in chapter18_split:
    if i in adj_master:
        adj_18.append(i)
    if i in adverb_master:
        adverb_18.append(i)
    if i in interjection_master:
        interjection_18.append(i)
    if i in intrans_master:
        intrans_18.append(i)
    if i in noun_master:
        noun_18.append(i)
    if i in plural_master:
        plural_18.append(i)
    if i in pronoun_master:
        pronoun_18.append(i)
    if i in trans_master:
        trans_18.append(i)
    if i in verb_master:
        verb_18.append(i)









