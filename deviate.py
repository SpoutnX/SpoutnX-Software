######################### SCRIPT DEVITION LUMIERE#############################

import numpy as np
from math import *
import os
import numpy
import webbrowser
import printplot
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

winShapiro = QWidget()
winShapiro.setWindowTitle("Résultats")
winShapiro.setFixedSize(QSize(600, 450))
winShapiro.setWindowIcon(
    QIcon('/usr/lib/spoutnx/icone2.ico'))

windowAberration = QWidget()
windowAberration.setWindowTitle("Résultats")
windowAberration.setFixedSize(QSize(600, 450))
windowAberration.setWindowIcon(
    QIcon('/usr/lib/spoutnx/icone2.ico'))

windowDeviation = QWidget()
windowDeviation.setWindowTitle("Résultats")
windowDeviation.setFixedSize(QSize(600, 450))
windowDeviation.setWindowIcon(
    QIcon('/usr/lib/spoutnx/icone2.ico'))

winResultDecSpec = QWidget()
winResultDecSpec.setWindowTitle("Résultats")
winResultDecSpec.setFixedSize(QSize(500, 450))
winResultDecSpec.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))


def swarsResults6():
    S = np.loadtxt(path2)
    S2 = ["%.1f" % i for i in S]
    ty = float(S[1])
    ty2 = str(S[4])
    ty4 = float(S[0])
    try:
        ty55 = str(S[5])
        ty62 = str(S[6])
        ty7 = str(S[7])
        winShapiroResults.deleteLater()
        winAberrationResults.deleteLater()
        winResult.deleteLater()
    except:
        pass

# RESULTATS DEVIATION

    if ty4 == 6 and ty == 3 or ty4 == 6 and ty == 1:
        windowDeviation.show()

        S22 = "{:.6e}".format(S[2])
        labDataMass = QLabel("m = " + "\n" + S22)
        labDataMass.setParent(windowDeviation)
        labDataMass.move(10, 100)
        labDataMass.setFixedSize(QSize(170, 50))
        labDataMass.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font2 = labDataMass.font()
        font2.setPointSize(10)
        labDataMass.setFont(font2)
        labDataMass.show()

        S23 = "{:.6e}".format(S[3])
        labDataB = QLabel("b = " + "\n" + S23)
        labDataB.setParent(windowDeviation)
        labDataB.move(10, 150)
        labDataB.setFixedSize(QSize(170, 50))
        labDataB.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataB.setFont(font2)
        labDataB.show()

        labTitle5 = QLabel(L[40])
        labTitle5.setParent(windowDeviation)
        labTitle5.setStyleSheet("background-color: #3EF724")
        labTitle5.move(145, 20)
        labTitle5.setFixedSize(QSize(350, 30))
        labTitle5.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font3 = labTitle5.font()
        font3.setPointSize(13)
        labTitle5.setFont(font3)
        labTitle5.show()

        labResAngle = QLabel(ty2)
        labResAngle.setParent(windowDeviation)
        labResAngle.move(195, 60)
        labResAngle.setFixedSize(QSize(250, 30))
        labResAngle.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font4 = labResAngle.font()
        font4.setPointSize(12)
        labResAngle.setFont(font4)
        labResAngle.setToolTip(L[178])
        labResAngle.show()

        labFormula = QLabel(L[22])
        labFormula.setParent(windowDeviation)
        labFormula.move(195, 110)
        labFormula.setFixedSize(QSize(250, 30))
        labFormula.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labFormula.setFont(font4)
        labFormula.show()

        logoFormula = QLabel()
        logoFormula.setPixmap(
            QPixmap('/usr/lib/spoutnx/img/deviation.png'))
        logoFormula.setParent(windowDeviation)
        logoFormula.move(220, 160)
        logoFormula.setFixedSize(QSize(150, 70))
        logoFormula.setScaledContents(True)
        logoFormula.show()

        def visual():
            printplot.visual()
            printplot.ModelOG_r()

        btnVisual = QPushButton(L[41])
        btnVisual.setParent(windowDeviation)
        btnVisual.move(260, 300)
        btnVisual.setFixedSize(QSize(120, 25))
        font65 = btnVisual.font()
        font65.setPointSize(10)
        btnVisual.setFont(font65)
        btnVisual.pressed.connect(visual)
        btnVisual.show()

        if ty == 3:
            labDataR0 = QLabel("r0 = " + "\n" + S2[5])
            labDataR0.setParent(windowDeviation)
            labDataR0.move(10, 200)
            labDataR0.setFixedSize(QSize(170, 50))
            labDataR0.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labDataR0.setFont(font2)
            labDataR0.show()

            labResREinsten = QLabel(L[100])
            labResREinsten.setParent(windowDeviation)
            labResREinsten.move(170, 370)
            labResREinsten.setFixedSize(QSize(300, 30))
            labResREinsten.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labResREinsten.setFont(font3)
            labResREinsten.setToolTip(L[179])
            labResREinsten.show()

            labREinstein = QLabel(ty62)
            labREinstein.setParent(windowDeviation)
            labREinstein.move(195, 400)
            labREinstein.setFixedSize(QSize(250, 30))
            labREinstein.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labREinstein.setFont(font4)
            labREinstein.show()

        def ReturnDat():
            windowDeviation.hide()
            windowDeviation.deleteLater()

            photondeviate()

        btnReturn = QPushButton(L[108])
        btnReturn.setParent(windowDeviation)
        btnReturn.move(10, 300)
        btnReturn.setFixedSize(QSize(150, 25))
        btnReturn.setFont(font65)
        btnReturn.pressed.connect(ReturnDat)
        btnReturn.show()


