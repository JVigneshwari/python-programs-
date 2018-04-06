i=input("Enter a string\n")
words=i.split(' ')
capitalize=[]
for word in words:
    f=word[0].upper()+word[1:]
    capitalize.append(f)
    output='  '.join(capitalize)
    print(output)
