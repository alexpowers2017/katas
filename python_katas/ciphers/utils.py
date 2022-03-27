import re

def position_of(letter: chr) -> int:
    return ord(letter) - 97

def letter_at(position: chr) -> chr:
    return chr(position + 97)

def remove_non_alpha(s: str) -> str:
    return '' if not s or has_number(s) else re.sub(r"[^A-Za-z]", '', s)

def has_number(s: str) -> bool:
    return True in [c.isnumeric() for c in s]
