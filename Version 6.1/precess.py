############################ PRECESSION GEODETIQUE############################
import numpy as np
from math import *
import os
from numpy import pi
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QWidget,
    QLineEdit,
    QListWidget,
    QDoubleSpinBox,
    QStackedWidget
)
from PySide6.QtGui import QIcon, QPixmap


user = os.getlogin()
Path = "/home/" + user + "/.SpoutnX/"
path2 = Path + "data.sptx"
path3 = Path + "user_data.txt"
path4 = Path + "lang/user_lang.sptx"

mes_nombres = open(path4).read()
L = mes_nombres.split('\n')


def swarsResults9():
    windowResults_Geodetic = QWidget()
    windowResults_Geodetic.setWindowTitle("Résultats")
    windowResults_Geodetic.setFixedSize(QSize(600, 500))
    windowResults_Geodetic.setWindowIcon(
        QIcon('/usr/lib/spoutnx/icone2.ico'))
    windowResults_Geodetic.show()

    windowResults_Periastre = QWidget()
    windowResults_Periastre.setWindowTitle("Résultats")
    windowResults_Periastre.setFixedSize(QSize(550, 400))
    windowResults_Periastre.setWindowIcon(
        QIcon('/usr/lib/spoutnx/icone2.ico'))
    windowResults_Periastre.show()
    S = np.loadtxt(path2)
    S2 = ["%.1f" % i for i in S]
    S5 = str(S[5])
    try:
        S6 = str(S[6])
        S9 = str(S[9])
        S10 = str(S[10])
    except:
        pass

# PRECESSION GEODETIQUE + LENSE-THIRRING -- RESULTATS

    if S[0] == 7 and S[1] == 1:
        S23 = "{:.9e}".format(S[3])
        labDataM = QLabel("m = " + "\n" + S23)
        labDataM.setParent(windowResults_Geodetic)
        labDataM.move(10, 200)
        labDataM.setFixedSize(QSize(170, 40))
        labDataM.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font2 = labDataM.font()
        font2.setPointSize(10)
        labDataM.setFont(font2)
        labDataM.show()

        labDataR = QLabel("r = " + "\n" + S2[2])
        labDataR.setParent(windowResults_Geodetic)
        labDataR.move(10, 150)
        labDataR.setFixedSize(QSize(170, 40))
        labDataR.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataR.setFont(font2)
        labDataR.show()

        labTitlePrec = QLabel(L[152])
        labTitlePrec.setParent(windowResults_Geodetic)
        labTitlePrec.setStyleSheet("background-color: #3EF724")
        labTitlePrec.move(175, 0)
        labTitlePrec.setFixedSize(QSize(300, 30))
        labTitlePrec.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font3 = labTitlePrec.font()
        font3.setPointSize(13)
        labTitlePrec.setFont(font3)
        labTitlePrec.show()

        def ReturnDat():
            windowResults_Geodetic.hide()
            windowResults_Geodetic.deleteLater()

            Sittereff()

        btn = QPushButton(L[108])
        btn.setParent(windowResults_Geodetic)
        btn.move(10, 400)
        btn.setFixedSize(QSize(150, 25))
        font65 = btn.font()
        font65.setPointSize(10)
        btn.setFont(font65)
        btn.pressed.connect(ReturnDat)
        btn.show()

        labResultVitAng = QLabel(L[105])
        labResultVitAng.setParent(windowResults_Geodetic)
        labResultVitAng.move(125, 30)
        labResultVitAng.setFixedSize(QSize(400, 30))
        labResultVitAng.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResultVitAng.setFont(font3)
        labResultVitAng.show()

        labVitAng = QLabel(S5)
        labVitAng.setParent(windowResults_Geodetic)
        labVitAng.move(175, 60)
        labVitAng.setFixedSize(QSize(300, 25))
        labVitAng.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labVitAng.setFont(font3)
        labVitAng.show()

        ImgFormulSitter = QLabel()
        ImgFormulSitter.setPixmap(
            QPixmap('/usr/lib/spoutnx/img/Precession Sitter.png'))
        ImgFormulSitter.setParent(windowResults_Geodetic)
        ImgFormulSitter.move(220, 160)
        ImgFormulSitter.setFixedSize(QSize(200, 70))
        ImgFormulSitter.setScaledContents(True)
        ImgFormulSitter.show()

        labResultAngPrec = QLabel(L[106])
        labResultAngPrec.setParent(windowResults_Geodetic)
        labResultAngPrec.move(100, 110)
        labResultAngPrec.setFixedSize(QSize(450, 25))
        labResultAngPrec.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResultAngPrec.setFont(font3)
        labResultAngPrec.show()

        labAngPrec = QLabel(S6)
        labAngPrec.setParent(windowResults_Geodetic)
        labAngPrec.move(150, 140)
        labAngPrec.setFixedSize(QSize(350, 25))
        labAngPrec.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labAngPrec.setFont(font3)
        labAngPrec.show()

        if S[11] != 0:
            S211 = "{:.7e}".format(S[11])
            labDataMc = QLabel("Mc = " + "\n" + S211)
            labDataMc.setParent(windowResults_Geodetic)
            labDataMc.move(10, 250)
            labDataMc.setFixedSize(QSize(170, 40))
            labDataMc.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labDataMc.setFont(font2)
            labDataMc.show()

            labTitleLT = QLabel(L[151])
            labTitleLT.setParent(windowResults_Geodetic)
            labTitleLT.setStyleSheet("background-color: #3EF724")
            labTitleLT.move(175, 260)
            labTitleLT.setFixedSize(QSize(300, 30))
            labTitleLT.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labTitleLT.setFont(font3)
            labTitleLT.show()

            labLT = QLabel(L[105])
            labLT.setParent(windowResults_Geodetic)
            labLT.move(125, 290)
            labLT.setFixedSize(QSize(400, 25))
            labLT.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labLT.setFont(font3)
            labLT.show()

            labRes = QLabel(S10)
            labRes.setParent(windowResults_Geodetic)
            labRes.move(150, 310)
            labRes.setFixedSize(QSize(350, 25))
            labRes.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labRes.setFont(font3)
            labRes.show()

            ImgFormulLense = QLabel()
            ImgFormulLense.setPixmap(
                QPixmap('/usr/lib/spoutnx/img/Precession Lense.png'))
            ImgFormulLense.setParent(windowResults_Geodetic)
            ImgFormulLense.move(200, 350)
            ImgFormulLense.setFixedSize(QSize(280, 150))
            ImgFormulLense.setScaledContents(True)
            ImgFormulLense.show()

        windowResults_Geodetic.show()

