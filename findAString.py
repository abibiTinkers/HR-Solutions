def count_substring(string, sub_string):
    l= len(string)
    count=0
    for i in range(l):
        if sub_string[0]==string[i]:
          
            if string[i:i+len(sub_string)]==sub_string:
                count=count+1
    return count

