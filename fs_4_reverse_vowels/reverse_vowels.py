def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowel_map = [idx for idx, char in enumerate(s) if char.lower() in 'aeiou']
    while len(vowel_map) > 1:
        front = vowel_map.pop(0)
        back = vowel_map.pop()
        s = s[:front] + s[back] + s[front + 1:back] + s[front] + s[back + 1:]
    return s