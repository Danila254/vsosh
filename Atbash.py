class Atbash:
    def encrypt(text):
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЧШЩЪЫЬЭЮЯ'
        alpha = 'абвгдеёжзийклмнопрстуфхчшщъыьэюя'
        result = ""
        for i in text:
            if i.islower():
                result += Atbash.func(text)
            else:
                result += Atbash.funcC(text)
        print(result)

    def func(text):
        alphabet = 'абвгдеёжзийклмнопрстуфхчшщъыьэюя'     
        cipher = {alphabet: alphabet[::i-1] for i in range(len(alphabet))}
        return "".join(cipher.get(symbol, symbol) for symbol in text)

    def funcC(text):
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЧШЩЪЫЬЭЮЯ'    
        cipher = {alphabet: alphabet[::i-1] for i in range(len(alphabet))}
        return "".join(cipher.get(symbol, symbol) for symbol in text)


Atbash.encrypt("Привет")
