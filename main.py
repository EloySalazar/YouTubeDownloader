import pytube
import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Download youtube videos")
        self.geometry("700x400")
        self.resizable(0,0)
        self.initialize_gui()

    def search(self,url):
        self.yt = pytube.YouTube(url)
        self.label_title.configure(text =  "Title: " + self.yt.title)
        self.label_length.configure(text = "Duracion (seg): "+ str(self.yt.length))
        self.label_description.configure(text = "Description: " + str(self.yt.description))

        self.lstst= self.yt.streams.filter().all()
        self.lis = []

        for st in self.lstst:
            
            self.lis.append(str(f"Type: {st.mime_type},File Size MB: {str(st._filesize_mb)}, Resolution: {st.resolution},Tag: {st.itag}"))
           
        self.menu_option.configure(values = self.lis)
        self.menu_option.set(self.lis[0])
            
    def download(self):
    
        s = [int(s) for s in str.split(self.menu_option.get()) if s.isdigit()]
        print(s)
        st = self.yt.streams.get_by_itag(s[0])
        st.download("")



    def initialize_gui(self):
        self.entry_search = ctk.CTkEntry(self,placeholder_text= "Enter video url",width= 450)
        self.entry_search.place(x = 0, y = 0)

        self.buton_search = ctk.CTkButton(self,text = "Search",command= lambda: self.search(self.entry_search.get()))
        self.buton_search.place(x = 460,y = 0)

        self.label_title = ctk.CTkLabel(self,text = "Title:",font = ("Arial",17))
        self.label_title.place(x = 0, y = 50)

        self.label_length = ctk.CTkLabel(self,text = "Duration (seg):",font = ("Arial",17))
        self.label_length.place(x = 0,y = 100)

        self.label_description = ctk.CTkLabel(self,text = "Description:",font = ("Arial",17))
        self.label_description.place(x = 0,y = 150)

        self.menu_option = ctk.CTkOptionMenu(self,width = 200,font = ("Arial",18),values= [])
        self.menu_option.place(x = 0,y = 200)
        self.menu_option.set("")

        self.buton_donwload = ctk.CTkButton(self,text = "Download",command= self.download)
        self.buton_donwload.place(x = 550,y = 200)

        


app = App()
app.mainloop()