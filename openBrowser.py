import re
import webbrowser

doipattern = re.compile("\\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?![\"&\'<>])\S)+)\\b")
# webbrowser.open_new_tab("http://www.baidu.com")

file = open("D:\Google Drive\FreeSurfAlgo\VOF\VOF.txt")
filestring = file.read()

dois = doipattern.findall(filestring)

webbrowser.open("http://", 1)
for doi in dois:
    webbrowser.open_new_tab("https://sci-hub.cc/" + doi)
