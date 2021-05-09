def trim_string(string: str, length: int) -> str:
    """
    Ensure that the length of a string does not exceed `length` characters.

    If length of `string` is greater than `length`, a shortened copy of the 
    string is returned with elipses in place of the first three removed
    characters. Otherwise the original string is returned.

    `string` : the string which is passed in for trimming.
    `length` : the size which the string will be trimmed to.
    """
    # Sample runs:
    # trim_window_title("Baby shark") -> "Baby shark"
    # trim_window_title("ABCDEFGHIJKLMNOPQRSTUVWXYZ_ABCDEFGHIJKLMNOPQRSTUVWXYZ") -> "ABCDEFGHIJKLMNOPQRSTUVWXYZ_ABCDEFGHIJKLMNOPQR..."

    pass  # TODO: Implementation goes here. `pass` keyword is used to tell
    # python that this function is not yet written.
