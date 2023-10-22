
################################## SCRIPT MAITRE###############################


# Copyright 2023 Tom Lafond
# Tous les scripts qui dépendent de ce script maître pour fonctionner sont sous
# le même copyright:
# (dilate, fall, gravwave, hole, printplot, printpdf, spectral, precess, deviate)
# Ce script maître et les scripts enfants sont sous licence GPL3 (voir licence)

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QWidget,
    QLineEdit,
    QListWidget,
    QMessageBox,
    QStackedWidget,
    QFileDialog,
)
import sys
from PySide6.QtGui import QAction, QIcon, QPixmap
import os
import numpy as np
import shutil

if getattr(sys, 'frozen', False):
    import pyi_splash

app = QApplication(sys.argv)

window = QMainWindow()

window.setWindowTitle("SpoutnX")
window.setMinimumSize(QSize(500, 400))
window.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))


user = os.getlogin()
print(user)
Path = "/home/" + user + "/.SpoutnX/"
path2 = Path + "data.sptx"
path3 = Path + "user_data.txt"
path4 = Path + "lang/user_lang.sptx"

try:
    file3 = sys.argv[1]
    Re = np.loadtxt(file3)
    shutil.copyfile(file3, path2)
    if Re[0] == 1:
        import dilate
        dilate.swarsResults()
    if Re[0] == 2:
        import fall
        fall.swarsResults2()
    if Re[0] == 3:
        import spectral
        spectral.swarsResults3()
    if Re[0] == 8:
        import hole
        hole.swarsResults8()
    if Re[0] == 6:
        import deviate
        deviate.swarsResults6()
    if Re[0] == 7:
        import precess
        precess.swarsResults9()
except:
    pass


try:
    os.mkdir("/home/" + user + "/.SpoutnX")
except:
    print("le dossier est déjà créé")

sourcelang = "/home/" + user + "/.SpoutnX/lang/user_lang.sptx"


test = os.path.isfile(sourcelang)
test2 = os.path.exists("/home/" + user + "/.SpoutnX/lang")
print(test)
if test is True:

if test is False:
    if test2 is False:
        print("4")
        os.mkdir("/home/" + user + "/.SpoutnX/lang")
    shutil.copy(
        '/usr/lib/spoutnx/user_langage_fr.sptx', sourcelang)


mes_nombres = open(path4).read()
L = mes_nombres.split('\n')

fileName = (Path + "data.sptx")
testex = os.path.isfile(fileName)
if testex == 'true':
    os.remove(path2)


def text_changed(objectif2):
    objectif = objectif2.text()
    print(objectif)
    if objectif == L[5]:
        import dilate
        dilate.timedilate()
    if objectif == L[6]:
        import fall
        fall.timefall()
    if objectif == L[7]:
        import spectral
        spectral.decspectral()
    if objectif == L[9]:
        import deviate
        deviate.photondeviate()
    if objectif == L[10]:
        import hole
        hole.caractHole()
    if objectif == L[102]:
        import precess
        precess.Sittereff()
    if objectif == L[155]:
        import gravwave
        gravwave.waves()


listeObjectifs = QListWidget()
listeObjectifs.addItem(L[5])
listeObjectifs.addItem(L[6])
listeObjectifs.addItem(L[7])
listeObjectifs.addItem(L[9])
listeObjectifs.addItem(L[10])
listeObjectifs.addItem(L[102])
listeObjectifs.addItem(L[155])
listeObjectifs.setParent(window)
listeObjectifs.move(50, 150)
listeObjectifs.setFixedSize(QSize(400, 180))
listeObjectifs.setStyleSheet(
    "QListView::item:selected{background-color: #3EF724}")
listeObjectifs.setCurrentItem(None)
font2 = listeObjectifs.font()
font2.setPointSize(12)
listeObjectifs.setFont(font2)
listeObjectifs.itemClicked.connect(text_changed)
listeObjectifs.setToolTip(L[168])
listeObjectifs.show()

labWelcome = QLabel(L[0])
labWelcome.setParent(window)  # Label Bienvenue
labWelcome.move(120, 40)
labWelcome.setFixedSize(QSize(300, 20))
labWelcome.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
font = labWelcome.font()
font.setPointSize(14)
labWelcome.setFont(font)
labWelcome.show()

labObjective = QLabel(L[1])     # Label "quel est votre objectif"
labObjective.setParent(window)
labObjective.move(158, 80)
labObjective.setFixedSize(QSize(225, 30))
labObjective.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
labObjective.setStyleSheet("background-color: #3EF724")
labObjective.setFont(font)
labObjective.show()

