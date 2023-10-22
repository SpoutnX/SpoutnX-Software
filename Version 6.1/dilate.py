################################ SCRIPT DILATATION ############################

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
    QListWidget,
    QComboBox,
    QStackedWidget,
    QDoubleSpinBox,
    QCheckBox
)
from PySide6.QtGui import QIcon, QPixmap


user = os.getlogin()
Path = "/home/" + user + "/.SpoutnX/"
path2 = Path + "data.sptx"
path3 = Path + "user_data.txt"
path4 = Path + "lang/user_lang.sptx"

mes_nombres = open(path4).read()
L = mes_nombres.split('\n')


windowMain_Contract_long = QWidget()
windowMain_Contract_long.setWindowTitle("Résultats")
windowMain_Contract_long.setFixedSize(QSize(500, 400))
windowMain_Contract_long.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))


def swarsResults():

    S = np.loadtxt(path2)
    S2 = ["%.2f" % i for i in S]
    Value0 = float(S[0])
    Value1 = float(S[1])

    Value4 = str(S[4])
    try:
        Value5 = str(S[5])
        Value7 = str(S[7])
        Value12 = str(S[12])
    except:
        pass

    windowResult_DilatationSpeed = QWidget()
    windowResult_DilatationSpeed.setWindowTitle("Résultats")
    windowResult_DilatationSpeed.setFixedSize(QSize(500, 400))
    windowResult_DilatationSpeed.setWindowIcon(
        QIcon('/usr/lib/spoutnx/icone2.ico'))
    windowResult_DilatationSpeed.show()


# DILATATION TEMPORELLE VITESSE MINKOWSKI -- RESULTATS

    if Value0 == 1 and Value1 == 2 or Value1 == 3:
        labDataSpeed2 = QLabel("v = " + "\n" + S2[2])
        labDataSpeed2.setParent(windowResult_DilatationSpeed)
        labDataSpeed2.move(10, 200)
        labDataSpeed2.setFixedSize(QSize(170, 50))
        labDataSpeed2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font2 = labDataSpeed2.font()
        font2.setPointSize(10)
        labDataSpeed2.setFont(font2)
        labDataSpeed2.show()

        labTitleDilatationMin = QLabel(L[20])
        labTitleDilatationMin.setStyleSheet("background-color: #3EF724")
        labTitleDilatationMin.setParent(windowResult_DilatationSpeed)
        labTitleDilatationMin.move(220, 20)
        labTitleDilatationMin.setFixedSize(QSize(200, 30))
        labTitleDilatationMin.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font3 = labTitleDilatationMin.font()
        font3.setPointSize(13)
        labTitleDilatationMin.setFont(font3)
        labTitleDilatationMin.show()

        labResultDilat = QLabel(Value7)
        if Value1 == 3:
            label66 = QLabel(Value12)
        labResultDilat.setParent(windowResult_DilatationSpeed)
        labResultDilat.move(195, 60)
        labResultDilat.setFixedSize(QSize(250, 30))
        labResultDilat.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font4 = labResultDilat.font()
        font4.setPointSize(12)
        labResultDilat.setFont(font4)
        labResultDilat.setToolTip(L[170] + "\n" + L[171])
        labResultDilat.show()

        labFormula4 = QLabel(L[22])
        labFormula4.setParent(windowResult_DilatationSpeed)
        labFormula4.move(195, 100)
        labFormula4.setFixedSize(QSize(250, 30))
        labFormula4.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labFormula4.setFont(font4)
        labFormula4.show()

        if Value1 == 2:
            path = '/usr/lib/spoutnx/img/Dilatation Min.png'
        else:
            path = '/usr/lib/spoutnx/img/dilatation perso.png'

        logoFormulaMinkowski = QLabel()
        logoFormulaMinkowski.setPixmap(
            QPixmap(path))
        logoFormulaMinkowski.setParent(windowResult_DilatationSpeed)
        logoFormulaMinkowski.move(220, 200)
        logoFormulaMinkowski.setFixedSize(QSize(200, 120))
        logoFormulaMinkowski.setScaledContents(True)
        logoFormulaMinkowski.show()

        def ReturnDat():
            windowResult_DilatationSpeed.hide()
            windowResult_DilatationSpeed.deleteLater()

            timedilate()

        btnReturn4 = QPushButton(L[108])
        btnReturn4.setParent(windowResult_DilatationSpeed)
        btnReturn4.move(10, 300)
        btnReturn4.setFixedSize(QSize(150, 25))
        btnReturn4.setFont(font2)
        btnReturn4.pressed.connect(ReturnDat)
        btnReturn4.show()


