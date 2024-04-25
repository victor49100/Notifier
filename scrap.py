import requests
import datetime
import bs4

fileChapter = open("/home/major/Téléchargements/scrapper/Chapter.txt", "r")
Chapter = fileChapter.read()
fileChapter.close()
chapitreSemaine = "#" + Chapter
url = "https://discord.com/api/webhooks//VnLszwU_2oKnxJ39550VPSkYu55lWEftrYWtL72MUowk1Hg2uqGWeFc557ZvrOdcfGwg?username=major&avatar_url=https://i.imgur.com/4M34hi2.png&content=message"
myobj = {"content": "Le nouveau chapitre "+str(int(Chapter)+1)+" est sorti ma boiii \n https://mangamoins.shaeishu.co/?q=one+piece"}

def check_chapitre(data):
    if chapitreSemaine in data:
        return True
    else:
        return False

def ecrire_dans_log(message):
    # Ouvre le fichier de log en mode append (ajout) pour écrire à la fin
    with open("/home/major/Téléchargements/scrapper/log.txt", "a") as fichier_log:
        heure_actuelle = datetime.datetime.now()
        heure_formattee = heure_actuelle.strftime("%Y-%m-%d %H:%M:%S")
        fichier_log.write(f"{heure_formattee} : {message}\n")
        fichier_log.close()

r = requests.get("https://mangamoins.shaeishu.co/?q=One+piece")
response = r.status_code
page_html = r.text

soup = bs4.BeautifulSoup(page_html, 'html.parser')
H3 = soup.h3.prettify()

if (check_chapitre(H3)):
    try:
      newChapter = int(Chapter) + 1
      requests.post(url, json=myobj)
      ecrire_dans_log("Chapter !")
      with open("/home/major/Téléchargements/scrapper/Chapter.txt", "w") as fileChapter:
        fileChapter.write(str(newChapter))
    except:
      ecrire_dans_log("discord Unreacheable")
else:
    ecrire_dans_log("No Chapter")


