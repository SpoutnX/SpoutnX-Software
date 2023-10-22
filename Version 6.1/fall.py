######################### SCRIPT ACCELERATION VERTICALE####################

import numpy as np
from math import *
import os
import numpy

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QWidget,
    QLineEdit,
    QDoubleSpinBox,
)

from PySide6.QtGui import QIcon, QPixmap

user = os.getlogin()
Path = "/home/" + user + "/.SpoutnX/"
path2 = Path + "data.sptx"
path3 = Path + "user_data.txt"
path4 = Path + "lang/user_lang.sptx"

mes_nombres = open(path4).read()
L = mes_nombres.split('\n')

winCaract = QWidget()
winCaract.setWindowTitle("Caractéristiques")
winCaract.setFixedSize(QSize(400, 400))
winCaract.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))


def swarsResults2():
    winResults = QWidget()
    winResults.setWindowTitle("Résultats")
    winResults.setFixedSize(QSize(600, 500))
    winResults.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))
    winResults.show()
    S = np.loadtxt(path2)
    S3 = str(S[3])

    if S[0] == 2:
        labDataA = QLabel(L[78] + "\n" + S3)
        labDataA.setParent(winResults)
        labDataA.move(10, 170)
        labDataA.setFixedSize(QSize(170, 40))
        labDataA.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font5 = labDataA.font()
        font5.setPointSize(10)
        labDataA.setFont(font5)
        labDataA.show()

        S22 = "{:.9e}".format(S[2])
        labDataM = QLabel(L[47] + "\n" + S22)
        labDataM.setParent(winResults)
        labDataM.move(10, 120)
        labDataM.setFixedSize(QSize(170, 40))
        labDataM.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataM.setFont(font5)
        labDataM.show()

        labTitle2 = QLabel(L[23])
        labTitle2.setStyleSheet("background-color: #3EF724")
        labTitle2.setParent(winResults)
        labTitle2.move(175, 0)
        labTitle2.setFixedSize(QSize(300, 30))
        labTitle2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font3 = labTitle2.font()
        font3.setPointSize(13)
        labTitle2.setFont(font3)
        labTitle2.show()

        def ReturnDat():
            winResults.hide()
            winResults.deleteLater()

            timefall()

        btn = QPushButton(L[108])
        btn.setParent(winResults)
        btn.move(10, 300)
        btn.setFixedSize(QSize(150, 25))
        btn.setFont(font5)
        btn.pressed.connect(ReturnDat)
        btn.show()

        S4 = str(S[4])
        labAcc = QLabel(S4)
        labAcc.setParent(winResults)
        labAcc.move(175, 30)
        labAcc.setFixedSize(QSize(300, 25))
        labAcc.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labAcc.setFont(font3)
        labAcc.show()

        labFormul = QLabel(L[22])
        labFormul.setParent(winResults)
        labFormul.move(160, 350)
        labFormul.setFixedSize(QSize(300, 25))
        labFormul.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font = labFormul.font()
        font.setPointSize(11)
        labFormul.setFont(font)
        labFormul.show()

        ImgFormul = QLabel()
        ImgFormul.setPixmap(
            QPixmap('/usr/lib/spoutnx/img/acceleration.png'))
        ImgFormul.setParent(winResults)
        ImgFormul.move(180, 370)
        ImgFormul.setFixedSize(QSize(300, 70))
        ImgFormul.setScaledContents(True)
        ImgFormul.show()

        laVitObj = QLabel(L[32])
        laVitObj.setParent(winResults)
        laVitObj.setStyleSheet("background-color: #3EF724")
        laVitObj.move(150, 80)
        laVitObj.setFixedSize(QSize(350, 25))
        laVitObj.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        laVitObj.setFont(font3)
        laVitObj.show()

        S6 = str(S[6])
        labResVitObj = QLabel(S6)
        labResVitObj.setParent(winResults)
        labResVitObj.move(150, 110)
        labResVitObj.setFixedSize(QSize(350, 25))
        labResVitObj.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResVitObj.setFont(font3)
        labResVitObj.setToolTip(L[174])
        labResVitObj.show()

        labRs = QLabel(L[33] + "\n" + L[34])
        labRs.setParent(winResults)
        labRs.move(150, 160)
        labRs.setFixedSize(QSize(350, 50))
        labRs.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labRs.setFont(font3)
        labRs.show()

        S5 = str(S[5])
        labResultRs = QLabel(S5)
        labResultRs.setParent(winResults)
        labResultRs.move(150, 215)
        labResultRs.setFixedSize(QSize(350, 25))
        labResultRs.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResultRs.setFont(font3)
        labResultRs.setToolTip(L[175])
        labResultRs.show()

        labVitOrb = QLabel(L[116])
        labVitOrb.setParent(winResults)
        labVitOrb.setStyleSheet("background-color: #3EF724")
        labVitOrb.move(150, 260)
        labVitOrb.setFixedSize(QSize(350, 25))
        labVitOrb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labVitOrb.setFont(font3)
        labVitOrb.show()

        S7 = str(S[7])
        labResVitOrb = QLabel(S7)
        labResVitOrb.setParent(winResults)
        labResVitOrb.move(150, 290)
        labResVitOrb.setFixedSize(QSize(350, 25))
        labResVitOrb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResVitOrb.setFont(font3)
        labResVitOrb.setToolTip(L[174])
        labResVitOrb.show()

    winResults.show()

