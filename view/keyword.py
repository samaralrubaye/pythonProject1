keywords = 'number,act'

#splitkeywordsing by ,
chunks =keywords.split(',')

print(chunks)
listwords =[]


for i in range(len(chunks)):
    listwords .append([chunks[i]])
print(listwords )


listsent = ['The number of people suffering acute hunger could almost double.',
            'Lockdowns and global economic recession have',
            'one more shock – like Covid-19 – to push them over the edge',
            'people must collectively act now to mitigate the impact']


def check_words(listwords, listsent):
    listsent_new = []
    # interate through each sentence
    for sentence in listsent:
        # iterate through each group of words
        for words in listwords:
            # check to see if each word group is in the current sentence
            if all(word in sentence for word in words):
                listsent_new.append(sentence)
    return listsent_new
lists=['aa','bb','cc','dd']
f=lists.index('bb')
l=lists.index('dd')
print(f)
print(l)

for i in range(f,l+1):
    print(lists[i])

    

if __name__ == '__main__':
    print(check_words(listwords, listsent))