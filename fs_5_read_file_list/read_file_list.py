import os
def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, in cwd containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """
    f = open(f"{os.getcwd()}\\{filename}", 'r')
    print("\n".join([f"- {line}" for line in f.read().split('\n')]))