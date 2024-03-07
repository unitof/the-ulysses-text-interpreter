# Breaks up books to a series of .txt files
def chapter_creator(fileName, firstChapter, lastChapter):
    # open/read file of interest, and save it to temp variable
    myvar = open(fileName, 'r')

    full_text = myvar.read()

    myvar.close()

    # loop to write each individual chapter as its own .txt file
    for i in range(int(firstChapter), int(lastChapter+1)):
    
        start = '[ '+str(i)+' ]'
        end = '[ '+str(i+1)+' ]'
        chapter_slice = full_text[full_text.find(start):full_text.find(end)]

        file_object = open('Chapter_'+str(i)+'.txt', 'w')
        file_object.write(chapter_slice)
        file_object.close()
    
    #return chapter_slice#
def punct_strip(lst):
    new_lst = []
    for i in lst:
        word=i.strip(".,!':")
        word=word.strip('-')
        word=word.strip('\n')
        new_lst.append(word)
    return new_lst


# assembles lists for parts of speech 
def POS_sorter(startChapter, endChapter):
    pos = ['adj','adverb','intrans','noun','plural','trans','verb']
    # make list of all words in chapter where sentace breaks are deliniated by an empty space.
    for chapter_num in range (startChapter, endChapter+1):
        chap = 'Chapter_'+str(chapter_num)+'.txt'
        myvar = open(chap, 'r')
        chapter_list = myvar.read()
        myvar.close()
        chapter_list = chapter_list.replace('\n',' ')
        chapter_list = chapter_list.replace('[ '+str(chapter_num)+' ]', '')
        chapter_list = chapter_list.split(' ')
        chapter_list = punct_strip(chapter_list)

        # make list of all words in pos subset
        for part in pos:
            # open pos library, create list of pos_parts
            pos_words = open(part+'.txt')
            pos_list = pos_words.read()
            pos_list = pos_list.replace("'",'')
            pos_list = pos_list.replace(' ','').lower()
            pos_list = pos_list.split(',')
            pos_words.close()
            for word in chapter_list:
                if len(word)>0:
                    if word[0] > 

                    
            
POS_sorter(1,2)