# RESULTATS SHAPIRO

    if ty4 == 6 and ty == 2:
        winShapiro.show()
        winShapiroResults = QStackedWidget()
        winShapiroResults.setParent(winShapiro)
        winShapiroResults.setFixedSize(QSize(600, 450))
        winShapiroResults.show()

        S22b = "{:.6e}".format(S[2])
        labDataMass = QLabel("m = " + "\n" + S22b)
        labDataMass.setParent(winShapiroResults)
        labDataMass.move(10, 100)
        labDataMass.setFixedSize(QSize(170, 50))
        labDataMass.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font2 = labDataMass.font()
        font2.setPointSize(10)
        labDataMass.setFont(font2)
        labDataMass.show()

        S23b = "{:.6e}".format(S[3])
        labDataR0 = QLabel("R0 = " + "\n" + S23b)
        labDataR0.setParent(winShapiroResults)
        labDataR0.move(10, 150)
        labDataR0.setFixedSize(QSize(170, 50))
        labDataR0.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataR0.setFont(font2)
        labDataR0.show()

        S24b = "{:.5e}".format(S[4])
        labDataRa = QLabel("Ra = " + "\n" + S24b)
        labDataRa.setParent(winShapiroResults)
        labDataRa.move(10, 200)
        labDataRa.setFixedSize(QSize(170, 50))
        labDataRa.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataRa.setFont(font2)
        labDataRa.show()

        S25b = "{:.5e}".format(S[5])
        labDataRb = QLabel("Rb = " + "\n" + S25b)
        labDataRb.setParent(winShapiroResults)
        labDataRb.move(10, 250)
        labDataRb.setFixedSize(QSize(170, 50))
        labDataRb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataRb.setFont(font2)
        labDataRb.show()

        labTitle6 = QLabel(L[90])
        labTitle6.setParent(winShapiroResults)
        labTitle6.setStyleSheet("background-color: #3EF724")
        labTitle6.move(145, 20)
        labTitle6.setFixedSize(QSize(350, 30))
        labTitle6.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font3 = labTitle6.font()
        font3.setPointSize(13)
        labTitle6.setFont(font3)
        labTitle6.show()

        labResShapiro = QLabel(ty7)
        labResShapiro.setParent(winShapiroResults)
        labResShapiro.move(195, 60)
        labResShapiro.setFixedSize(QSize(250, 30))
        labResShapiro.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font4 = labResShapiro.font()
        font4.setPointSize(12)
        labResShapiro.setFont(font4)
        labResShapiro.show()

        labFormula = QLabel(L[22])
        labFormula.setParent(winShapiroResults)
        labFormula.move(195, 100)
        labFormula.setFixedSize(QSize(250, 30))
        labFormula.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labFormula.setFont(font4)
        labFormula.show()

        winShapiroResults.show()

        logoFormul = QLabel()
        logoFormul.setPixmap(
            QPixmap('/usr/lib/spoutnx/img/Shapiro.png'))
        logoFormul.setParent(winShapiroResults)
        logoFormul.move(225, 210)
        logoFormul.setFixedSize(QSize(250, 80))
        logoFormul.setScaledContents(True)
        logoFormul.show()

        def ReturnDat():
            winShapiro.hide()
            winShapiroResults.hide()
            winShapiroResults.deleteLater()

            photondeviate()

        btnReturn = QPushButton(L[108])
        btnReturn.setParent(winShapiroResults)
        btnReturn.move(10, 300)
        btnReturn.setFixedSize(QSize(150, 25))
        font65 = btnReturn.font()
        font65.setPointSize(10)
        btnReturn.setFont(font65)
        btnReturn.pressed.connect(ReturnDat)
        btnReturn.show()

