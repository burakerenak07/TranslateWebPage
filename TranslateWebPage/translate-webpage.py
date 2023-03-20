from bs4 import BeautifulSoup
import os,fileinput
from deep_translator import GoogleTranslator


def translator():
    translatedlist=[]
    mydict={}
    htmlfilescount=0

    #The part that lists the html and htm files.
    path="C:/Users/burak/Desktop/c1"
    htmlfiles = [os.path.join(root, name)
                for root,dirr, files in os.walk(path)
                for name in files
                if name.endswith((".html", ".htm"))]
    
    
    #Navigating the files that the list contains.
    while htmlfilescount<len(htmlfiles):
        try:
            with open(htmlfiles[htmlfilescount],"r",encoding="utf-8",errors="ignore") as fp:
                soup=BeautifulSoup(fp,"html.parser")
                soup.prettify()

            for s in soup.select('style'):
                s.extract()
            for s in soup.select('script'):
                s.extract()


            soup.find_all(string=True)
            text=(soup.find_all(string=True))
            text = [item.strip() for item in text if item.strip()]

            #Removing of the words that may cause errors from the list.
            elements_to_remove = ["/","html","content","in","or"]

            text = [elem for elem in text if elem not in elements_to_remove]
            #Translate part of the list elements and appending to new list.
            for i, word in enumerate(text):
            
                translatedText = GoogleTranslator(source='auto',target='hi').translate(word)
                translatedlist.append(translatedText)

            #Combining the sentence snippets to be translated and the translated snippets with the dictionary.
            for key in text:
                for value in translatedlist:
                    mydict[key] = value
                    translatedlist.remove(value)
                    break
    
            count=1
            for k,v in mydict.items():
   
                #Detection and removal of the none parts of the dictionary structure from the dictionary
                if v is None:
                    del[mydict[k]]

                # It is the part where the translated sentence parts in the file are written to the file.
                with fileinput.FileInput(htmlfiles[htmlfilescount], inplace=True, backup=".bak",encoding="utf-8") as file:
                        for line in file:
                                print(line.replace(k, v), end='')
                count+=1
            htmlfilescount+=1
        except:
                htmlfilescount+=1
                print("File error. Moved to other sections.")
                pass

translator()
