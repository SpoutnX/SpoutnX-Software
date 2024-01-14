from fpdf import FPDF
import os
import numpy as np
from PySide6.QtWidgets import (QFileDialog)
import datetime


def printPDF():
    user = os.getlogin()
    Path = "/home/" + user + "/.SpoutnX/"
    path2 = Path + "data.sptx"
    path4 = Path + "lang/user_lang.sptx"
    path5 = Path + "pngplot.png"

    mes_nombres = open(path4).read()
    L = mes_nombres.split('\n')

    S = np.loadtxt(path2)

    pdf = FPDF()
    pdf.add_page()

    x1 = int(S[23])
    x2 = int(S[33])

    # Affichage du titre
    pdf.set_fill_color(r=62, g=247, b=36)
    pdf.set_font("Arial", size=18)
    w = pdf.get_string_width(L[x2]) + 16
    pdf.set_y(15)
    pdf.set_x((210 - w) / 2)
    pdf.cell(w, 15, txt=L[x2], border=1, ln=1, align="C", fill=True)

    # Affichage des Infos de haut de page: Date, utilisateur...
    Date = datetime.datetime.today()
    print(Date)
    Date = str(Date)
    InfosPage = Date + "       Made by: " + user + " using the software SpoutnX"
    pdf.set_font("Arial", size=9)
    pdf.set_y(10)
    pdf.set_x((210 - w) / 2)
    pdf.cell(20, 2, txt=InfosPage, border=0, ln=1, align="C", fill=False)

    # Affichage des données utilisateur

    pdf.set_font("Arial", size=12)
    w2 = pdf.get_string_width(L[183])+100
    pdf.set_y(33)
    pdf.set_x((210 - w2) / 2)
    pdf.cell(w2, 8, txt=L[183], border=1, ln=1, align="C", fill=False)

    S24 = "{:.3e}".format(S[24])
    w2 = pdf.get_string_width(L[x1])+10
    pdf.set_y(40)
    pdf.set_x((100 - w2) / 2)
    pdf.cell(w2, 20, txt=L[x1] + ":  " + S24, border=0, ln=2, align="C")

    if S[25] != 0:
        x3 = int(S[25])
        S26 = "{:.3e}".format(S[26])
        pdf.set_font("Arial", size=11)
        pdf.set_y(40)
        w3 = pdf.get_string_width(L[x3])+10
        pdf.set_x((330 - w3) / 2)
        pdf.cell(w3, 20, txt=L[x3] + ":  " + S26, ln=1, align="C")

    if S[27] != 0:
        x4 = int(S[27])
        S28 = "{:.3e}".format(S[28])
        w4 = pdf.get_string_width(L[x4])+10
        pdf.set_y(50)
        pdf.set_x((100 - w4) / 2)
        pdf.cell(w4, 20, txt=L[x4] + ":  " + S28, border=0, ln=2, align="C")

    if S[29] != 0:
        x5 = int(S[29])
        S30 = "{:.3e}".format(S[30])
        pdf.set_font("Arial", size=11)
        pdf.set_y(50)
        w5 = pdf.get_string_width(L[x5])+10
        pdf.set_x((330 - w5) / 2)
        pdf.cell(w5, 20, txt=L[x5] + ":  " + S30, ln=1, align="C")

    if S[31] != 0:
        x6 = int(S[31])
        S32 = "{:.3e}".format(S[32])
        w6 = pdf.get_string_width(L[x6])+10
        pdf.set_y(60)
        pdf.set_x((100 - w6) / 2)
        pdf.cell(w6, 20, txt=L[x6] + ":  " + S32, border=0, ln=2, align="C")

    pdf.set_font("Arial", size=16)

    # Affichage des Résultats

    pdf.set_fill_color(r=62, g=247, b=36)
    w7 = pdf.get_string_width(L[29]) + 16
    pdf.set_y(75)
    pdf.set_x((210 - w7) / 2)
    pdf.cell(w7, 10, txt=L[29], ln=1, align="C", fill=True)

    pdf.set_font("Arial", style="B", size=14)  # Affichage sous-titre 1
    x14 = int(S[34])
    pdf.set_fill_color(r=62, g=247, b=36)
    w14 = pdf.get_string_width(L[x14]) + 16
    pdf.set_y(85)
    pdf.set_x((210 - w14) / 2)
    pdf.cell(w14, 10, txt=L[x14], ln=1, align="C")

    pdf.set_font("Arial", size=12)

    x8 = int(S[35])
    y8 = str(S[36])
    w8 = pdf.get_string_width(L[x8] + ":   " + y8) + 16
    pdf.set_y(95)
    pdf.set_x((210 - w8) / 2)
    pdf.cell(w8, 10, txt=L[x8] + ":   " + y8, ln=1, align="C")

    if S[37] != 0:
        x9 = int(S[37])
        y9 = str(S[38])
        w9 = pdf.get_string_width(L[x9] + ":   " + y9) + 16
        pdf.set_y(105)
        pdf.set_x((210 - w9) / 2)
        pdf.cell(w9, 10, txt=L[x9] + ":   " + y9, ln=1, align="C")

    if S[39] != 0:
        x10 = int(S[39])
        y10 = str(S[40])
        w10 = pdf.get_string_width(L[x10] + ":   " + y10) + 16
        pdf.set_y(115)
        pdf.set_x((210 - w10) / 2)
        pdf.cell(w10, 10, txt=L[x10] + ":   " + y10, ln=1, align="C")

    if S[41] != 0:
        x11 = int(S[41])
        y11 = str(S[42])
        w11 = pdf.get_string_width(L[x11] + ":   " + y11) + 16
        pdf.set_y(125)
        pdf.set_x((210 - w11) / 2)
        pdf.cell(w11, 10, txt=L[x11] + ":   " + y11, ln=1, align="C")

    if S[43] != 0:          # Affichage type trou noir de Kerr
        pdf.set_font("Arial", style="B", size=12)
        x13 = int(S[43])
        w13 = pdf.get_string_width(L[x13]) + 16
        pdf.set_y(130)
        pdf.set_x((210 - w13) / 2)
        pdf.cell(w13, 10, txt=L[x13], ln=1, align="C")

    # Deuxième plage de données
    print(S[44])
    if S[44] != 0:
        pdf.set_font("Arial", style="B", size=14)  # Affichage sous-titre 2
        x15 = int(S[44])
        pdf.set_fill_color(r=62, g=247, b=36)
        w15 = pdf.get_string_width(L[x15]) + 16
        pdf.set_y(147)
        pdf.set_x((210 - w15) / 2)
        pdf.cell(w15, 10, txt=L[x15], ln=1, align="C")

        pdf.set_font("Arial", size=12)

        x16 = int(S[45])
        y16 = str(S[46])
        w16 = pdf.get_string_width(L[x16] + ":   " + y16) + 16
        pdf.set_y(155)
        pdf.set_x((210 - w16) / 2)
        pdf.cell(w16, 10, txt=L[x16] + ":   " + y16, ln=1, align="C")

        if S[47] != 0:
            x17 = int(S[47])
            y17 = str(S[48])
            w17 = pdf.get_string_width(L[x17] + ":   " + y17) + 16
            pdf.set_y(165)
            pdf.set_x((210 - w17) / 2)
            pdf.cell(w17, 10, txt=L[x17] + ":   " + y17, ln=1, align="C")

        if S[49] != 0:
            x18 = int(S[49])
            y18 = str(S[50])
            w18 = pdf.get_string_width(L[x18] + ":   " + y18) + 16
            pdf.set_y(175)
            pdf.set_x((210 - w18) / 2)
            pdf.cell(w18, 10, txt=L[x18] + ":   " + y18, ln=1, align="C")

        if S[51] != 0:
            x19 = int(S[51])
            y19 = str(S[52])
            w19 = pdf.get_string_width(L[x19] + ":   " + y19) + 16
            pdf.set_y(185)
            pdf.set_x((210 - w19) / 2)
            pdf.cell(w19, 10, txt=L[x19] + ":   " + y19, ln=1, align="C")

    # Affichage de la visualisation

    if S[53] == 1:
        try:
            pdf.set_font("Arial", size=16)

            pdf.set_fill_color(r=62, g=247, b=36)
            w20 = pdf.get_string_width(L[182]) + 16
            pdf.set_y(240)
            pdf.set_x(15)
            pdf.cell(w20, 10, txt=L[182], ln=1, align="C", fill=True)

            pdf.image(path5, x=100, y=197, w=100, h=100)
        except:
            pass

    filename = QFileDialog.getSaveFileName()
    file2 = str(filename[0])
    file2 = (file2 + ".pdf")
    pdf.output(file2)