# DILATATION TEMPORELLE VITESSE SCHWARSZCHILD -- RESULTATS

    if Value0 == 1 and Value1 == 1:

        S24 = "{:.9e}".format(S[4])
        labDataMass2 = QLabel("m = " + "\n" + S24)
        labDataMass2.setParent(windowResult_DilatationSpeed)
        labDataMass2.move(10, 100)
        labDataMass2.setFixedSize(QSize(170, 50))
        labDataMass2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font2 = labDataMass2.font()
        font2.setPointSize(10)
        labDataMass2.setFont(font2)
        labDataMass2.show()

        labDataR2 = QLabel("r = " + "\n" + S2[3])
        labDataR2.setParent(windowResult_DilatationSpeed)
        labDataR2.move(10, 150)
        labDataR2.setFixedSize(QSize(170, 50))
        labDataR2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataR2.setFont(font2)
        labDataR2.show()

        labDataV = QLabel("v = " + "\n" + S2[2])
        labDataV.setParent(windowResult_DilatationSpeed)
        labDataV.move(10, 200)
        labDataV.setFixedSize(QSize(170, 50))
        labDataV.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataV.setFont(font2)
        labDataV.show()

        labTitleDilatationSC = QLabel(L[20])
        labTitleDilatationSC.setStyleSheet("background-color: #3EF724")
        labTitleDilatationSC.setParent(windowResult_DilatationSpeed)
        labTitleDilatationSC.move(220, 20)
        labTitleDilatationSC.setFixedSize(QSize(200, 30))
        labTitleDilatationSC.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font3 = labTitleDilatationSC.font()
        font3.setPointSize(13)
        labTitleDilatationSC.setFont(font3)
        labTitleDilatationSC.show()

        labResultDilat = QLabel(Value5)
        labResultDilat.setParent(windowResult_DilatationSpeed)
        labResultDilat.move(195, 60)
        labResultDilat.setFixedSize(QSize(250, 30))
        labResultDilat.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font4 = labResultDilat.font()
        font4.setPointSize(12)
        labResultDilat.setFont(font4)
        labResultDilat.setToolTip(L[170] + "\n" + L[171])
        labResultDilat.show()

        labFormula3 = QLabel(L[22])
        labFormula3.setParent(windowResult_DilatationSpeed)
        labFormula3.move(195, 100)
        labFormula3.setFixedSize(QSize(250, 30))
        labFormula3.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labFormula3.setFont(font4)
        labFormula3.show()

        logoFormulaDilat = QLabel()
        logoFormulaDilat.setPixmap(
            QPixmap('/usr/lib/spoutnx/img/dilatation SC.png'))
        logoFormulaDilat.setParent(windowResult_DilatationSpeed)
        logoFormulaDilat.move(220, 200)
        logoFormulaDilat.setFixedSize(QSize(200, 120))
        logoFormulaDilat.setScaledContents(True)
        logoFormulaDilat.show()

        def ReturnDat():
            windowResult_DilatationSpeed.hide()
            windowResult_DilatationSpeed.deleteLater()

            timedilate()

        btnReturn3 = QPushButton(L[108])
        btnReturn3.setParent(windowResult_DilatationSpeed)
        btnReturn3.move(10, 300)
        btnReturn3.setFixedSize(QSize(150, 25))
        btnReturn3.setFont(font2)
        btnReturn3.pressed.connect(ReturnDat)
        btnReturn3.show()

