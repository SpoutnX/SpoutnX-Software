################################ SCRIPT TROU NOIR############################

import numpy as np
from math import *
import os
import printplot
import math
import webbrowser
import numpy
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QWidget,
    QLineEdit,
    QListWidget,
    QStackedWidget,
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


def swarsResults8():
    winSchwarszchildBlackHole = QWidget()
    winSchwarszchildBlackHole.setWindowTitle("Résultats")
    winSchwarszchildBlackHole.setFixedSize(QSize(600, 500))
    winSchwarszchildBlackHole.setWindowIcon(
        QIcon('/usr/lib/spoutnx/icone2.ico'))

    winMassDecSpectral = QStackedWidget()
    winMassDecSpectral.setParent(winSchwarszchildBlackHole)
    winMassDecSpectral.setFixedSize(QSize(600, 500))

    S = np.loadtxt(path2)
    S2 = ["%.1f" % i for i in S]
    ty2 = str(S[4])
    try:
        ty6 = str(S[6])
        ty7 = str(S[7])
        ty8 = str(S[8])
        ty9 = str(S[9])
        ty10 = str(S[10])
        ty11 = str(S[11])
        ty12 = str(S[12])
        ty125 = float(S[12])
        ty13 = str(S[13])
        ty14 = str(S[14])
        print("good")
    except:
        pass
    ty5 = str(S[5])