# RESULTATS ABERRATION DE LA LUMIERE

    if ty4 == 6 and ty == 4:
        windowAberration.show()
        winAberrationResults = QStackedWidget()
        winAberrationResults.setParent(windowAberration)
        winAberrationResults.setFixedSize(QSize(600, 450))

        labDataV = QLabel("v = " + "\n" + S2[2])
        labDataV.setParent(winAberrationResults)
        labDataV.move(10, 100)
        labDataV.setFixedSize(QSize(170, 50))
        labDataV.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font2 = labDataV.font()
        font2.setPointSize(10)
        labDataV.setFont(font2)
        labDataV.show()

        labDataA = QLabel("a = " + "\n" + S2[4])
        labDataA.setParent(winAberrationResults)
        labDataA.move(10, 150)
        labDataA.setFixedSize(QSize(170, 50))
        labDataA.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataA.setFont(font2)
        labDataA.show()

        labDataFreq = QLabel("fe = " + "\n" + S2[3])
        labDataFreq.setParent(winAberrationResults)
        labDataFreq.move(10, 200)
        labDataFreq.setFixedSize(QSize(170, 50))
        labDataFreq.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDataFreq.setFont(font2)
        labDataFreq.show()
        winAberrationResults.show()

        labTitle7 = QLabel(L[123])
        labTitle7.setParent(winAberrationResults)
        labTitle7.setStyleSheet("background-color: #3EF724")
        labTitle7.move(145, 10)
        labTitle7.setFixedSize(QSize(350, 30))
        labTitle7.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font3 = labTitle7.font()
        font3.setPointSize(13)
        labTitle7.setFont(font3)
        labTitle7.show()

        labResAberration = QLabel(L[124])
        labResAberration.setParent(winAberrationResults)
        font5 = labResAberration.font()
        font5.setPointSize(12)
        labResAberration.move(145, 60)
        labResAberration.setFixedSize(QSize(350, 20))
        labResAberration.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResAberration.setFont(font5)
        labResAberration.show()

        labAberration = QLabel(ty55)
        labAberration.setParent(winAberrationResults)
        labAberration.move(195, 90)
        labAberration.setFixedSize(QSize(250, 30))
        labAberration.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labAberration.setFont(font5)
        labAberration.show()

        logoFormulAberr = QLabel()
        logoFormulAberr.setPixmap(
            QPixmap('/usr/lib/spoutnx/img/aberration.png'))
        logoFormulAberr.setParent(winAberrationResults)
        logoFormulAberr.move(220, 125)
        logoFormulAberr.setFixedSize(QSize(180, 100))
        logoFormulAberr.setScaledContents(True)
        logoFormulAberr.show()

        labTitleDoppler = QLabel(L[125])
        labTitleDoppler.setParent(winAberrationResults)
        labTitleDoppler.setStyleSheet("background-color: #3EF724")
        labTitleDoppler.move(145, 250)
        labTitleDoppler.setFixedSize(QSize(350, 30))
        labTitleDoppler.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labTitleDoppler.setFont(font3)
        labTitleDoppler.show()

        labResDoppler = QLabel(L[126])
        labResDoppler.setParent(winAberrationResults)
        labResDoppler.move(145, 290)
        labResDoppler.setFixedSize(QSize(350, 20))
        labResDoppler.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labResDoppler.setFont(font5)
        labResDoppler.show()

        labDoppler = QLabel(ty62)
        labDoppler.setParent(winAberrationResults)
        labDoppler.move(195, 320)
        labDoppler.setFixedSize(QSize(250, 30))
        labDoppler.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labDoppler.setFont(font5)
        labDoppler.show()

        logoFormulDoppler = QLabel()
        logoFormulDoppler.setPixmap(
            QPixmap('/usr/lib/spoutnx/img/doppler.png'))
        logoFormulDoppler.setParent(winAberrationResults)
        logoFormulDoppler.move(220, 350)
        logoFormulDoppler.setFixedSize(QSize(180, 100))
        logoFormulDoppler.setScaledContents(True)
        logoFormulDoppler.show()

        def visual3():
            printplot.visual3()
        btnVisual2 = QPushButton(L[41])
        btnVisual2.setParent(winAberrationResults)
        btnVisual2.move(460, 90)
        btnVisual2.setFixedSize(QSize(120, 25))
        font65 = btnVisual2.font()
        font65.setPointSize(10)
        btnVisual2.setFont(font65)
        btnVisual2.pressed.connect(visual3)
        btnVisual2.show()

        def ReturnDat():
            windowAberration.hide()
            winAberrationResults.deleteLater()

            photondeviate()

        btnReturn = QPushButton(L[108])
        btnReturn.setParent(winAberrationResults)
        btnReturn.move(10, 300)
        btnReturn.setFixedSize(QSize(150, 25))
        btnReturn.setFont(font65)
        btnReturn.pressed.connect(ReturnDat)
        btnReturn.show()

