# (U)lysses (T)ext (I)nterpreter

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



###LETS GET STARTED!!
##
### Chapter 1

chapter1 = chapter_creator(1)
chapter1 = chapter1.replace(',','')
chapter1 = chapter1.replace('.','').lower()
chapter1 = chapter1.replace('-','')

chapter1_split = chapter1.split()
##
##adj_1 = []
##adverb_1 = []
##interjection_1 = []
##intrans_1 = []
##noun_1 = []
##plural_1 = []
##pronoun_1 = []
##trans_1 = []
##verb_1 = []
##conj_1 = []
##
##for i in chapter1_split:
##    if i in adj_master:
##        adj_1.append(i)
##    if i in adverb_master:
##        adverb_1.append(i)
##    if i in interjection_master:
##        interjection_1.append(i)
##    if i in intrans_master:
##        intrans_1.append(i)
##    if i in noun_master:
##        noun_1.append(i)
##    if i in plural_master:
##        plural_1.append(i)
##    if i in pronoun_master:
##        pronoun_1.append(i)
##    if i in trans_master:
##        trans_1.append(i)
##    if i in verb_master:
##        verb_1.append(i)
##    if i in conj_master:
##        conj_1.append(i)
##     
##
### Chapter 4
##
chapter4 = chapter_creator(4)
chapter4 = chapter4.replace(',','')
chapter4 = chapter4.replace('.','').lower()
chapter4 = chapter4.replace('-','')

chapter4_split = chapter4.split()
##
##adj_4 = []
##adverb_4 = []
#interjection_4 = []
##intrans_4 = []
##noun_4 = []
##plural_4 = []
##pronoun_4 = []
##trans_4 = []
##verb_4 = []
##conj_4 = []
##
##for i in chapter4_split:
##    if i in adj_master:
##        adj_4.append(i)
##    if i in adverb_master:
##        adverb_4.append(i)
##    if i in interjection_master:
##        interjection_4.append(i)
##    if i in intrans_master:
##       intrans_4.append(i)
##    if i in noun_master:
##        noun_4.append(i)
##    if i in plural_master:
##        plural_4.append(i)
##    if i in pronoun_master:
##        pronoun_4.append(i)
##    if i in trans_master:
##        trans_4.append(i)
##    if i in verb_master:
##        verb_4.append(i)
##    if i in conj_master:
##        conj_4.append(i)
##
##
##
##
##
### Chapter 15
##
chapter15 = chapter_creator(15)
chapter15 = chapter15.replace(',','')
chapter15 = chapter15.replace('.','').lower()
chapter15 = chapter15.replace('-','')

chapter15_split = chapter15.split()
##
##adj_15 = []
##adverb_15 = []
#interjection_15 = []
##intrans_15 = []
##noun_15 = []
##plural_15 = []
##pronoun_15 = []
##trans_15 = []
##verb_15 = []
##conj_15 = []
##
#for i in chapter15_split:
##    if i in adj_master:
##        adj_15.append(i)
##    if i in adverb_master:
##        adverb_15.append(i)
##    if i in interjection_master:
##        interjection_15.append(i)
##    if i in intrans_master:
##        intrans_15.append(i)
##    if i in noun_master:
##        noun_15.append(i)
##    if i in plural_master:
##        plural_15.append(i)
##    if i in pronoun_master:
##        pronoun_15.append(i)
##    if i in trans_master:
##        trans_15.append(i)
##    if i in verb_master:
##        verb_15.append(i)
##    if i in conj_master:
##        conj_1.append(i)
##
##
##
# Chapter 18

chapter18 = chapter_creator(18)
chapter18 = chapter18.replace(',','')
chapter18 = chapter18.replace('.','').lower()
chapter18 = chapter18.replace('-','')