# DILATATION TEMPORELLE OBJET MASSIF --- RESULTATS
    if Value0 == 1 and Value1 == 4:

        S23 = "{:.9e}".format(S[3])
        labDataMass = QLabel("m = " + "\n" + S23)
        labDataMass.setParent(windowResult_DilatationSpeed)
        labDataMass.move(10, 100)
        labDataMass.setFixedSize(QSize(170, 50))
        labDataMass.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font2 = labDataMass.font()
        font2.setPointSize(10)
        labDataMass.setFont(font2)
        labDataMass.show()

        labDataR = QLabel("r = " + "\n" + S2[2])
        labDataR.setParent(windowResult_DilatationSpeed)
        labDataR.move(10, 150)
        labDataR.setFixedSize(QSize(170, 50))
        labDataR.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataR.setFont(font2)
        labDataR.show()

        labTitleObjMassif = QLabel(L[20])
        labTitleObjMassif.setStyleSheet("background-color: #3EF724")
        labTitleObjMassif.setParent(windowResult_DilatationSpeed)
        labTitleObjMassif.move(220, 20)
        labTitleObjMassif.setFixedSize(QSize(200, 30))
        labTitleObjMassif.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font3 = labTitleObjMassif.font()
        font3.setPointSize(13)
        labTitleObjMassif.setFont(font3)
        labTitleObjMassif.show()

        labResultDilate = QLabel(Value4)
        labResultDilate.setParent(windowResult_DilatationSpeed)
        labResultDilate.move(195, 60)
        labResultDilate.setFixedSize(QSize(250, 30))
        labResultDilate.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font4 = labResultDilate.font()
        font4.setPointSize(12)
        labResultDilate.setToolTip(L[170] + "\n" + L[171])
        labResultDilate.setFont(font4)
        labResultDilate.show()

        labFormula2 = QLabel(L[22])
        labFormula2.setParent(windowResult_DilatationSpeed)
        labFormula2.move(195, 100)
        labFormula2.setFixedSize(QSize(250, 30))
        labFormula2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labFormula2.setFont(font4)
        labFormula2.show()

        ImgDilatation = QLabel()
        ImgDilatation.setPixmap(
            QPixmap('/usr/lib/spoutnx/img/dilatation obj.png'))
        ImgDilatation.setParent(windowResult_DilatationSpeed)
        ImgDilatation.move(240, 200)
        ImgDilatation.setFixedSize(QSize(200, 160))
        ImgDilatation.setScaledContents(True)
        ImgDilatation.show()

        def ReturnDat():
            windowResult_DilatationSpeed.hide()
            windowResult_DilatationSpeed.deleteLater()

            timedilate()

        btnReturn2 = QPushButton(L[108])
        btnReturn2.setParent(windowResult_DilatationSpeed)
        btnReturn2.move(10, 300)
        btnReturn2.setFixedSize(QSize(150, 25))
        btnReturn2.setFont(font2)
        btnReturn2.pressed.connect(ReturnDat)
        btnReturn2.show()

# CONTRACTION DES LONGUEURS ---- RESULTATS

    if Value0 == 1 and Value1 == 5:
        global windowResult_Contract_long
        try:
            windowResult_Contract_long.deleteLater()
        except:
            pass
        windowResult_Contract_long = QStackedWidget()
        windowResult_Contract_long.setParent(windowMain_Contract_long)
        windowResult_Contract_long.setFixedSize(QSize(550, 400))
        windowMain_Contract_long.show()
        windowResult_Contract_long.show()
        try:
            label56.hide()
        except:
            pass

        labDataSpeed = QLabel("v = " + "\n" + S2[3])
        labDataSpeed.setParent(windowResult_Contract_long)
        labDataSpeed.move(10, 100)
        labDataSpeed.setFixedSize(QSize(170, 50))
        labDataSpeed.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font2 = labDataSpeed.font()
        font2.setPointSize(10)
        labDataSpeed.setFont(font2)
        labDataSpeed.show()

        labDataLong = QLabel("l = " + "\n" + S2[2])
        labDataLong.setParent(windowResult_Contract_long)
        labDataLong.move(10, 150)
        labDataLong.setFixedSize(QSize(170, 50))
        labDataLong.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataLong.setFont(font2)
        labDataLong.show()

        labTitleContract = QLabel(L[132])
        labTitleContract.setStyleSheet("background-color: #3EF724")
        labTitleContract.setParent(windowResult_Contract_long)
        labTitleContract.move(145, 10)
        labTitleContract.setFixedSize(QSize(350, 30))
        labTitleContract.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font3 = labTitleContract.font()
        font3.setPointSize(13)
        labTitleContract.setFont(font3)
        labTitleContract.show()

        labResultNewLong = QLabel(L[134])
        labResultNewLong.setParent(windowResult_Contract_long)
        labResultNewLong.move(145, 60)
        labResultNewLong.setFixedSize(QSize(350, 30))
        labResultNewLong.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font4 = labResultNewLong.font()
        font4.setPointSize(12)
        labResultNewLong.setFont(font4)
        labResultNewLong.show()

        labNewLong = QLabel(Value5)
        labNewLong.setParent(windowResult_Contract_long)
        labNewLong.move(195, 90)
        labNewLong.setFixedSize(QSize(250, 30))
        labNewLong.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labNewLong.setFont(font4)
        labNewLong.show()

        labResultLorentz = QLabel(L[135])
        labResultLorentz.setParent(windowResult_Contract_long)
        labResultLorentz.move(145, 150)
        labResultLorentz.setFixedSize(QSize(350, 30))
        labResultLorentz.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResultLorentz.setFont(font4)
        labResultLorentz.show()

        labLorentz = QLabel(Value4)
        labLorentz.setParent(windowResult_Contract_long)
        labLorentz.move(195, 180)
        labLorentz.setFixedSize(QSize(250, 30))
        labLorentz.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labLorentz.setFont(font4)
        labLorentz.show()

        labFormula = QLabel(L[22])
        labFormula.setParent(windowResult_Contract_long)
        labFormula.move(195, 220)
        labFormula.setFixedSize(QSize(250, 30))
        labFormula.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labFormula.setFont(font4)
        labFormula.show()

        ImgFormul = QLabel()
        ImgFormul.setPixmap(
            QPixmap('/usr/lib/spoutnx/img/Contraction.png'))
        ImgFormul.setParent(windowResult_Contract_long)
        ImgFormul.move(200, 270)
        ImgFormul.setFixedSize(QSize(250, 130))
        ImgFormul.setScaledContents(True)
        ImgFormul.setToolTip("Transformation de Lorentz")
        ImgFormul.show()

        def ReturnDat():
            windowResult_Contract_long.deleteLater()
            windowMain_Contract_long.hide()
            timedilate()

        btnReturn = QPushButton(L[108])
        btnReturn.setParent(windowResult_Contract_long)
        btnReturn.move(10, 300)
        btnReturn.setFixedSize(QSize(150, 25))
        btnReturn.setFont(font2)
        btnReturn.pressed.connect(ReturnDat)
        btnReturn.show()

