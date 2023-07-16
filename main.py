import sys
import tkinter as tk
import customtkinter
from tkinter import filedialog
import os
import re
import shutil
import glob
from PIL import Image, ImageTk

root = customtkinter
wz_path = None
BigImage_path = None
file_path = None

global img
wz_path = os.path.join(os.path.dirname('__file__'), './Example')

def button_callback_2():
    global BigImage_path
    BigImage_path=filedialog.askdirectory( initialdir = "/", title = "Wybierz Big image" )
    button_2.configure(fg_color = 'green')
def button_callback_3():
    global file_path
    file_path = filedialog.askopenfilename( title = "Wybierz plik SVG" )
    button_3.configure(fg_color = 'green')
def program() :
    # Otwórz okno dialogowe, aby wybrać plik SVG
    root=tk.Tk()
    root.withdraw()
    ## Wyciety fragment wzoru
    splitter=wz_path.split( "/" )
    print(splitter)
    destination="/".join( splitter[:-1] )
    txt_version=glob.glob( f'{wz_path}\*.txt' )  ##txt
    tflite_version = glob.glob( f'{wz_path}\*.tflite' )  ##tflie
    BigImage_version=glob.glob( f'{wz_path}\*.jpg' )  ##BigImageJpg
    print(destination)
    ##ID
    spliters = file_path.split( "/" )
    nazwa=spliters[-1]
    nazwa_edit=nazwa.split( "_" )
    nazwa_końcowa=nazwa_edit[0]

    with open( file_path, "r" ) as f :
        svg_data=f.read()

    # Plik wz
    # ROI BIERZE SIE Z GORNEGO ID
    match=re.findall( r'inkscape:label="(.+)"', svg_data )  # ID
    name = match[0]
    print(name)
    # camera = re.findall(r'\s+style=.+\s+id="\D+(.+)"', svg_data) #id kamery
    # kamera = camera

    # width height x y label na liczbe i _ROI
    select_text = r'</g>([\S\s]*)</g>'
    texter=re.findall( select_text, svg_data )
    textester=" ".join( texter )
    textest=textester.replace( ".", "," )
    # print(kamera)
    ###### Podpinanie elementów
    roi_regex=r'<rect'
    roi_matches=re.findall( roi_regex, textest )
    ##id
    roi_regex_id=nazwa_końcowa
    ##width
    roi_regex_width=r'width="(.+)"'
    roi_width=re.findall( roi_regex_width, textest )
    ##height
    roi_regex_height=r'height="(.+)"'
    roi_height=re.findall( roi_regex_height, textest )
    ##x
    roi_regex_x=r'\s[x]="(.+)"'
    roi_x=re.findall( roi_regex_x, textest )
    ##y
    roi_regex_y=r'\s[y]="(.+)"'
    roi_y=re.findall( roi_regex_y, textest )
    ##label
    roi_regex_label=r'"(.+_ROI)"'
    roi_label=re.findall( roi_regex_label, textest )
    print(roi_label)
    #print( roi_label )
    ##łączenie elementów
    elements=[roi_width, roi_height, roi_x, roi_y, roi_label]
    ##pętla robocza, przypisanie elementow + wycinanie zdjecia + generacja plikow
    #print( elements )
    for item in range( len( roi_matches ) ) :
        width=roi_width[item]
        height=roi_height[item]
        width=width.replace( ',', '.' )
        height=height.replace( ',', '.' )
        x=roi_x[item]
        y=roi_y[item]
        x=x.replace( ',', '.' )
        y=y.replace( ',', '.' )
        print( x, y )
        label=roi_label[item]
        # kameras = kamera[item]
        roi_data=f"({x}, {y}, {width}, {height})"
        print( roi_data )
        x_final=round( int( float( x ) ) + round( int( float( width ) ) ) )
        y_final=round( int( float( y ) ) + round( int( float( height ) ) ) )
        x_int=round( int( float( x ) ) )
        y_int=round( int( float( y ) ) )
        roi_data=f"({x_int}, {y_int}, {width}, {height})"
        print( roi_data )
        print( x_final, y_final, x_int, y_int )
        ##obraz
        for big in BigImage_version :
            print( big )
            Bigimage=Image.open( big )
            Big_Image_Crop = Bigimage.crop( (x_int, y_int, x_final, y_final))
            func(Big_Image_Crop)
            Big_Image_Crop = Big_Image_Crop.save( f"{big}_new_{label}.jpg" )
        ##Folder
        roi_folder_path=os.path.join( os.path.dirname( file_path ), f"{name}_{label}" )
        os.makedirs( roi_folder_path, exist_ok = True )
        for file in ["1_OK", "2_NOK"] :
            for filex in txt_version :
                shutil.copy2( filex, f'{destination}/{name}.txt' )
            for file_tfile in tflite_version :
                shutil.copy2( file_tfile, f'{destination}/{name}.tflite' )
        ##Zapis
        for folder_name in ["1_OK", "2_NOK"] :
            folder_path=os.path.join( roi_folder_path, folder_name )
            os.makedirs( folder_path, exist_ok = True )
            # Zapisz plik tekstowy z parametrami ROI w katalogu głównym
            output_file_path=os.path.join( os.path.dirname( file_path ), f"{name}_{label}.txt" )
            with open( output_file_path, "w" ) as f :
                f.write( roi_data )
            print(
                f"Zapisano dane dla ROI {name} w pliku {output_file_path} oraz utworzono foldery dla ROI w katalogu {roi_folder_path}" )


def func(item):
    img = customtkinter.CTkImage(item, size = (250, 250) )
    labels = customtkinter.CTkLabel(master = frame_1, width = 300, height = 300, image = img, text = '' )
    labels.pack()
    labels.update()
    def function():
        labels.destroy()
    app.after(100, function())
    app.update()

def _quit():
    app.quit()
    app.destroy()
    sys.exit()

#----------------------------------------------------GUI--------------------------------
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("600x680")
app.title("Testing_set_1.py")


frame_1=customtkinter.CTkFrame( master = app )
frame_1.pack( pady = 20, padx = 60, fill = "both", expand = True )

label_1=customtkinter.CTkLabel( master = frame_1, justify = customtkinter.LEFT, text = 'Program' )
label_1.pack( pady = 10, padx = 10 )

button_2 = customtkinter.CTkButton( master = frame_1,text = "Wybierz Big image", command = button_callback_2)
button_2.pack( pady = 20, padx = 20 )

button_3=customtkinter.CTkButton( master = frame_1,text = "Wybierz plik SVG", command = button_callback_3)
button_3.pack( pady = 20, padx = 20 )

button_4=customtkinter.CTkButton( master = frame_1, text = 'Start',command = program)
button_4.pack( pady = 20, padx = 20 )

app.protocol("WM_DELETE_WINDOW", _quit)


app.mainloop()




