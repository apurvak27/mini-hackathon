""" Hackathon - Level 1 """

def min_max_product(list):
    """
    
    Returns a product of the min and max of a list.
    
    Parameters
    ----------
    list : list of integers

    Returns
    -------
    integer i

    """
    return min(list)*max(list)

if __name__ == '__main__':
    print(min_max_product([2, 100, 24, 15, 4, 9, 61]))