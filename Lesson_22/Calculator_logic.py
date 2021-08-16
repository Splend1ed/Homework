from calculator_Ui import *
from math import sqrt
from time import sleep


class CaLogic(UiCalculator):
    def ui_setup(self, window):
        super().ui_setup(window)
        self.button_connect()

    def button_connect(self):
        self.button_0.clicked.connect(lambda: self.input_to_screen(self.button_0.text()))
        self.button_1.clicked.connect(lambda: self.input_to_screen(self.button_1.text()))
        self.button_2.clicked.connect(lambda: self.input_to_screen(self.button_2.text()))
        self.button_3.clicked.connect(lambda: self.input_to_screen(self.button_3.text()))
        self.button_4.clicked.connect(lambda: self.input_to_screen(self.button_4.text()))
        self.button_5.clicked.connect(lambda: self.input_to_screen(self.button_5.text()))
        self.button_6.clicked.connect(lambda: self.input_to_screen(self.button_6.text()))
        self.button_7.clicked.connect(lambda: self.input_to_screen(self.button_7.text()))
        self.button_8.clicked.connect(lambda: self.input_to_screen(self.button_8.text()))
        self.button_9.clicked.connect(lambda: self.input_to_screen(self.button_9.text()))
        self.button_div.clicked.connect(lambda: self.input_to_screen(self.button_div.text()))
        self.button_minus.clicked.connect(lambda: self.input_to_screen(self.button_minus.text()))
        self.button_mul.clicked.connect(lambda: self.input_to_screen(self.button_mul.text()))
        self.button_plus.clicked.connect(lambda: self.input_to_screen(self.button_plus.text()))
        self.button_percent.clicked.connect(lambda: self.input_to_screen(self.button_percent.text()))
        self.button_comma.clicked.connect(lambda: self.input_to_screen(self.button_comma.text()))
        self.button_open_brackets.clicked.connect(lambda: self.input_to_screen(self.button_open_brackets.text()))
        self.button_X2.clicked.connect(lambda: self.input_to_screen(self.button_X2.text()))
        self.button_squareroot.clicked.connect(lambda: self.input_to_screen(self.button_squareroot.text()))
        self.button_close_brackets.clicked.connect(lambda: self.input_to_screen(self.button_close_brackets.text()))
        self.button_clearall.clicked.connect(self.clear_all)
        self.button_backstep.clicked.connect(self.back_step)
        self.button_equals.clicked.connect(self.logic)

    def input_to_screen(self, symbol: str):
        self.input_screen.setText(self.input_screen.text() + symbol)

    def find_nums_front_symbol(self, symbol: str):
        screen = self.input_screen.text()
        if symbol in screen:
            index_percent = screen.index(symbol)
            for symbols in ['+', '-', '×', '÷', '²', ',', '√', '(', ')', '%']:
                if symbols in screen:
                    index_symbol = screen.index(symbols)
                    this_symbols = screen[index_symbol + 1: index_percent]
                    return this_symbols
            else:
                this_symbols2 = screen[:index_percent]
                return this_symbols2
        else:
            return '0'

    def find_nums(self, symbol: str):
        screen = self.input_screen.text()
        list_of_symbols = ['+', '-', '×', '÷', '(', ')', '²', ',', '%', '√']
        if symbol in screen:
            index_sq = screen.index(symbol)
            for symbols in list_of_symbols:
                for count in range(screen.count(symbols)):
                    if symbols in screen:
                        try:
                            front_cut = screen[index_sq + 1:]
                            symb_index = front_cut.index(symbols)
                            back_cut = front_cut[:symb_index]
                            return back_cut
                        except ValueError:
                            pass
            else:
                this_symbols3 = screen[index_sq + 1:]
                return this_symbols3
        else:
            return '0'

    def logic(self):
        # try:
            percent = self.find_nums_front_symbol('%')
            sq = self.find_nums('√')
            result = eval(self.input_screen.text().replace(f'{percent}%', f'{percent}/100')
                          .replace(f'√{int(sq)}', f"sqrt({int(sq)})").replace('×', '*')
                          .replace('÷', '/').replace('²', '**2').replace(',', '.'))
            self.output_screen.setText(self.input_screen.text() + '\t=\t' + str(result))
        # except (ValueError, SyntaxError):
        #     self.input_screen.setText('Incorrect expression!')

    def clear_all(self):
        self.input_screen.setText('')

    def back_step(self):
        self.input_screen.setText(self.input_screen.text()[:-1])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = CaLogic()
    ui.ui_setup(Calculator)
    Calculator.show()
    sys.exit(app.exec_())


# Якщо було б більше часу зробив би кращий алгоритм пошуку,та доробив би відсоток
