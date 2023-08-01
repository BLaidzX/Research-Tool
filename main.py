import wolframalpha

client = wolframalpha.Client(API key)

import wikipedia



import PySimpleGUI as sg

sg.theme('DarkPurple')
layout = [[sg.Text('Search'), sg.InputText()], [sg.Button('Ok'), sg.Button('Cancel')]]
window = sg.Window('Search', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text

        sg.PopupNonBlocking("Wolfram Result: " + wolfram_res, "Wikipedia Result: " + wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text

        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text

        sg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)

        sg.PopupNonBlocking(wiki_res)

        print(values[0])
window.close()
