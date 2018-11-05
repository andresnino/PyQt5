# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       graficoCircular.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       04 de Noviembre 2018
# Modificado:   04 de Noviembre 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__version__ = "1.0"

"""
El módulo *graficoCircular* permite crear un gráfico circular o gráfica circular,
también llamado "gráfico de pastel", "gráfico de tarta", "gráfico de torta" o
"gráfica de 360 grados".
"""

# Versión Python: 3.5.2
# Versión PyQt5: 5.11.3
# Versión PyQtChart: 5.11.3

from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice, QLegend
from PyQt5.QtGui import QFont, QIcon, QPalette, QColor, QPainter
from PyQt5.QtCore import Qt, QTranslator, QLocale, QLibraryInfo, pyqtSlot
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout,
                             QLabel, QComboBox, QSizePolicy, QCheckBox)


# ==================== CLASE graficoCircular =======================

class graficoCircular(QWidget):
    def __init__(self, parent=None):
        super(graficoCircular, self).__init__(parent)

        self.initUI()

    def initUI(self):

        self.m_temaComboBox = self.crearTemaCaja()
        self.m_animacionComboBox = self.crearAnimacionCaja()
        self.m_leyendaComboBox = self.crearLeyendaCaja()
        self.m_marcadorLeyendaComboBox = self.crearMarcadorLeyendaCaja()
        self.m_posicionEtiquetaComboBox = self.crearPosicionEtiquetaCaja()
        
        self.m_visibilidadEtiquetaCheckBox = QCheckBox("Visibilidad etiqueta")

        # Crear gráficos.
        vistaGrafico = QChartView(self.crearGraficoCircular())
        # Suceden cosas divertidas si las etiquetas de la porción circular no encajan en la
        # pantalla ...
        vistaGrafico.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        vistaGrafico.setRenderHint(QPainter.Antialiasing, True)

        self.m_grafico = vistaGrafico

      # ========================== DISEÑO ==========================

        disenioConfiguracion = QVBoxLayout()
        disenioConfiguracion.addWidget(QLabel("Tema:"))
        disenioConfiguracion.addWidget(self.m_temaComboBox)
        disenioConfiguracion.addWidget(QLabel("Animación:"))
        disenioConfiguracion.addWidget(self.m_animacionComboBox)
        disenioConfiguracion.addWidget(QLabel("Leyenda:"))
        disenioConfiguracion.addWidget(self.m_leyendaComboBox)
        disenioConfiguracion.addWidget(QLabel("Marcador leyenda:"))
        disenioConfiguracion.addWidget(self.m_marcadorLeyendaComboBox)
        disenioConfiguracion.addWidget(QLabel("Posición etiqueta:"))
        disenioConfiguracion.addWidget(self.m_posicionEtiquetaComboBox)
        disenioConfiguracion.addWidget(self.m_visibilidadEtiquetaCheckBox)
        disenioConfiguracion.addStretch()

        baseDisenio = QGridLayout()
        baseDisenio.addLayout(disenioConfiguracion, 0, 0, 0, 1)
        baseDisenio.addWidget(vistaGrafico, 0, 1, 0, 4)

        self.setLayout(baseDisenio)

      # ===================== CONECTAR SEÑALES =====================

        self.m_temaComboBox.currentIndexChanged.connect(self.actualizarUI)
        self.m_animacionComboBox.currentIndexChanged.connect(self.actualizarUI)
        self.m_leyendaComboBox.currentIndexChanged.connect(self.actualizarUI)
        self.m_marcadorLeyendaComboBox.currentIndexChanged.connect(self.actualizarUI)
        self.m_posicionEtiquetaComboBox.currentIndexChanged.connect(self.actualizarUI)
        self.m_visibilidadEtiquetaCheckBox.toggled.connect(self.actualizarUI)

        # Establecer los valores predeterminados
        self.m_visibilidadEtiquetaCheckBox.setChecked(True)
        self.actualizarUI()

  # ========================= FUNCIONES ============================

    def crearTemaCaja(self):
        temaComboBox = QComboBox()

        temaComboBox.addItem("Luz", QChart.ChartThemeLight)
        temaComboBox.addItem("Azul cerúleo", QChart.ChartThemeBlueCerulean)
        temaComboBox.addItem("Oscuro", QChart.ChartThemeDark)
        temaComboBox.addItem("Arena marrón", QChart.ChartThemeBrownSand)
        temaComboBox.addItem("Azul NCS", QChart.ChartThemeBlueNcs)
        temaComboBox.addItem("Alto contraste", QChart.ChartThemeHighContrast)
        temaComboBox.addItem("Azul helado", QChart.ChartThemeBlueIcy)
        temaComboBox.addItem("Tema Qt", QChart.ChartThemeQt)

        return temaComboBox

    def crearAnimacionCaja(self):
        animacionComboBox = QComboBox()

        animacionComboBox.addItem("No animaciones", QChart.NoAnimation)
        animacionComboBox.addItem("Animaciones GridAxis", QChart.GridAxisAnimations)
        animacionComboBox.addItem("Serie de animaciones", QChart.SeriesAnimations)
        animacionComboBox.addItem("Todas las animaciones", QChart.AllAnimations)

        return animacionComboBox

    def crearLeyendaCaja(self):
        leyendaComboBox = QComboBox()

        leyendaComboBox.addItem("No Leyenda", 0)
        leyendaComboBox.addItem("Leyenda superior", Qt.AlignTop)
        leyendaComboBox.addItem("Leyenda inferior", Qt.AlignBottom)
        leyendaComboBox.addItem("Leyenda izquierda", Qt.AlignLeft)
        leyendaComboBox.addItem("Leyenda derecha", Qt.AlignRight)

        return leyendaComboBox

    def crearMarcadorLeyendaCaja(self):
        marcadorLeyendaComboBox = QComboBox()

        marcadorLeyendaComboBox.addItem("Predeterminado", QLegend.MarkerShapeDefault)
        marcadorLeyendaComboBox.addItem("Rectangular", QLegend.MarkerShapeRectangle)
        marcadorLeyendaComboBox.addItem("Circular", QLegend.MarkerShapeCircle)
        marcadorLeyendaComboBox.addItem("Determinado por la serie",
                                        QLegend.MarkerShapeFromSeries)

        return marcadorLeyendaComboBox

    def crearPosicionEtiquetaCaja(self):
        posicionEtiquetaComboBox = QComboBox()

        posicionEtiquetaComboBox.addItem("Etiqueta predeterminada", QPieSlice.LabelOutside)
        posicionEtiquetaComboBox.addItem("Etiqueta interior horizontal",
                                         QPieSlice.LabelInsideHorizontal)
        posicionEtiquetaComboBox.addItem("Etiqueta interior tangencial",
                                         QPieSlice.LabelInsideTangential)
        posicionEtiquetaComboBox.addItem("Etiqueta interior normal",
                                         QPieSlice.LabelInsideNormal)

        return posicionEtiquetaComboBox

    def crearGraficoCircular(self):
        """Una serie de sectores consiste en segmentos que se definen como objetos QPieSlice.
           Los segmentos pueden tener cualquier valor, ya que el objeto QPieSeries calcula el
           porcentaje de un segmento en comparación con la suma de todos los segmentos de la
           serie para determinar el tamaño real del segmento en el gráfico."""
        
        grafico = QChart()
        grafico.setTitle("Lenguajes de programación más usados (TIOBE)")

        lista_datos = [("Java", 17.801), ("C", 15.376), ("C++", 7.593),
                       ("Python", 7.156), ("Visual Basic .NET", 5.884)]

        series = QPieSeries(grafico)
        for etiqueta, valor in lista_datos:
            slice = series.append(etiqueta, valor)

        grafico.addSeries(series)
        grafico.createDefaultAxes()

        return grafico

    @pyqtSlot()
    def actualizarUI(self):

      # ====================== CONFIGURAR TEMA =====================
      
        tema = self.m_temaComboBox.itemData(self.m_temaComboBox.currentIndex())

        if self.m_grafico.chart().theme() != tema:
            self.m_grafico.chart().setTheme(tema)

            pal = self.window().palette()

            if tema == QChart.ChartThemeLight:
                pal.setColor(QPalette.Window, QColor(0xf0f0f0))
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            elif tema == QChart.ChartThemeDark:
                pal.setColor(QPalette.Window, QColor(0x121218))
                pal.setColor(QPalette.WindowText, QColor(0xd6d6d6))
            elif tema == QChart.ChartThemeBlueCerulean:
                pal.setColor(QPalette.Window, QColor(0x40434a))
                pal.setColor(QPalette.WindowText, QColor(0xd6d6d6))
            elif tema == QChart.ChartThemeBrownSand:
                pal.setColor(QPalette.Window, QColor(0x9e8965))
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            elif tema == QChart.ChartThemeBlueNcs:
                pal.setColor(QPalette.Window, QColor(0x018bba))
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            elif tema == QChart.ChartThemeHighContrast:
                pal.setColor(QPalette.Window, QColor(0xffab03))
                pal.setColor(QPalette.WindowText, QColor(0x181818))
            elif tema == QChart.ChartThemeBlueIcy:
                pal.setColor(QPalette.Window, QColor(0xcee7f0))
                pal.setColor(QPalette.WindowText, QColor(0x404044))
            else:
                pal.setColor(QPalette.Window, QColor(0xf0f0f0))
                pal.setColor(QPalette.WindowText, QColor(0x404044))

            self.window().setPalette(pal)

      # =================== CONFIGURAR ANIMACIÓN ===================

        opciones = QChart.AnimationOptions(self.m_animacionComboBox.itemData(
            self.m_animacionComboBox.currentIndex()))

        if self.m_grafico.chart().animationOptions() != opciones:
            self.m_grafico.chart().setAnimationOptions(opciones)

      # ====================== OBTENER LEYENDA =====================

        leyenda = self.m_grafico.chart().legend()

      # ================ CONFIGURAR POSICIÓN LEYENDA ===============

        alineacion = self.m_leyendaComboBox.itemData(self.m_leyendaComboBox.currentIndex())

        if alineacion == 0:
            leyenda.hide()
        else:
            leyenda.setAlignment(Qt.Alignment(alineacion))
            leyenda.show()

      # ================ CONFIGURAR MARCADOR LEYENDA ===============

        marcador = self.m_marcadorLeyendaComboBox.itemData(
            self.m_marcadorLeyendaComboBox.currentIndex()) 

        if leyenda != marcador:
            leyenda.setMarkerShape(marcador)

      # =============== CONFIGURAR POSICIÓN ETIQUETA ===============

        posicionEtiqueta = self.m_posicionEtiquetaComboBox.itemData(
            self.m_posicionEtiquetaComboBox.currentIndex())
        self.m_grafico.chart().series()[0].setLabelsPosition(posicionEtiqueta)

      # ============== CONFIGURAR VISIBILIDAD ETIQUETA =============

        visibilidadEtiqueta = self.m_visibilidadEtiquetaCheckBox.isChecked()
        self.m_grafico.chart().series()[0].setLabelsVisible(visibilidadEtiqueta)


# ==================================================================           

if __name__ == "__main__":

    import sys

    aplicacion = QApplication(sys.argv)

    traductor = QTranslator(aplicacion)
    lugar = QLocale.system().name()
    path = QLibraryInfo.location(QLibraryInfo.TranslationsPath)
    traductor.load("qtbase_%s" % lugar, path)
    aplicacion.installTranslator(traductor)

    fuente = QFont()
    fuente.setPointSize(10)
    aplicacion.setFont(fuente)

    ventana = QMainWindow()
    ventana.setWindowIcon(QIcon("Qt.png"))
    ventana.setWindowTitle("Gráfico Circular por: ANDRES NIÑO")
    ventana.setMinimumSize(900, 500)
        
    widget = graficoCircular()
    
    ventana.setCentralWidget(widget)
    ventana.show()

    sys.exit(aplicacion.exec_())