logoSpoutnX = QLabel()
logoSpoutnX.setPixmap(QPixmap('/usr/lib/spoutnx/icone3.png'))
logoSpoutnX.setParent(window)
logoSpoutnX.move(50, 50)
logoSpoutnX.setFixedSize(QSize(65, 65))
logoSpoutnX.setScaledContents(True)
logoSpoutnX.show()


def opens():
    filename = QFileDialog.getOpenFileName()
    file2 = str(filename[0])
    Re = np.loadtxt(file2)
    shutil.copyfile(file2, path2)
    if Re[0] == 1:
        import dilate
        dilate.swarsResults()
    if Re[0] == 2:
        import fall
        fall.swarsResults2()
    if Re[0] == 3:
        import spectral
        spectral.swarsResults3()
    if Re[0] == 8:
        import hole
        hole.swarsResults8()
    if Re[0] == 6:
        import deviate
        deviate.swarsResults6()
    if Re[0] == 7:
        import precess
        precess.swarsResults9()


def saves():
    filename = QFileDialog.getSaveFileName()
    file2 = str(filename[0])
    filename2 = (file2 + ".sptx")
    shutil.copyfile(path2, filename2)
    global VarSave
    VarSave = 1


windowAbout = QWidget()
windowAbout.setWindowTitle(L[3])
windowAbout.setMinimumSize(QSize(500, 400))
windowAbout.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))


def vers():

    file = open("/usr/lib/spoutnx/A propos.txt", "r")
    l = file.readlines()
    ligne2 = (l[0] + l[1] + l[2] + l[3] + l[4]
              + l[5] + l[6] + l[7] + l[8] + l[9] + l[10])

    file.close()
    labAbout = QLabel(ligne2)
    labAbout.setParent(windowAbout)
    labAbout.move(25, 10)
    labAbout.setFixedSize(QSize(450, 400))
    labAbout.setAlignment(Qt.AlignHCenter)
    font = labAbout.font()
    font.setPointSize(12)
    labAbout.setFont(font)
    labAbout.show()
    window2.hide()

    logo = QLabel()
    logo.setPixmap(QPixmap('/usr/lib/spoutnx/icone2.ico'))
    logo.setParent(windowAbout)
    logo.move(200, 300)
    logo.setFixedSize(QSize(100, 100))
    logo.setScaledContents(True)
    logo.show()
    windowAbout.show()


def sett():         # voir l
    windowSettings.show()


def help1():
    os.system('/usr/bin/xdg-open ' +
              '/usr/lib/spoutnx/Guide_utilisateur_du_logiciel_Spoutnx.pdf')


def pdf1():
    import printpdf
    printpdf.printPDF()


button_action = QAction(
    QIcon("/usr/lib/spoutnx/img/enregistrer.png"), L[68], window)
button_action.triggered.connect(saves)

button_action2 = QAction(
    QIcon("/usr/lib/spoutnx/img/open.png"), L[67], window)
button_action2.triggered.connect(opens)

button_action3 = QAction(
    QIcon("/usr/lib/spoutnx/img/about.png"), L[3], window)
button_action3.triggered.connect(vers)

button_action4 = QAction(
    QIcon("/usr/lib/spoutnx/img/settings.png"), L[4], window)
button_action4.triggered.connect(sett)

button_action5 = QAction(
    QIcon("/usr/lib/spoutnx/img/help.png"), L[107], window)
button_action5.triggered.connect(help1)

button_action6 = QAction(
    QIcon("/usr/lib/spoutnx/img/PDF.png"), L[189], window)
button_action6.triggered.connect(pdf1)