# RESULTATS TROU NOIR DE KERR

    if S[0] == 8 and S[1] == 1:
        print("2222")
        winKerrBlackHole = QWidget()
        winKerrBlackHole.setWindowTitle("Résultats")
        winKerrBlackHole.setFixedSize(QSize(700, 600))
        winKerrBlackHole.setWindowIcon(
            QIcon('/usr/lib/spoutnx/icone2.ico'))
        winKerrBlackHole.show()

        S24 = "{:.9e}".format(S[4])
        labDataMass = QLabel("m = " + "\n" + S24)
        labDataMass.setParent(winKerrBlackHole)
        labDataMass.move(10, 250)
        labDataMass.setFixedSize(QSize(210, 50))
        labDataMass.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font2 = labDataMass.font()
        font2.setPointSize(10)
        labDataMass.setFont(font2)
        labDataMass.show()
        print("111")

        labDataMc = QLabel("Mc = " + "\n" + S2[2])
        labDataMc.setParent(winKerrBlackHole)
        labDataMc.move(30, 300)
        labDataMc.setFixedSize(QSize(170, 50))
        labDataMc.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataMc.setFont(font2)
        labDataMc.show()

        labDataLat = QLabel("lat = " + "\n" + S2[3])
        labDataLat.setParent(winKerrBlackHole)
        labDataLat.move(30, 350)
        labDataLat.setFixedSize(QSize(170, 50))
        labDataLat.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataLat.setFont(font2)
        labDataLat.show()

        labDataRs = QLabel("Rs = " + "\n" + S2[7])
        labDataRs.setParent(winKerrBlackHole)
        labDataRs.move(30, 400)
        labDataRs.setFixedSize(QSize(170, 50))
        labDataRs.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataRs.setFont(font2)
        labDataRs.show()

        labResTitle = QLabel(L[62])
        labResTitle.setStyleSheet("background-color: #3EF724")
        labResTitle.setParent(winKerrBlackHole)
        labResTitle.move(175, 10)
        labResTitle.setFixedSize(QSize(350, 25))
        labResTitle.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font3 = labResTitle.font()
        font3.setPointSize(13)
        labResTitle.setFont(font3)
        labResTitle.show()

        labResTr = QLabel(L[63] + "\n" + ty5)   # Taux de rotation
        labResTr.setParent(winKerrBlackHole)
        labResTr.move(20, 50)
        labResTr.setFixedSize(QSize(250, 40))
        labResTr.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font4 = labResTr.font()
        font4.setPointSize(12)
        labResTr.setFont(font4)
        labResTr.show()

        labResPr = QLabel(L[64] + "\n" + ty6)   # Paramètre de Spin
        labResPr.setParent(winKerrBlackHole)
        labResPr.move(375, 50)
        labResPr.setFixedSize(QSize(250, 40))
        labResPr.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResPr.setFont(font4)
        labResPr.show()

        try:
            print(3)
            print(ty12)
            if 0.8 <= ty125 <= 1.1:

                labTypeBlackHole1 = QLabel(L[136])
                labTypeBlackHole1.setStyleSheet("font-weight: bold")
                labTypeBlackHole1.setParent(winKerrBlackHole)
                labTypeBlackHole1.move(170, 110)
                labTypeBlackHole1.setFixedSize(QSize(350, 40))
                labTypeBlackHole1.setAlignment(
                    Qt.AlignHCenter | Qt.AlignVCenter)
                labTypeBlackHole1.setFont(font4)
                labTypeBlackHole1.show()

                labResRISCO = QLabel(L[114] + "\n" + ty13)
                labResRISCO.setParent(winKerrBlackHole)
                labResRISCO.move(20, 150)
                labResRISCO.setFixedSize(QSize(250, 40))
                labResRISCO.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                labResRISCO.setFont(font4)
                labResRISCO.show()

                labResVISCO = QLabel(L[137] + "\n" + ty14)
                labResVISCO.setParent(winKerrBlackHole)
                labResVISCO.move(400, 150)
                labResVISCO.setFixedSize(QSize(250, 40))
                labResVISCO.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                labResVISCO.setFont(font4)
                labResVISCO.show()

            if ty125 > 1.1:
                print(5)
                labTypeBlackHole2 = QLabel(L[139])
                labTypeBlackHole2.setStyleSheet("font-weight: bold")
                labTypeBlackHole2.setParent(winKerrBlackHole)
                labTypeBlackHole2.move(170, 110)
                labTypeBlackHole2.setFixedSize(QSize(350, 40))
                labTypeBlackHole2.setAlignment(
                    Qt.AlignHCenter | Qt.AlignVCenter)
                labTypeBlackHole2.setFont(font4)
                labTypeBlackHole2.show()

            if ty125 < 0.8:
                print(6)
                labTypeBlackHole3 = QLabel(L[140])
                labTypeBlackHole3.setStyleSheet("font-weight: bold")
                labTypeBlackHole3.setParent(winKerrBlackHole)
                labTypeBlackHole3.move(170, 110)
                labTypeBlackHole3.setFixedSize(QSize(350, 40))
                labTypeBlackHole3.setAlignment(
                    Qt.AlignHCenter | Qt.AlignVCenter)
                labTypeBlackHole3.setFont(font4)
                labTypeBlackHole3.show()

        except:
            print(4)
            labOldVersion = QLabel(L[141] + "\n" + L[142])
            labOldVersion.setParent(winKerrBlackHole)
            labOldVersion.move(170, 120)
            labOldVersion.setFixedSize(QSize(350, 40))
            labOldVersion.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labOldVersion.setFont(font2)
            labOldVersion.show()

        labTitleLimits = QLabel(L[138])
        labTitleLimits.setStyleSheet("background-color: #3EF724")
        labTitleLimits.setParent(winKerrBlackHole)
        labTitleLimits.move(175, 200)
        labTitleLimits.setFixedSize(QSize(350, 25))
        labTitleLimits.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labTitleLimits.setFont(font3)
        labTitleLimits.show()

        labResHorizonExt = QLabel(L[65] + "\n" + ty9)
        labResHorizonExt.setParent(winKerrBlackHole)
        labResHorizonExt.move(250, 255)
        labResHorizonExt.setFixedSize(QSize(350, 60))
        labResHorizonExt.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResHorizonExt.setFont(font4)
        labResHorizonExt.setToolTip(L[181])
        labResHorizonExt.show()

        labResHorizonInt = QLabel(L[66] + "\n" + ty8)
        labResHorizonInt.setParent(winKerrBlackHole)
        labResHorizonInt.move(250, 335)
        labResHorizonInt.setFixedSize(QSize(350, 60))
        labResHorizonInt.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResHorizonInt.setFont(font4)
        labResHorizonInt.show()

        labResLimitext = QLabel(L[91] + "\n" + ty11)
        labResLimitext.setParent(winKerrBlackHole)
        labResLimitext.move(250, 405)
        labResLimitext.setFixedSize(QSize(350, 60))
        labResLimitext.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResLimitext.setFont(font4)
        labResLimitext.setToolTip(L[180])
        labResLimitext.show()

        labResLimitInt = QLabel(L[92] + "\n" + ty10)
        labResLimitInt.setParent(winKerrBlackHole)
        labResLimitInt.move(250, 475)
        labResLimitInt.setFixedSize(QSize(350, 60))
        labResLimitInt.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResLimitInt.setFont(font4)
        labResLimitInt.show()

        def visual():
            printplot.visual2()
        btnVisual = QPushButton(L[41])
        btnVisual.setParent(winKerrBlackHole)
        btnVisual.move(350, 560)
        btnVisual.setFixedSize(QSize(120, 25))
        font65 = btnVisual.font()
        font65.setPointSize(10)
        btnVisual.setFont(font65)
        btnVisual.pressed.connect(visual)
        btnVisual.show()

        def ReturnDat():
            winKerrBlackHole.hide()
            winKerrBlackHole.deleteLater()

            caractHole()

        btnReturn = QPushButton(L[108])
        btnReturn.setParent(winKerrBlackHole)
        btnReturn.move(20, 560)
        btnReturn.setFixedSize(QSize(150, 25))
        btnReturn.setFont(font65)
        btnReturn.pressed.connect(ReturnDat)
        btnReturn.show()


