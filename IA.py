from urllib.request import urlopen
from translate import Translator
from random import choice
import speech_recognition as sr
import pyttsx3
import subprocess
import wolframalpha
import webbrowser
import wikipedia

def assistant_voix(sortie):
    if sortie != None:
        voix = pyttsx3.init()
        print("A.I : " + sortie)
        voix.say(sortie)
        voix.runAndWait()


def internet():
    try:
        urlopen('https://www.google.com', timeout=1)
        print("Connecté")
        return True
    except:
        print("Déconnecté")
        return False


def reconnaissance():
    r = sr.Recognizer()
    r.energy_threshold = 4000
    pas_compris = "Désolé, je n'ai pas compris ."
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.7
        print(".... ")
        audio = r.listen(source)
        if internet():
            try:
                vocal = r.recognize_google(audio, language = 'fr-FR')
                print(vocal)
                return vocal
            except sr.UnknownValueError:
                assistant_voix(pas_compris)
        else:
            try:
                vocal = r.recognize_sphinx(audio, language = 'fr-fr')
                print(vocal)
                return vocal
            except sr.UnknownValueError:
                assistant_voix(pas_compris)

def application(entree):
    if entree != None:
        dico_apps = {
            "note": ["notepad","note pad"],
            "sublime": ["sublime","sublime texte"],
            "obs": ["obs","obs capture","capture l'ecran"],
            "edge": ["microsoft edge","edge"]
        }
        fini = False
        while not fini:
            for x in dico_apps["note"]:
                if x in entree.lower():
                    assistant_voix("Ouverture de Notepad .")
                    subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
                    fini = True
            for x in dico_apps["sublime"]:
                if x in entree.lower():
                    assistant_voix("Ouverture de Sublime Text .")
                    subprocess.Popen('C:\\Program Files\\Sublime Text 3\\sublime_text.exe')
                    fini = True
            for x in dico_apps["obs"]:
                if x in entree.lower():
                    assistant_voix("Ouverture de Obs .")
                    subprocess.Popen('C:\\Program Files\\obs-studio\bin\\64bit\\obs64')
                    fini = True
            for x in dico_apps["edge"]:
                if x in entree.lower():
                    assistant_voix("Ouverture de Edge .")
                    subprocess.Popen('C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')
                    fini = True
            fini = True



def sur_le_net(entree):
    if entree != None:
        if "youtube" in entree.lower(): 
            indx = entree.lower().split().index("youtube") 
            recherche = entree.lower().split()[indx + 1:]
            if len(recherche) != 0:
                assistant_voix("recherche sur YouTube .")
                webbrowser.open("http://www.youtube.com/results?search_query=" + "+".join(recherche), new = 2)
        elif "wikipédia" in entree.lower(): 
            wikipedia.set_lang("fr")
            try:
                recherche = entree.lower().replace("cherche sur wikipédia","")
                if len(recherche) != 0:
                    resultat = wikipedia.summary(recherche, sentences = 1)
                    assistant_voix("recherche sur Wikipédia .")
                    assistant_voix(resultat)
            except:
                assistant_voix("Désolé, aucune page trouvée .") 
        else: 
            if "google" in entree.lower():
                indx = entree.lower().split().index("google") 
                recherche = entree.lower().split()[indx + 1:]
                if len(recherche) != 0:
                    assistant_voix("recherche sur Google .")
                    webbrowser.open("https://www.google.com/search?q=" + "+".join(recherche), new = 2)
            elif "cherche" in entree.lower() or "recherche" in entree.lower():
                indx = entree.lower().split().index("cherche") 
                recherche = entree.lower().split()[indx + 1:]
                if len(recherche) != 0:
                    assistant_voix("recherche par défaut .")
                    webbrowser.open("https://www.google.com/search?q=" + "+".join(recherche), new = 2)
            elif "recherche" in entree.lower():
                    indx = entree.lower().split().index("recherche")
                    recherche = entree.lower().split()[indx + 1:]
                    if len(recherche) != 0:
                        assistant_voix("recherche sur Google .")
                        webbrowser.open("http://www.google.com/search?q="+"+".join(recherche), new = 2)

def main():
    assistant_voix("Bonjour Dounia, je suis votre assistant de bureau. Dîtes-moi ce que je peux faire pour vous ?")
    fermer = ["arrête-toi"]
    ouvrir = ["ouvre","ouvrir"]
    cava = ["comment allez-vous","es que ça va"]
    cherche = ["cherche sur youtube","cherche sur google","cherche sur wikipédia","cherche"]
    actif = True
    while actif:
        entree = reconnaissance()
        if entree is not None:
            for x in range(len(fermer)):
                if fermer[x] in entree.lower():
                    assistant_voix("A bientôt Dounia .")
                    actif = False
            for x in range(len(ouvrir)):
                if ouvrir[x] in entree.lower():
                    application(entree)
                    break
            for x in range(len(cava)):
                if cava[x] in entree.lower():
                    assistant_voix("Je vais bien merci, et vous ?")
                    break
            for x in range(len(cherche)):
                if cherche[x] in entree.lower():
                    sur_le_net(entree)
                    break
           

if __name__ == '__main__':
    main()