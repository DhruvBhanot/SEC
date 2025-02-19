import db_interactor
from docx import Document
import os
from datetime import date

def admitionhelper(room):
  info = db_interactor.select(room)
  current = date.today().strftime("%m/%d/%Y")
  print(current)
  data ={
    '[header]': 'Admittion',
    "[date]": str(current),
    "[first]": info[0],
    "[last]": info[1],
    "[room_dest]": info[2],
    "[id]": info[3],
    "[home]":info[4],
    "[level_dest]": "we",
    "[destination]": "win",
    '[current]': 'Bn'
    }
  
  return data
  

def admition(temp_path,storage,room):
 data = admitionhelper(room)
 print(data)
 doc = Document(temp_path)
 for paragraph in doc.paragraphs:
   for key, val in data.items():
     for run in paragraph.runs:
       run.text = run.text.replace(key,val)

 doc.save(storage)
 print("save")

def main():
  
    #admition()
 

main()


def main():
 admitionhelper("112")
 

main()
