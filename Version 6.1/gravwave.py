######################### SCRIPT ONDES GRAVITATIONNELLES#######################

import numpy as np
from math import *
import os
import numpy
import webbrowser
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QWidget,
    QLineEdit,
    QDoubleSpinBox
)

from PySide6.QtGui import QIcon, QPixmap

user = os.getlogin()
Path = "/home/" + user + "/.SpoutnX/"
path2 = Path + "data.sptx"
path3 = Path + "user_data.txt"
path4 = Path + "lang/user_lang.sptx"

mes_nombres = open(path4).read()
L = mes_nombres.split('\n')
winCaracteristiques = QWidget()
winCaracteristiques.setWindowTitle("Caractéristiques")
winCaracteristiques.setFixedSize(QSize(450, 530))
winCaracteristiques.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))


def swarsResults4():
    winResults = QWidget()
    winResults.setWindowTitle("Résultats")
    winResults.setFixedSize(QSize(550, 500))
    winResults.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))
    winResults.show()
    S = np.loadtxt(path2)
    S2 = ["%.3f" % i for i in S]
    S8 = str(S[8])
    S10 = str(S[10])
    S11 = str(S[11])
    S12 = str(S[12])
    S13 = str(S[13])

    if S[0] == 4 and S[1] == 1:
        S23 = "{:.9e}".format(S[3])
        labM1r = QLabel("m2 = " + "\n" + S23)
        labM1r.setParent(winResults)
        labM1r.move(0, 150)
        labM1r.setFixedSize(QSize(170, 40))
        labM1r.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font2 = labM1r.font()
        font2.setPointSize(10)
        labM1r.setFont(font2)
        labM1r.show()

        S22 = "{:.9e}".format(S[2])
        labM2r = QLabel("m1 = " + "\n" + S22)
        labM2r.setParent(winResults)
        labM2r.move(0, 100)
        labM2r.setFixedSize(QSize(170, 40))
        labM2r.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labM2r.setFont(font2)
        labM2r.show()

        labM2r = QLabel("a = " + "\n" + S2[4])
        labM2r.setParent(winResults)
        labM2r.move(0, 200)
        labM2r.setFixedSize(QSize(170, 40))
        labM2r.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labM2r.setFont(font2)
        labM2r.show()

        labM2r = QLabel("angle = " + "\n" + S2[6])
        labM2r.setParent(winResults)
        labM2r.move(0, 250)
        labM2r.setFixedSize(QSize(170, 40))
        labM2r.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labM2r.setFont(font2)
        labM2r.show()

        labM2r = QLabel("r = " + "\n" + S2[5])
        labM2r.setParent(winResults)
        labM2r.move(0, 300)
        labM2r.setFixedSize(QSize(170, 40))
        labM2r.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labM2r.setFont(font2)
        labM2r.show()

        labTitler = QLabel(L[166] + "\n" + L[167])
        labTitler.setStyleSheet("background-color: #3EF724")
        labTitler.setParent(winResults)
        labTitler.move(125, 0)
        labTitler.setFixedSize(QSize(300, 50))
        labTitler.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font3 = labTitler.font()
        font3.setPointSize(13)
        labTitler.setFont(font3)
        labTitler.show()

        labFreq = QLabel(L[162])
        labFreq.setParent(winResults)
        labFreq.move(130, 60)
        labFreq.setFixedSize(QSize(350, 25))
        labFreq.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font4 = labFreq.font()
        font4.setPointSize(12)
        labFreq.setFont(font4)
        labFreq.show()

        labFreqR = QLabel(S8)
        labFreqR.setParent(winResults)
        labFreqR.move(130, 85)
        labFreqR.setFixedSize(QSize(350, 25))
        labFreqR.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labFreqR.setFont(font4)
        labFreqR.show()

        labH1 = QLabel(L[163])
        labH1.setParent(winResults)
        labH1.move(130, 140)
        labH1.setFixedSize(QSize(350, 25))
        labH1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labH1.setFont(font4)
        labH1.show()

        labH1r = QLabel(S10)
        labH1r.setParent(winResults)
        labH1r.move(130, 165)
        labH1r.setFixedSize(QSize(350, 25))
        labH1r.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labH1r.setFont(font4)
        labH1r.show()

        labH2 = QLabel(L[164])
        labH2.setParent(winResults)
        labH2.move(130, 220)
        labH2.setFixedSize(QSize(350, 25))
        labH2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labH2.setFont(font4)
        labH2.show()

        labH2r = QLabel(S11)
        labH2r.setParent(winResults)
        labH2r.move(130, 245)
        labH2r.setFixedSize(QSize(350, 25))
        labH2r.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labH2r.setFont(font4)
        labH2r.show()

        labPas = QLabel(L[161])
        labPas.setParent(winResults)
        labPas.move(105, 375)
        labPas.setFixedSize(QSize(400, 25))
        labPas.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labPas.setFont(font4)
        labPas.show()

        labPasr = QLabel(S13)
        labPasr.setParent(winResults)
        labPasr.move(130, 400)
        labPasr.setFixedSize(QSize(350, 25))
        labPasr.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labPasr.setFont(font4)
        labPasr.show()

        labPt = QLabel(L[165])
        labPt.setParent(winResults)
        labPt.move(130, 300)
        labPt.setFixedSize(QSize(350, 25))
        labPt.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labPt.setFont(font4)
        labPt.show()

        labPtr = QLabel(S12)
        labPtr.setParent(winResults)
        labPtr.move(130, 325)
        labPtr.setFixedSize(QSize(350, 25))
        labPtr.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labPtr.setFont(font4)
        labPtr.show()

        def ReturnDat():
            winResults.deleteLater()
            waves()

        btn = QPushButton(L[108])
        btn.setParent(winResults)
        btn.move(10, 400)
        btn.setFixedSize(QSize(150, 25))
        font65 = btn.font()
        font65.setPointSize(10)
        btn.setFont(font65)
        btn.pressed.connect(ReturnDat)
        btn.show()

