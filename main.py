import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import Slot, Qt, QLibraryInfo, QLocale, QTranslator
from PySide6.QtGui import QImage, QPixmap, QPainter, QPen, QKeySequence, QShortcut, QIcon, QColor
from form import Ui_MainWindow
from colormaps import tables
import bind
import numpy as np


def parse_loc(location):
    inde = 0
    for i in range(len(location)):
        if location[-i-1] == "/" or location[-i-1] == "\\":
            inde = i+1
            break
    return location[:-inde+1], location[-inde+1:]


def transform(pic, coef, coef2):
    pic = (np.log(np.expand_dims(np.nan_to_num(pic), axis=2))*(-1))**coef2
    pic = np.nan_to_num(pic, posinf=0.)
    koe = np.average(pic)/2**6
    pic = pic/koe/10*coef
    pic[pic > 256] = 255.
    pic[pic < 0] = 0.
    pic = pic.astype(np.uint8)
    return pic


def iterate_files(location, change):
    path, name = parse_loc(location)
    try:
        files = os.listdir(path)
    except:
        files = []
    A = []
    for i in files:
        if i[-4:] == ".npy":
            A.append(i)
    try:
        inde2 = A.index(name)
    except:
        inde2 = 0
        A = [""]
    last = False
    first = False
    if inde2 == 0:
        first = True
    if inde2 == len(A)-1:
        last = True
    if (last and change == 1) or (first and change == -1):
        change = 0
    loc2 = path+A[inde2+change]
    return loc2, first, last


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(self.tr("Klikátko"))
        self.setWindowIcon(QIcon(QPixmap(":/icons/icon.png")))
        self.short = QShortcut(QKeySequence('Ctrl+Z'), self)
        self.short2 = QShortcut(QKeySequence('Ctrl+A'), self)
        self.short3 = QShortcut(QKeySequence('Ctrl+D'), self)
        self.short4 = QShortcut(QKeySequence('Ctrl+S'), self)
        self.short5 = QShortcut(QKeySequence('Ctrl+R'), self)

        self.address = self.ui.umiste.toPlainText()
        self.address_out = self.ui.umiste_out.toPlainText()
        self.address_load = self.address
        self.firstlast(0)
        self.turn = self.ui.dial.value()
        self.turn2 = self.ui.dial_2.value()/3
        self.slide = 1.
        self.image = QImage()
        self.mkmode = False
        self.coord = []
        self.table = tables()
        self.tab = self.ui.slider2.value()
        self.saved = True
        self.outcome = 1048576
        self.m_rev = True
        self.m_sou = False
        self.m_hor = False
        self.m_ver = True
        self.ui.slider2.setMaximum(len(self.table)-1)
        self.overwrite = False
        self.pic = np.array([[10.]])
        self.pic_rot = np.array([[10.]])
        self.pic_tran = np.array([[100]])
        self.pic_col = QImage()
        self.pic_scal = QImage()

        self.short.activated.connect(self.zpet)
        self.short2.activated.connect(self.update_last)
        self.short3.activated.connect(self.update_next)
        self.short4.activated.connect(self.saving)
        self.short5.activated.connect(self.update_pict)
        self.ui.loader.clicked.connect(self.update_pict)
        self.ui.umiste.textChanged.connect(self.update_address)
        self.ui.umiste_out.textChanged.connect(self.update_address_out)
        self.ui.marker.clicked.connect(self.marking)
        self.ui.next.clicked.connect(self.update_next)
        self.ui.last.clicked.connect(self.update_last)
        self.ui.dial.valueChanged.connect(self.upd_turn)
        self.ui.dial_2.valueChanged.connect(self.upd_turn2)
        self.ui.slider2.valueChanged.connect(self.upd_slide2)
        self.ui.saver.clicked.connect(self.saving)
        self.ui.invert.clicked.connect(self.mapping)
        self.ui.loca_in.clicked.connect(self.browse_in)
        self.ui.loca_out.clicked.connect(self.browse_out)
        self.ui.reload.clicked.connect(self.reloadis)
        self.ui.counter.clicked.connect(self.rot_co)
        self.ui.clock.clicked.connect(self.rot_cl)
        self.ui.verti.clicked.connect(self.mir_ve)
        self.ui.horiz.clicked.connect(self.mir_ho)

        
    @Slot()
    def load_only(self):
        try:
            self.pic = np.load(self.address)
            self.ui.info.append(self.tr("==\nNačteny data z: ") + str(self.address))
            self.address_load = self.address
        except:
            message = self.tr("Adresa vstupních dat neexistuje a data proto nebyla načtena!")
            self.ui.info.append(message)
        self.transfo()

    @Slot()
    def transfo(self):
        if self.m_sou:
            self.pic_rot = self.pic.T
        else:
            self.pic_rot = self.pic
        if self.m_hor:
            self.pic_rot = np.fliplr(self.pic_rot)
        if self.m_ver:
            self.pic_rot = np.flipud(self.pic_rot)
        self.pic_rot = np.ascontiguousarray(self.pic_rot)
        self.visage()

    @Slot()
    def visage(self):
        self.pic_tran = transform(self.pic_rot, self.turn, self.turn2)
        self.mapping()

    @Slot()
    def mapping(self):
        hei, wid = self.pic_rot.shape
        self.pic_col = QImage(np.array(self.pic_tran), wid, hei, QImage.Format_Indexed8)
        if self.ui.invert.isChecked():
            self.pic_col.invertPixels()
        self.pic_col.setColorTable(self.table[self.tab])
        self.pic_col.convertTo(QImage.Format_RGB32)
        self.scaling()

    @Slot()
    def scaling(self):
        hei = self.pic_col.height()
        self.slide = 1
        self.get_size()
        self.pic_scal = self.pic_col.scaledToHeight(int(hei*self.slide))
        self.coord_draw()

    @Slot()
    def update_address(self):
        self.address = self.ui.umiste.toPlainText()
        self.firstlast(0)

    @Slot()
    def update_address_out(self):
        self.address_out = self.ui.umiste_out.toPlainText()
        self.pastdata()

    @Slot()
    def update_pict(self):
        if self.ui.with_next.isChecked():
            self.saving()
        if not self.testik():
            return
        self.coord = []
        self.load_only()

    @Slot()
    def update_next(self):
        if not self.ui.next.isEnabled():
            return
        if self.ui.with_next.isChecked():
            self.saving()
        if not self.testik():
            return
        self.firstlast(1)
        self.ui.umiste.setPlainText(self.address)
        self.coord = []
        self.load_only()

    @Slot()
    def update_last(self):
        if not self.ui.last.isEnabled():
            return
        if self.ui.with_next.isChecked():
            self.saving()
        if not self.testik():
            return
        self.firstlast(-1)
        self.ui.umiste.setPlainText(self.address)
        self.coord = []
        self.load_only()

    @Slot()
    def upd_turn(self, val):
        self.turn = val
        self.visage()

    @Slot()
    def upd_turn2(self, val):
        self.turn2 = val/3
        self.visage()

    @Slot()
    def upd_slide2(self, val):
        self.tab = val
        self.mapping()

    @Slot()
    def rot_cl(self):
        if (self.m_sou+self.m_rev)%2!=0:
            self.m_ver = not self.m_ver
        else:
            self.m_hor = not self.m_hor
        self.m_sou = not self.m_sou
        self.transfo()

    @Slot()
    def rot_co(self):
        if (self.m_sou+self.m_rev)%2!=0:
            self.m_hor = not self.m_hor
        else:
            self.m_ver = not self.m_ver
        self.m_sou = not self.m_sou
        self.transfo()

    @Slot()
    def mir_ve(self):
        self.m_ver = not self.m_ver
        self.m_rev = not self.m_rev
        self.transfo()

    @Slot()
    def mir_ho(self):
        self.m_hor = not self.m_hor
        self.m_rev = not self.m_rev
        self.transfo()

    @Slot()
    def zpet(self):
        if len(self.coord) != 0:
            self.coord = self.coord[:-1]
            self.coord_draw()
            self.saved = False

    @Slot()
    def browse_in(self):
        ftype = "Numpy files (*.npy)"
        soubor = QFileDialog.getOpenFileName(self, self.tr('Vyberte soubor'), "", ftype)
        if soubor[0] != '':
            self.address = soubor[0]
            self.firstlast(0)
            self.ui.umiste.setPlainText(self.address)

    @Slot()
    def browse_out(self):
        slozka = QFileDialog.getExistingDirectory(self, self.tr('Vyberte složku'), "")
        if slozka != '':
            self.address_out = slozka
            self.pastdata()
            self.ui.umiste_out.setPlainText(self.address_out)

    @Slot()
    def marking(self):
        self.mkmode = not self.mkmode
        if self.mkmode:
            self.ui.picture.setCursor(Qt.CrossCursor)
        else:
            self.ui.picture.setCursor(Qt.ArrowCursor)

    @Slot()
    def reloadis(self):
        path, name = parse_loc(self.address_load)
        adresa = self.address_out
        if adresa[-1:] not in ["/", "\\"]:
            adresa += path[-1:]
        location = adresa+name[:-4]+"_out.npy"
        data = np.load(location)
        data = data.tolist()
        for i in data:
            for k in i:
                if k not in self.coord:
                    self.coord.append(k)
        if len(data) != 0:
            self.saved = False
            message = self.tr("Přidány dříve uložené souřadnice.")
            self.ui.info.append(message)
            self.coord_draw()
        else:
            message = self.tr("V dříve uloženém souboru nebyly žádné souřadnice.")
            self.ui.info.append(message)

    @Slot()
    def saving(self):
        path, name = parse_loc(self.address_load)
        if self.address_out[-1:] not in ["/", "\\"]:
            self.address_out += path[-1:]
            self.ui.umiste_out.setPlainText(self.address_out)
        coor = []
        for i in range(len(self.coord)):
            if i != 0 and (i-1) % 2 == 0:
                coor.append([self.coord[i-1], self.coord[i]])
        coor = np.array(coor)
        location = self.address_out+name[:-4]+"_out.npy"
        if os.path.exists(location) and not self.ui.rewrite.isChecked() and not self.overwrite:
            message = self.tr("Data NEBYLA ULOŽENA, protože daný soubor již existuje a přepisování je vypnuté.")
            self.ui.info.append(message)
        else:
            try:
                np.save(location, coor)
                self.ui.info.append(self.tr("Data uložena do: ") + str(location))
                self.saved = True
            except:
                self.ui.info.append(self.tr("Data se NEPODAŘILO ULOŽIT do cílové destinace!"))
                self.saved = False

    def pastdata(self):
        path, name = parse_loc(self.address_load)
        adresa = self.address_out
        if adresa[-1:] not in ["/", "\\"]:
            adresa += path[-1:]
        location = adresa+name[:-4]+"_out.npy"
        if os.path.exists(location):
            self.ui.reload.setEnabled(True)
        else:
            self.ui.reload.setEnabled(False)

    def firstlast(self, change):
        self.address, first, last2 = iterate_files(self.address, change)
        self.ui.last.setEnabled(not first)
        self.ui.next.setEnabled(not last2)
        self.pastdata()

    def get_size(self):
        pic = [self.ui.picture.size().width(), self.ui.picture.size().height()]
        ima = [self.pic_col.size().width(), self.pic_col.size().height()]
        if 0 in ima:
            return True
        if pic[1] <= 50:
            self.slide *= 50/ima[1]
            return False
        if pic[0]/ima[0] > pic[1]/ima[1]:
            self.slide *= pic[1]/ima[1]
        else:
            self.slide *= pic[0]/ima[0]
        return False

    def coloord(self, coord):
        col = self.pic_scal.pixelColor(coord[0], coord[1])
        r, g, b, a = col.getRgb()
        if (r+g+b)/3 > 128:
            return QColor(Qt.black)
        else:
            return QColor(Qt.white)
        # legacy methods
        rgb = col.rgb()
        ind = self.table[self.tab].index(rgb)
        if ind < 128:
            ind = 255
        else:
            ind = 0
        return QColor.fromRgb(255 - r, 255 - g, 255 - b)
        return QColor.fromRgb((r+128) % 256, (g+128) % 256, (b+128) % 256)
        return QColor(self.table[self.tab][ind])

    def correction(self, coor):
        if self.m_ver:
            coor[1] = self.pic_rot.shape[0]-1-coor[1]
        if self.m_hor:
            coor[0] = self.pic_rot.shape[1]-1-coor[0]
        if self.m_sou:
            coor.reverse()
        return coor

    def recorrect(self, kor):
        coor = list(kor)
        if self.m_sou:
            coor.reverse()
        if self.m_ver:
            coor[1] = self.pic_rot.shape[0]-1-coor[1]
        if self.m_hor:
            coor[0] = self.pic_rot.shape[1]-1-coor[0]
        return coor

    def combine(self, col, col2):
        r, g, b, a = col.getRgb()
        R, G, B, A = col2.getRgb()
        return QColor.fromRgb(int((r+R)/2),int((g+G)/2),int((b+B)/2))

    def mousePressEvent(self, info):
        if self.mkmode:
            X = info.position().x()-1
            Y = info.position().y()-1
            coor = self.ui.picture.geometry()
            coim = self.image.size()
            if coor.x() < X < coor.x() + coim.width() and coor.y() < Y < coor.y() + coim.height():
                if info.button() == Qt.LeftButton:
                    sourad = [int((X-coor.x())/self.slide), int((Y-coor.y())/self.slide)]
                    self.coord.append(self.correction(sourad))
                    self.saved = False
                    self.ui.info.append(self.tr("Zvoleny souřadnice: ") + str(sourad))
                    self.coord_draw()
                elif info.button() == Qt.RightButton:
                    self.zpet()

    def closeEvent(self, info):
        if not self.testik():
            info.ignore()
        else:
            info.accept()

    def resizeEvent(self, info):
        if str(info.__repr__())[-17:-2] == "non-spontaneous":
            return
        if self.get_size():
            return
        self.scaling()

    def coord_draw(self):
        self.image = QImage(self.pic_scal)
        painter = QPainter(self.image)
        pen = QPen(Qt.black, 2)
        painter.setPen(pen)
        for i in range(len(self.coord)):
            coor = self.recorrect(self.coord[i])
            coor2 = self.recorrect(self.coord[i-1])
            co = [coor[0]*self.slide, coor[1]*self.slide]
            co2 = [coor2[0]*self.slide, coor2[1]*self.slide]
            col = self.coloord([co[0]+1,co[1]+1])
            col2 = self.coloord([co2[0]+1,co2[1]+1])
            colc = self.combine(col, col2)
            pen.setColor(col)
            painter.setPen(pen)
            painter.drawEllipse(co[0]-4, co[1]-4, 10, 10)
            if i != 0 and (i-1) % 2 == 0:
                pen.setColor(colc)
                painter.setPen(pen)
                painter.drawLine(co[0]+1, co[1]+1, co2[0]+1, co2[1]+1)
        self.ui.picture.setPixmap(QPixmap(self.image))
        self.ui.picture.setMinimumSize(0,0)
        painter.end()

    def vystraha(self):
        zprava = QMessageBox()
        zprava.setWindowTitle(self.tr("Neuložená data"))
        zprava.setText(self.tr("Některá data nejsou uložená, přesto pokračovat?"))
        zprava.setIcon(QMessageBox.Question)
        zprava.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Ignore)
        zprava.setDefaultButton(QMessageBox.Cancel)
        zprava.setInformativeText(self.tr("Uložení přepíše již uložená data"))
        self.outcome = zprava.exec()

    def testik(self):
        if not self.saved:
            self.vystraha()
        if self.outcome == 2048:
            self.overwrite = True
            self.outcome = 1048576
            self.saving()
            self.overwrite = False
            if self.saved == False:
                return False
        elif self.outcome == 4194304:
            self.outcome = 1048576
            return False
        self.saved = True
        return True


if __name__ == "__main__":
    app = QApplication(sys.argv)

    path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    translator = QTranslator(app)
    if translator.load(QLocale.system(), 'qtbase', '_', path):
        app.installTranslator(translator)
    elif QLocale.system().language() != QLocale.Czech:
        translator.load(QLocale.English, 'qtbase', '_', path)
        app.installTranslator(translator)
    translator = QTranslator(app)
    path = ":/translations/"
    if translator.load(QLocale.system(), 'tra', '_', path):
        app.installTranslator(translator)
    elif QLocale.system().language() != QLocale.Czech:
        translator.load(QLocale.English, 'tra', '_', path)
        app.installTranslator(translator)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
