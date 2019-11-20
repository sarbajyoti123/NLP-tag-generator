import nltk 
from nltk.corpus import wordnet 
from collections import Counter
import sys
# print(sys.getrecursionlimit())
a=[]
# sys.setrecursionlimit(1000)
word=str(input('enter word '))
for syn in wordnet.synsets(word): 
        for l in syn.hyponyms():
            for j in l.lemmas():
                print('#'+j.name())
        for k in syn.lemmas(): 
            l=k.name()
            a.append(l)
UniqW = Counter(a) 
for i in UniqW.keys():
    print('#'+i)
if ' ' or '_' in word:
    b=[]
    c=[]
    d=[]
    a=word.replace(' ',' ').replace('_',' ').split()
    if len(a)==3:
        word=a[0]
        word2=a[1]
        word3=a[2]
        print('#'+a[0]+a[1]+a[2])
        print('#'+a[0]+'_'+a[1]+'_'+a[2])
        # print('#'+a[0]+'_'+a[1]+a[2])
        # print('#'+a[0]+a[1]+'_'+a[2])
        for syn in wordnet.synsets(word): 
            for l in syn.lemmas():
                a=l.name()
                b.append(a)
        UniqW = Counter(b) 
        for i in UniqW.keys():
            print('#'+i.replace('-','_'))
        for syn in wordnet.synsets(word2): 
            for l in syn.lemmas():
                a=l.name()
                c.append(a)
        UniqW = Counter(c) 
        for i in UniqW.keys():
            print('#'+i.replace('-','_'))
                
        for syn in wordnet.synsets(word3): 
            for l in syn.lemmas():
                a=l.name()
                d.append(a)
        UniqW = Counter(d) 
        for i in UniqW.keys():
            print('#'+i.replace('-','_'))
    elif len(a)>3:
        word=a[0]
        word2=a[1]
        print('#'+a[0]+a[1])
        print('#'+a[0]+'_'+a[1])
       
        for syn in wordnet.synsets(word): 
            for l in syn.lemmas():
                a=l.name()
                print('#'+a.replace('-','_'))
        for syn in wordnet.synsets(word2): 
            for l in syn.lemmas():
                a=l.name()
                print('#'+a.replace('-','_'))
    else:
        if '_' in word:
            a=[str(i) for i in word.split('_')]
            if len(a)<3:
                word=a[0]
                word2=a[1]
                # word3=a[2]
                print('#'+a[0]+a[1])
                print('#'+a[0]+'_'+a[1])
                for syn in wordnet.synsets(word): 
                    for l in syn.lemmas():
                        a=l.name()
                        print('#'+a.replace('-','_'))
                for syn in wordnet.synsets(word2): 
                    for l in syn.lemmas():
                        a=l.name()
                        print('#'+a.replace('-','_'))
            elif len(a)==3:
                word=a[0]
                word2=a[1]
                word3=a[2]
                print('#'+a[0]+a[1]+a[2])
                print('#'+a[0]+'_'+a[2]+'_'+a[2])
                for syn in wordnet.synsets(word): 
                    for l in syn.lemmas():
                        a=l.name()
                        print('#'+a.replace('-','_'))
                for syn in wordnet.synsets(word2): 
                    for l in syn.lemmas():
                        a=l.name()
                        print('#'+a.replace('-','_'))
                for syn in wordnet.synsets(word3): 
                    for l in syn.lemmas():
                        a=l.name()
                        print('#'+a.replace('-','_'))
            else:
                print('Not more than 3')
        elif ' ' in word:
            a=[str(i) for i in word.split(' ')]
            if len(a)<3:
                word=a[0]
                word2=a[1]
                print('#'+a[0]+a[1])
                print('#'+a[0]+'_'+a[1])
                for syn in wordnet.synsets(word): 
                    for l in syn.lemmas():
                        a=l.name()
                        print('#'+a.replace('-','_'))
                for syn in wordnet.synsets(word2): 
                    for l in syn.lemmas():
                        a=l.name()
                        print('#'+a.replace('-','_'))
            elif len(a)==3:
                word=a[0]
                word2=a[1]
                word4=a[2]
                print('#'+a[0]+a[1]+a[2])
                print('#'+a[0]+'_'+a[1]+'_'+a[2])
                for syn in wordnet.synsets(word): 
                    for l in syn.lemmas():
                        a=l.name()
                        print('#'+a.replace('-','_'))
                for syn in wordnet.synsets(word2): 
                    for l in syn.lemmas():
                        a=l.name()
                        print('#'+a.replace('-','_'))
                for syn in wordnet.synsets(word4): 
                    for l in syn.lemmas():
                        a=l.name()
                        print('#'+a.replace('-','_'))
                        
else:
    print('yes')
