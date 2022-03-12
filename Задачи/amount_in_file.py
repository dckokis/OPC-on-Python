def amount_in_file(fname):
    d = open(fname, 'r', encoding='utf-8')
    words_am = 0
    lines_am = 0
    symbols_am = 0
    in_word = False
    for line in d:
        lines_am += 1
        for symbol in line:
            symbols_am += 1
            if symbol.isspace():
                if in_word:
                    in_word = False
            else:
                if not in_word:
                    in_word = True
                    words_am += 1

    d.close()
    return words_am, lines_am, symbols_am


fname = input()
words, lines, symbols = amount_in_file(fname)
print("Words:", words, "Lines:", lines, "Symbols:", symbols)
