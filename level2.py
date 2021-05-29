""" Hackathon - Level 2 """

def longest_word(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    no_punct = ""
    for char in string:
       if char not in punctuations:
           no_punct = no_punct + char
           
    string=no_punct.split()
    longest = ""
    for i in range(0,len(string)):
        if (len(string[i]) > len(longest)):
            longest=string[i]
    return longest


if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return lorem
    print(longest_word("lorem ipsum, dolor sit amet"))
