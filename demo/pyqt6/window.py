from PyQt6.QtWidgets import QMainWindow, QWidget, QFormLayout
from PyQt6.QtCore import Qt
from pyqtcountrypicker import CountryPicker


class Window(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)

        self.setWindowTitle('Country Picker Demo')

        # Country picker with default settings
        self.country_picker_1 = CountryPicker(self)
        self.country_picker_1.setFixedHeight(32)
        self.country_picker_1.countryChanged.connect(
            lambda country: print('Country 1 changed: {} ({})'.format(
                country, self.country_picker_1.getCountryName(country))
            )
        )

        # Country picker with custom settings
        self.country_picker_2 = CountryPicker(self)
        self.country_picker_2.setFixedHeight(32)
        self.country_picker_2.setCountries([
            'at', 'be', 'bg', 'hr', 'cy', 'cz', 'dk', 'ee', 'fi',
            'fr', 'de', 'gr', 'hu', 'ie', 'it', 'lt', 'lu', 'lv',
            'mt', 'nl', 'pl', 'pt', 'ro', 'sk', 'si', 'es', 'se'
        ])
        self.country_picker_2.setStyleSheet(open('css/custom-combobox.css').read())
        self.country_picker_2.countryChanged.connect(
            lambda country: print('Country 2 changed: {} ({})'.format(
                country, self.country_picker_2.getCountryName(country))
            )
        )

        # Form layout
        form_layout = QFormLayout()
        form_layout.addRow('Default:', self.country_picker_1)
        form_layout.addRow('Custom:', self.country_picker_2)
        form_layout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        form_layout.setSpacing(20)
        form_layout.setContentsMargins(35, 35, 40, 40)

        central_widget = QWidget()
        central_widget.setLayout(form_layout)
        self.setCentralWidget(central_widget)