# RESULTATS DECALAGE SPECTRAL

    winResult = QStackedWidget()
    winResult.setParent(winResultDecSpec)
    winResult.setFixedSize(QSize(500, 450))

    if ty4 == 6 and ty == 5 or ty4 == 3 and ty == 1:
        winResult.show()
        winResultDecSpec.show()
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
            winResultDecSpec.hide()
            photondeviate()

        btn = QPushButton(L[108])
        btn.setParent(winResult)
        btn.move(10, 300)
        btn.setFixedSize(QSize(150, 25))
        btn.setFont(font3)
        btn.pressed.connect(ReturnDat)
        btn.show()

        labResult = QLabel(ty2)
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

# ____________________________ PARTIE CARACTERISTIQUES ________________________


windowCaracteristiques = QWidget()
windowCaracteristiques.setWindowTitle("Caractéristiques")
windowCaracteristiques.setFixedSize(QSize(450, 500))
windowCaracteristiques.setWindowIcon(
    QIcon('/usr/lib/spoutnx/icone2.ico'))

windowDeviationCarac = QStackedWidget()
windowDeviationCarac.setParent(windowCaracteristiques)
windowDeviationCarac.setFixedSize(QSize(450, 500))

windowShapiroCarac = QStackedWidget()
windowShapiroCarac.setParent(windowCaracteristiques)
windowShapiroCarac.setFixedSize(QSize(450, 500))

windowAberrationCarac = QStackedWidget()
windowAberrationCarac.setParent(windowCaracteristiques)
windowAberrationCarac.setFixedSize(QSize(450, 500))

winCaract = QStackedWidget()
winCaract.setParent(windowCaracteristiques)
winCaract.setFixedSize(QSize(400, 500))


def photondeviate():
    labTitle1 = QLabel(L[84])
    labTitle1.setParent(windowCaracteristiques)
    labTitle1.move(150, 100)
    labTitle1.setStyleSheet("background-color: #3EF724")
    labTitle1.setFixedSize(QSize(150, 25))
    labTitle1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    font1 = labTitle1.font()
    font1.setPointSize(13)
    labTitle1.setFont(font1)
    labTitle1.show()

    try:
        windowDeviationCarac.hide()
        windowShapiroCarac.hide()
        windowAberrationCarac.hide()
        winCaract.hide()
    except:
        pass

    def ChoiceUser(c):
        c = c.text()

