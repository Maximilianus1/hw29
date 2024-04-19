import requests
import json
import os
from tkinter import *
root = Tk()
root.title("DOWNLOADER")
os.chdir(os.getcwd())
def main(id):
    response = requests.get(f'https://jsonplaceholder.org/posts/{id}')
    y = json.loads(response.text)
    os.mkdir(f"file{id}")
    with open(f"file{id}/file{id}.txt","w") as file:
        file.write(str(y))
id_label=Label(root,text="id:",width=20)
id_label.grid(row=1,column=1)
id_num = Entry(root,width=20)
id_num.grid(row=1, column=2)

createFile = Button(root, text="download info with id",command=lambda: main(int(id_num.get())), background="#fcfcd5",width=40)
createFile.grid(row=2, column=1,columnspan=2)

root.mainloop()