import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def handleSpellCheck(self, e):
        language = self._view.ddLanguage.value
        modalita = self._view.ddOpzioni.value
        testo = self._view.txtTesto.value

        if language == None or modalita == None or testo == "":
            self._view.lvOut.controls.append(ft.Text("Errore, almeno un parametro non è stato inserito"))

        else:
            parole_errate, tempo = self.handleSentence(testo, language, modalita)

            self._view.lvOut.controls.append(ft.Text(f"Frase inserita {testo}"))

            if parole_errate == " - ":
                self._view.lvOut.controls.append(ft.Text(f"Parole errate: nessuna"))
            else:
                self._view.lvOut.controls.append(ft.Text(f"Parole errate: {parole_errate}"))

            self._view.lvOut.controls.append(ft.Text(f"Tempo richiesto dalla ricerca: {tempo}"))

        self._view.update()







def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text