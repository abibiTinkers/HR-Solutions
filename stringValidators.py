if __name__ == '__main__':
    s = input()
    one=two=three=four=five=False
    for i in s:
        if i.isalnum():
            one=True
        if i.isalpha():
            two=True
        if i.isdigit():
            three=True
        if i.islower():
            four=True
        if i.isupper():
            five=True
    print(one, two, three, four, five, sep='\n')
