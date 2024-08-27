"""
import requests
from bs4 import BeautifulSoup

base_url = "https://www.arcanum.com"
url = "https://www.arcanum.com/hu/online-kiadvanyok/Lexikonok-a-magyar-nyelv-ertelmezo-szotara-1BE8B/a-a-1BFAF/?page=29"

word_dict = {}

for i in range(29, 33):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    target_class = soup.find("div", class_="list-group mb-3")
    links = target_class.find_all("a")

    for link in links:
        new_url = base_url + link["href"]
        new_response = requests.get(new_url)
        new_soup = BeautifulSoup(new_response.content, "html.parser")

        target_div = new_soup.find("div", class_="Lexikonok_PA_LexC_mSz_")

        result = target_div.text.strip().split(" ")[0]
        for word in target_div.text.strip().split(" ")[1:]:
            if (
                word.strip() == ""
                or word.strip()[0].isdigit()
                or "(" in word
                or ")" in word
                or "[" in word
                or "]" in word
                or "," in word
                or ";" in word
                or "*" in word
                or word.strip()[-1] == "."
                or word.strip()[-1] == ".."
                or word.strip()[-1] == "..."
                or word.strip()[-1] == ","
                or word.strip()[-1] == ";"
                or word.strip()[-1] == ":"
                
            ):
                continue
            elif "-" in word:
                for w in word.split("-"):
                    if len(w) >= 3:
                        result += " " + w
            else:
                if len(word) >= 3:
                    result += " " + word

        word_dict[result.strip().split(" ")[0]] = result.strip().split(" ")[1:]
        print(result.strip())
    url = "https://www.arcanum.com/hu/online-kiadvanyok/Lexikonok-a-magyar-nyelv-ertelmezo-szotara-1BE8B/a-a-1BFAF/?page=" + str(i+1)

# a weboldal/ak x adatainak pontos meghatározása és kódja
    
# Szótár tartalmának kiírása
for key, value in word_dict.items():
    print(f"{key}: {value}")
    



#kiiratott szótár adatok elmentése egy txt fileba
with open('dict_output.txt', 'a') as file:
    for key, value in word_dict.items():
        file.write(f"{key}: {value}\n")
"""

#txt file valueinek leggyakoribb szavainak keresése, mellyel a leggyakoribb hibákat is megtalálja a program
with open("dict_output.txt") as file:
    word_counter = {}
    for line in file:
        line = line.strip().split(": ")
        key = line[0]
        values = line[1].split(", ")
        for value in values:
            if value in word_counter:
                word_counter[value] += 1
            else:
                word_counter[value] = 1

top_20 = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)[:100]
for item in top_20:
    print(f"{item[0]}: {item[1]}")


with open("dict_output.txt", "r") as file:
    lines = file.readlines()

with open("dict_output.txt", "w") as file:
    for line in lines:
        line = line.replace("'", '"')
        file.write(line)
#remove_words_be beledobott szavak, azok a gyakori hibák, amik nem valóak, a a txt valueibe, és ezáltal egyszerre távolítjuk el az adathalmazból a hibát, ezzel is felgyorsítjuk a manuális hibakeresést/kezelést
remove_words = ["abb", "jon", "jék", "zon", "ani", "..iája", "..asson", "..kája", "tája", "lag", "..kája", "..tája", "egyes", "zék", "ebb", "..mája", "csak", "zen", "..való", "vája", "..rája", "..vája", "..dája", "ága", "..rája", "..nája", "számban", "irodalmi", "kissé", "főmondatbeli", "üzemi", "<Főként", "abc", "műszaki", "első", "..lma", "leg"]

with open("dict_output.txt", "r") as file:
    lines = file.readlines()

with open("dict_output.txt", "w") as file:
    for line in lines:
        for word in remove_words:
            line = line.replace('"' + word + '"', '')
        file.write(line)

with open("dict_output.txt", "r") as file:
    lines = file.readlines()

with open("dict_output.txt", "w") as file:
    for line in lines:
        # szögletes zárójel benne van-e a sorban
        if "[" in line and "]" in line:
            # szögletes zárójelek közti rész kivágása
            data = line[line.index("[") + 1:line.index("]")]
            # szavak listájának létrehozása a vesszők mentén
            words = data.split(",")
            # fölösleges üres szavak kihagyása
            words = [word.strip() for word in words if word.strip()]
            # új lista stringének létrehozása
            new_data = ", ".join(words)
            # új sor létrehozása az új listával
            new_line = line.replace(data, new_data)
            file.write(new_line)
        else:
            file.write(line)