# PRECESSION DU PERIASTRE -- RESULTATS

    if S[0] == 7 and S[1] == 2:
        windowResults_Periastre.show()

        S24 = "{:.6e}".format(S[4])
        labMass2 = QLabel("m = " + "\n" + S24)
        labMass2.setParent(windowResults_Periastre)
        labMass2.move(10, 200)
        labMass2.setFixedSize(QSize(170, 40))
        labMass2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font2 = labMass2.font()
        font2.setPointSize(10)
        labMass2.setFont(font2)
        labMass2.show()

        labA2 = QLabel("a = " + "\n" + S2[2])
        labA2.setParent(windowResults_Periastre)
        labA2.move(10, 150)
        labA2.setFixedSize(QSize(170, 40))
        labA2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labA2.setFont(font2)
        labA2.show()

        labEx2 = QLabel("e = " + "\n" + S2[3])
        labEx2.setParent(windowResults_Periastre)
        labEx2.move(10, 250)
        labEx2.setFixedSize(QSize(170, 40))
        labEx2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labEx2.setFont(font2)
        labEx2.show()

        def ReturnDat():
            windowResults_Periastre.deleteLater()

            Sittereff()

        btn = QPushButton(L[108])
        btn.setParent(windowResults_Periastre)
        btn.move(10, 300)
        btn.setFixedSize(QSize(150, 25))
        font65 = btn.font()
        font65.setPointSize(10)
        btn.setFont(font65)
        btn.pressed.connect(ReturnDat)
        btn.show()

        labTitle2 = QLabel(L[149])
        labTitle2.setParent(windowResults_Periastre)
        labTitle2.setStyleSheet("background-color: #3EF724")
        labTitle2.move(125, 10)
        labTitle2.setFixedSize(QSize(400, 30))
        labTitle2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font3 = labTitle2.font()
        font3.setPointSize(13)
        labTitle2.setFont(font3)
        labTitle2.show()

        labAnsw = QLabel(S5)
        labAnsw.setParent(windowResults_Periastre)
        labAnsw.move(175, 90)
        labAnsw.setFixedSize(QSize(300, 25))
        labAnsw.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labAnsw.setFont(font3)
        labAnsw.show()

        labForm = QLabel(L[22])
        labForm.setParent(windowResults_Periastre)
        labForm.move(170, 180)
        labForm.setFixedSize(QSize(300, 25))
        labForm.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font = labForm.font()
        font.setPointSize(11)
        labForm.setFont(font)
        labForm.show()

        ImgFormulPeri = QLabel()
        ImgFormulPeri.setPixmap(
            QPixmap('/usr/lib/spoutnx/img/Precession periastre.png'))
        ImgFormulPeri.setParent(windowResults_Periastre)
        ImgFormulPeri.move(240, 200)
        ImgFormulPeri.setFixedSize(QSize(200, 120))
        ImgFormulPeri.setScaledContents(True)
        ImgFormulPeri.show()

