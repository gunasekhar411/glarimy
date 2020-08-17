def deduplicate(s):
    words=s.split(" ")
    distwords=[]
    for i in words:
        if i not in distwords:
            distwords.append(i)
    return distwords
def sort(list_words):
    for i in range(0,len(list_words)):
        for j in range(i+1,len(list_words)):
            if list_words[i]>list_words[j]:
                list_words[i],list_words[j]=list_words[j],list_words[i]
    return list_words


def parse(s):
    fp=open(s,'r')
    sentences=list(fp)
    words=[]
    allsentences=""
    for i in sentences:
        k=i.rstrip("\n")
        allsentences=allsentences+k+" "
    remove_duplicate=deduplicate(allsentences)
    sort_words=sort(remove_duplicate)
    sort_words=sort_words[1:]
    for i in sort_words:
        print(i)



