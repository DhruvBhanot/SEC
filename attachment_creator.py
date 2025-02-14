import db_interactor
from docx import Document
import os
from datetime import date

def admitionhelper(room):
  info = db_interactor.select(room)
  print(info)
  data ={
    "[first]": info[0],
    "[last]": info[1],
    "[room_dest]": info[2],
    "[id]": info[3],
    "[name]":info[4],
    "[date]": date.today().strftime("%m/%d/%Y"),
    "[level_dest]": "template",
    "[destination]": "template"
    }
  print(data)
  return data
  

def admition(temp_path,storage,room):
 data = admitionhelper(room)
 print(data)
 doc = Document(temp_path)



def main():
 admitionhelper("112")
 

main()