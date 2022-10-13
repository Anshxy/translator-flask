from googletrans import Translator #googletrans==4.0.0-rc1




def translation(text, d=None):

    if d is None:
        d='en'


    t = Translator()
    a = t.translate(str(text), d)

    z = [a.text, a.dest, a.src]

    return z


# print(translation("아니오", "en"))


