def search4vowels(word: str) -> set:
    """Return a boolean based on any vowels found."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return vowels.intersection(set(word))
    '''결과값으로 set 이 나올수도 있어요!!!'''


search4vowels('hitch-hiker')

search4vowels('galaxy')

search4vowels('life, the universe and everything')

search4vowels('sky')