#
# Def window caracteristics!


def waves():
    labTitle = QLabel(L[166] + "\n" + L[167])
    labTitle.setStyleSheet("background-color: #3EF724")
    labTitle.setParent(winCaracteristiques)
    labTitle.move(65, 5)
    labTitle.setFixedSize(QSize(320, 50))
    labTitle.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    font2 = labTitle.font()
    font2.setPointSize(13)
    labTitle.setFont(font2)
    labTitle.show()

    def value_changed_m1(vn1):
        global val_m1
        val_m1 = vn1
        print(val_m1)

    def text_m1(m112):
        global m11
        m11 = float(m112)

    def value_changed_m2(vn2):
        global val_m1
        val_m2 = vn2
        print(val_m2)

    def text_m2(m222):
        global m22
        m22 = float(m222)

    def text_alt(alt2):
        global alt
        alt = float(alt2)

    def text_A(A2):
        global a
        a = float(A2)

    def text_R(R2):
        global R
        R = float(R2)

    def text_Ang(ang2):
        global ang
        ang = float(ang2)

    labm1 = QLabel(L[156])
    labm1.setParent(winCaracteristiques)
    labm1.move(75, 90)
    labm1.setFixedSize(QSize(300, 30))
    labm1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    font = labm1.font()
    font.setPointSize(12)
    labm1.setFont(font)
    labm1.show()

    entm1 = QLineEdit()
    entm1.setParent(winCaracteristiques)
    entm1.move(85, 120)
    entm1.setFixedSize(QSize(200, 20))
    entm1.setFont(font)
    entm1.textChanged.connect(text_m1)
    entm1.show()

    labm2 = QLabel(L[157])
    labm2.setParent(winCaracteristiques)
    labm2.move(75, 170)
    labm2.setFixedSize(QSize(300, 30))
    labm2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    labm2.setFont(font)
    labm2.show()

    entm2 = QLineEdit()
    entm2.setParent(winCaracteristiques)
    entm2.move(85, 200)
    entm2.setFixedSize(QSize(200, 20))
    entm2.textChanged.connect(text_m2)
    entm2.setFont(font)
    entm2.show()

    labA = QLabel(L[159])
    labA.setParent(winCaracteristiques)
    labA.move(75, 250)
    labA.setFixedSize(QSize(300, 30))
    labA.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    labA.setFont(font)
    labA.show()

    entA = QLineEdit()
    entA.setParent(winCaracteristiques)
    entA.move(125, 280)
    entA.setFixedSize(QSize(200, 20))
    entA.textChanged.connect(text_A)
    entA.setFont(font)
    entA.show()

    labR = QLabel(L[160])
    labR.setParent(winCaracteristiques)
    labR.move(25, 330)
    labR.setFixedSize(QSize(400, 30))
    labR.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    labR.setFont(font)
    labR.show()

    entR = QLineEdit()
    entR.setParent(winCaracteristiques)
    entR.move(125, 360)
    entR.setFixedSize(QSize(200, 20))
    entR.textChanged.connect(text_R)
    entR.setFont(font)
    entR.show()

    labAng = QLabel(L[158])
    labAng.setParent(winCaracteristiques)
    labAng.move(75, 410)
    labAng.setFixedSize(QSize(300, 30))
    labAng.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    labAng.setFont(font)
    labAng.show()

    entAng = QLineEdit()
    entAng.setParent(winCaracteristiques)
    entAng.move(125, 440)
    entAng.setFixedSize(QSize(200, 20))
    entAng.textChanged.connect(text_Ang)
    entAng.setFont(font)
    entAng.show()

    spinboxM1 = QDoubleSpinBox()
    spinboxM1.setRange(0, 1000)
    spinboxM1.setParent(winCaracteristiques)
    spinboxM1.setFixedSize(QSize(80, 20))
    spinboxM1.move(295, 120)
    spinboxM1.setPrefix("x10*  ")
    spinboxM1.setSingleStep(1)
    spinboxM1.valueChanged.connect(value_changed_m1)
    spinboxM1.show()

    spinboxM2 = QDoubleSpinBox()
    spinboxM2.setRange(0, 1000)
    spinboxM2.setParent(winCaracteristiques)
    spinboxM2.setFixedSize(QSize(80, 20))
    spinboxM2.move(295, 200)
    spinboxM2.setPrefix("x10*  ")
    spinboxM2.setSingleStep(1)
    spinboxM2.valueChanged.connect(value_changed_m2)
    spinboxM2.show()

    def recupdata11():
        try:
            m1 = m11*10**val_m1
        except:
            m1 = m11

        try:
            m2 = m22*10**val_m2
        except:
            m2 = m22

        M = m1 + m2
        w = sqrt(((6.67*10**-11)*M)/(a**3))

        u = (m1*m2)/M

        fH = (4*(6.67*10**-11)*u*(a**2)*(w**2))/(R*(299792458**4))
        fH2 = (1+(cos(ang)**2))/2
        H1 = fH*fH2*cos(2*w)
        H2 = fH * cos(ang)*sin(2*w)

        Pt = (32*(6.67*10**-11)*(u**2)*(a**4)*(w**6))/(5*(299792458**5))

        fP = (2*(6.67*10**-11)*(u**2)*(a**4)*(w**6))/(pi*(299792458**5))

        Pa = fP*(1/4)*(1 + 6*(cos(ang)**2)+(cos(ang)**4))

        x = [4, 1, m1, m2, a, R, ang, M, w, u, H1, H2, Pt, Pa, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 156, m1, 157, m2, 159, a, 191, R, 158, ang,
             166, 167, 162, w, 163, H1, 164, H2, 0, 0, 0,
             184, 161, Pa, 165, Pt, 0, 0, 0, 0, 0]
        np.savetxt(path2, x)
        winCaracteristiques.hide()
        swarsResults4()

    btn = QPushButton(L[11])
    btn.setParent(winCaracteristiques)
    btn.move(180, 480)
    btn.setFixedSize(QSize(90, 30))
    font65 = btn.font()
    font65.setPointSize(12)
    btn.setFont(font65)
    btn.pressed.connect(recupdata11)
    btn.show()

    def web():
        webbrowser.open_new(
            r"https://fr.wikipedia.org/wiki/D%C3%A9calage_d%27Einstein")

    btn1 = QPushButton()
    btn1.setParent(winCaracteristiques)
    btn1.move(15, 50)
    btn1.setFixedSize(QSize(30, 20))
    btn1.pressed.connect(web)
    btn1.setStyleSheet(
        "border-image : url(/usr/lib/spoutnx/img/logo wiki.png);")
    btn1.show()

    winCaracteristiques.show()
