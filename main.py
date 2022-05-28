def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename,"r") as f:
        txt = f.read()
        return txt
        
print('\033[1m'+"Find below, the content of the text file named Story.txt"+'\033[0m')
print(read_file_content("C:\\Users\\engrk\\Desktop\\Training\\Zuri\\backend\\python\\Tasks\\Reading-Text-Files\\story.txt"))

def count_words(str):
    # [assignment] Add your code here
    counts = dict()
    words = str.split()
    for  word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print('\n')
print('\033[1m'+"Find below, the number of times each word appeared in the file"+'\033[0m')
print (count_words(read_file_content("story.txt")))
print(input("Press Enter to Terminate"))