def text_changed2(objectif3):  # s is a str
    objectif2 = objectif3.text()
    if objectif2 == L[75]:
        window34.show()
        try:
            window33.hide()
        except:
            pass

        def text_changed3(tes2):
            tes = tes2.text()
            if tes == "Français":
                shutil.copy(
                    '/usr/lib/spoutnx/user_langage_fr.sptx', path4)
            if tes == "English":
                shutil.copy(
                    '/usr/lib/spoutnx/user_langage_ang.sptx', path4)
            if tes == "Espanol":
                shutil.copy(
                    '/usr/lib/spoutnx/user_langage_esp.sptx', path4)
            if tes == "Portugues":
                shutil.copy(
                    '/usr/lib/spoutnx/user_langage_por.sptx', path4)
        labTitleChangeLang = QLabel(L[75])
        labTitleChangeLang.setParent(window34)
        labTitleChangeLang.move(95, 20)
        labTitleChangeLang.setFixedSize(QSize(180, 25))
        labTitleChangeLang.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font = labTitleChangeLang.font()
        font.setPointSize(13)
        labTitleChangeLang.setFont(font)
        labTitleChangeLang.setStyleSheet("background-color: #3EF724")
        labTitleChangeLang.show()

        listeLang = QListWidget()
        listeLang.addItem("Français")
        listeLang.addItem("English")
        listeLang.addItem("Espanol")
        listeLang.addItem("Portugues")
        listeLang.setParent(window34)
        listeLang.move(70, 100)
        listeLang.setFixedSize(QSize(200, 100))
        listeLang.setStyleSheet(
            "QListView::item:selected{background-color: #3EF724}")
        listeLang.setFont(font)
        listeLang.itemClicked.connect(text_changed3)
        listeLang.show()

        labRestart = QLabel(L[80] + "\n" + L[81])
        labRestart.setParent(window34)
        labRestart.move(20, 200)
        labRestart.setFixedSize(QSize(300, 50))
        labRestart.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font = labRestart.font()
        font.setPointSize(10)
        labRestart.setFont(font)
        labRestart.show()

    if objectif2 == L[70]:
        try:
            window34.hide()
        except:
            pass
        window33.show()
        labTitleAddMetric = QLabel(L[70] + "\n" + L[113])
        labTitleAddMetric.setParent(window33)
        labTitleAddMetric.move(15, 10)
        labTitleAddMetric.setFixedSize(QSize(300, 50))
        labTitleAddMetric.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font7 = labTitleAddMetric.font()
        font7.setPointSize(12)
        font7.setUnderline(True)
        labTitleAddMetric.setFont(font7)
        labTitleAddMetric.setStyleSheet("background-color: #3EF724")
        labTitleAddMetric.show()

        def tgrt(n):
            global g00t
            g00t = str(n)

        def g01(n):
            global g01t
            g01t = str(n)

        def g02(n):
            global g02t
            g02t = str(n)

        def g03(n):
            global g03t
            g03t = str(n)

        def g10(n):
            global g10t
            g10t = str(n)

        def g11(n):
            global g11t
            g11t = str(n)

        def g12(n):
            global g12t
            g12t = str(n)

        def g13(n):
            global g13t
            g13t = str(n)

        def g20(n):
            global g20t
            g20t = str(n)

        def g21(n):
            global g21t
            g21t = str(n)

        def g22(n):
            global g22t
            g22t = str(n)

        def g23(n):
            global g23t
            g23t = str(n)

        def g30(n):
            global g30t
            g30t = str(n)

        def g31(n):
            global g31t
            g31t = str(n)

        def g32(n):
            global g32t
            g32t = str(n)

        def g33(n):
            global g33t
            g33t = str(n)

        def text_name(na):
            global name
            name = str(na)

        g00 = QLabel("g = ")
        g00.setParent(window33)
        g00.move(120, 60)
        g00.setFixedSize(QSize(30, 25))
        g00.show()

        entree1 = QLineEdit()       # Entrées pour chaque valeur de la metrique
        entree1.setParent(window33)
        entree1.move(15, 90)
        entree1.setFixedSize(QSize(70, 20))
        entree1.textChanged.connect(tgrt)
        entree1.show()

        entree2 = QLineEdit()
        entree2.setParent(window33)
        entree2.move(95, 90)
        entree2.setFixedSize(QSize(70, 20))
        entree2.textChanged.connect(g01)
        entree2.show()

        entree3 = QLineEdit()
        entree3.setParent(window33)
        entree3.move(175, 90)
        entree3.setFixedSize(QSize(70, 20))
        entree3.textChanged.connect(g02)
        entree3.show()

        entree4 = QLineEdit()
        entree4.setParent(window33)
        entree4.move(255, 90)
        entree4.setFixedSize(QSize(70, 20))
        entree4.textChanged.connect(g03)
        entree4.show()

        entree5 = QLineEdit()
        entree5.setParent(window33)
        entree5.move(15, 120)
        entree5.setFixedSize(QSize(70, 20))
        entree5.textChanged.connect(g10)
        entree5.show()

        entree6 = QLineEdit()
        entree6.setParent(window33)
        entree6.move(95, 120)
        entree6.setFixedSize(QSize(70, 20))
        entree6.textChanged.connect(g11)
        entree6.show()

        entree7 = QLineEdit()
        entree7.setParent(window33)
        entree7.move(175, 120)
        entree7.setFixedSize(QSize(70, 20))
        entree7.textChanged.connect(g12)
        entree7.show()

        entree8 = QLineEdit()
        entree8.setParent(window33)
        entree8.move(255, 120)
        entree8.setFixedSize(QSize(70, 20))
        entree8.textChanged.connect(g13)
        entree8.show()

        entree9 = QLineEdit()
        entree9.setParent(window33)
        entree9.move(15, 150)
        entree9.setFixedSize(QSize(70, 20))
        entree9.textChanged.connect(g20)
        entree9.show()

        entree10 = QLineEdit()
        entree10.setParent(window33)
        entree10.move(95, 150)
        entree10.setFixedSize(QSize(70, 20))
        entree10.textChanged.connect(g21)
        entree10.show()

        entree11 = QLineEdit()
        entree11.setParent(window33)
        entree11.move(175, 150)
        entree11.setFixedSize(QSize(70, 20))
        entree11.textChanged.connect(g22)
        entree11.show()

        entree12 = QLineEdit()
        entree12.setParent(window33)
        entree12.move(255, 150)
        entree12.setFixedSize(QSize(70, 20))
        entree12.textChanged.connect(g23)
        entree12.show()

        entree13 = QLineEdit()
        entree13.setParent(window33)
        entree13.move(15, 180)
        entree13.setFixedSize(QSize(70, 20))
        entree13.textChanged.connect(g30)
        entree13.show()

        entree14 = QLineEdit()
        entree14.setParent(window33)
        entree14.move(95, 180)
        entree14.setFixedSize(QSize(70, 20))
        entree14.textChanged.connect(g31)
        entree14.show()

        entree15 = QLineEdit()
        entree15.setParent(window33)
        entree15.move(175, 180)
        entree15.setFixedSize(QSize(70, 20))
        entree15.textChanged.connect(g32)
        entree15.show()

        entree16 = QLineEdit()
        entree16.setParent(window33)
        entree16.move(255, 180)
        entree16.setFixedSize(QSize(70, 20))
        entree16.textChanged.connect(g33)
        entree16.show()

        labInfosType = QLabel(L[71] + "\n" + L[72])
        labInfosType.setParent(window33)
        labInfosType.move(20, 250)
        labInfosType.setFixedSize(QSize(300, 45))
        labInfosType.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        font5 = labInfosType.font()
        font5.setPointSize(10)
        labInfosType.setFont(font5)
        labInfosType.show()

        labNameMetric = QLabel(L[73])
        labNameMetric.setParent(window33)
        labNameMetric.move(70, 290)
        labNameMetric.setFixedSize(QSize(200, 25))
        labNameMetric.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        labNameMetric.setFont(font7)
        labNameMetric.show()

        entName = QLineEdit()
        entName.setParent(window33)
        entName.move(70, 320)
        entName.setFixedSize(QSize(200, 20))
        entName.textChanged.connect(text_name)
        entName.setFont(font5)
        entName.show()

        def recupUserDat():
            data = [g00t+"\n", g01t+"\n", g02t+"\n", g03t+"\n", g10t+"\n",
                    g11t+"\n", g12t+"\n", g13t+"\n", g20t+"\n",
                    g21t+"\n", g22t+"\n", g23t+"\n", g30t+"\n",
                    g31t+"\n", g32t+"\n", g33t+"\n", name]
            fichier2 = open(path3, "w")
            fichier2.writelines(data)
            fichier2.close()

        btn = QPushButton(L[11])
        btn.setParent(window33)
        btn.move(135, 350)
        btn.setFont(font7)
        btn.pressed.connect(recupUserDat)
        btn.show()