# ______________________________ CARACTERISTIQUES ____________________________


windowCaracteristics = QWidget()
windowCaracteristics.setWindowTitle("Caractéristiques")
windowCaracteristics.setFixedSize(QSize(400, 500))
windowCaracteristics.setWindowIcon(
    QIcon('/usr/lib/spoutnx/icone2.ico'))

windowPrecess_Periastre = QStackedWidget()
windowPrecess_Periastre.setParent(windowCaracteristics)
windowPrecess_Periastre.setFixedSize(QSize(400, 500))

windowPrecess_Geodetic = QStackedWidget()
windowPrecess_Geodetic.setParent(windowCaracteristics)
windowPrecess_Geodetic.setFixedSize(QSize(400, 450))


def Sittereff():
    labTitle1 = QLabel(L[84])
    labTitle1.setParent(windowCaracteristics)
    labTitle1.setStyleSheet("background-color: #3EF724")
    labTitle1.move(125, 100)
    labTitle1.setFixedSize(QSize(150, 25))
    labTitle1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    font1 = labTitle1.font()
    font1.setPointSize(13)
    labTitle1.setFont(font1)
    labTitle1.show()
    try:
        windowPrecess_Periastre.hide()
    except:
        pass

    try:
        windowPrecess_Geodetic.hide()
    except:
        pass

    def ChoiceUser(c):
        c = c.text()