# _______________________________CARACTERISTIQUES_____________________________


def timefall():
    labTitle1 = QLabel(L[23] + "\n" + L[45])
    labTitle1.setStyleSheet("background-color: #3EF724")
    labTitle1.setParent(winCaract)
    labTitle1.move(50, 20)
    labTitle1.setFixedSize(QSize(300, 50))
    labTitle1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    font2 = labTitle1.font()
    font2.setPointSize(13)
    labTitle1.setFont(font2)
    labTitle1.show()

    def value_changed(vn):
        global val
        val = vn
        print(val)

    def text_mass(m2):
        global m3
        m3 = float(m2)

    def text_alt(alt2):
        global alt
        alt = float(alt2)

    labAlt = QLabel(L[16])
    labAlt.setParent(winCaract)
    labAlt.move(50, 100)
    labAlt.setFixedSize(QSize(300, 30))
    labAlt.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    font = labAlt.font()
    font.setPointSize(11)
    labAlt.setFont(font)
    labAlt.setToolTip(L[172])
    labAlt.show()

    entAlt = QLineEdit()
    entAlt.setParent(winCaract)
    entAlt.move(100, 140)
    entAlt.setFixedSize(QSize(200, 20))
    entAlt.setFont(font)
    entAlt.textChanged.connect(text_alt)
    entAlt.show()

    labMass = QLabel(L[17])
    labMass.setParent(winCaract)
    labMass.move(50, 190)
    labMass.setFixedSize(QSize(300, 30))
    labMass.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    labMass.setFont(font)
    labMass.show()

    entMass = QLineEdit()
    entMass.setParent(winCaract)
    entMass.move(70, 230)
    entMass.setFixedSize(QSize(200, 20))
    entMass.textChanged.connect(text_mass)
    entMass.setFont(font)
    entMass.show()

    spinbox = QDoubleSpinBox()
    spinbox.setRange(0, 1000)
    spinbox.setParent(winCaract)
    spinbox.setFixedSize(QSize(80, 20))
    spinbox.move(280, 230)
    spinbox.setPrefix("x10*  ")
    spinbox.setSingleStep(1)
    spinbox.valueChanged.connect(value_changed)
    spinbox.setToolTip(L[173])
    spinbox.show()

    def recupdata11():
        try:
            m = m3*10**val
        except:
            m = m3

        first = (-(((6.67*10**-11)*m)/(alt**2)))
        second = 1-((2*(6.67*10**-11)*m)/((299792458**2)*alt))
        third = 1-((3*(6.67*10**-11)*m)/((299792458**2)*alt))

        Acceleration = first*second*third

        first2 = (sqrt((2*(6.67*10**-11)*m)/alt))
        second2 = (1-((2*(6.67*10**-11)*m)/((299792458**2)*alt)))

        Speed = first2*second2

        Rs = (2*(6.67*10**-11)*m)/(299792458**2)

        VitOr = sqrt(Rs/(2*alt))
        VitOr = VitOr*(299792458)

        x = [2, 1, alt, m, Acceleration, Rs, Speed, VitOr, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0,
             16, alt, 17, m, 0, 0, 0, 0, 0, 0,
             6, 45, 108, Acceleration, 0, 0, 0, 0, 0, 0, 0,
             190, 32, Speed, 33, Rs, 116, VitOr, 0, 0, 0]
        np.savetxt(path2, x)
        winCaract.hide()
        swarsResults2()

    btn = QPushButton(L[11])
    btn.setParent(winCaract)
    btn.move(155, 300)
    btn.setFixedSize(QSize(90, 30))
    font65 = btn.font()
    font65.setPointSize(12)
    btn.setFont(font65)
    btn.pressed.connect(recupdata11)
    btn.show()

    winCaract.show()
