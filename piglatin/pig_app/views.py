from django.shortcuts import render


def index(request):
    return render(request, 'pig_app/index.html')


def about(request):
    return render(request, 'pig_app/about.html')    


def piglatin(request):

    # GRABS USERINPUT
    untranslated = request.GET['untranslated'].lower()

    translated = ''
    # SPLITS THE SENTENCE GIVIN BY THE USER
    for word in untranslated.split():
        # CHECKS IF THE FIRST LETTER IS IN THE LIST
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            # VOWEL
            translated += word
            translated += 'yay '
        else:
            # CONSONANT
            translated += word[1:]
            translated += word[0]
            translated += 'ay '

    return render(request, 'pig_app/piglatin.html',
                           {'untranslated': untranslated,
                            'translated': translated})