# CARACTERISTIQUES DEVIATION

        if c == L[82]:
            windowDeviationCarac.show()
            try:
                windowShapiroCarac.hide()
                windowAberrationCarac.hide()
                winCaract.hide()
            except:
                pass
            listeChoice.hide()
            labTitle1.hide()
            labTitle2 = QLabel(L[35] + "\n" + L[36])
            labTitle2.setParent(windowDeviationCarac)
            labTitle2.setStyleSheet("background-color: #3EF724")
            labTitle2.move(75, 20)
            labTitle2.setFixedSize(QSize(300, 50))
            labTitle2.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labTitle2.setFont(font1)
            labTitle2.setToolTip(L[176])
            labTitle2.show()

            def text_mass(m2):
                global m3
                m3 = float(m2)

            def text_alt(b2):
                global b
                b = float(b2)

            def text_r(r02):
                global r0
                r0 = r02

            def value_changed(vn):
                global val
                val = vn

            def exp_changed(DistObs2):
                global DistObs
                DistObs = DistObs2

            labMass = QLabel(L[17])
            labMass.setParent(windowDeviationCarac)
            labMass.move(50, 100)
            labMass.setFixedSize(QSize(300, 30))
            labMass.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            font2 = labMass.font()
            font2.setPointSize(11)
            labMass.setFont(font2)
            labMass.show()
            entMass = QLineEdit()
            entMass.setParent(windowDeviationCarac)
            entMass.move(80, 140)
            entMass.setFixedSize(QSize(200, 20))
            entMass.textChanged.connect(text_mass)
            entMass.show()

            spinboxMass = QDoubleSpinBox()
            spinboxMass.setRange(0, 1000)
            spinboxMass.setParent(windowDeviationCarac)
            spinboxMass.setFixedSize(QSize(80, 20))
            spinboxMass.move(290, 140)
            spinboxMass.setPrefix("x10*  ")
            spinboxMass.setSingleStep(1)
            spinboxMass.valueChanged.connect(value_changed)
            spinboxMass.show()

            labParamB = QLabel(L[37])
            labParamB.setParent(windowDeviationCarac)
            labParamB.move(25, 200)
            labParamB.setFixedSize(QSize(400, 30))
            labParamB.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labParamB.setFont(font2)
            labParamB.setToolTip(L[177])
            labParamB.show()

            entParamB = QLineEdit()
            entParamB.setParent(windowDeviationCarac)
            entParamB.move(125, 240)
            entParamB.setFixedSize(QSize(200, 20))
            entParamB.textChanged.connect(text_alt)
            entParamB.show()

            labLentilleGrav = QLabel(L[99])
            labLentilleGrav.setParent(windowDeviationCarac)
            labLentilleGrav.move(25, 320)
            labLentilleGrav.setFixedSize(QSize(400, 25))
            labLentilleGrav.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labLentilleGrav.setFont(font1)
            labLentilleGrav.show()

            labDistObs = QLabel(L[101])
            labDistObs.setParent(windowDeviationCarac)
            labDistObs.move(50, 350)
            labDistObs.setFixedSize(QSize(350, 30))
            labDistObs.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labDistObs.setFont(font2)
            labDistObs.show()
            entDistObs = QLineEdit()
            entDistObs.setParent(windowDeviationCarac)
            entDistObs.move(80, 390)
            entDistObs.setFixedSize(QSize(200, 20))
            entDistObs.textChanged.connect(text_r)
            entDistObs.show()

            spinboxDistObs = QDoubleSpinBox()
            spinboxDistObs.setRange(0, 1000)
            spinboxDistObs.setParent(windowDeviationCarac)
            spinboxDistObs.setFixedSize(QSize(80, 20))
            spinboxDistObs.move(290, 390)
            spinboxDistObs.setPrefix("x10*  ")
            spinboxDistObs.setSingleStep(1)
            spinboxDistObs.valueChanged.connect(exp_changed)
            spinboxDistObs.show()

            def recupdata61():
                try:
                    r01 = float(r0)
                    try:
                        r01 = r0*10**DistObs
                    except:
                        pass
                except:
                    r01 = 0

                try:
                    m = m3*10**val
                except:
                    m = m3

                a = (4*(6.67*10**-11)*m)/(b*(299792458**2))
                re = sqrt(((4*(6.67*10**-11)*m)/(299792458**2))*r01)

                if re == 0:
                    x = [6, 1, m, b, a, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0,
                         17, m, 37, b, 0, 0, 0, 0, 0, 0,
                         35, 36, 40, a, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0, 0, 0, 0, 1
                         ]
                else:
                    x = [6, 3, m, b, a, r01, re, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0, 0,
                         17, m, 37, b, 191, r01, 0, 0, 0, 0,
                         35, 36, 40, a, 0, 0, 0, 0, 0, 0, 0,
                         99, 100, re, 0, 0, 0, 0, 0, 0, 1]
                np.savetxt(path2, x)

                windowDeviationCarac.hide()
                windowCaracteristiques.hide()
                swarsResults6()

            btnValid = QPushButton(L[11])
            btnValid.setParent(windowDeviationCarac)
            btnValid.move(180, 450)
            btnValid.setFixedSize(QSize(90, 30))
            btnValid.pressed.connect(recupdata61)
            btnValid.setFont(font2)

            btnValid.show()