chapter18_split = chapter18.split()
##
##adj_18 = []
##adverb_18 = []
##interjection_18 = []
##intrans_18 = []
##noun_18 = []
##plural_18 = []
##pronoun_18 = []
##trans_18 = []
##verb_18 = []
##
##
##for i in chapter18_split:
##    if i in adj_master:
##        adj_18.append(i)
##    if i in adverb_master:
##        adverb_18.append(i)
##    if i in interjection_master:
##        interjection_18.append(i)
##    if i in intrans_master:
##        intrans_18.append(i)
##    if i in noun_master:
##        noun_18.append(i)
##    if i in plural_master:
##        plural_18.append(i)
##    if i in pronoun_master:
##        pronoun_18.append(i)
##    if i in trans_master:
##        trans_18.append(i)
##    if i in verb_master:
##        verb_18.append(i)
##
###write files 
##file_object = open('adj1.txt','w')
##file_object.write(str(adj_1))
##file_object.close()
##
##file_object = open('adj4.txt','w')
##file_object.write(str(adj_4))
##file_object.close()
##
##file_object = open('adj15.txt','w')
##file_object.write(str(adj_15))
##file_object.close()
##
##file_object = open('adj18.txt','w')
##file_object.write(str(adj_18))
##file_object.close()
### adverbs
##file_object = open('adverb1.txt','w')
##file_object.write(str(adverb_1))
##file_object.close()
##
##file_object = open('adverb4.txt','w')
##file_object.write(str(adverb_4))
##file_object.close()
##
##file_object = open('adverb15.txt','w')
##file_object.write(str(adverb_15))
##file_object.close()
##
##file_object = open('adverb18.txt','w')
##file_object.write(str(adverb_18))
##file_object.close()
##
### intrans
##file_object = open('intrans1.txt','w')
##file_object.write(str(intrans_1))
##file_object.close()
##
##file_object = open('intrans4.txt','w')
##file_object.write(str(intrans_4))
##file_object.close()

##file_object = open('intrans15.txt','w')
##file_object.write(str(intrans_15))
##file_object.close()
##
##file_object = open('intrans18.txt','w')
##file_object.write(str(intrans_18))
##file_object.close()
##
### trans
##file_object = open('trans1.txt','w')
##file_object.write(str(trans_1))
##file_object.close()
##
##file_object = open('trans4.txt','w')
##file_object.write(str(trans_4))
##file_object.close()
##
##file_object = open('trans15.txt','w')
##file_object.write(str(trans_15))
##file_object.close()
##
##file_object = open('trans18.txt','w')
##file_object.write(str(trans_18))
##file_object.close()
##
### noun
##file_object = open('noun1.txt','w')
##file_object.write(str(noun_1))
##file_object.close()
##
##file_object = open('noun4.txt','w')
##file_object.write(str(noun_4))
##file_object.close()
##
##file_object = open('noun15.txt','w')
##file_object.write(str(noun_15))
##file_object.close()
##
##file_object = open('noun18.txt','w')
##file_object.write(str(noun_18))
##file_object.close()
##
### plural
##file_object = open('plural1.txt','w')
##file_object.write(str(plural_1))
##file_object.close()
##
##file_object = open('plural4.txt','w')
##file_object.write(str(plural_4))
##file_object.close()

##file_object = open('plural15.txt','w')
##file_object.write(str(plural_15))
##file_object.close()
##
##file_object = open('plural18.txt','w')
##file_object.write(str(plural_18))
##file_object.close()
##
### pronoun
##file_object = open('pronoun1.txt','w')
##file_object.write(str(pronoun_1))
##file_object.close()
##
##file_object = open('pronoun4.txt','w')
##file_object.write(str(pronoun_4))
##file_object.close()
##
##file_object = open('pronoun15.txt','w')
##file_object.write(str(pronoun_15))
##file_object.close()
##
##file_object = open('pronoun18.txt','w')
##file_object.write(str(pronoun_18))
##file_object.close()
##
### verb
##file_object = open('verb1.txt','w')
##file_object.write(str(verb_1))
##file_object.close()
##
##file_object = open('verb4.txt','w')
##file_object.write(str(verb_4))
##file_object.close()
##
##file_object = open('verb15.txt','w')
##file_object.write(str(verb_15))
##file_object.close()
##
##file_object = open('verb18.txt','w')
##file_object.write(str(verb_18))
##file_object.close()


##
        ##
##


#  ADJ
myvar = open('adj1.txt', 'r')

adj_1 = myvar.read()
adj_1 = adj_1.replace("'",'')
adj_1 = adj_1.replace(" ",'').lower()
adj_1 = adj_1.split(',')

myvar.close()

myvar = open('adj4.txt', 'r')

adj_4 = myvar.read()
adj_4 = adj_4.replace("'",'')
adj_4 = adj_4.replace(" ",'').lower()
adj_4 = adj_4.split(',')

myvar.close()

myvar = open('adj15.txt', 'r')

