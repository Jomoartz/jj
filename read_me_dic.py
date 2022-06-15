def read_file_content(filename):
    with open(filename) as f:
        content = f.readlines()
        contents=content.copy()
        f.close()
        return contents
       
       
#in COUNT_WORDS FUNCT.(read_file_content() function is used without 'import" because both functs are in same file.)
def count_words(filename):
    texts=read_file_content(filename)
    string_mker=(' '.join(texts))
    string=string_mker.split(' ')
    dic={
    " ":" ",}
    msg=string
    for words in msg:
        word_count=msg.count(words)
        dic[words]=word_count
    return(dic)
    
    


#trial:
print (count_words("story.txt"))
    
   


    
