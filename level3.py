""" Hackathon - Level 3 """

def oddish_evenish_num(n):
    """
    Returns Oddish if odd, else returns Evenish
    

    Parameters
    ----------
    n : integer to evaluate

    Returns
    -------
    Oddish: if n == odd
    Evenish: if n == even

    """
    return 'Oddish' if sum(map(int, str(n))) % 2 else 'Evenish'

if __name__ == "__main__" :
    print(oddish_evenish_num(1190))