# CARACTERISTIQUES SHAPIRO
        if c == L[83]:
            windowShapiroCarac.show()
            try:
                windowDeviationCarac.hide()
                windowAberrationCarac.hide()
                winCaract.hide()
            except:
                pass

            listeChoice.hide()
            labTitle1.hide()

            labTitle3 = QLabel(L[83])
            labTitle3.setParent(windowShapiroCarac)
            labTitle3.setStyleSheet("background-color: #3EF724")
            labTitle3.move(125, 15)
            labTitle3.setFixedSize(QSize(200, 30))
            labTitle3.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labTitle3.setFont(font1)
            labTitle3.show()

            def text_mass(m2):
                global m3
                m3 = float(m2)

            def text_ra(Ra2):
                global Ra
                Ra = float(Ra2)

            def text_r0(r02):
                global R0
                R0 = float(r02)

            def text_rb(Rb2):
                global Rb
                Rb = float(Rb2)

            def value_changed(vn):
                global val
                val = vn

            def value_changed_A(exp_A2):
                global exp_A
                exp_A = exp_A2

            def value_changed_B(exp_B2):
                global exp_B
                exp_B = exp_B2

            labMass = QLabel(L[17])
            labMass.setParent(windowShapiroCarac)
            labMass.move(75, 80)
            labMass.setFixedSize(QSize(300, 30))
            labMass.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            font2 = labMass.font()
            font2.setPointSize(11)
            labMass.setFont(font2)
            labMass.show()
            entMass = QLineEdit()
            entMass.setParent(windowShapiroCarac)
            entMass.move(80, 120)
            entMass.setFixedSize(QSize(200, 20))
            entMass.textChanged.connect(text_mass)
            entMass.show()

            spinboxMass = QDoubleSpinBox()
            spinboxMass.setRange(0, 1000)
            spinboxMass.setParent(windowShapiroCarac)
            spinboxMass.setFixedSize(QSize(80, 20))
            spinboxMass.move(290, 120)
            spinboxMass.setPrefix("x10*  ")
            spinboxMass.setSingleStep(1)
            spinboxMass.valueChanged.connect(value_changed)
            spinboxMass.show()

