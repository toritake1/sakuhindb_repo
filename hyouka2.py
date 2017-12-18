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
   table = soup.findAll("table", class_="table")[1]

   table2 = table.findAll("table", class_="table")[3]
   rows = table2.findAll("tr")

   cnt = cnt + 1
   csvFile = open("hyouka_"+ str(cnt) +".csv", 'wt', newline = '', encoding = 'utf-8')
   writer = csv.writer(csvFile)

   for row in rows:
      csvRow = []
      for cell in row.findAll(['td', 'th']):
         csvRow.append(cell.get_text())
      writer.writerow(csvRow)

   csvFile.close()

