word=input("Enter the word you want to search for: ")

with open('test.txt','r') as f:
    file=f.read()
if word in file:
    print(f'{word} is present in the file')
else:
    print(f'{word} is present not in the file')