# ________________________CARACTERISTIQUES_________________________________


windowCaracteristics = QWidget()
windowCaracteristics.setWindowTitle("Caractéristiques")
windowCaracteristics.setFixedSize(QSize(400, 450))
windowCaracteristics.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))

window_RG = QStackedWidget()
window_RG.setParent(windowCaracteristics)
window_RG.setFixedSize(QSize(400, 450))


windowRR_Minkowski = QStackedWidget()
windowRR_Minkowski.setParent(windowCaracteristics)
windowRR_Minkowski.setFixedSize(QSize(400, 450))

windowRR_Schwarszchild = QStackedWidget()
windowRR_Schwarszchild.setParent(windowCaracteristics)
windowRR_Schwarszchild.setFixedSize(QSize(400, 450))

window_Contract_long = QWidget()
window_Contract_long.setWindowTitle("Caractéristiques")
window_Contract_long.setFixedSize(QSize(400, 450))
window_Contract_long.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))


def timedilate():
    try:
        window_RG.hide()
        windowRR_Minkowski.hide()
        windowRR_Schwarszchild.hide()
        windowResult_DilatationSpeed.hide()
        metri.hide()
    except:
        pass

    labTitle1 = QLabel(L[84])
    labTitle1.setParent(windowCaracteristics)
    labTitle1.move(125, 100)
    labTitle1.setFixedSize(QSize(150, 25))
    labTitle1.setStyleSheet("background-color: #3EF724")
    labTitle1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    font1 = labTitle1.font()
    font1.setPointSize(13)
    labTitle1.setFont(font1)
    labTitle1.show()

    def ChoiceUser(ObjectivUser):
        labTitle1.hide()
        listeChoices.hide()
        btnChoices.hide()
        ObjectivUser = ObjectivUser.text()

