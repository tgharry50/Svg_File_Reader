import sys
import tkinter as tk
import customtkinter
from tkinter import filedialog
import os
import re
import shutil
import glob
import subprocess
from PIL import Image, ImageTk
import time
wz_path = None
BigImage_path = None
file_path = None
global img

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mikołaj Harężlak")
        self.resizable(width=False, height=False)
        self.geometry("300x400")
        self.grid_columnconfigure(0, weight=1)
        #UI
        self.button = customtkinter.CTkButton(self, text="Edytuj wzór", command=self.edit, fg_color="green")
        self.button.grid(row=0, column=0, padx=5, pady=2,)
        ##Wzór
        self.button1 = customtkinter.CTkButton(self, text="Wybierz Big", command=self.BigImage_Path, fg_color="blue")
        self.button1.grid(row=1, column=0, padx=5, pady=2)
        ##Big
        self.button2 = customtkinter.CTkButton(self, text="Wybierz SVG", command=self.Svg_Path, fg_color="blue")
        self.button2.grid(row=2, column=0, padx=5, pady=2)
        ##SVG
        self.button3 = customtkinter.CTkButton(self, text="Start", command=self.Start)
        self.button3.grid(row=3, column=0, padx=5, pady=2)
        ##Start


    wzór = "./Example"
    save = "./Result"
    if not os.path.exists(wzór):
        os.makedirs(wzór)
        os.makedirs(save)
        target = os.path.join(wzór, "wzor.txt")
        File = open(target, "w")
        File.write("1_OK\n2_NOK")
        File.close()
    def edit(self):
        subprocess.Popen(["notepad","./Example/wzor.txt"])
    def BigImage_Path(self):
        global BigImage_path
        BigImage_path = filedialog.askdirectory(initialdir="/", title="Wybierz Big image")
        self.button1 = customtkinter.CTkButton(self, text="Wybierz Big", command=self.BigImage_Path, fg_color="green")
        self.button1.grid(row=1, column=0, padx=5, pady=2)
    def Svg_Path(self):
        global file_path
        file_path = filedialog.askopenfilename(title="Wybierz plik SVG")
        self.button2 = customtkinter.CTkButton(self, text="Wybierz SVG", command=self.Svg_Path, fg_color="green")
        self.button2.grid(row=2, column=0, padx=5, pady=2)
    def Start(self):
        BigImage_version = glob.glob(f'{BigImage_path}\*.jpg')
        txt_file = "./Example/wzor.txt"
        tflite_file = "./Example/wzor.tflite"
        with open(file_path, "r") as f:
            svg_data = f.read()
        # Plik wz
        # ROI BIERZE SIE Z GORNEGO ID
        match = re.findall(r'inkscape:label="(.+)"', svg_data)  # ID
        name = match[0]
        # width height x y label na liczbe i _ROI
        select_text = r'</g>([\S\s]*)</g>'
        texter = re.findall(select_text, svg_data)
        textester = " ".join(texter)
        textest = textester.replace(".", ",")
        # print(kamera)
        ###### Podpinanie elementów
        roi_regex = r'<rect'
        roi_matches = re.findall(roi_regex, textest)
        ##width
        roi_regex_width = r'width="(.+)"'
        roi_width = re.findall(roi_regex_width, textest)
        ##height
        roi_regex_height = r'height="(.+)"'
        roi_height = re.findall(roi_regex_height, textest)
        ##x
        roi_regex_x = r'\s[x]="(.+)"'
        roi_x = re.findall(roi_regex_x, textest)
        ##y
        roi_regex_y = r'\s[y]="(.+)"'
        roi_y = re.findall(roi_regex_y, textest)
        ##label
        roi_regex_label = r'"(.+_ROI)"'
        roi_label = re.findall(roi_regex_label, textest)
        print(roi_label)
        ##łączenie elementów
        elements = [roi_width, roi_height, roi_x, roi_y, roi_label]
        ##pętla robocza, przypisanie elementow + wycinanie zdjecia + generacja plikow
        # print( elements )
        for item in range(len(roi_matches)):
            width = roi_width[item]
            height = roi_height[item]
            width = width.replace(',', '.')
            height = height.replace(',', '.')
            x = roi_x[item]
            y = roi_y[item]
            x = x.replace(',', '.')
            y = y.replace(',', '.')
            label = roi_label[item]
            temp = label.split("_")
            smth = temp[0]
            print("TO jest label: ", label)
            print(x,y,width,height)
            # kameras = kamera[item]
            x_final = round(float(x)) + round(float(width))
            y_final = round(float(y)) + round(float(height))
            x_int = round(float(x))
            y_int = round(float(y))
            roi_data = f"({x_int}, {y_int}, {round(float(width))}, {round(float(height))})"
            print(roi_data)
            ##obraz
            for big in BigImage_version:
                Bigimage = Image.open(big)
                Big_Image_Crop = Bigimage.crop((x_int, y_int, x_final, y_final)).resize((299, 299), Image.LANCZOS)
                img = customtkinter.CTkImage(light_image=Big_Image_Crop, dark_image=Big_Image_Crop, size=(250,250))
                self.labes = customtkinter.CTkLabel(self, image=img, width=250, height=250, text = "")
                self.labes.grid(row=5, column=0)
                time.sleep(0.1)
                Big_Image_Crop.save(f"{big}_new_{label}.jpg")
                self.labes.update()
                self.labes.destroy()
            ##Folder
            roi_folder_path = os.path.join(os.path.dirname(file_path), f"{name}_{label}")
            os.makedirs(roi_folder_path, exist_ok=True)
            wasd = file_path.split("/")
            rasd = wasd[:-1]
            nasd = "/".join(rasd)
            with open("./Example/wzor.txt") as fp:
                lines = fp.read().splitlines()
            for file in lines:
                shutil.copy2(txt_file, f'{nasd}/{name}_{smth}.txt')
                shutil.copy2(tflite_file, f'{nasd}/{name}_{smth}.tflite')
            ##Zapis
            for folder_name in lines:
                folder_path = os.path.join(roi_folder_path, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                # Zapisz plik tekstowy z parametrami ROI w katalogu głównym
                output_file_path = os.path.join(os.path.dirname(file_path), f"{name}_{label}.txt")
                with open(output_file_path, "w") as f:
                    f.write(roi_data)
                print(
                    f"Zapisano dane dla ROI {name} w pliku {output_file_path} oraz utworzono foldery dla ROI w katalogu {roi_folder_path}")
            self.button1 = customtkinter.CTkButton(self, text="Wybierz Big", command=self.BigImage_Path,fg_color="blue")
            self.button1.grid(row=1, column=0, padx=5, pady=2)
            self.button2 = customtkinter.CTkButton(self, text="Wybierz SVG", command=self.Svg_Path, fg_color="blue")
            self.button2.grid(row=2, column=0, padx=5, pady=2)

    def _quit(self):
        self.quit()
        self.destroy()
        sys.exit()



app = App()
app.mainloop()