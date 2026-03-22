import textwrap
def merge_the_tools(string, k):
    # your code goes here
    for x in textwrap.wrap(string, k):
        my_list = list(dict.fromkeys(x))
        print( ''.join(my_list) )