# PRECESSION DU PERIASTRE -- CARACTERISTIQUES

        if c == L[104]:
            windowPrecess_Periastre.show()
            liste.hide()
            labTitle1.hide()
            label1 = QLabel(L[103] + "\n" + L[104])
            label1.setStyleSheet("background-color: #3EF724")
            label1.setParent(windowPrecess_Periastre)
            label1.move(70, 20)     # Calcul effet de De Sitter
            label1.setFixedSize(QSize(260, 50))
            label1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            font2 = label1.font()
            font2.setPointSize(13)
            label1.setFont(font2)
            label1.show()

            def Mass_changed(v1):
                global valM
                valM = v1
                print(valM)

            def Mc_changed(v2):
                global valJ
                valJ = v2
                print(valJ)

            def text_mass(m2):
                global m3
                m3 = float(m2)

            def text_alt(alt2):
                global alt
                alt = float(alt2)

            def text_vit(vit2):
                global j2
                j2 = float(vit2)

            labAlt = QLabel(L[16])          # Altitude de la particule test
            labAlt.setParent(windowPrecess_Periastre)
            labAlt.move(50, 70)
            labAlt.setFixedSize(QSize(300, 30))
            labAlt.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            font = labAlt.font()
            font.setPointSize(11)
            labAlt.setFont(font)
            labAlt.show()

            entAlt = QLineEdit()
            entAlt.setParent(windowPrecess_Periastre)
            entAlt.move(100, 100)
            entAlt.setFixedSize(QSize(200, 20))
            entAlt.setFont(font)
            entAlt.textChanged.connect(text_alt)
            entAlt.show()

            labMass = QLabel(L[17])         # Masse de l'objet attirant
            labMass.setParent(windowPrecess_Periastre)
            labMass.move(50, 150)
            labMass.setFixedSize(QSize(300, 30))
            labMass.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labMass.setFont(font)
            labMass.show()

            entMass = QLineEdit()
            entMass.setParent(windowPrecess_Periastre)
            entMass.move(70, 180)
            entMass.setFixedSize(QSize(200, 20))
            entMass.textChanged.connect(text_mass)
            entMass.setFont(font)
            entMass.show()

            spinboxMass = QDoubleSpinBox()
            spinboxMass.setRange(0, 1000)
            spinboxMass.setParent(windowPrecess_Periastre)
            spinboxMass.setFixedSize(QSize(80, 20))
            spinboxMass.move(280, 180)
            spinboxMass.setPrefix("x10*  ")
            spinboxMass.setSingleStep(1)
            spinboxMass.valueChanged.connect(Mass_changed)
            spinboxMass.show()

            labTitle3 = QLabel(L[150])      # Calcul effet Lense-Thirring
            labTitle3.setStyleSheet("background-color: #3EF724")
            labTitle3.setParent(windowPrecess_Periastre)
            labTitle3.move(40, 240)
            labTitle3.setFixedSize(QSize(320, 30))
            labTitle3.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labTitle3.setFont(font2)
            labTitle3.show()

            labVit = QLabel(L[60])      # Moment cinetique de l'objet
            labVit.setParent(windowPrecess_Periastre)
            labVit.move(50, 320)
            labVit.setFixedSize(QSize(300, 30))
            labVit.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labVit.setFont(font)
            labVit.show()

            entVit = QLineEdit()
            entVit.setParent(windowPrecess_Periastre)
            entVit.move(70, 350)
            entVit.setFixedSize(QSize(200, 20))
            entVit.textChanged.connect(text_vit)
            entVit.setFont(font)
            entVit.show()

            spinboxMc = QDoubleSpinBox()
            spinboxMc.setRange(0, 1000)
            spinboxMc.setParent(windowPrecess_Periastre)
            spinboxMc.setFixedSize(QSize(80, 20))
            spinboxMc.move(280, 350)
            spinboxMc.setPrefix("x10*  ")
            spinboxMc.setSingleStep(1)
            spinboxMc.valueChanged.connect(Mc_changed)
            spinboxMc.show()

            def recupdata11():
                try:
                    m = m3*10**valM
                except:
                    m = m3

                Rs = (2*(6.67*10**-11)*m)/(299792458**2)

                K = sqrt(((6.67*10**-11)*m)/(alt**3))
                T = (2*pi)/K

                Ang = (3*pi*m*(6.67*10**-11))/(alt*(299792458**2))
                VitAng = Ang*(31536000/T)

                if 'j2' in globals():
                    try:
                        j = j2*10**valJ
                    except:
                        j = j2
                    a = j/(299792458*m)
                    f1 = (Rs*a)/(alt)
                    f2 = (alt**2)+(a**2)+((Rs*(a**2))/alt)

                    VitAng2 = (299792458)*(f1/f2)

                    x = [7, 1, alt, m, Rs, VitAng, Ang, K, T, a, VitAng2, j, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         16, alt, 17, m, 60, j, 0, 0, 0, 0,
                         102, 103, 105, VitAng, 106, Ang, 0, 0, 0, 0, 0,
                         151, 105, VitAng2, 0, 0, 0, 0, 0, 0, 0]
                else:
                    x = [7, 1, alt, m, Rs, VitAng, Ang, K, T, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         16, alt, 17, m, 0, 0, 0, 0, 0, 0,
                         103, 104, 105, VitAng, 106, Ang, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                np.savetxt(path2, x)

                windowPrecess_Periastre.hide()
                windowCaracteristics.hide()
                swarsResults9()

            btn = QPushButton(L[11])
            btn.setParent(windowPrecess_Periastre)
            btn.move(155, 450)
            btn.setFixedSize(QSize(90, 30))
            font65 = btn.font()
            font65.setPointSize(12)
            btn.setFont(font65)
            btn.pressed.connect(recupdata11)
            btn.show()

            windowPrecess_Periastre.show()

# PRECESSION GEODETIQUE -- CARACTERISTIQUES

        if c == L[148]:
            windowPrecess_Geodetic.show()
            liste.hide()
            labTitle1.hide()
            labTitle = QLabel(L[148])
            labTitle.setStyleSheet("background-color: #3EF724")
            labTitle.setParent(windowPrecess_Geodetic)
            labTitle.move(70, 5)
            labTitle.setFixedSize(QSize(260, 30))
            labTitle.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            font2 = labTitle.font()
            font2.setPointSize(13)
            labTitle.setFont(font2)
            labTitle.show()

            def value_changed(vn):
                global val
                val = vn
                print(val)

            def text_mass(m2):
                global m3
                m3 = float(m2)

            def text_ex(Ex2):
                global e
                e = float(Ex2)

            def text_a(A2):
                global a
                a = float(A2)

            labMass = QLabel(L[17])         # Masse de l'objet attirant
            labMass.setParent(windowPrecess_Geodetic)
            labMass.move(50, 70)
            labMass.setFixedSize(QSize(300, 30))
            labMass.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            font = labMass.font()
            font.setPointSize(11)
            labMass.setFont(font)
            labMass.show()

            entMass = QLineEdit()
            entMass.setParent(windowPrecess_Geodetic)
            entMass.move(70, 100)
            entMass.setFixedSize(QSize(200, 20))
            entMass.setFont(font)
            entMass.textChanged.connect(text_mass)
            entMass.show()

            labEx = QLabel(L[146])  # Excentricité de l'ellipse
            labEx.setParent(windowPrecess_Geodetic)
            labEx.move(50, 160)
            labEx.setFixedSize(QSize(300, 30))
            labEx.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labEx.setFont(font)
            labEx.show()

            entEx = QLineEdit()
            entEx.setParent(windowPrecess_Geodetic)
            entEx.move(100, 190)
            entEx.setFixedSize(QSize(200, 20))
            entEx.textChanged.connect(text_ex)
            entEx.setFont(font)
            entEx.show()

            labA = QLabel(L[147])  # Demi grand axe de l'ellipse orbitale
            labA.setParent(windowPrecess_Geodetic)
            labA.move(50, 250)
            labA.setFixedSize(QSize(300, 30))
            labA.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labA.setFont(font)
            labA.show()

            entA = QLineEdit()
            entA.setParent(windowPrecess_Geodetic)
            entA.move(100, 280)
            entA.setFixedSize(QSize(200, 20))
            entA.textChanged.connect(text_a)
            entA.setFont(font)
            entA.show()

            spinbox = QDoubleSpinBox()
            spinbox.setRange(0, 1000)
            spinbox.setParent(windowPrecess_Geodetic)
            spinbox.setFixedSize(QSize(80, 20))
            spinbox.move(280, 100)
            spinbox.setPrefix("x10*  ")
            spinbox.setSingleStep(1)
            spinbox.valueChanged.connect(value_changed)
            spinbox.show()

            def recupdata11():
                try:
                    m = m3*10**val
                except:
                    m = m3

                AvPer = (6*pi*(6.67*10**-11)*m)/((1-e*e)*a*(299792458**2))

                x = [7, 2, a, e, m, AvPer, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0,
                     17, m, 146, e, 147, a, 0, 0, 0, 0,
                     148, 149, 149, AvPer, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                np.savetxt(path2, x)

                windowCaracteristics.hide()
                windowPrecess_Geodetic.hide()
                swarsResults9()

            btn = QPushButton(L[11])
            btn.setParent(windowPrecess_Geodetic)
            btn.move(155, 360)
            btn.setFixedSize(QSize(90, 30))
            font65 = btn.font()
            font65.setPointSize(12)
            btn.setFont(font65)
            btn.pressed.connect(recupdata11)
            btn.show()

            windowPrecess_Geodetic.show()

    liste = QListWidget()
    liste.addItem(L[148])
    liste.addItem(L[104])
    liste.setParent(windowCaracteristics)
    liste.move(50, 200)
    liste.setFixedSize(QSize(300, 70))
    liste.setStyleSheet("QListView::item:selected{background-color: #3EF724}")
    liste.setCurrentItem(None)
    font2 = liste.font()
    font2.setPointSize(12)
    liste.setFont(font2)
    liste.itemClicked.connect(ChoiceUser)
    liste.show()

    windowCaracteristics.show()
