import sys #line:1
import tkinter as tk #line:2
import customtkinter #line:3
from tkinter import filedialog #line:4
import os #line:5
import re #line:6
import shutil #line:7
import glob #line:8
import subprocess #line:9
from PIL import Image #line:10
import time #line:11
wz_path =None #line:12
BigImage_path =None #line:13
file_path =None #line:14
global img #line:15
class App (customtkinter .CTk ):#line:17
    def __init__ (OOO0000O000OO0O0O ):#line:18
        super ().__init__ ()#line:19
        OOO0000O000OO0O0O .title ("Mikołaj Harężlak")#line:21
        OOO0000O000OO0O0O .resizable (width =False ,height =False )#line:22
        OOO0000O000OO0O0O .geometry ("300x400")#line:23
        OOO0000O000OO0O0O .grid_columnconfigure (0 ,weight =1 )#line:24
        OOO0000O000OO0O0O .button =customtkinter .CTkButton (OOO0000O000OO0O0O ,text ="Edid example",command =OOO0000O000OO0O0O .edit ,fg_color ="green")#line:26
        OOO0000O000OO0O0O .button .grid (row =0 ,column =0 ,padx =5 ,pady =2 ,)#line:27
        OOO0000O000OO0O0O .button1 =customtkinter .CTkButton (OOO0000O000OO0O0O ,text ="Select BIG file",command =OOO0000O000OO0O0O .BigImage_Path ,fg_color ="blue")#line:29
        OOO0000O000OO0O0O .button1 .grid (row =1 ,column =0 ,padx =5 ,pady =2 )#line:30
        OOO0000O000OO0O0O .button2 =customtkinter .CTkButton (OOO0000O000OO0O0O ,text ="Select SVG file",command =OOO0000O000OO0O0O .Svg_Path ,fg_color ="blue")#line:32
        OOO0000O000OO0O0O .button2 .grid (row =2 ,column =0 ,padx =5 ,pady =2 )#line:33
        OOO0000O000OO0O0O .button3 =customtkinter .CTkButton (OOO0000O000OO0O0O ,text ="Start",command =OOO0000O000OO0O0O .Start )#line:35
        OOO0000O000OO0O0O .button3 .grid (row =3 ,column =0 ,padx =5 ,pady =2 )#line:36
    wzór ="./Example"#line:40
    conf ="./Config"#line:41
    if not os .path .exists (wzór ):#line:42
        os .makedirs (wzór )#line:43
        target =os .path .join (wzór ,"example.txt")#line:44
        target2 =os .path .join (wzór ,"ok_only.txt")#line:45
        File =open (target ,"w")#line:47
        File .write ("1_OK\n2_NOK")#line:48
        File .close ()#line:49
        File2 =open (target2 ,"w")#line:51
        File2 .write ("1_OK\n1_OK")#line:52
        File2 .close ()#line:53
    if not os .path .exists (conf ):#line:56
        os .makedirs (conf )#line:57
        target3 =os .path .join (conf ,"config.txt")#line:58
        File3 =open (target3 ,"w")#line:60
        File3 .write ("w=242\nh=242")#line:61
        File3 .close ()#line:62
    def edit (O00O00O00O00OOOOO ):#line:64
        subprocess .Popen (["notepad","./Example/example.txt"])#line:65
    def BigImage_Path (O00O000OOOOOO0O00 ):#line:66
        global BigImage_path #line:67
        BigImage_path =filedialog .askdirectory (initialdir ="/",title ="Select BIG file")#line:68
        O00O000OOOOOO0O00 .button1 =customtkinter .CTkButton (O00O000OOOOOO0O00 ,text ="Select BIG file",command =O00O000OOOOOO0O00 .BigImage_Path ,fg_color ="green")#line:69
        O00O000OOOOOO0O00 .button1 .grid (row =1 ,column =0 ,padx =5 ,pady =2 )#line:70
    def Svg_Path (OO0O0OOO00OOO00OO ):#line:71
        global file_path #line:72
        file_path =filedialog .askopenfilename (title ="Select SVG file")#line:73
        OO0O0OOO00OOO00OO .button2 =customtkinter .CTkButton (OO0O0OOO00OOO00OO ,text ="Select SVG file",command =OO0O0OOO00OOO00OO .Svg_Path ,fg_color ="green")#line:74
        OO0O0OOO00OOO00OO .button2 .grid (row =2 ,column =0 ,padx =5 ,pady =2 )#line:75
    def Start (O0OO00OOOO0OO0OOO ):#line:76
        OOOOO00OOO0OO00OO =glob .glob (f'{BigImage_path}/*.jpg')#line:77
        OO0OOO00OO0OOOO00 ="./Example/example.txt"#line:78
        O00OO00OOOOOO0OO0 ="./Example/example.tflite"#line:79
        OOO00000OOOOO0O00 ="./Example/ok_only.txt"#line:80
        OO00O0OO0000OOOO0 ="./Config/config.txt"#line:82
        O0000OO00OO00O000 =open (OO00O0OO0000OOOO0 ,"r")#line:83
        O0O0O0O0000O0OO0O =O0000OO00OO00O000 .read ()#line:84
        O000000OOOO00000O =re .findall (r'w=(.+)',O0O0O0O0000O0OO0O )#line:85
        OOOO0O00O00OOO000 =O000000OOOO00000O [0 ]#line:86
        O00O000O0OO0O00O0 =int (OOOO0O00O00OOO000 )#line:87
        O0OO0O00O0000O000 =re .findall (r'h=(.+)',O0O0O0O0000O0OO0O )#line:88
        OOOO0OOOO0O00O0OO =O0OO0O00O0000O000 [0 ]#line:89
        OOOOOOO00O0O00000 =int (OOOO0OOOO0O00O0OO )#line:90
        with open (file_path ,"r")as O0OOOOOO00O00O00O :#line:92
            OO000OOO00O0OOOOO =O0OOOOOO00O00O00O .read ()#line:93
        O0O0000O00OO0OO00 =re .findall (r'inkscape:label="(.+)"',OO000OOO00O0OOOOO )#line:96
        OOO0O0OO00OO000O0 =O0O0000O00OO0OO00 [0 ]#line:97
        O00OO00O0O0OO0OO0 =r'</g>([\S\s]*)</g>'#line:99
        OOOOO0OO000OO000O =re .findall (O00OO00O0O0OO0OO0 ,OO000OOO00O0OOOOO )#line:100
        O0OO000OOO000000O =" ".join (OOOOO0OO000OO000O )#line:101
        OO0000O0OO00OOOO0 =O0OO000OOO000000O .replace (".",",")#line:102
        O000OO0O0OO0O0O0O =r'<rect'#line:105
        OOOO0OOOO0OO0O000 =re .findall (O000OO0O0OO0O0O0O ,OO0000O0OO00OOOO0 )#line:106
        OO00O0O0O0O0OO000 =r'width="(.+)"'#line:108
        O0OOOO00O000OO000 =re .findall (OO00O0O0O0O0OO000 ,OO0000O0OO00OOOO0 )#line:109
        O0OO0O0000000OO0O =r'height="(.+)"'#line:111
        O000OO000O000000O =re .findall (O0OO0O0000000OO0O ,OO0000O0OO00OOOO0 )#line:112
        O0O0O00O00OOOOO0O =r'\s[x]="(.+)"'#line:114
        OOO0OOO0OO00OO0O0 =re .findall (O0O0O00O00OOOOO0O ,OO0000O0OO00OOOO0 )#line:115
        OO0OOO0OO000O0OOO =r'\s[y]="(.+)"'#line:117
        OOO00O0000O0O0O00 =re .findall (OO0OOO0OO000O0OOO ,OO0000O0OO00OOOO0 )#line:118
        OOOOOO0000OOOOO00 =r'"(.+_ROI)"'#line:120
        O0OOO0OOOO0O00000 =re .findall (OOOOOO0000OOOOO00 ,OO0000O0OO00OOOO0 )#line:121
        print (O0OOO0OOOO0O00000 )#line:122
        OO000O0OO00O0OOOO =[O0OOOO00O000OO000 ,O000OO000O000000O ,OOO0OOO0OO00OO0O0 ,OOO00O0000O0O0O00 ,O0OOO0OOOO0O00000 ]#line:124
        for OO000OOO0OOOO0OO0 in range (len (OOOO0OOOO0OO0O000 )):#line:127
            O0O0O0O0OO0O0OO00 =O0OOOO00O000OO000 [OO000OOO0OOOO0OO0 ]#line:128
            OOO0O0O00O00O0OOO =O000OO000O000000O [OO000OOO0OOOO0OO0 ]#line:129
            O0O0O0O0OO0O0OO00 =O0O0O0O0OO0O0OO00 .replace (',','.')#line:130
            OOO0O0O00O00O0OOO =OOO0O0O00O00O0OOO .replace (',','.')#line:131
            OO0000000O000O00O =OOO0OOO0OO00OO0O0 [OO000OOO0OOOO0OO0 ]#line:132
            OOO0O0OO0OO00O00O =OOO00O0000O0O0O00 [OO000OOO0OOOO0OO0 ]#line:133
            OO0000000O000O00O =OO0000000O000O00O .replace (',','.')#line:134
            OOO0O0OO0OO00O00O =OOO0O0OO0OO00O00O .replace (',','.')#line:135
            OOO000OOO0OOOOOOO =O0OOO0OOOO0O00000 [OO000OOO0OOOO0OO0 ]#line:136
            O00OO0OO0OO0OOOO0 =OOO000OOO0OOOOOOO .split ("_")#line:137
            OOOOOO00000O0OO00 =O00OO0OO0OO0OOOO0 [0 ]#line:138
            OO00OOOO0OOO0O00O =round (float (OO0000000O000O00O ))+round (float (O0O0O0O0OO0O0OO00 ))#line:140
            OO0OO0OOOO00OOO00 =round (float (OOO0O0OO0OO00O00O ))+round (float (OOO0O0O00O00O0OOO ))#line:141
            OOOO00OOO0000O000 =round (float (OO0000000O000O00O ))#line:142
            OO00O0O0O000O0O00 =round (float (OOO0O0OO0OO00O00O ))#line:143
            OO00O000OOOOO0OO0 =f"({OOOO00OOO0000O000}, {OO00O0O0O000O0O00}, {round(float(O0O0O0O0OO0O0OO00))}, {round(float(OOO0O0O00O00O0OOO))})"#line:144
            for O00O00O0O0OO0O000 in OOOOO00OOO0OO00OO :#line:146
                OOOO00OOOOO000OO0 =Image .open (O00O00O0O0OO0O000 )#line:147
                O0000O00O00O0OO0O =OOOO00OOOOO000OO0 .crop ((OOOO00OOO0000O000 ,OO00O0O0O000O0O00 ,OO00OOOO0OOO0O00O ,OO0OO0OOOO00OOO00 )).resize ((O00O000O0OO0O00O0 ,OOOOOOO00O0O00000 ),Image .LANCZOS )#line:148
                OOOOOO00O0OO0O00O =customtkinter .CTkImage (light_image =O0000O00O00O0OO0O ,dark_image =O0000O00O00O0OO0O ,size =(250 ,250 ))#line:149
                O0OO00OOOO0OO0OOO .labes =customtkinter .CTkLabel (O0OO00OOOO0OO0OOO ,image =OOOOOO00O0OO0O00O ,width =250 ,height =250 ,text ="")#line:150
                O0OO00OOOO0OO0OOO .labes .grid (row =5 ,column =0 )#line:151
                time .sleep (0.1 )#line:152
                O0000O00O00O0OO0O .save (f"{O00O00O0O0OO0O000}_new_{OOO000OOO0OOOOOOO}.jpg")#line:153
                O0OO00OOOO0OO0OOO .labes .update ()#line:154
                O0OO00OOOO0OO0OOO .labes .destroy ()#line:155
            O00O00O00O00OO000 =os .path .join (os .path .dirname (file_path ),f"{OOO0O0OO00OO000O0}_{OOO000OOO0OOOOOOO}")#line:157
            OOO0OO000O00O000O =os .path .join (os .path .dirname (file_path ),"OK_only")#line:158
            os .makedirs (O00O00O00O00OO000 ,exist_ok =True )#line:159
            os .makedirs (OOO0OO000O00O000O ,exist_ok =True )#line:160
            O00OOOOOOOO0O0O0O =file_path .split ("/")#line:161
            OO0OOO0O00000O0O0 =O00OOOOOOOO0O0O0O [:-1 ]#line:162
            O00OOO0OOO000O00O ="/".join (OO0OOO0O00000O0O0 )#line:163
            print (f'{O00OOO0OOO000O00O} < nasd')#line:164
            with open ("./Example/example.txt")as OO0000OOO0O00OO0O :#line:165
                OO0O000O00O00OO0O =OO0000OOO0O00OO0O .read ().splitlines ()#line:166
            shutil .copy2 (OO0OOO00OO0OOOO00 ,f'{O00OOO0OOO000O00O}/{OOO0O0OO00OO000O0}_{OOOOOO00000O0OO00}.txt')#line:167
            shutil .copy2 (O00OO00OOOOOO0OO0 ,f'{O00OOO0OOO000O00O}/{OOO0O0OO00OO000O0}_{OOOOOO00000O0OO00}.tflite')#line:168
            shutil .copy2 (OOO00000OOOOO0O00 ,f'{O00OOO0OOO000O00O}/OK_only/{OOO0O0OO00OO000O0}_{OOOOOO00000O0OO00}.txt')#line:169
            for O0O00OOO0O000000O in OO0O000O00O00OO0O :#line:171
                O000O0OO0OOOOO0O0 =os .path .join (O00O00O00O00OO000 ,O0O00OOO0O000000O )#line:172
                os .makedirs (O000O0OO0OOOOO0O0 ,exist_ok =True )#line:173
                OOO00O00000O0OOOO =os .path .join (os .path .dirname (file_path ),f"{OOO0O0OO00OO000O0}_{OOO000OOO0OOOOOOO}.txt")#line:175
                with open (OOO00O00000O0OOOO ,"w")as O0OOOOOO00O00O00O :#line:176
                    O0OOOOOO00O00O00O .write (OO00O000OOOOO0OO0 )#line:177
            O0OO00OOOO0OO0OOO .button1 =customtkinter .CTkButton (O0OO00OOOO0OO0OOO ,text ="Select BIG file",command =O0OO00OOOO0OO0OOO .BigImage_Path ,fg_color ="blue")#line:178
            O0OO00OOOO0OO0OOO .button1 .grid (row =1 ,column =0 ,padx =5 ,pady =2 )#line:179
            O0OO00OOOO0OO0OOO .button2 =customtkinter .CTkButton (O0OO00OOOO0OO0OOO ,text ="Select SVG file",command =O0OO00OOOO0OO0OOO .Svg_Path ,fg_color ="blue")#line:180
            O0OO00OOOO0OO0OOO .button2 .grid (row =2 ,column =0 ,padx =5 ,pady =2 )#line:181
    def _quit (O0OO00O00O0000OO0 ):#line:183
        O0OO00O00O0000OO0 .quit ()#line:184
        O0OO00O00O0000OO0 .destroy ()#line:185
        sys .exit ()#line:186
app =App ()#line:187
app .mainloop ()