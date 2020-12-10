from googletrans import Translator

def translate(inputstr: str, dest: str = 'ja') -> str:
    translator = Translator()
    result = translator.translate(inputstr, dest)
    return result.text

if __name__ == '__main__':
    print(translate(inputstr='こんにちは', dest='en'))
    print(translate('Hello', dest='ja'))