# RESULTATS SCHWARSZCHILD
    if S[0] == 8 and S[1] == 2:

        S22 = "{:.9e}".format(S[2])
        labDataMass2 = QLabel("m = " + "\n" + S22)
        labDataMass2.setParent(winSchwarszchildBlackHole)
        labDataMass2.move(10, 150)
        labDataMass2.setFixedSize(QSize(170, 50))
        labDataMass2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font6 = labDataMass2.font()
        font6.setPointSize(10)
        labDataMass2.setFont(font6)
        labDataMass2.show()

        labDataR2 = QLabel("r = " + "\n" + S2[3])
        labDataR2.setParent(winSchwarszchildBlackHole)
        labDataR2.move(10, 200)
        labDataR2.setFixedSize(QSize(170, 50))
        labDataR2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataR2.setFont(font6)
        labDataR2.show()

        labTitle3 = QLabel(L[76])
        labTitle3.setStyleSheet("background-color: #3EF724")
        labTitle3.setParent(winSchwarszchildBlackHole)
        labTitle3.move(125, 10)
        labTitle3.setFixedSize(QSize(400, 25))
        labTitle3.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font3 = labTitle3.font()
        font3.setPointSize(13)
        labTitle3.setFont(font3)
        labTitle3.show()

        labResultRs = QLabel(L[33])
        labResultRs.setParent(winSchwarszchildBlackHole)
        labResultRs.move(20, 50)
        labResultRs.setFixedSize(QSize(300, 25))
        labResultRs.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResultRs.setFont(font3)
        labResultRs.show()

        labRs = QLabel(ty2)
        labRs.setParent(winSchwarszchildBlackHole)
        labRs.move(70, 70)
        labRs.setFixedSize(QSize(250, 30))
        labRs.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font4 = labRs.font()
        font4.setPointSize(12)
        labRs.setFont(font4)
        labRs.show()

        labResultScal = QLabel(L[52])
        labResultScal.setParent(winSchwarszchildBlackHole)
        labResultScal.move(310, 50)
        labResultScal.setFixedSize(QSize(250, 30))
        labResultScal.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResultScal.setFont(font3)
        labResultScal.show()
        labScal = QLabel(ty5)
        labScal.setParent(winSchwarszchildBlackHole)
        labScal.move(330, 70)
        labScal.setFixedSize(QSize(250, 30))
        labScal.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labScal.setFont(font4)
        labScal.show()

        labResRISCO = QLabel(L[114])
        labResRISCO.setParent(winSchwarszchildBlackHole)
        labResRISCO.move(145, 120)
        labResRISCO.setFixedSize(QSize(350, 30))
        labResRISCO.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResRISCO.setFont(font3)
        labResRISCO.show()
        labRISCO = QLabel(ty8)
        labRISCO.setParent(winSchwarszchildBlackHole)
        labRISCO.move(195, 140)
        labRISCO.setFixedSize(QSize(250, 30))
        labRISCO.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labRISCO.setFont(font4)
        labRISCO.show()

        labResVISCO = QLabel(L[116])
        labResVISCO.setParent(winSchwarszchildBlackHole)
        labResVISCO.move(195, 180)
        labResVISCO.setFixedSize(QSize(250, 30))
        labResVISCO.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResVISCO.setFont(font3)
        labResVISCO.show()

        labVISCO = QLabel(ty9)
        labVISCO.setParent(winSchwarszchildBlackHole)
        labVISCO.move(195, 200)
        labVISCO.setFixedSize(QSize(250, 30))
        labVISCO.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labVISCO.setFont(font4)
        labVISCO.show()
        winSchwarszchildBlackHole.show()

        def ReturnDat():
            winSchwarszchildBlackHole.hide()
            winSchwarszchildBlackHole.deleteLater()

            caractHole()

        btnReturn = QPushButton(L[108])
        btnReturn.setParent(winSchwarszchildBlackHole)
        btnReturn.move(10, 300)
        btnReturn.setFixedSize(QSize(150, 25))
        font65 = btnReturn.font()
        font65.setPointSize(10)
        btnReturn.setFont(font65)
        btnReturn.pressed.connect(ReturnDat)
        btnReturn.show()

        def ray():
            labResTemp = QLabel(L[54])
            labResTemp.setParent(winSchwarszchildBlackHole)
            labResTemp.move(195, 310)
            labResTemp.setFixedSize(QSize(250, 30))
            labResTemp.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labResTemp.setFont(font3)
            labResTemp.show()

            labTemp = QLabel(ty6)
            labTemp.setParent(winSchwarszchildBlackHole)
            labTemp.move(195, 330)
            labTemp.setFixedSize(QSize(250, 30))
            labTemp.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labTemp.setFont(font4)
            labTemp.show()

            labResTimeEvap = QLabel(L[55])
            labResTimeEvap.setParent(winSchwarszchildBlackHole)
            labResTimeEvap.move(170, 370)
            labResTimeEvap.setFixedSize(QSize(300, 30))
            labResTimeEvap.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labResTimeEvap.setFont(font3)
            labResTimeEvap.show()

            labTimeEvap = QLabel(ty7)
            labTimeEvap.setParent(winSchwarszchildBlackHole)
            labTimeEvap.move(195, 390)
            labTimeEvap.setFixedSize(QSize(250, 30))
            labTimeEvap.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labTimeEvap.setFont(font4)
            labTimeEvap.show()

            labInfos = QLabel(L[56] + "\n" + L[57] + L[58])
            labInfos.setParent(winSchwarszchildBlackHole)
            labInfos.move(70, 440)
            labInfos.setFixedSize(QSize(500, 70))
            labInfos.setAlignment(Qt.AlignHCenter)
            labInfos.setFont(font65)
            labInfos.show()

        btnRayon = QPushButton(L[53])
        btnRayon.setParent(winSchwarszchildBlackHole)
        btnRayon.move(190, 260)
        btnRayon.setFixedSize(QSize(250, 30))
        btnRayon.setFont(font65)
        btnRayon.pressed.connect(ray)
        btnRayon.show()

