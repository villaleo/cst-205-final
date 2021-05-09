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
    # Sample runs:
    # trim_string("Baby shark", 10) -> "Baby shark"
    # trim_string("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5) -> "ABCDE..."
    # trim_string("ABC", -1) -> Error! length must be greater than -1.

    pass  # TODO: Implementation goes here. `pass` keyword is used to tell
    # python that this function is not yet written.
