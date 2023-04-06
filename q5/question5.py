str1 = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
str2 = "Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,"

def reverse_words(str):
    list1 = list(str.split(' '))
    list1.reverse()
    str1 = ' '.join(list1)

    return str1

def main():
    print("original string :",str1)
    print("reverse string :",reverse_words(str1))
    print()
    print("original string :", str2)
    print("reverse string :", reverse_words(str2))

if __name__ == '__main__':
    main()

