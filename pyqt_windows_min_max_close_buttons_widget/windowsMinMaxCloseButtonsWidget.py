from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QFont, qGray
from PyQt5.QtWidgets import QWidget
from pyqt_min_max_close_buttons_widget import MinMaxCloseButtonsWidget

from python_color_getter.pythonColorGetter import PythonColorGetter


class WindowsMinMaxCloseButtonsWidget(MinMaxCloseButtonsWidget):
    def __init__(self, base_widget: QWidget, hint=Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint, font=QFont('Arial', 12)):
        super().__init__(hint)
        self.__initVal(base_widget, hint, font)
        self.__initUi()

    def __initVal(self, base_widget, hint, font):
        self.__baseWidget = base_widget
        self.__hint = hint
        self.__font = font

    def __initUi(self):
        self.layout().setSpacing(0)

        self._minimizeBtn.setText('🗕')
        self._maximizeBtn.setText('🗖')
        self._closeBtn.setText('🗙')

        self.__styleInit()
        
    def __getHoverColor(self, base_color):
        hover_factor = 130
        r, g, b = base_color.red(), base_color.green(), base_color.blue()
        gray = qGray(r, g, b)
        if gray > 255 // 2:
            hover_color = base_color.darker(hover_factor)
        else:
            hover_color = base_color.lighter(hover_factor)
        return hover_color

    def __getButtonTextColor(self, r, g, b):
        if r == g == b:
            btn_text_color = QColor(r, g, b)
        else:
            gray = qGray(r, g, b)
            if gray > 255 // 2:
                btn_text_color = QColor(255, 255, 255)
            else:
                btn_text_color = QColor(0, 0, 0)
        return btn_text_color

    def __styleInit(self):
        btns = [self._minimizeBtn, self._maximizeBtn, self._closeBtn]

        base_color = self.__baseWidget.palette().color(QPalette.Base)
        hover_color = self.__getHoverColor(base_color)

        r, g, b = PythonColorGetter.get_complementary_color(hover_color.red(),
                                                            hover_color.green(),
                                                            hover_color.blue())

        btn_text_color = self.__getButtonTextColor(r, g, b)

        h_padding_size = self.__font.pointSize() // 2
        v_padding_size = self.__font.pointSize() // 5

        tool_button_style = f'''
                            QPushButton
                            {{ 
                            background: {base_color.name()};
                            color: {btn_text_color.name()};
                            padding-left: {h_padding_size};
                            padding-right: {h_padding_size};
                            padding-top: {v_padding_size};
                            padding-bottom: {v_padding_size};
                            border: 0; 
                            }}
                            QPushButton:hover
                            {{ 
                            background-color: {hover_color.name()};
                            }}
                            '''

        close_button_style = tool_button_style + f'''
                             QPushButton:hover 
                             {{ 
                             background-color: #EE0000; 
                             color: #ffffff;
                             }}
                             '''

        font_size = self.__font.pointSize() // 1.2

        for btn in btns:
            font = btn.font()
            font.setPointSize(font_size)
            btn.setFont(font)
            btn.setStyleSheet(tool_button_style)

        self._closeBtn.setStyleSheet(close_button_style)

    def event(self, e):
        if e.type() == 100:
            self.__styleInit()
        return super().event(e)