# RESULTATS MASSE TROU NOIR

    if S[0] == 8 and S[1] == 3:
        winSchwarszchildBlackHole.show()
        winMassDecSpectral.show()
        labDataB = QLabel("b = " + "\n" + S2[2])
        labDataB.setParent(winMassDecSpectral)
        labDataB.move(10, 150)
        labDataB.setFixedSize(QSize(170, 50))
        labDataB.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font2 = labDataB.font()
        font2.setPointSize(10)
        labDataB.setFont(font2)
        labDataB.show()

        labDataDec = QLabel("dec = " + "\n" + str(S[3]))
        labDataDec.setParent(winMassDecSpectral)
        labDataDec.move(10, 200)
        labDataDec.setFixedSize(QSize(170, 50))
        labDataDec.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataDec.setFont(font2)
        labDataDec.show()

        labTitle4 = QLabel(L[77])
        labTitle4.setStyleSheet("background-color: #3EF724")
        labTitle4.setParent(winMassDecSpectral)
        labTitle4.move(145, 10)
        labTitle4.setFixedSize(QSize(350, 25))
        labTitle4.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font3 = labTitle4.font()
        font3.setPointSize(13)
        labTitle4.setFont(font3)
        labTitle4.show()

        labResMass = QLabel(L[78])
        labResMass.setParent(winMassDecSpectral)
        labResMass.move(145, 50)
        labResMass.setFixedSize(QSize(350, 25))
        labResMass.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResMass.setFont(font3)
        labResMass.show()

        labMass = QLabel(ty5)
        labMass.setParent(winMassDecSpectral)
        labMass.move(195, 70)
        labMass.setFixedSize(QSize(250, 30))
        labMass.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font4 = labMass.font()
        font4.setPointSize(12)
        labMass.setFont(font4)
        labMass.show()

        labResRS = QLabel(L[33])
        labResRS.setParent(winMassDecSpectral)
        labResRS.move(145, 120)
        labResRS.setFixedSize(QSize(350, 25))
        labResRS.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResRS.setFont(font3)
        labResRS.show()

        labRS = QLabel(ty2)
        labRS.setParent(winMassDecSpectral)
        labRS.move(195, 140)
        labRS.setFixedSize(QSize(250, 30))
        labRS.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labRS.setFont(font4)
        labRS.show()

        labFormula = QLabel(L[22])
        labFormula.setParent(winMassDecSpectral)
        labFormula.move(195, 200)
        labFormula.setFixedSize(QSize(250, 30))
        labFormula.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labFormula.setFont(font3)
        labFormula.show()

        logoFormule = QLabel()
        logoFormule.setPixmap(
            QPixmap('/usr/lib/spoutnx/img/masse trou.png'))
        logoFormule.setParent(winMassDecSpectral)
        logoFormule.move(220, 250)
        logoFormule.setFixedSize(QSize(220, 120))
        logoFormule.setScaledContents(True)
        logoFormule.show()

        def ReturnDat():
            winSchwarszchildBlackHole.hide()
            winMassDecSpectral.deleteLater()

            caractHole()

        btnReturn = QPushButton(L[108])
        btnReturn.setParent(winMassDecSpectral)
        btnReturn.move(10, 300)
        btnReturn.setFixedSize(QSize(150, 25))
        font65 = btnReturn.font()
        font65.setPointSize(10)
        btnReturn.setFont(font65)
        btnReturn.pressed.connect(ReturnDat)
        btnReturn.show()

#########################   CARACTERISTIQUES ############################


windowCaracteristique = QWidget()
windowCaracteristique.setWindowTitle("Caractéristiques")
windowCaracteristique.setFixedSize(QSize(400, 450))
windowCaracteristique.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))

window8 = QWidget()
window8.setWindowTitle("Caractéristiques")
window8.setFixedSize(QSize(400, 450))
window8.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))

windowCaractSchwarszchild = QStackedWidget()
windowCaractSchwarszchild.setParent(windowCaracteristique)
windowCaractSchwarszchild.setFixedSize(QSize(400, 450))

windowCaractKerr = QStackedWidget()
windowCaractKerr.setParent(windowCaracteristique)
windowCaractKerr.setFixedSize(QSize(400, 450))


