######################### SCRIPT ACCELERATION VERTICALE#######################
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
winCaract = QWidget()

winCaract.setWindowTitle("Caractéristiques")
winCaract.setFixedSize(QSize(400, 400))
winCaract.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))

# DECALAGE SPECTRAL -- RESULTATS


def swarsResults3():
    winResult = QWidget()
    winResult.setWindowTitle("Résultats")
    winResult.setFixedSize(QSize(500, 450))
    winResult.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))
    winResult.show()
    S = np.loadtxt(path2)
    S2 = ["%.3f" % i for i in S]
    S4 = str(S[4])

    if S[0] == 3:
        S23 = "{:.9e}".format(S[3])
        labDataM = QLabel("m = " + "\n" + S23)
        labDataM.setParent(winResult)
        labDataM.move(10, 170)
        labDataM.setFixedSize(QSize(170, 40))
        labDataM.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font3 = labDataM.font()
        font3.setPointSize(10)
        labDataM.setFont(font3)
        labDataM.show()

        labDataR = QLabel("r = " + "\n" + S2[2])
        labDataR.setParent(winResult)
        labDataR.move(10, 120)
        labDataR.setFixedSize(QSize(170, 40))
        labDataR.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataR.setFont(font3)
        labDataR.show()

        labTitle2 = QLabel(L[79])
        labTitle2.setStyleSheet("background-color: #3EF724")
        labTitle2.setParent(winResult)
        labTitle2.move(200, 10)
        labTitle2.setFixedSize(QSize(250, 30))
        labTitle2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font4 = labTitle2.font()
        font4.setPointSize(13)
        labTitle2.setFont(font4)
        labTitle2.show()

        def ReturnDat():
            winResult.hide()
            winResult.deleteLater()

            decspectral()

        btn = QPushButton(L[108])
        btn.setParent(winResult)
        btn.move(10, 300)
        btn.setFixedSize(QSize(150, 25))
        btn.setFont(font3)
        btn.pressed.connect(ReturnDat)
        btn.show()

        labResult = QLabel(S4)
        labResult.setParent(winResult)
        labResult.move(175, 50)
        labResult.setFixedSize(QSize(300, 25))
        labResult.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResult.setFont(font4)
        labResult.show()

        labFormul = QLabel(L[22])
        labFormul.setParent(winResult)
        labFormul.move(160, 120)
        labFormul.setFixedSize(QSize(300, 25))
        labFormul.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font = labFormul.font()
        font.setPointSize(11)
        labFormul.setFont(font)
        labFormul.show()

        ImgFormul = QLabel()
        ImgFormul.setPixmap(
            QPixmap('/usr/lib/spoutnx/img/Dec spectral.png'))
        ImgFormul.setParent(winResult)
        ImgFormul.move(220, 200)
        ImgFormul.setFixedSize(QSize(200, 120))
        ImgFormul.setScaledContents(True)
        ImgFormul.show()

    winResult.show()

# _______________________________ CARACTERISTIQUES ____________________________


def decspectral():
    labTitle = QLabel(L[7] + "\n" + L[45])
    labTitle.setStyleSheet("background-color: #3EF724")
    labTitle.setParent(winCaract)
    labTitle.move(70, 20)
    labTitle.setFixedSize(QSize(260, 50))
    labTitle.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    font2 = labTitle.font()
    font2.setPointSize(13)
    labTitle.setFont(font2)
    labTitle.show()

    def exp_changed(vn):
        global exp
        exp = vn

    def text_mass(m2):
        global m3
        m3 = float(m2)

    def text_alt(alt2):
        global alt
        alt = float(alt2)

    labDist = QLabel(L[27])
    labDist.setParent(winCaract)
    labDist.move(50, 100)
    labDist.setFixedSize(QSize(300, 30))
    labDist.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    font = labDist.font()
    font.setPointSize(11)
    labDist.setFont(font)
    labDist.show()

    entDist = QLineEdit()
    entDist.setParent(winCaract)
    entDist.move(100, 140)
    entDist.setFixedSize(QSize(200, 20))
    entDist.setFont(font)
    entDist.textChanged.connect(text_alt)
    entDist.show()

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
    spinbox.valueChanged.connect(exp_changed)
    spinbox.show()

    def recupdata11():
        try:
            m = m3*10**exp
        except:
            m = m3

        first = (1-((2*(6.67*10**-11)*m)/((299792458**2)*alt)))
        z = (1/(sqrt(first)))-1

        x = [3, 1, alt, m, z, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0,
             27, alt, 17, m, 0, 0, 0, 0, 0, 0,
             7, 45, 79, z, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        np.savetxt(path2, x)
        winCaract.hide()
        swarsResults3()

    btnValid = QPushButton(L[11])
    btnValid.setParent(winCaract)
    btnValid.move(155, 300)
    btnValid.setFixedSize(QSize(90, 30))
    font65 = btnValid.font()
    font65.setPointSize(12)
    btnValid.setFont(font65)
    btnValid.pressed.connect(recupdata11)
    btnValid.show()

    def web():
        webbrowser.open_new(
            r"https://fr.wikipedia.org/wiki/D%C3%A9calage_d%27Einstein")

    btnWiki = QPushButton()
    btnWiki.setParent(winCaract)
    btnWiki.move(15, 50)
    btnWiki.setFixedSize(QSize(30, 20))
    btnWiki.pressed.connect(web)
    btnWiki.setStyleSheet(
        "border-image : url(/usr/lib/spoutnx/img/logo wiki.png);")
    btnWiki.show()

    winCaract.show()
