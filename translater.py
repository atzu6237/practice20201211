from googletrans import Translator

def translate(inputstr: str, dest: str) -> str:
    t = Translator()
    result = t.translate(inputstr, dest)
    return result.text

def detect_lang(inputstr: str) -> str:
    """                                                                            return 'ja'                                                                     >>> detect_lang('こんにちは')                                     
    'ja'                                                                           """
    t = Translator()
    result = t.detect(inputstr)
    return result.lang


def get_lang_ja():
    """
    return 'ja'
    
    >>> detect_lang('こんにちは')
    'ja'
    """

if __name__ == '__main__':
    
    print(detect_lang('こんにちは'))

    print(translate(inputstr='こんにちは', dest='en'))
    print(translate('Hello', dest='ja'))