# DILATATION A CAUSE D UNE VITESSE

        if ObjectivUser == L[97]:

            def Metrique(Metric):
                windowRR_Minkowski.hide()
                if Metric == "Schwarzschild":
                    windowRR_Schwarszchild.show()

                    def Value_VitAng(v):
                        global v2
                        v2 = float(v)

                    def Value_alt(alt):
                        global alt2
                        alt2 = float(alt)

                    def Value_Mass(m):
                        global m3
                        m3 = float(m)

                    def value_exp_Mass(vn):
                        global val
                        val = vn
                        print(val)

                    labTitleCaract1 = QLabel(L[20] + "\n" + L[97])
                    labTitleCaract1.setParent(windowRR_Schwarszchild)
                    labTitleCaract1.move(100, 10)
                    labTitleCaract1.setFixedSize(QSize(200, 50))
                    labTitleCaract1.setStyleSheet("background-color: #3EF724")
                    labTitleCaract1.setAlignment(
                        Qt.AlignHCenter | Qt.AlignVCenter)
                    font1 = labTitleCaract1.font()
                    font1.setPointSize(13)
                    labTitleCaract1.setFont(font1)
                    labTitleCaract1.show()

                    labChoiceMetric = QLabel(L[12])
                    labChoiceMetric.setParent(windowRR_Schwarszchild)
                    labChoiceMetric.move(125, 70)
                    labChoiceMetric.setFixedSize(QSize(150, 25))
                    labChoiceMetric.setAlignment(
                        Qt.AlignHCenter | Qt.AlignVCenter)
                    font2 = labChoiceMetric.font()
                    font2.setPointSize(12)
                    labChoiceMetric.setFont(font2)
                    labChoiceMetric.show()

                    labVitAng = QLabel(L[15])
                    labVitAng.setParent(windowRR_Schwarszchild)
                    labVitAng.move(25, 160)
                    labVitAng.setFixedSize(QSize(350, 25))
                    labVitAng.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    labVitAng.setFont(font2)
                    labVitAng.show()
                    entVitAng = QLineEdit()
                    entVitAng.setParent(windowRR_Schwarszchild)
                    entVitAng.move(100, 190)
                    entVitAng.setFixedSize(QSize(200, 20))
                    entVitAng.textChanged.connect(Value_VitAng)
                    entVitAng.show()

                    labAltitud = QLabel(L[16])
                    labAltitud.setParent(windowRR_Schwarszchild)
                    labAltitud.move(25, 240)
                    labAltitud.setFixedSize(QSize(350, 25))
                    labAltitud.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    labAltitud.setFont(font2)
                    labAltitud.show()
                    entAltitud = QLineEdit()
                    entAltitud.setParent(windowRR_Schwarszchild)
                    entAltitud.move(100, 270)
                    entAltitud.setFixedSize(QSize(200, 20))
                    entAltitud.textChanged.connect(Value_alt)
                    entAltitud.show()

                    labMass = QLabel(L[17])
                    labMass.setParent(windowRR_Schwarszchild)
                    labMass.move(25, 320)
                    labMass.setFixedSize(QSize(350, 25))
                    labMass.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    labMass.setFont(font2)
                    labMass.show()
                    entMass = QLineEdit()
                    entMass.setParent(windowRR_Schwarszchild)
                    entMass.move(70, 350)
                    entMass.setFixedSize(QSize(200, 20))
                    entMass.textChanged.connect(Value_Mass)
                    entMass.show()

                    spinboxMass = QDoubleSpinBox()
                    spinboxMass.setRange(0, 1000)
                    spinboxMass.setParent(windowRR_Schwarszchild)
                    spinboxMass.setFixedSize(QSize(80, 20))
                    spinboxMass.move(280, 350)
                    spinboxMass.setPrefix("x10*  ")
                    spinboxMass.setSingleStep(1)
                    spinboxMass.valueChanged.connect(value_exp_Mass)
                    spinboxMass.show()

                    def recupdata():
                        try:
                            m2 = m3*10**val
                        except:
                            m2 = m3
                        vtHaut = 299792458**2+(alt2**2)*((v2)**2)
                        vtBas = 299792458**2-((2*(6.67*10**-11)*m2)/alt2)
                        vtTotal = sqrt((vtHaut/vtBas))
                        x = [1, 1, v2, alt2, m2, vtTotal, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             15, v2, 16, alt2, 17, m2, 0, 0, 0, 0,
                             5, 97, 20, vtTotal, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                        metri.hide()
                        windowCaracteristics.hide()
                        np.savetxt(path2, x)
                        swarsResults()

                    btnValid = QPushButton(L[11])
                    btnValid.setParent(windowRR_Schwarszchild)
                    btnValid.move(155, 400)
                    btnValid.setFixedSize(QSize(90, 30))
                    btnValid.pressed.connect(recupdata)
                    btnValid.setFont(font2)
                    btnValid.show()

                    def web():
                        webbrowser.open_new(
                            r"https://fr.wikipedia.org/wiki/Dilatation_du_temps")

                    btnWiki = QPushButton()
                    btnWiki.setParent(windowRR_Schwarszchild)
                    btnWiki.move(15, 50)
                    btnWiki.setFixedSize(QSize(30, 20))
                    btnWiki.pressed.connect(web)
                    btnWiki.setStyleSheet(
                        "border-image : url(/usr/lib/spoutnx/img/logo wiki.png);")
                    btnWiki.show()

                if Metric == "Minkowski" or Metric == L[13]:
                    windowRR_Schwarszchild.hide()
                    windowRR_Minkowski.show()

                    def text_vt(v):
                        global v2
                        v2 = float(v)
                    try:
                        choiceR.hide()
                        choiceColat.hide()
                        choiceLong.hide()
                    except:
                        pass

                    labTitleCaract2 = QLabel(L[20] + "\n" + L[97])
                    labTitleCaract2.setStyleSheet("background-color: #3EF724")
                    labTitleCaract2.setParent(windowRR_Minkowski)
                    labTitleCaract2.move(100, 10)
                    labTitleCaract2.setFixedSize(QSize(200, 50))
                    labTitleCaract2.setAlignment(
                        Qt.AlignHCenter | Qt.AlignVCenter)
                    font1 = labTitleCaract2.font()
                    font1.setPointSize(13)
                    labTitleCaract2.setFont(font1)
                    labTitleCaract2.show()

                    labChoiceMetric2 = QLabel(L[12])
                    labChoiceMetric2.setParent(windowRR_Minkowski)
                    labChoiceMetric2.move(50, 80)
                    labChoiceMetric2.setFixedSize(QSize(300, 25))
                    labChoiceMetric2.setAlignment(
                        Qt.AlignHCenter | Qt.AlignVCenter)
                    font2 = labChoiceMetric2.font()
                    font2.setPointSize(12)
                    labChoiceMetric2.setFont(font2)
                    labChoiceMetric2.show()

                    labVitAng2 = QLabel(L[15])
                    labVitAng2.setParent(windowRR_Minkowski)
                    labVitAng2.move(25, 200)
                    labVitAng2.setFixedSize(QSize(350, 25))
                    labVitAng2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    labVitAng2.setFont(font2)
                    labVitAng2.show()

                    entVitAng2 = QLineEdit()
                    entVitAng2.setParent(windowRR_Minkowski)
                    entVitAng2.move(100, 230)
                    entVitAng2.setFixedSize(QSize(200, 20))
                    entVitAng2.textChanged.connect(text_vt)
                    entVitAng2.show()

                    if Metric == L[13]:

                        def text_v0(v02):
                            global v0
                            v0 = float(v02)

                        def show_stateR(state):
                            print(state)
                            global cho1
                            cho1 = state
                            if cho1 == 2:
                                choiceColat.setCheckState(
                                    Qt.CheckState.PartiallyChecked)
                                choiceLong.setCheckState(
                                    Qt.CheckState.PartiallyChecked)

                        def show_stateColat(state2):
                            print(state2)
                            global cho2
                            cho2 = state2
                            if cho2 == 2:
                                choiceR.setCheckState(
                                    Qt.CheckState.PartiallyChecked)
                                choiceLong.setCheckState(
                                    Qt.CheckState.PartiallyChecked)

                        def show_stateLong(state3):
                            global cho3
                            cho3 = state3
                            print(state3)
                            if cho3 == 2:
                                choiceColat.setCheckState(
                                    Qt.CheckState.PartiallyChecked)
                                choiceR.setCheckState(
                                    Qt.CheckState.PartiallyChecked)

                        choiceR = QCheckBox(L[143])
                        choiceR.setParent(windowRR_Minkowski)
                        choiceR.move(125, 290)
                        choiceR.setFixedSize(QSize(200, 25))
                        choiceR.stateChanged.connect(show_stateR)
                        choiceR.show()

                        choiceColat = QCheckBox(L[144])
                        choiceColat.setParent(windowRR_Minkowski)
                        choiceColat.move(125, 310)
                        choiceColat.setFixedSize(QSize(200, 25))
                        choiceColat.stateChanged.connect(show_stateColat)
                        choiceColat.show()

                        choiceLong = QCheckBox(L[145])
                        choiceLong.setParent(windowRR_Minkowski)
                        choiceLong.move(125, 330)
                        choiceLong.setFixedSize(QSize(200, 25))
                        choiceLong.stateChanged.connect(show_stateLong)
                        choiceLong.show()

                    def recupdata():

                        if Metric == "Minkowski":
                            try:
                                choiceR.hide()
                                choiceColat.hide()
                                choiceLong.hide()
                            except:
                                pass

                            vH = (299792458**2)+(v2**2)
                            vtTot = sqrt((vH/(299792458**2)))
                            x = [1, 2, v2, 0, 0, 0, 0, vtTot, 0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 15, v2, 0, 0, 0, 0, 0, 0, 0, 0,
                                 5, 97, 20, vtTot, 0, 0, 0, 0, 0, 0, 187,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                        if Metric == L[13]:
                            file = open(path3, "r+")
                            lignes = file.readlines()[0:16]
                            file.close()
                            float_list = list(np.float_(lignes))
                            print(float_list[0])

                            if cho1 == 2:
                                g01 = float_list[1]
                                g10 = float_list[4]
                                g11 = float_list[5]

                            if cho2 == 2:
                                g01 = float_list[2]
                                g10 = float_list[8]
                                g11 = float_list[10]

                            if cho3 == 2:
                                g01 = float_list[3]
                                g10 = float_list[12]
                                g11 = float_list[15]
                            delta = ((g01*v2+g10*v2)**2)-4 * \
                                float_list[0]*(g11*(v2**2)-(299792458**2))
                            print(delta)
                            if delta >= 0:
                                x1 = (-(g01*v2)-sqrt(delta))/(2*float_list[0])
                                x2 = (-(g01*v2)+sqrt(delta))/(2*float_list[0])
                                print(x1, x2)
                                VTot = x2

                            choiceR.hide()
                            choiceColat.hide()
                            choiceLong.hide()
                            x = [1, 3, v2, cho1, cho2, cho3,
                                 float_list[0], g01, g10, g11, x1, x2, VTot,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                 15, v2, 0, 0, 0, 0, 0, 0, 0, 0,
                                 5, 97, 20, VTot, 0, 0, 0, 0, 0, 0, 188,
                                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                        np.savetxt(path2, x)
                        metri.hide()
                        windowCaracteristics.hide()
                        swarsResults()

                    btnValid2 = QPushButton(L[11])
                    btnValid2.setParent(windowRR_Minkowski)
                    btnValid2.move(155, 400)
                    btnValid2.setFixedSize(QSize(90, 30))
                    btnValid2.pressed.connect(recupdata)
                    btnValid2.setFont(font2)
                    btnValid2.show()

                    def web():
                        webbrowser.open_new(
                            r"https://fr.wikipedia.org/wiki/Dilatation_du_temps")

                    btnWiki2 = QPushButton()
                    btnWiki2.setParent(windowRR_Minkowski)
                    btnWiki2.move(15, 50)
                    btnWiki2.setFixedSize(QSize(30, 20))
                    btnWiki2.pressed.connect(web)
                    btnWiki2.setStyleSheet(
                        "border-image : url(/usr/lib/spoutnx/img/logo wiki.png);")
                    btnWiki2.show()

            metri = QComboBox()
            metri.setParent(windowCaracteristics)
            metri.move(125, 105)
            metri.setFixedSize(QSize(150, 25))
            metri.addItem("Schwarzschild")
            metri.addItem("Minkowski")
            metri.addItem(L[13])
            metri.currentTextChanged.connect(Metrique)
            metri.setCurrentIndex(1)
            font2 = metri.font()
            font2.setPointSize(12)
            metri.setFont(font2)
            metri.show()

        if ObjectivUser == L[98]:
            window_RG.show()

            def text_m3(m5):
                print("ytre")
                global m3
                m3 = float(m5)

            def text_alt2(alt3):
                print("erty")
                global alt2
                alt2 = float(alt3)

            def Mass_exp(vn):
                global val
                val = vn
                print(val)

            labTitleCaract3 = QLabel(L[20] + "\n" + L[98])
            labTitleCaract3.setStyleSheet("background-color: #3EF724")
            labTitleCaract3.setParent(window_RG)
            labTitleCaract3.move(75, 10)
            labTitleCaract3.setFixedSize(QSize(250, 50))
            labTitleCaract3.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            font1 = labTitleCaract3.font()
            font1.setPointSize(13)
            labTitleCaract3.setFont(font1)
            labTitleCaract3.show()

            labAlt = QLabel(L[16])
            labAlt.setParent(window_RG)
            labAlt.move(100, 100)
            labAlt.setFixedSize(QSize(200, 25))
            labAlt.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            font2 = labAlt.font()
            font2.setPointSize(12)
            labAlt.setFont(font2)
            labAlt.show()

            entAlt = QLineEdit()
            entAlt.setParent(window_RG)
            entAlt.move(100, 130)
            entAlt.setFixedSize(QSize(200, 20))
            entAlt.textChanged.connect(text_alt2)
            entAlt.show()

            labMass2 = QLabel(L[17])
            labMass2.setParent(window_RG)
            labMass2.move(50, 190)
            labMass2.setFixedSize(QSize(300, 25))
            labMass2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labMass2.setFont(font2)
            labMass2.show()

            entMass2 = QLineEdit()
            entMass2.setParent(window_RG)
            entMass2.move(60, 220)
            entMass2.setFixedSize(QSize(200, 20))
            entMass2.textChanged.connect(text_m3)
            entMass2.show()

            spinboxMass2 = QDoubleSpinBox()
            spinboxMass2.setRange(0, 1000)
            spinboxMass2.setParent(window_RG)
            spinboxMass2.setFixedSize(QSize(80, 20))
            spinboxMass2.move(280, 220)
            spinboxMass2.setPrefix("x10*  ")
            spinboxMass2.setSingleStep(1)
            spinboxMass2.valueChanged.connect(Mass_exp)
            spinboxMass2.show()

            def recupdata1():
                try:
                    m2 = m3*10**val
                except:
                    m2 = m3
                U = -(((6.67*10**-11)*m2)/alt2)
                gtt = 1+(2*U/(299792458**2))
                dT = 1/gtt

                x = [1, 4, alt2, m2, dT, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0,
                     16, alt2, 17, m2, 0, 0, 0, 0, 0, 0,
                     5, 98, 20, dT, 0, 0, 0, 0, 0, 0, 45,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                np.savetxt(path2, x)
                windowCaracteristics.hide()
                swarsResults()

            btnValid3 = QPushButton(L[11])
            btnValid3.setParent(window_RG)
            btnValid3.move(155, 350)
            btnValid3.setFixedSize(QSize(90, 30))
            btnValid3.pressed.connect(recupdata1)
            btnValid3.setFont(font2)
            btnValid3.show()

    listeChoices = QListWidget()
    listeChoices.addItem(L[97])
    listeChoices.addItem(L[98])
    listeChoices.setParent(windowCaracteristics)
    listeChoices.move(100, 200)
    listeChoices.setFixedSize(QSize(200, 70))
    listeChoices.setStyleSheet(
        "QListView::item:selected{background-color: #3EF724}")
    listeChoices.setCurrentItem(None)
    font2 = listeChoices.font()
    font2.setPointSize(12)
    listeChoices.setFont(font2)
    listeChoices.itemClicked.connect(ChoiceUser)
    listeChoices.setToolTip(L[169])
    listeChoices.show()

# CALCUL CONTRACTION DES LONGUEURS

    def contractLong():
        windowCaracteristics.hide()
        window_Contract_long.show()
        labTitleContract = QLabel(L[132])
        labTitleContract.setStyleSheet("background-color: #3EF724")
        labTitleContract.setParent(window_Contract_long)
        labTitleContract.move(25, 10)
        labTitleContract.setFixedSize(QSize(350, 30))
        labTitleContract.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font1 = labTitleContract.font()
        font1.setPointSize(13)
        labTitleContract.setFont(font1)
        labTitleContract.show()

        labRelativity = QLabel(L[118])
        labRelativity.setParent(window_Contract_long)
        labRelativity.move(75, 50)
        labRelativity.setFixedSize(QSize(250, 25))
        labRelativity.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labRelativity.setFont(font2)
        labRelativity.show()

        def text_vit(v2):
            global v
            v = float(v2)

        def text_long(l2):
            global l
            l = float(l2)

        labVit = QLabel(L[19])
        labVit.setParent(window_Contract_long)
        labVit.move(75, 120)
        labVit.setFixedSize(QSize(250, 25))
        labVit.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labVit.setFont(font2)
        labVit.show()
        entVit = QLineEdit()
        entVit.setParent(window_Contract_long)
        entVit.move(100, 160)
        entVit.setFixedSize(QSize(200, 20))
        entVit.textChanged.connect(text_vit)
        entVit.show()

        labLong = QLabel(L[133])
        labLong.setParent(window_Contract_long)
        labLong.move(75, 250)
        labLong.setFixedSize(QSize(250, 25))
        labLong.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labLong.setFont(font2)
        labLong.show()
        entLong = QLineEdit()
        entLong.setParent(window_Contract_long)
        entLong.move(100, 290)
        entLong.setFixedSize(QSize(200, 20))
        entLong.textChanged.connect(text_long)
        entLong.show()

        def recupdata11():
            Fl = (1/(sqrt(1-((v**2)/(299792458**2)))))
            Cl = l/Fl

            x = [1, 5, l, v, Fl, Cl, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0,
                 19, v, 133, l, 0, 0, 0, 0, 0, 0,
                 132, 118, 134, Cl, 135, Fl, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            np.savetxt(path2, x)
            window_Contract_long.hide()
            swarsResults()
        btnValid4 = QPushButton(L[11])
        btnValid4.setParent(window_Contract_long)
        btnValid4.move(150, 350)
        btnValid4.setFixedSize(QSize(100, 25))
        font65 = btnValid4.font()
        font65.setPointSize(10)
        btnValid4.setFont(font65)
        btnValid4.pressed.connect(recupdata11)
        btnValid4.show()

        def web():
            webbrowser.open_new(
                r"https://fr.wikipedia.org/wiki/Contraction_des_longueurs")

        btnWiki3 = QPushButton()
        btnWiki3.setParent(window_Contract_long)
        btnWiki3.move(15, 50)
        btnWiki3.setFixedSize(QSize(30, 20))
        btnWiki3.pressed.connect(web)
        btnWiki3.setStyleSheet(
            "border-image : url(/usr/lib/spoutnx/img/logo wiki.png);")
        btnWiki3.show()

    btnChoices = QPushButton(L[132])
    btnChoices.setParent(windowCaracteristics)
    btnChoices.move(50, 350)
    btnChoices.setFixedSize(QSize(300, 25))
    font65 = btnChoices.font()
    font65.setPointSize(10)
    btnChoices.setFont(font65)
    btnChoices.pressed.connect(contractLong)
    btnChoices.show()

    windowCaracteristics.show()
