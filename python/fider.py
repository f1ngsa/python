a = input("Enter 3 words with a space between: ")
word1 = a[:a.find(" ")]
word2 = a[a.find(" ")+1:a.rfind(" ")]
word3 = a[a.rfind(" ")+1:]
"""print(word2.replace("a", "A"))"""
print(word1)
print(word2)
print(word3)