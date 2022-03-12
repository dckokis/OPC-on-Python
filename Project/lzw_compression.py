import sys

def encode(message):
    """Compresses data with LZW algorithm"""
    encoded_message = ''
    dictionary = {bytes([a]): a for a in range(256)}
    words_count = 255
    degree = 8
    i = 0
    if len(message) == 0:
        return message
    while i != len(message):
        if i == len(message) - 1:  # если остался один символ, то кодируем его и выходим из цикла
            code = str(bin(dictionary[message[i: i + 1]]))[2:]
            margin = degree - len(code)
            encoded_message = encoded_message + '0' * margin + code
            break
        j = i + 1

        while True:
            if (message[i: j + 1] in dictionary) and (j + 1 <= len(message)):  # проверяем,есть ли слово в словаре
                j = j + 1
            else:
                if message[
                   i: j + 1] not in dictionary:  # послденее слово могло испортить словарь - дополнительная проверка
                    words_count += 1
                    if words_count == 2 ** degree:  # повышение битной кодировки при достижении количеcтва слов 2**degree
                        degree += 1
                    dictionary[message[i:j + 1]] = words_count
                code = str(bin(dictionary[message[i: j]]))[2:]
                margin = degree - len(code)
                encoded_message = encoded_message + '0' * margin + code
                i = j
                break

    return encoded_message

def decode(message):
    """Decompresses data with LZW algorithm"""
    dictionary = {a: bytes([a]).decode('ISO-8859-1') for a in range(256)}  # словарь кодов и символов с кодировкой по умолчанию
    words = set(dictionary.values())  # все известные слова
    words_count = 256
    decoded_message = ''
    if len(message) == 0:
        return message
    if len(message) == 8:  # сообщение состоит из одного символа
        return dictionary[int(message[0:8], 2)]
    buffer = dictionary[int(message[0:9], 2)]

    degree = 9
    i = 9
    while i < len(message):
        if i + degree > len(message):  # больше раскодировать нечего - опустошаем буфер
            decoded_message += buffer
            break
        if (len(words) == 2 ** degree - 1) and (len(message) >= i + 2 * degree):
            buffer += dictionary[int(message[i: i + degree + 1], 2)]
        else:
            if int(message[i: i + degree], 2) == words_count:
                if len(decoded_message) == 0:
                    buffer = buffer * 3
                else:
                    symbol = dictionary[words_count - 1][-1]
                    word = dictionary[words_count - 1]
                    summary = 1
                    for k in range(len(word) - 1, 0, -1):
                        if word[k] == symbol:
                            summary += 1
                        else:
                            break
                    buffer += symbol * summary
            else:
                buffer += dictionary[int(message[i: i + degree], 2)]

        j = 0
        while (buffer[0:j + 1] in words) and (
                j <= len(buffer)):  # ищем слово в буфере, которое мы не знаем или доходим до конца буфера
            j += 1
        if buffer[0:j + 1] not in words:  # добавляем неизвестное слово
            words.add(buffer[0:j + 1])
            dictionary[words_count] = buffer[0:j + 1]
            words_count += 1
        decoded_message += buffer[0:j]
        buffer = buffer[j:]
        if words_count == 2 ** degree:  # повышение битной кодировки при достижении количеcтва слов 2**degree
            degree += 1
        i += degree

    return decoded_message

def full_encode(input_file, output_file):
    """Compresses data from input file using the output function encode. Is a command line argument. """
    f = open(input_file, 'rb')
    message = f.read()
    f.close()
    encoded_message = encode(message)
    bytes_array = b''
    while True:
        if len(encoded_message) >= 8:
            bytes_array += int(encoded_message[0:8], 2).to_bytes(1, 'big')
            encoded_message = encoded_message[8:]
        elif len(encoded_message) == 0:
            break
        else:
            margin = 8 - len(encoded_message)
            bytes_array += int(encoded_message + '0' * margin, 2).to_bytes(1, 'big')
            break
    f = open(output_file, 'wb')
    f.write(bytes_array)
    f.close()

def full_decode(input_file, output_file):
    """Decompresses data from input file using the output function decode. Is a command line argument."""
    f = open(input_file, 'rb')
    code = f.read()
    f.close()
    message = ''
    for i in range(len(code)):
        bits = str(bin(int.from_bytes(bytes([code[i]]), 'big')))[2:]
        margin = 8 - len(bits)
        message = message + '0' * margin + bits
    decoded_message = decode(message)
    f = open(output_file, 'w')
    f.write(decoded_message)
    f.close()


def main():
    if len(sys.argv) != 4:
        print("Error: wrong input format. There must be 3 arguments.")
    function = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    if function == "--encode":
        full_encode(input_file, output_file)
    elif function == "--decode":
        full_decode(input_file, output_file)
    else:
        print("Error: wrong command: {}".format(function))


if __name__ == '__main__':
    main()