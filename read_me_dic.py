with open('story.txt') as f:
    content = f.readlines()
    contents=content.copy()
    f.close()
   
   
contents
string_mker=(' '.join(contents))
string=string_mker.split(' ')

dic={
" ":" ",}

msg=string
for words in msg:
    word_count=msg.count(words)
    dic[words]=word_count
return(dic)
   


    