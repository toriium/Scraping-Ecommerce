import re


def get_only_numbers(text_received):
    regex_syntax = r"\D"
    num_str = re.sub(regex_syntax, "", text_received)
    num = int(num_str)
    return num


def remove_dollar_sign(text: str):
    text = text.replace('$', '')
    try:
        num = float(text)
    except ValueError:
        num = 0
    return num
