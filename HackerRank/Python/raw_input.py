import os

def read_file():
    """
    Read input.txt file and return list of lines.

    Returns
    -------
    list
        file lines as a list of strings.
    """
    result = list()
    filename = os.path.join(os.getcwd(), 'input.txt')
    with open(filename, 'r') as file_handler:
        for line in file_handler:
            result.append(line.strip())
    return result


def gen_input(result):
    """
    Generator function to iterate through file list

    Parameters:
    ----------
    arg: list (strings)

    Returns
    -------
    string
        iterated string
    """
    for value in result:
        yield value


result = read_file()
gen = gen_input(result)


def input():
    """
    Simple wrapper to iterate through generator

    Parameters:
    ----------
    None - However, a gen global object needs to be created

    Returns
    -------
    string item from list managed by a generator.
    """
    try:
        result = next(gen)
        return result
    except StopIteration:
        return "End of line!"