adj_15 = myvar.read()
adj_15 = adj_15.replace("'",'')
adj_15 = adj_15.replace(" ",'').lower()
adj_15 = adj_15.split(',')

myvar.close()

myvar = open('adj18.txt', 'r')

adj_18 = myvar.read()
adj_18 = adj_18.replace("'",'')
adj_18 = adj_18.replace(" ",'').lower()
adj_18 = adj_18.split(',')

myvar.close()

# Adverbs

myvar = open('adverb1.txt', 'r')

adverb_1 = myvar.read()
adverb_1 = adverb_1.replace("'",'')
adverb_1 = adverb_1.replace(" ",'').lower()
adverb_1 = adverb_1.split(',')

myvar.close()
myvar = open('adverb4.txt', 'r')

adverb_4 = myvar.read()
adverb_4 = adverb_4.replace("'",'')
adverb_4 = adverb_4.replace(" ",'').lower()
adverb_4 = adverb_4.split(',')

myvar.close()
myvar = open('adverb18.txt', 'r')

adverb_18 = myvar.read()
adverb_18 = adverb_18.replace("'",'')
adverb_18 = adverb_18.replace(" ",'').lower()
adverb_18 = adverb_18.split(',')

myvar.close()
myvar = open('adverb15.txt', 'r')

adverb_15 = myvar.read()
adverb_15 = adverb_15.replace("'",'')
adverb_15 = adverb_15.replace(" ",'').lower()
adverb_15 = adverb_15.split(',')

myvar.close()

#interjections 
myvar = open('interjection1.txt', 'r')

interjection_1 = myvar.read()
interjection_1 = interjection_1.replace("'",'')
interjection_1 = interjection_1.replace(" ",'').lower()
interjection_1 = interjection_1.split(',')

myvar.close()

myvar = open('interjection4.txt', 'r')

interjection_4 = myvar.read()
interjection_4 = interjection_4.replace("'",'')
interjection_4 = interjection_4.replace(" ",'').lower()
interjection_4 = interjection_4.split(',')

myvar.close()

myvar = open('interjection15.txt', 'r')

interjection_15 = myvar.read()
interjection_15 = interjection_15.replace("'",'')
interjection_15 = interjection_15.replace(" ",'').lower()
interjection_15 = interjection_15.split(',')

myvar.close()

myvar = open('interjection18.txt', 'r')

interjection_18 = myvar.read()
interjection_18 = interjection_18.replace("'",'')
interjection_18 = interjection_18.replace(" ",'').lower()
interjection_18 = interjection_18.split(',')

myvar.close()


#intrans 
myvar = open('intrans1.txt', 'r')

intrans_1 = myvar.read()
intrans_1 = intrans_1.replace("'",'')
intrans_1 = intrans_1.replace(" ",'').lower()
intrans_1 = intrans_1.split(',')

myvar.close()

myvar = open('intrans4.txt', 'r')

intrans_4 = myvar.read()
intrans_4 = intrans_4.replace("'",'')
intrans_4 = intrans_4.replace(" ",'').lower()
intrans_4 = intrans_4.split(',')

myvar.close()

myvar = open('intrans15.txt', 'r')

intrans_15 = myvar.read()
intrans_15 = intrans_15.replace("'",'')
intrans_15 = intrans_15.replace(" ",'').lower()
intrans_15 = intrans_15.split(',')

myvar.close()

myvar = open('intrans18.txt', 'r')

intrans_18 = myvar.read()
intrans_18 = intrans_18.replace("'",'')
intrans_18 = intrans_18.replace(" ",'').lower()
intrans_18 = intrans_18.split(',')

myvar.close()


#plural 
myvar = open('noun1.txt', 'r')

noun_1 = myvar.read()
noun_1 = noun_1.replace("'",'')
noun_1 = noun_1.replace(" ",'').lower()
noun_1 = noun_1.split(',')

myvar.close()

myvar = open('noun4.txt', 'r')

noun_4 = myvar.read()
noun_4 = noun_4.replace("'",'')
noun_4 = noun_4.replace(" ",'').lower()
noun_4 = noun_4.split(',')

myvar.close()

myvar = open('noun15.txt', 'r')

noun_15 = myvar.read()
noun_15 = noun_15.replace("'",'')
noun_15 = noun_15.replace(" ",'').lower()
noun_15 = noun_15.split(',')