def caractHole():
    labTitleChoice = QLabel(L[84])  # Titre fenêtre choix type de Trous noirs
    labTitleChoice.setParent(windowCaracteristique)
    labTitleChoice.setStyleSheet("background-color: #3EF724")
    labTitleChoice.move(125, 100)
    labTitleChoice.setFixedSize(QSize(150, 25))
    labTitleChoice.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    font1 = labTitleChoice.font()
    font1.setPointSize(13)
    labTitleChoice.setFont(font1)
    labTitleChoice.show()
    try:
        windowCaractSchwarszchild.hide()
        windowCaractKerr.hide()
    except:
        pass

    def ChoiceUser(choiceTypeBlachHole):
        choiceTypeBlachHole = choiceTypeBlachHole.text()
        try:
            windowCaractKerr.hide()
        except:
            pass
        windowCaractSchwarszchild.show()
        if choiceTypeBlachHole == L[43]:  # Trou noir de Schwarszchild
            liste.hide()
            labTitleChoice.hide()

            labTitle1 = QLabel(L[112] + "\n" + L[45])
            labTitle1.setStyleSheet("background-color: #3EF724")
            labTitle1.setParent(windowCaractSchwarszchild)
            labTitle1.move(70, 20)
            labTitle1.setFixedSize(QSize(260, 50))
            labTitle1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labTitle1.setFont(font1)
            labTitle1.show()

            def text_mass(m2):
                global m3
                m3 = float(m2)

            def text_alt(b2):
                global b
                b = float(b2)

            def value_changed(vn):
                global val
                val = vn
                print(val)

            labMass = QLabel(L[46])
            labMass.setParent(windowCaractSchwarszchild)
            labMass.move(100, 100)
            labMass.setFixedSize(QSize(200, 30))
            labMass.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            font2 = labMass.font()
            font2.setPointSize(12)
            labMass.setFont(font2)
            labMass.show()
            entMass = QLineEdit()
            entMass.setParent(windowCaractSchwarszchild)
            entMass.move(70, 140)
            entMass.setFixedSize(QSize(200, 20))
            entMass.textChanged.connect(text_mass)
            entMass.show()

            spinboxMass = QDoubleSpinBox()
            spinboxMass.setRange(0, 1000)
            spinboxMass.setParent(windowCaractSchwarszchild)
            spinboxMass.setFixedSize(QSize(80, 20))
            spinboxMass.move(280, 140)
            spinboxMass.setPrefix("x10*  ")
            spinboxMass.setSingleStep(1)
            spinboxMass.valueChanged.connect(value_changed)
            spinboxMass.show()

            labAlt = QLabel(L[47])
            labAlt.setParent(windowCaractSchwarszchild)
            labAlt.move(25, 200)
            labAlt.setFixedSize(QSize(350, 30))
            labAlt.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labAlt.setFont(font2)
            labAlt.setToolTip(L[178])
            labAlt.show()
            entAlt = QLineEdit()
            entAlt.setParent(windowCaractSchwarszchild)
            entAlt.move(100, 240)
            entAlt.setFixedSize(QSize(200, 20))
            entAlt.textChanged.connect(text_alt)
            entAlt.show()

            def recupdata81():
                try:
                    m = m3*10**val
                except:
                    m = m3
                rs = (2*(6.67*10**-11)*m)/(299792458**2)

                sk = ((48*((6.67*10**-11)**2)*(m**2))/((299792458**4)*(b**6)))

                Temp1 = 1/(8*3.141592653589793238*(1.380649*10**-23))
                Temp2 = (1.054571818*10**-34)/((6.67*10**-11)*m)
                Temp = Temp1*Temp2

                Te1 = 5120*3.141592653589793238
                Te2 = ((6.67*10**-11)**2) / \
                    ((299792458**4)*(1.054571818*10**-34))

                Te = Te1*Te2*(m**3)
                Risco = 3*rs
                Visco1 = sqrt(rs/(2*Risco))
                Visco = Visco1*(299792458)

                x = [8, 2, m, b, rs, sk, Temp, Te, Risco, Visco, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     46, m, 47, b, 0, 0, 0, 0, 0, 0,
                     76, 45, 33, rs, 52, sk, 114, Risco, 116, Visco, 0,
                     53, 54, Temp, 55, Te, 0, 0, 0, 0, 0]
                np.savetxt(path2, x)

                windowCaractSchwarszchild.hide()
                windowCaracteristique.hide()
                swarsResults8()

            btnValid1 = QPushButton(L[11])
            btnValid1.setParent(windowCaractSchwarszchild)
            btnValid1.move(155, 300)
            btnValid1.setFixedSize(QSize(90, 30))
            btnValid1.pressed.connect(recupdata81)
            btnValid1.setFont(font2)
            btnValid1.show()

            labDecMassOpt = QLabel(L[109] + "\n" + L[110])
            labDecMassOpt.setParent(windowCaractSchwarszchild)
            labDecMassOpt.move(25, 360)
            labDecMassOpt.setFixedSize(QSize(360, 50))
            labDecMassOpt.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            font4 = labDecMassOpt.font()
            font4.setPointSize(10)
            labDecMassOpt.setFont(font4)
            labDecMassOpt.show()

            def MassDecCalc():
                windowCaracteristique.hide()
                window8.show()
                labTitle2 = QLabel(L[48] + "\n" + L[49])
                labTitle2.setStyleSheet("background-color: #3EF724")
                labTitle2.setParent(window8)
                labTitle2.move(70, 15)
                labTitle2.setFixedSize(QSize(260, 50))
                labTitle2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                labTitle2.setFont(font1)
                labTitle2.show()

                def text_Dec(dec2):
                    global dec
                    dec = float(dec2)

                def text_Dis(dis2):
                    global dis
                    dis = float(dis2)

                labDecSpect = QLabel(L[50])
                labDecSpect.setParent(window8)
                labDecSpect.move(50, 90)
                labDecSpect.setFixedSize(QSize(300, 30))
                labDecSpect.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                labDecSpect.setFont(font2)
                labDecSpect.show()
                entDecSpect = QLineEdit()
                entDecSpect.setParent(window8)
                entDecSpect.move(100, 140)
                entDecSpect.setFixedSize(QSize(200, 20))
                entDecSpect.textChanged.connect(text_Dec)
                entDecSpect.show()

                labDistance = QLabel(L[51])
                labDistance.setParent(window8)
                labDistance.move(25, 185)
                labDistance.setFixedSize(QSize(350, 45))
                labDistance.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                labDistance.setFont(font2)
                labDistance.show()
                entDistance = QLineEdit()
                entDistance.setParent(window8)
                entDistance.move(100, 260)
                entDistance.setFixedSize(QSize(200, 20))
                entDistance.textChanged.connect(text_Dis)
                entDistance.show()

                def recupdata83():

                    first = (((299792458**2)*dis)/((dec+1)**2)) - \
                        ((299792458**2)*dis)
                    M = first/((-2)*(6.67*10**-11))

                    rs = (2*(6.67*10**-11)*M)/(299792458**2)

                    x = [8, 3, dis, dec, rs, M, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0,
                         50, dec, 51, dis, 0, 0, 0, 0, 0, 0,
                         48, 49, 78, M, 33, rs, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                    np.savetxt(path2, x)
                    window8.hide()
                    windowCaracteristique.hide()
                    swarsResults8()

                btnValid2 = QPushButton(L[11])
                btnValid2.setParent(window8)
                btnValid2.move(135, 350)
                btnValid2.setFixedSize(QSize(130, 25))
                btnValid2.pressed.connect(recupdata83)
                btnValid2.setFont(font4)
                btnValid2.show()

            btnValid1 = QPushButton(L[111])
            btnValid1.setParent(windowCaractSchwarszchild)
            btnValid1.move(135, 420)
            btnValid1.setFixedSize(QSize(130, 25))
            btnValid1.pressed.connect(MassDecCalc)
            btnValid1.setFont(font4)
            btnValid1.show()

            def web():
                webbrowser.open_new(
                    r"https://fr.wikipedia.org/wiki/Trou_noir_de_Schwarzschild")

            btnWiki = QPushButton()
            btnWiki.setParent(windowCaractSchwarszchild)
            btnWiki.move(15, 50)
            btnWiki.setFixedSize(QSize(30, 20))
            btnWiki.pressed.connect(web)
            btnWiki.setStyleSheet(
                "border-image : url(/usr/lib/spoutnx/img/logo wiki.png);")
            btnWiki.show()

#   KERR CARACTERISTIQUES

        if choiceTypeBlachHole == L[44]:
            windowCaractKerr.show()
            try:
                windowCaractSchwarszchild.hide()
            except:
                pass
            liste.hide()
            labTitleChoice.hide()

            labTitle1 = QLabel(L[112] + "\n" + L[59])
            labTitle1.setStyleSheet("background-color: #3EF724")
            labTitle1.setParent(windowCaractKerr)
            labTitle1.move(70, 15)
            labTitle1.setFixedSize(QSize(260, 50))
            labTitle1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labTitle1.setFont(font1)
            labTitle1.show()

            def text_mass(m2):
                global m3
                m3 = float(m2)

            def text_Mc(Mc3):
                global Mc2
                Mc2 = float(Mc3)

            def text_Cl(Cl2):
                global Cl
                Cl = float(Cl2)

            def Mass_changed(vn):
                global val
                val = vn
                print(val)

            def Mc_changed(vn2):
                global val2
                val2 = vn2

            def FcntMomentCinetic():
                windowMomentCinetic.show()
                print("stackedwidget")

            labMc = QLabel(L[60])
            labMc.setParent(windowCaractKerr)
            labMc.move(50, 80)
            labMc.setFixedSize(QSize(300, 30))
            font2 = labMc.font()
            font2.setPointSize(12)
            labMc.setFont(font2)
            labMc.show()

            entMc = QLineEdit()
            entMc.setParent(windowCaractKerr)
            entMc.move(70, 120)
            entMc.setFixedSize(QSize(200, 20))
            entMc.textChanged.connect(text_Mc)
            entMc.show()

            spinboxMc = QDoubleSpinBox()
            spinboxMc.setParent(windowCaractKerr)
            spinboxMc.setRange(0, 1000)
            spinboxMc.setFixedSize(QSize(80, 20))
            spinboxMc.move(280, 120)
            spinboxMc.setPrefix("x10*  ")
            spinboxMc.setSingleStep(1)
            spinboxMc.valueChanged.connect(Mc_changed)
            spinboxMc.show()

            labAngle = QLabel(L[61])
            labAngle.setParent(windowCaractKerr)
            labAngle.move(25, 165)
            labAngle.setFixedSize(QSize(350, 45))
            labAngle.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labAngle.setFont(font2)
            labAngle.show()
            entAngle = QLineEdit()
            entAngle.setParent(windowCaractKerr)
            entAngle.move(100, 220)
            entAngle.setFixedSize(QSize(200, 20))
            entAngle.textChanged.connect(text_Cl)
            entAngle.show()

            labMass = QLabel(L[46])
            labMass.setParent(windowCaractKerr)
            labMass.move(25, 280)
            labMass.setFixedSize(QSize(350, 30))
            labMass.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labMass.setFont(font2)
            labMass.show()
            entMass = QLineEdit()
            entMass.setParent(windowCaractKerr)
            entMass.move(70, 310)
            entMass.setFixedSize(QSize(200, 20))
            entMass.textChanged.connect(text_mass)
            entMass.show()

            spinboxMass = QDoubleSpinBox()
            spinboxMass.setRange(0, 1000)
            spinboxMass.setParent(windowCaractKerr)
            spinboxMass.setFixedSize(QSize(80, 20))
            spinboxMass.move(280, 310)
            spinboxMass.setPrefix("x10*  ")
            spinboxMass.setSingleStep(1)
            spinboxMass.valueChanged.connect(Mass_changed)
            spinboxMass.show()

            def recupdata62():
                try:
                    m = m3*10**val
                except:
                    m = m3

                try:
                    Mc = Mc2*10**val2
                except:
                    Mc = Mc2
                tr = (299792458*Mc)/((6.67*10**-11)*m)
                ps = tr/m

                a3 = ((299792458**2)/(6.67*10**-11))*(tr/m)
                risco = ((6.67*10**-11)*m)/(299792458**2)
                eisco = (299792458**2)/(sqrt(3))

                rs = (2*(6.67430*10**-11)*m)/(299792458**2)
                rm = (rs/2)-sqrt(((rs/2)**2)-(tr**2))
                rp = (rs/2)+sqrt(((rs/2)**2)-(tr**2))

                f = math.cos(Cl)

                rSm = (rs/2) - sqrt(((rs/2)**2)-((tr**2)*(f**2)))
                rSp = (rs/2) + sqrt(((rs/2)**2)-((tr**2)*(f**2)))
                print(rm, rp, rSm, rSp)

                if 0.8 <= a3 <= 1.1:
                    TXT = 136

                if a3 < 0.8:
                    TXT = 140

                if a3 > 1.1:
                    TXT = 139

                x = [8, 1, Mc, Cl, m, tr, ps, rs, rm,
                     rp, rSm, rSp, a3, risco, eisco, 0, 0, 0, 0, 0, 0, 0, 0,
                     60, Mc, 61, Cl, 46, m, 0, 0, 0, 0,
                     112, 59, 63, tr, 64, ps, 0, 0, 0, 0, TXT,
                     138, 65, rp, 66, rm, 91, rSp, 92, rSm, 1]
                np.savetxt(path2, x)
                windowCaractKerr.hide()
                windowCaracteristique.hide()
                swarsResults8()

            def web():
                webbrowser.open_new(
                    r"https://fr.wikipedia.org/wiki/Trou_noir_de_Kerr#M%C3%A9trique_de_Kerr")

            btnWiki = QPushButton()
            btnWiki.setParent(windowCaractKerr)
            btnWiki.move(15, 50)
            btnWiki.setFixedSize(QSize(30, 20))
            btnWiki.pressed.connect(web)
            btnWiki.setStyleSheet(
                "border-image : url(/usr/lib/spoutnx/img/logo wiki.png);")
            btnWiki.show()

            btnValid = QPushButton(L[11])
            btnValid.setParent(windowCaractKerr)
            btnValid.move(155, 350)
            btnValid.setFixedSize(QSize(90, 30))
            btnValid.pressed.connect(recupdata62)
            btnValid.setFont(font2)
            btnValid.show()

            # Calcul du moment cinétique

            def Value_Rayon(R1):
                global R
                R = float(R1)

            def Value_Mass(M1):
                global m_Mc
                m_Mc = float(M1)

            def Value_Angle(Vw):
                global w
                w = float(Vw)

            def Mass_changed_Mc(expM1):
                global expM
                expM = float(expM1)

            def Calc_Mc():

                try:
                    m = m_Mc*10**expM
                except:
                    m = m_Mc
                windowMomentCinetic.hide()
                Mc = 2/5*m*R*w
                entMc.setText(str(Mc))

            btnMomentCinetic = QPushButton()
            btnMomentCinetic.setStyleSheet(
                "border-image : url(/usr/lib/spoutnx/img/logo moment cinetique.png);")
            btnMomentCinetic.setParent(windowCaractKerr)
            btnMomentCinetic.move(10, 110)
            btnMomentCinetic.setFixedSize(QSize(40, 40))
            btnMomentCinetic.pressed.connect(FcntMomentCinetic)
            btnMomentCinetic.show()

            windowMomentCinetic = QStackedWidget()
            windowMomentCinetic.setParent(windowCaractKerr)
            windowMomentCinetic.setFixedSize(QSize(250, 200))
            windowMomentCinetic.setStyleSheet('background-color: #0089ff;')
            windowMomentCinetic.move(50, 100)

            labTitle_Mc = QLabel(L[221])
            labTitle_Mc.setParent(windowMomentCinetic)
            labTitle_Mc.move(10, 5)
            labTitle_Mc.setFixedSize(QSize(230, 20))
            labTitle_Mc.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            font5 = labTitle_Mc.font()
            font5.setPointSize(10)
            font5.setBold(True)
            font3 = labTitle_Mc.font()
            font3.setPointSize(10)
            labTitle_Mc.setFont(font5)
            labTitle_Mc.show()

            labRayonEtoile = QLabel(L[219] + "\n" + L[220])
            labRayonEtoile.setParent(windowMomentCinetic)
            labRayonEtoile.move(10, 30)
            labRayonEtoile.setFixedSize(QSize(100, 40))
            labRayonEtoile.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labRayonEtoile.setFont(font3)
            labRayonEtoile.show()

            entRayonEtoile = QLineEdit()
            entRayonEtoile.setParent(windowMomentCinetic)
            entRayonEtoile.move(130, 40)
            entRayonEtoile.setFixedSize(QSize(90, 20))
            entRayonEtoile.textChanged.connect(Value_Rayon)
            entRayonEtoile.show()

            labMassEtoile = QLabel(L[78])
            labMassEtoile.setParent(windowMomentCinetic)
            labMassEtoile.move(10, 80)
            labMassEtoile.setFixedSize(QSize(100, 20))
            labMassEtoile.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labMassEtoile.setFont(font3)
            labMassEtoile.show()

            entMassEtoile = QLineEdit()
            entMassEtoile.setParent(windowMomentCinetic)
            entMassEtoile.move(130, 80)
            entMassEtoile.setFixedSize(QSize(90, 20))
            entMassEtoile.textChanged.connect(Value_Mass)
            entMassEtoile.show()

            spinboxMass_Mc = QDoubleSpinBox()
            spinboxMass_Mc.setRange(0, 1000)
            spinboxMass_Mc.setParent(windowMomentCinetic)
            spinboxMass_Mc.setFixedSize(QSize(80, 20))
            spinboxMass_Mc.move(130, 105)
            spinboxMass_Mc.setPrefix("x10*  ")
            spinboxMass_Mc.setSingleStep(1)
            spinboxMass_Mc.valueChanged.connect(Mass_changed_Mc)
            spinboxMass_Mc.show()

            labVitAngEtoile = QLabel(L[222])
            labVitAngEtoile.setParent(windowMomentCinetic)
            labVitAngEtoile.move(5, 140)
            labVitAngEtoile.setFixedSize(QSize(110, 20))
            labVitAngEtoile.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labVitAngEtoile.setFont(font3)
            labVitAngEtoile.show()

            entVitAngEtoile = QLineEdit()
            entVitAngEtoile.setParent(windowMomentCinetic)
            entVitAngEtoile.move(130, 140)
            entVitAngEtoile.setFixedSize(QSize(90, 20))
            entVitAngEtoile.textChanged.connect(Value_Angle)
            entVitAngEtoile.show()

            btnValid_Mc = QPushButton(L[11])
            btnValid_Mc.setParent(windowMomentCinetic)
            btnValid_Mc.move(5, 170)
            btnValid_Mc.setFixedSize(QSize(240, 25))
            btnValid_Mc.pressed.connect(Calc_Mc)
            btnValid_Mc.setFont(font3)
            btnValid_Mc.show()

            def Close_Tool():
                windowMomentCinetic.hide()

            btnClose_Tool = QPushButton("X")
            btnClose_Tool.setParent(windowMomentCinetic)
            btnClose_Tool.move(230, 5)
            btnClose_Tool.setFixedSize(QSize(15, 15))
            btnClose_Tool.pressed.connect(Close_Tool)
            btnClose_Tool.setFont(font3)
            btnClose_Tool.show()

    liste = QListWidget()
    liste.addItem(L[43])
    liste.addItem(L[44])
    liste.setParent(windowCaracteristique)
    liste.move(50, 200)
    liste.setFixedSize(QSize(300, 70))
    liste.setStyleSheet("QListView::item:selected{background-color: #3EF724}")
    liste.setCurrentItem(None)
    font2 = liste.font()
    font2.setPointSize(12)
    liste.setFont(font2)
    liste.itemClicked.connect(ChoiceUser)
    liste.show()

    windowCaracteristique.show()
