from qtpy.QtWidgets import QWidget, QComboBox
from qtpy.QtGui import QIcon
from qtpy.QtCore import Qt
from .countries import countries
from .os_utils import OSUtils


class CountryPicker(QComboBox):

    def __init__(self, parent: QWidget = None):
        """Create a new CountryPicker instance

        :param parent: parent widget
        """

        super(CountryPicker, self).__init__(parent)

        self.countries = countries.copy()
        self.flag_icons_enabled = True

        self.current_country = next(iter(self.countries.keys()))

        for country_code, country_name in self.countries.items():
            self.addItem(
                QIcon(OSUtils.get_current_directory() + '/flags/' + country_code + '.png'),
                country_name
            )

    def getCurrentCountry(self) -> str:
        return self.current_country

    def setCurrentCountry(self, country_code: str):
        self.current_country = country_code
        self.setCurrentIndex(self.findText(self.countries[country_code]))

    def getCountryName(self, country_code) -> str:
        return self.countries[country_code]

    def setCountryName(self, country_code: str, country_name: str):
        item_index = self.findText(self.countries[country_code])
        self.setItemText(item_index, country_name)
        self.model().sort(self.modelColumn(), Qt.SortOrder.AscendingOrder)
        self.countries[country_code] = country_name

    def getCountryNames(self) -> dict[str, str]:
        return self.countries

    def setCountryNames(self, country_names: dict[str, str]):
        for country_code, country_name in country_names.items():
            item_index = self.findText(self.countries[country_code])
            self.setItemText(item_index, country_name)
            self.countries[country_code] = country_name
        self.model().sort(self.modelColumn(), Qt.SortOrder.AscendingOrder)

    def resetCountryNames(self):
        self.clear()
        self.countries = countries.copy()

        for country_code, country_name in self.countries.items():
            if self.flag_icons_enabled:
                self.addItem(
                    QIcon(OSUtils.get_current_directory() + '/flags/' + country_code + '.png'),
                    country_name
                )
            else:
                self.addItem(country_name)

        self.model().sort(self.modelColumn(), Qt.SortOrder.AscendingOrder)
        self.setCurrentCountry(self.current_country)

    def isFlagIconsEnabled(self) -> bool:
        return self.flag_icons_enabled

    def setFlagIconsEnabled(self, enabled: bool):
        self.flag_icons_enabled = enabled
        self.clear()

        for country_code, country_name in self.countries.items():
            if self.flag_icons_enabled:
                self.addItem(
                    QIcon(OSUtils.get_current_directory() + '/flags/' + country_code + '.png'),
                    country_name
                )
            else:
                self.addItem(country_name)

        self.model().sort(self.modelColumn(), Qt.SortOrder.AscendingOrder)
        self.setCurrentCountry(self.current_country)
