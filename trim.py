def trim_string(string: str, length: int) -> str:
    """
    Ensure that the length of a string does not exceed `length` characters.

    > Preconditions:`length` > 0

    > Postconditions: If length of `string` is greater than `length`, a
    shortened copy of the string is returned with elipses in place of 
    the first three removed characters. Otherwise the original string is returned.

    + `string` : the string which is passed in for trimming.
    + `length` : the size which the string will be trimmed to.
    """

    if length == len(string):
        return string
    elif length > 0:
        if length > len(string):
            return "Length too long"
        
        string = string[:length] + "..."
        return string
    
    else:
        return "Length too short"




print(trim_string("Baby shark", 10))
print(trim_string("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5))
print(trim_string("ABC", -1))
print(trim_string("A", 2))
    