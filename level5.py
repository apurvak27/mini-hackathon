""" Hackathon - Level 5 """

def convert(numeral):
    """
    Converts a Roman Numeral string to an int.

    Parameters
    ----------
    numeral : A string of valid Roman numerals

    Returns
    -------
    int_val : the corresponding integer

    """
    roman_dictionary = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    num = 0
    for i in range(len(numeral)):
        if (i > 0 and
            roman_dictionary[numeral[i]] > roman_dictionary[numeral[i - 1]]):
            num += roman_dictionary[numeral[i]] - 2 * roman_dictionary[numeral[i - 1]]
        else:
            num += roman_dictionary[numeral[i]]
    return num

if __name__ == '__main__':
    print(convert('MCXLV'))
    