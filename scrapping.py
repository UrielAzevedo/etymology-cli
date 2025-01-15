#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys

def all_syntaxes_(word, aux):

    url = f"https://www.etymonline.com/word/{word}#etymonline_v_25849"
    try:
        html = urlopen(url)
    except:
        return 'no results'
    soup = BeautifulSoup(html, 'lxml')

    word_etymology = soup.find_all('section', {"class" : "word__defination--2q7ZH"})
    etymology_tittles = []
    etymology_tittles.append(soup.find('h1', {"class" : "word__name--TTbAA"}))
    etymology_tittles.extend(soup.find_all('p', {"class" : "word__name--TTbAA"}))
    etymology_meanings = []

    for etymology_meaning in word_etymology:
        etymology_meaning = etymology_meaning.findChildren('p', recursive=False)
        text = ''
        for child in etymology_meaning:
            text += child.text
        etymology_meanings.append(text)

    meaning_rows = []
    meanings = ''

    for i, tittle in enumerate(etymology_tittles):
        if '(' not in tittle.text:
            etymology_tittles[i] = 'null'
        else:
            etymology_tittles[i] = tittle.text.split('(', 1)[1].split(')')[0].split('.',1)[0]

        meaning_rows.append({'category' : etymology_tittles[i], 'meaning': etymology_meanings[i]})

        if etymology_tittles[i] == 'v':
            etymology_tittles[i] = 'verb'
        elif etymology_tittles[i] == 'n':
            etymology_tittles[i] = 'noun'
        elif etymology_tittles[i] == 'adj':
            etymology_tittles[i] = 'adjective'
        elif etymology_tittles[i] == 'adv':
            etymology_tittles[i] = 'adverb'

        meanings += f"\n{etymology_tittles[i]} - {etymology_meanings[i]}\n"

    if aux:
        return meaning_rows
    else:
        return meanings

def noun_search_(word):
    search_results = all_syntaxes_(word, True)
#    if "error" in search_results:
#        return search_results
    if search_results == 'no results':
        return 'no results'

    nouns = ''

    for result in search_results:
        if result['category'] == 'n':
            #nouns.append(result['meaning'])
            nouns += f"\n{result['meaning']}\n"
    if nouns == '':
        return "no results"

    return nouns

def verb_search_(word):
    search_results = all_syntaxes_(word, True)
#    if "error" in search_results:
#        return search_results
    if search_results == 'no results':
        return 'no results'


    verbs = ''

    for result in search_results:
        if result['category'] == 'v':
            verbs += f"\n{result['meaning']} \n"

    if verbs == '':
        return 'no results'
        
    return verbs

def adjective_search_(word):
    search_results = all_syntaxes_(word, True)
    #if "error" in search_results:
    #   return search_results
    if search_results == 'no results':
        return 'no results'

    adjectives = ''

    for result in search_results:
        if result['category'] == 'adj':
            adjectives += f"\n{result['meaning']}\n"

    if adjectives == '':
        return 'no results'

    return adjectives

def adverb_search_(word):
    search_results = all_syntaxes_(word, True)
    #if "error" in search_results:
    #   return search_results
    if search_results == 'no results':
        return 'no results'

    adverbs = ''

    for result in search_results:
        if result['category'] == 'adv':
            adverbs += f"\n{result['meaning']}\n"

    if adverbs == '':
        return 'no results'

    return adverbs

if __name__ == "__main__":
    if len(sys.argv) > 2:
        if sys.argv[1] == "--all-syntax" or sys.argv[1] == '-a':
            print(all_syntaxes_(sys.argv[2], False))
        elif sys.argv[1] == "--noun" or sys.argv[1] == '-n':
            print(noun_search_(sys.argv[2]))
        elif sys.argv[1] == "--verb" or sys.argv[1] == '-v':
            print(verb_search_(sys.argv[2]))
        elif sys.argv[1] == "--adjective" or sys.argv[1] == '-adj':
            print(adjective_search_(sys.argv[2]))
        elif sys.argv[1] == "--adverb" or sys.argv[1] == '-adv':
            print(adverb_search_(sys.argv[2]))
        else:
            print("Invalid option.")
    else:
        print("No argument provided.")