########### Fenêtre des réglages ########

windowSettings = QWidget()
windowSettings.setWindowTitle(L[4])
windowSettings.setFixedSize(QSize(500, 400))
windowSettings.setWindowIcon(QIcon('/usr/lib/spoutnx/icone2.ico'))

window33 = QStackedWidget()
window33.setParent(windowSettings)
window33.move(150, 0)
window33.setFixedSize(QSize(350, 400))

window34 = QStackedWidget()
window34.setParent(windowSettings)
window34.move(150, 0)
window34.setFixedSize(QSize(350, 400))
liste = QListWidget()

liste.addItem(L[75])
liste.addItem(L[70])
liste.setParent(windowSettings)
liste.move(0, 0)
liste.setFixedSize(QSize(150, 500))
liste.setStyleSheet("QListView::item:selected{background-color: #3EF724}")
liste.setCurrentItem(None)
font2 = liste.font()
font2.setPointSize(10)
liste.setFont(font2)
liste.itemClicked.connect(text_changed2)
liste.show()


menu = window.menuBar()

file_menu = menu.addMenu(L[2])
file_menu.addAction(button_action)
file_menu.addAction(button_action2)
file_menu.addAction(button_action4)
file_menu.addAction(button_action6)

file_menu2 = menu.addMenu(L[3])
file_menu2.addAction(button_action3)
file_menu2.addAction(button_action5)


window.show()

# MessageBox pour enregistrer le fichier


def myExitHandler():
    if 'var' in locals():
        Varsave = VarSave + 1

    else:
        button = QMessageBox.question(window, "Enregistrer",
                                      L[192])

        if button == QMessageBox.Yes:
            saves()


if getattr(sys, 'frozen', False):
    pyi_splash.close()

app.aboutToQuit.connect(myExitHandler)

app.exec()
