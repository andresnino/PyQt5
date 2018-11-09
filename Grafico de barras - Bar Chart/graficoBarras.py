# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       graficoBarras.py
# Autores:      Miguel Andres Garcia Niño - Ángel Iván Hernández
# Creado:       08 de Noviembre 2018
# Modificado:   08 de Noviembre 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__version__ = "1.0"

"""
El módulo *graficoBarras* tiene como objetivo graficar en un diagrama de barras
un conjunto de datos.
"""

# Versión Python: 3.5.2
# Versión PyQt5: 5.11.3
# Versión PyQtChart: 5.11.3

from PyQt5.QtChart import (QChart, QChartView, QBarCategoryAxis, QBarSeries, QBarSet,
                           QValueAxis, QAbstractBarSeries)
from PyQt5.QtGui import QFont, QIcon, QPainter, QPixmap, QColor
from PyQt5.QtCore import Qt, QMargins, QTranslator, QLocale, QLibraryInfo
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QSizePolicy,
                             QGridLayout, QLabel, QColorDialog, QComboBox, QCheckBox,
                             QPushButton, QFileDialog, QMessageBox)


# ===================== CLASE graficoBarras ========================

class graficoBarras(QWidget):
    def __init__(self, parent=None):
        super(graficoBarras, self).__init__(parent)

        self.initUI()

    def initUI(self):

        comboBoxColor = QComboBox()
        comboBoxColor.addItems(["Color del fondo del CharView",
                                "Color del fondo del Chart",
                                "Color del título del Chart",
                                "Color de las etiquetas del eje X",
                                "Color de las etiquetas del eje Y",
                                "Color de las etiquetas de la leyenda"])

        checkBoxVisibilidadFondoChart = QCheckBox("Visibilidad fondo (chart)")
        checkBoxMargenesChart = QCheckBox("Margenes del chart")
        checkBoxEsquinasChart = QCheckBox("Esquinas del chart")

        buttonGuardar = QPushButton("Guardar gráfico")

        # Crear gráficos.
        self.vistaGrafico = QChartView(self.crearGraficoBarras())
        self.vistaGrafico.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.vistaGrafico.setRenderHint(QPainter.Antialiasing, True)

      # ========================== DISEÑO ==========================

        disenioConfiguracion = QVBoxLayout()
        disenioConfiguracion.addWidget(QLabel("Cambiar colores:"))
        disenioConfiguracion.addWidget(comboBoxColor)
        disenioConfiguracion.addWidget(checkBoxVisibilidadFondoChart)
        disenioConfiguracion.addWidget(checkBoxMargenesChart)
        disenioConfiguracion.addWidget(checkBoxEsquinasChart)
        disenioConfiguracion.setSpacing(4)
        disenioConfiguracion.addStretch()
        disenioConfiguracion.addWidget(buttonGuardar)

        baseDisenio = QGridLayout()
        baseDisenio.addLayout(disenioConfiguracion, 0, 0, 0, 1)
        baseDisenio.addWidget(self.vistaGrafico, 0, 1, 0, 4)
        baseDisenio.setSpacing(10)
        baseDisenio.setContentsMargins(10, 10, 10, 10)

        self.setLayout(baseDisenio)

      # ===================== CONECTAR SEÑALES =====================

        comboBoxColor.activated.connect(self.Color)
        checkBoxVisibilidadFondoChart.toggled.connect(self.visibilidadFondoChart)
        checkBoxMargenesChart.toggled.connect(self.margenesChart)
        checkBoxEsquinasChart.toggled.connect(self.esquinasChart)
        buttonGuardar.clicked.connect(self.Guardar)

        # Establecer los valores predeterminados
        comboBoxColor.setCurrentIndex(-1)
        checkBoxVisibilidadFondoChart.setChecked(True)
        checkBoxMargenesChart.setChecked(True)
        checkBoxEsquinasChart.setChecked(True)

  # ========================== FUNCIONES ===========================

    def crearGraficoBarras(self):
        paises = ["EEUU", "China", "Japon", "Alemania", "Reino Unido", "Resto del mundo"]
        valores = [24.32, 14.85, 8.91, 12.54, 7.85, 31.53]
        colores = [Qt.blue, Qt.red, Qt.darkYellow, Qt.gray, Qt.black, Qt.darkCyan]

        grafico = QChart()
        grafico.setMargins(QMargins(30, 30, 30, 30))
        grafico.setTheme(QChart.ChartThemeLight)
        grafico.setTitle("% Distribución del PIB global")
        grafico.setAnimationOptions(QChart.SeriesAnimations)

        for i in range(len(paises)):
            series = QBarSeries()
            
            barSet = QBarSet(paises[i])
            barSet.setColor(colores[i])
            barSet.setLabelColor(Qt.yellow)
            barSet.append(valores[i])
            
            series.append(barSet)
            series.setLabelsVisible(True)
            series.setLabelsAngle(-90)
            # series.setLabelsPrecision(2)
            series.setLabelsFormat("@value %")
            series.setLabelsPosition(QAbstractBarSeries.LabelsCenter)
            
            grafico.addSeries(series)

        axisX = QBarCategoryAxis()
        axisX.append(paises)

        axisY = QValueAxis()
        axisY.setRange(0, 31.53)
        axisY.setTickCount(10)
        axisY.setLabelFormat("%.2f %")
        
        grafico.createDefaultAxes()
        grafico.setAxisX(axisX, None)
        grafico.setAxisY(axisY, None)

        grafico.legend().setVisible(True)
        grafico.legend().setAlignment(Qt.AlignBottom)

        return grafico

    def Color(self, item):
        if item == 0:
            color = (self.vistaGrafico.backgroundBrush().color()
                     if self.vistaGrafico.backgroundBrush().color().isValid()
                     else QColor(Qt.white))
        elif item == 1:
            color = (self.vistaGrafico.chart().backgroundBrush().color()
                     if self.vistaGrafico.chart().backgroundBrush().color().isValid()
                     else QColor(Qt.white))
        elif item == 2:
            color = (self.vistaGrafico.chart().titleBrush().color()
                     if self.vistaGrafico.chart().titleBrush().color().isValid()
                     else QColor(Qt.black))
        elif item == 3:
            color = (self.vistaGrafico.chart().axisX().labelsBrush().color()
                     if self.vistaGrafico.chart().axisX().labelsBrush().color().isValid()
                     else QColor(Qt.black))
        elif item == 4:
            color = (self.vistaGrafico.chart().axisY().labelsBrush().color()
                     if self.vistaGrafico.chart().axisY().labelsBrush().color().isValid()
                     else QColor(Qt.black))
        elif item == 5:
            color = (self.vistaGrafico.chart().legend().labelColor()
                     if self.vistaGrafico.chart().legend().labelColor().isValid()
                     else QColor(Qt.black))
            
        color = QColorDialog.getColor(color, self)
        if color.isValid():
            if item == 0:
                self.vistaGrafico.setBackgroundBrush(color)
            elif item == 1:
                self.vistaGrafico.chart().setBackgroundBrush(color)
            elif item == 2:
                self.vistaGrafico.chart().setTitleBrush(color)
            elif item == 3:
                self.vistaGrafico.chart().axisX().setLabelsBrush(color)
            elif item == 4:
                self.vistaGrafico.chart().axisY().setLabelsBrush(color)
            elif item == 5:
                self.vistaGrafico.chart().legend().setLabelColor(color)

    def visibilidadFondoChart(self, bool):
        self.vistaGrafico.chart().setBackgroundVisible(bool)

    def margenesChart(self, bool):
        if bool:
            self.vistaGrafico.chart().layout().setContentsMargins(9, 9, 9, 9)
        else:
            self.vistaGrafico.chart().layout().setContentsMargins(0, 0, 0, 0)

    def esquinasChart(self, bool):
        if bool:
            self.vistaGrafico.chart().setBackgroundRoundness(5)
        else:
            self.vistaGrafico.chart().setBackgroundRoundness(0)

    def Guardar(self):
        nombre, extension = QFileDialog.getSaveFileName(self, "Guardar como",
                                                        "Gráfico de barras",
                                                        "JPG (*.jpg);;PNG (*.png)",
                                                        options=QFileDialog.Options())
                
        if nombre:
            guardar = QPixmap(self.vistaGrafico.grab())
            guardar.save(nombre, quality = 100)

            if guardar:
                QMessageBox.information(self, "Guardar gráfico", "Gráfico guardado con éxito.",
                                        QMessageBox.Ok)
            else:
                QMessageBox.critical(self, "Guardar gráfico", "Error al guardar el gráfico.",
                                     QMessageBox.Ok)
                

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
    ventana.setWindowTitle("Gráfico de barras por: ANDRES NIÑO - ÁNGEL HERNÁNDEZ")
    ventana.setMinimumSize(900, 550)
        
    widget = graficoBarras()
    
    ventana.setCentralWidget(widget)
    ventana.show()

    sys.exit(aplicacion.exec_())
