def check_codeword(codeword):
    if codeword == "Horse":
        return "Correct, come in!"
    elif codeword[0] == "H" and codeword[-1] == "e":
        return "close, but nope."
    else:
        return "WRONG!"