myvar.close()

myvar = open('noun18.txt', 'r')

noun_18 = myvar.read()
noun_18 = noun_18.replace("'",'')
noun_18 = noun_18.replace(" ",'').lower()
noun_18 = noun_18.split(',')

myvar.close()

#plural 
myvar = open('plural1.txt', 'r')

plural_1 = myvar.read()
plural_1 = plural_1.replace("'",'')
plural_1 = plural_1.replace(" ",'').lower()
plural_1 = plural_1.split(',')

myvar.close()

myvar = open('plural4.txt', 'r')

plural_4 = myvar.read()
plural_4 = plural_4.replace("'",'')
plural_4 = plural_4.replace(" ",'').lower()
plural_4 = plural_4.split(',')

myvar.close()

myvar = open('plural15.txt', 'r')

plural_15 = myvar.read()
plural_15 = plural_15.replace("'",'')
plural_15 = plural_15.replace(" ",'').lower()
plural_15 = plural_15.split(',')

myvar.close()

myvar = open('plural18.txt', 'r')

plural_18 = myvar.read()
plural_18 = plural_18.replace("'",'')
plural_18 = plural_18.replace(" ",'').lower()
plural_18 = plural_18.split(',')

myvar.close()

#pronoun 
myvar = open('pronoun1.txt', 'r')

pronoun_1 = myvar.read()
pronoun_1 = pronoun_1.replace("'",'')
pronoun_1 = pronoun_1.replace(" ",'').lower()
pronoun_1 = pronoun_1.split(',')

myvar.close()

myvar = open('pronoun4.txt', 'r')

pronoun_4 = myvar.read()
pronoun_4 = pronoun_4.replace("'",'')
pronoun_4 = pronoun_4.replace(" ",'').lower()
pronoun_4 = pronoun_4.split(',')

myvar.close()

myvar = open('pronoun15.txt', 'r')

pronoun_15 = myvar.read()
pronoun_15 = pronoun_15.replace("'",'')
pronoun_15 = pronoun_15.replace(" ",'').lower()
pronoun_15 = pronoun_15.split(',')

myvar.close()

myvar = open('pronoun18.txt', 'r')

pronoun_18 = myvar.read()
pronoun_18 = pronoun_18.replace("'",'')
pronoun_18 = pronoun_18.replace(" ",'').lower()
pronoun_18 = pronoun_18.split(',')

myvar.close()

#trans 
myvar = open('trans1.txt', 'r')

trans_1 = myvar.read()
trans_1 = trans_1.replace("'",'')
trans_1 = trans_1.replace(" ",'').lower()
trans_1 = trans_1.split(',')

myvar.close()

myvar = open('trans4.txt', 'r')

trans_4 = myvar.read()
trans_4 = trans_4.replace("'",'')
trans_4 = trans_4.replace(" ",'').lower()
trans_4 = trans_4.split(',')

myvar.close()

myvar = open('trans15.txt', 'r')

trans_15 = myvar.read()
trans_15 = trans_15.replace("'",'')
trans_15 = trans_15.replace(" ",'').lower()
trans_15 = trans_15.split(',')

myvar.close()

myvar = open('trans18.txt', 'r')

trans_18 = myvar.read()
trans_18 = trans_18.replace("'",'')
trans_18 = trans_18.replace(" ",'').lower()
trans_18 = trans_18.split(',')

myvar.close()

#verb 
myvar = open('verb1.txt', 'r')

verb_1 = myvar.read()
verb_1 = verb_1.replace("'",'')
verb_1 = verb_1.replace(" ",'').lower()
verb_1 = verb_1.split(',')

myvar.close()

myvar = open('verb4.txt', 'r')

verb_4 = myvar.read()
verb_4 = verb_4.replace("'",'')
verb_4 = verb_4.replace(" ",'').lower()
verb_4 = verb_4.split(',')

myvar.close()

myvar = open('verb15.txt', 'r')

verb_15 = myvar.read()
verb_15 = verb_15.replace("'",'')
verb_15 = verb_15.replace(" ",'').lower()
verb_15 = verb_15.split(',')

myvar.close()

myvar = open('verb18.txt', 'r')

verb_18 = myvar.read()
verb_18 = verb_18.replace("'",'')
verb_18 = verb_18.replace(" ",'').lower()
verb_18 = verb_18.split(',')

myvar.close()