# label pour coordonnee radiale proche de l'objet attirant

            labRprocheObjet = QLabel(L[85] + "\n" + L[86])
            labRprocheObjet.setParent(windowShapiroCarac)
            labRprocheObjet.move(25, 165)
            labRprocheObjet.setFixedSize(QSize(400, 45))
            labRprocheObjet.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labRprocheObjet.setFont(font2)
            labRprocheObjet.show()
            entRprocheObjet = QLineEdit()
            entRprocheObjet.setParent(windowShapiroCarac)
            entRprocheObjet.move(125, 220)
            entRprocheObjet.setFixedSize(QSize(200, 20))
            entRprocheObjet.textChanged.connect(text_r0)
            entRprocheObjet.show()

            labRa = QLabel(L[87])
            labRa.setParent(windowShapiroCarac)
            labRa.move(50, 280)
            labRa.setFixedSize(QSize(350, 30))
            labRa.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labRa.setFont(font2)
            labRa.show()
            entRa = QLineEdit()
            entRa.setParent(windowShapiroCarac)
            entRa.move(80, 310)
            entRa.setFixedSize(QSize(200, 20))
            entRa.textChanged.connect(text_ra)
            entRa.show()

            spinbox_A = QDoubleSpinBox()
            spinbox_A.setRange(0, 1000)
            spinbox_A.setParent(windowShapiroCarac)
            spinbox_A.setFixedSize(QSize(80, 20))
            spinbox_A.move(290, 310)
            spinbox_A.setPrefix("x10*  ")
            spinbox_A.setSingleStep(1)
            spinbox_A.valueChanged.connect(value_changed_A)
            spinbox_A.show()

            labRb = QLabel(L[89])
            labRb.setParent(windowShapiroCarac)
            labRb.move(50, 380)
            labRb.setFixedSize(QSize(350, 30))
            labRb.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labRb.setFont(font2)
            labRb.show()
            entRb = QLineEdit()
            entRb.setParent(windowShapiroCarac)
            entRb.move(80, 410)
            entRb.setFixedSize(QSize(200, 20))
            entRb.textChanged.connect(text_rb)
            entRb.show()

            spinbox_B = QDoubleSpinBox()
            spinbox_B.setRange(0, 1000)
            spinbox_B.setParent(windowShapiroCarac)
            spinbox_B.setFixedSize(QSize(80, 20))
            spinbox_B.move(290, 410)
            spinbox_B.setPrefix("x10*  ")
            spinbox_B.setSingleStep(1)
            spinbox_B.valueChanged.connect(value_changed_B)
            spinbox_B.show()

            def recupdata62():
                try:
                    m = m3*10**val
                except:
                    m = m3

                try:
                    Ra = Ra*10**exp_A
                except:
                    Ra = Ra

                try:
                    Rb = Rb*10**exp_B
                except:
                    Rb = Rb

                Rs = (2*(6.67*10**-11)*m)/(299792458**2)
                first = Rs/(299792458**2)
                second = (4*Ra*Rb)/(R0**2)
                second2 = np.log(second)
                Es = first*(second2-1)

                Rar = (Ra*2)/R0
                Rbr = (Rb*2)/R0

                RaI = sqrt((Ra**2)-4)
                RbI = sqrt((Rb**2)-4)

                x = [6, 2, m, R0, Ra, Rb, Rs, Es, Rar, Rbr, RaI, RbI, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     17, m, 87, Ra, 89, Rb, 85, R0, 0, 0,
                     185, 83, 90, Es, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                np.savetxt(path2, x)

                windowShapiroCarac.hide()
                windowCaracteristiques.hide()
                swarsResults6()

            btnValid2 = QPushButton(L[11])
            btnValid2.setParent(windowShapiroCarac)
            btnValid2.move(180, 450)
            btnValid2.setFixedSize(QSize(90, 30))
            btnValid2.pressed.connect(recupdata62)
            btnValid2.setFont(font2)
            btnValid2.show()


# CARACTERISTIQUES ABERRATION
        if c == L[117]:
            windowAberrationCarac.show()
            try:
                windowDeviationCarac.hide()
                windowShapiroCarac.hide()
                winCaract.hide()
            except:
                pass

            listeChoice.hide()
            labTitle1.hide()

            labTitle4 = QLabel(L[123] + "\n" + L[121])
            labTitle4.setParent(windowAberrationCarac)
            labTitle4.setStyleSheet("background-color: #3EF724")
            labTitle4.move(50, 10)
            labTitle4.setFixedSize(QSize(350, 50))
            labTitle4.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labTitle4.setFont(font1)
            labTitle4.show()

            labRelativityRest = QLabel(L[118])
            labRelativityRest.setParent(windowAberrationCarac)
            labRelativityRest.move(100, 80)
            labRelativityRest.setFixedSize(QSize(250, 30))
            labRelativityRest.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            font2 = labRelativityRest.font()
            font2.setPointSize(11)
            labRelativityRest.setFont(font2)
            labRelativityRest.show()

            def text_vit(vit2):
                global vit
                vit = float(vit2)

            def text_alph(ang2):
                global angre
                angre = float(ang2)

            def text_freqt(fre2):
                global fret
                fret = float(fre2)

            labVitObjet = QLabel(L[19])
            labVitObjet.setParent(windowAberrationCarac)
            labVitObjet.move(50, 140)
            labVitObjet.setFixedSize(QSize(350, 30))
            labVitObjet.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labVitObjet.setFont(font2)
            labVitObjet.show()
            entVitObj = QLineEdit()
            entVitObj.setParent(windowAberrationCarac)
            entVitObj.move(125, 170)
            entVitObj.setFixedSize(QSize(200, 20))
            entVitObj.textChanged.connect(text_vit)
            entVitObj.show()

            labAngle = QLabel(L[119] + "\n" + L[120])
            labAngle.setParent(windowAberrationCarac)
            labAngle.move(50, 230)
            labAngle.setFixedSize(QSize(350, 50))
            labAngle.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labAngle.setFont(font2)
            labAngle.show()
            entAngle = QLineEdit()
            entAngle.setParent(windowAberrationCarac)
            entAngle.move(125, 280)
            entAngle.setFixedSize(QSize(200, 20))
            entAngle.textChanged.connect(text_alph)
            entAngle.show()

            labFrequency = QLabel(L[122])
            labFrequency.setParent(windowAberrationCarac)
            labFrequency.move(50, 320)
            labFrequency.setFixedSize(QSize(350, 30))
            labFrequency.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labFrequency.setFont(font2)
            labFrequency.show()
            entFrequency = QLineEdit()
            entFrequency.setParent(windowAberrationCarac)
            entFrequency.move(125, 350)
            entFrequency.setFixedSize(QSize(200, 20))
            entFrequency.textChanged.connect(text_freqt)
            entFrequency.show()

            def recupdata67():
                print(angre)
                cosa = np.cos(angre)

                first = (cosa+(vit/(299792458)))/(1+((vit/299792458)*cosa))
                an56 = np.arccos(first)
                print("alpha2")

                print(fret)
                frmo = fret*(1/(vit/299792458))
                print("freq")

                x = [6, 4, vit, fret, angre, an56, frmo, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0,
                     19, vit, 119, angre, 122, fret, 0, 0, 0, 0,
                     117, 123, 124, an56, 0, 0, 0, 0, 0, 0, 0,
                     125, 126, frmo, 0, 0, 0, 0, 0, 0, 1]
                np.savetxt(path2, x)
                windowAberrationCarac.hide()
                windowCaracteristiques.hide()
                swarsResults6()

            btnValid3 = QPushButton(L[11])
            btnValid3.setParent(windowAberrationCarac)
            btnValid3.move(180, 430)
            btnValid3.setFixedSize(QSize(90, 30))
            btnValid3.pressed.connect(recupdata67)
            btnValid3.setFont(font2)
            btnValid3.show()

            def web():
                webbrowser.open_new(
                    r"https://fr.wikipedia.org/wiki/Aberration_de_la_lumi%C3%A8re")

            btnWiki = QPushButton()
            btnWiki.setParent(windowAberrationCarac)
            btnWiki.move(15, 50)
            btnWiki.setFixedSize(QSize(30, 20))
            btnWiki.pressed.connect(web)
            btnWiki.setStyleSheet(
                "border-image : url(/usr/lib/spoutnx/img/logo wiki.png);")
            btnWiki.show()


# CARACTERISTIQUES DECALAGE SPECTRAL

        if c == L[223]:
            winCaract.show()
            try:
                windowDeviationCarac.hide()
                windowShapiroCarac.hide()
                windowAberrationCarac.hide()
            except:
                pass
            listeChoice.hide()
            labTitle1.hide()
            labTitle = QLabel(L[7] + "\n" + L[45])
            labTitle.setStyleSheet("background-color: #3EF724")
            labTitle.setParent(winCaract)
            labTitle.move(95, 20)
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

            def value_changed(dist2):
                global dist
                dist = float(dist2)

            labDist = QLabel(L[27])
            labDist.setParent(winCaract)
            labDist.move(75, 100)
            labDist.setFixedSize(QSize(300, 30))
            labDist.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            font = labDist.font()
            font.setPointSize(11)
            labDist.setFont(font)
            labDist.show()

            entDist = QLineEdit()
            entDist.setParent(winCaract)
            entDist.move(95, 140)
            entDist.setFixedSize(QSize(200, 20))
            entDist.setFont(font)
            entDist.textChanged.connect(text_alt)
            entDist.show()

            spinboxMass = QDoubleSpinBox()
            spinboxMass.setRange(0, 1000)
            spinboxMass.setParent(winCaract)
            spinboxMass.setFixedSize(QSize(80, 20))
            spinboxMass.move(305, 140)
            spinboxMass.setPrefix("x10*  ")
            spinboxMass.setSingleStep(1)
            spinboxMass.valueChanged.connect(value_changed)
            spinboxMass.show()

            labMass = QLabel(L[17])
            labMass.setParent(winCaract)
            labMass.move(75, 190)
            labMass.setFixedSize(QSize(300, 30))
            labMass.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            labMass.setFont(font)
            labMass.show()

            entMass = QLineEdit()
            entMass.setParent(winCaract)
            entMass.move(95, 230)
            entMass.setFixedSize(QSize(200, 20))
            entMass.textChanged.connect(text_mass)
            entMass.setFont(font)
            entMass.show()

            spinbox = QDoubleSpinBox()
            spinbox.setRange(0, 1000)
            spinbox.setParent(winCaract)
            spinbox.setFixedSize(QSize(80, 20))
            spinbox.move(305, 230)
            spinbox.setPrefix("x10*  ")
            spinbox.setSingleStep(1)
            spinbox.valueChanged.connect(exp_changed)
            spinbox.show()

            def recupdata11():
                try:
                    m = m3*10**exp
                except:
                    m = m3

                try:
                    d = alt*10**dist
                except:
                    d = alt

                first = (1-((2*(6.67*10**-11)*m)/((299792458**2)*d)))
                z = (1/(sqrt(first)))-1

                x = [6, 5, d, m, z, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0,
                     27, d, 17, m, 0, 0, 0, 0, 0, 0,
                     7, 45, 79, z, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                np.savetxt(path2, x)
                winCaract.hide()
                windowCaracteristiques.hide()
                swarsResults6()

            btnValid = QPushButton(L[11])
            btnValid.setParent(winCaract)
            btnValid.move(180, 330)
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

    listeChoice = QListWidget()
    listeChoice.addItem(L[82])
    listeChoice.addItem(L[83])
    listeChoice.addItem(L[117])
    listeChoice.addItem(L[223])
    listeChoice.setParent(windowCaracteristiques)
    listeChoice.move(50, 200)
    listeChoice.setFixedSize(QSize(350, 120))
    listeChoice.setStyleSheet(
        "QListView::item:selected{background-color: #3EF724}")
    listeChoice.setCurrentItem(None)
    font2 = listeChoice.font()
    font2.setPointSize(12)
    listeChoice.setFont(font2)
    listeChoice.itemClicked.connect(ChoiceUser)
    listeChoice.setToolTip(L[168])
    listeChoice.show()

    windowCaracteristiques.show()
