import os
import email_auto
import attachment_creator




def startup():
 if not os.path.exists('C:/AImail'):
  os.mkdir('C:/AImail')
  os.mkdir('C:/AImail/a')
  os.mkdir('C:/AImail/b')
  os.mkdir('C:/AImail/c')
  os.mkdir('C:/AImail/d')
  print('created folders')
 else:
  print('satisfied library conditions')

  

# def admission():
  

# def expired():

# def transfer():

# def loa():

def main():
 startup()

main()