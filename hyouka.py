# coding: UTF-8
import csv
from urllib.request import urlopen
import re
import requests
from bs4 import BeautifulSoup

urllist = [line.rstrip() for line in open('rank.txt')]

cnt = 0
for url in urllist:
   print (url)
   # URLにアクセスする htmlが帰ってくる
   html = urlopen(url)

   # htmlをBeautifulSoupで扱う
   soup = BeautifulSoup(html, "html.parser")

   #テーブルを指定
   table = soup.findAll("table", class_="table")[2]

   table2 = table.findAll("table", class_="table")[3]
   rows = table2.findAll("tr")

#table3 = table.findAll("table", class_="table")[4]
#rows2 = table3.findAll("tr")

   cnt = cnt + 1
   csvFile = open("hyouka_"+ str(cnt) +".csv", 'wt', newline = '', encoding = 'utf-8')
   writer = csv.writer(csvFile)

#csvFile2 = open("hyouka2.csv", 'wt', newline = '', encoding = 'utf-8')
#writer2 = csv.writer(csvFile2)

   try:
      for row in rows:
         csvRow = []
         for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
         writer.writerow(csvRow)

#   for row2 in rows2:
#      csvRow2 = []
#      for cell2 in row2.findAll(['td', 'th']):
#         csvRow2.append(cell2.get_text())
#      writer2.writerow(csvRow2)

   finally:
       csvFile.close()
#    csvFile2.close()

