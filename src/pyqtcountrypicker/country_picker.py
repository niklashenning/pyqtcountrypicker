from qtpy.QtWidgets import QWidget, QComboBox
from qtpy.QtGui import QIcon
from qtpy.QtCore import Qt, Signal
from .countries import countries
from .enums import FilterType
from .os_utils import OSUtils


class CountryPicker(QComboBox):

    # Signal
    countryChanged = Signal(str)

    def __init__(self, parent: QWidget = None):
        """Create a new CountryPicker instance

        :param parent: parent widget
        """

        super(CountryPicker, self).__init__(parent)

        self.countries = countries.copy()
        self.flag_icons_enabled = True
        self.filter = None
        self.filtered_countries = set()

        self.current_country = next(iter(self.countries.keys()))
        self.blocking_signals = False

        self.__update_dropdown_items()

        self.currentTextChanged.connect(self.__current_text_changed)

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
            self.countries[country_code] = country_name
        self.__update_dropdown_items()

    def resetCountryNames(self):
        self.countries = countries.copy()
        self.__update_dropdown_items()

    def isFlagIconsEnabled(self) -> bool:
        return self.flag_icons_enabled

    def setFlagIconsEnabled(self, enabled: bool):
        self.flag_icons_enabled = enabled
        self.__update_dropdown_items()

    def getFilter(self) -> FilterType | None:
        return self.filter

    def setFilter(self, filter: FilterType | None):
        self.filter = filter
        self.__update_dropdown_items()

    def getFilteredCountries(self) -> set[str]:
        return self.filtered_countries

    def setFilteredCountries(self, filtered_countries: set[str]):
        self.filtered_countries = filtered_countries
        self.__update_dropdown_items()

    def __update_dropdown_items(self):
        self.blocking_signals = True
        self.clear()

        for country_code, country_name in self.countries.items():
            if self.filter == FilterType.BLACKLIST and country_code in self.filtered_countries:
                continue
            if self.filter == FilterType.WHITELIST and country_code not in self.filtered_countries:
                continue

            if self.flag_icons_enabled:
                self.addItem(
                    QIcon(OSUtils.get_current_directory() + '/flags/' + country_code + '.png'),
                    country_name, userData=country_code
                )
            else:
                self.addItem(country_name, userData=country_code)

        self.model().sort(self.modelColumn(), Qt.SortOrder.AscendingOrder)
        self.setCurrentCountry(self.current_country)
        self.blocking_signals = False

    def __current_text_changed(self, text: str):
        if not self.blocking_signals:
            self.current_country = self.currentData()
            self.countryChanged.emit(self.current_country)
