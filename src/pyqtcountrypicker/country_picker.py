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

        self.__country_names = countries.copy()
        self.__country_flags = self.__get_default_country_flags()
        self.__flag_icons_enabled = True
        self.__filter = None
        self.__filtered_countries = set()

        self.__current_country = next(iter(self.__country_names.keys()))
        self.__blocking_signals = False

        self.__update_dropdown_items()
        self.currentTextChanged.connect(self.__current_text_changed)

    def getCurrentCountry(self) -> str:
        return self.__current_country

    def setCurrentCountry(self, country_code: str):
        country_code = country_code.lower()
        if country_code not in self.__country_names:
            return

        self.__current_country = country_code
        self.setCurrentIndex(self.findText(self.__country_names[country_code]))

    def getCountryName(self, country_code) -> str:
        country_code = country_code.lower()
        if country_code not in self.__country_names:
            return ''
        return self.__country_names[country_code]

    def setCountryName(self, country_code: str, country_name: str):
        country_code = country_code.lower()
        if country_code not in self.__country_names:
            return

        item_index = self.findText(self.__country_names[country_code])
        self.setItemText(item_index, country_name)
        self.model().sort(self.modelColumn(), Qt.SortOrder.AscendingOrder)
        self.__country_names[country_code] = country_name

    def getCountryNames(self) -> dict[str, str]:
        return self.__country_names

    def setCountryNames(self, country_names: dict[str, str]):
        for country_code, country_name in country_names.items():
            country_code = country_code.lower()
            if country_code not in self.__country_names:
                continue
            self.__country_names[country_code] = country_name
        self.__update_dropdown_items()

    def resetCountryNames(self):
        self.__country_names = countries.copy()
        self.__update_dropdown_items()

    def isFlagIconsEnabled(self) -> bool:
        return self.__flag_icons_enabled

    def setFlagIconsEnabled(self, enabled: bool):
        self.__flag_icons_enabled = enabled
        self.__update_dropdown_items()

    def getCountryFlag(self, country_code: str) -> QIcon:
        country_code = country_code.lower()
        if country_code not in self.__country_names:
            return QIcon()
        return self.__country_flags[country_code]

    def setCountryFlag(self, country_code: str, icon: QIcon):
        country_code = country_code.lower()
        if country_code not in self.__country_names:
            return
        self.__country_flags[country_code] = icon
        self.__update_dropdown_items()

    def getCountryFlags(self) -> dict[str, QIcon]:
        return self.__country_flags

    def setCountryFlags(self, country_flags: dict[str, QIcon]):
        for country_code, flag_icon in country_flags.items():
            country_code = country_code.lower()
            if country_code not in self.__country_names:
                continue
            self.__country_flags[country_code] = flag_icon
        self.__update_dropdown_items()

    def resetCountryFlags(self):
        self.__country_flags = self.__get_default_country_flags()
        self.__update_dropdown_items()

    def getFilter(self) -> FilterType | None:
        return self.__filter

    def setFilter(self, filter: FilterType | None):
        self.__filter = filter
        self.__update_dropdown_items()

    def getFilteredCountries(self) -> set[str]:
        return self.__filtered_countries

    def setFilteredCountries(self, filtered_countries: set[str]):
        self.__filtered_countries = {country_code.lower() for country_code in filtered_countries}
        self.__update_dropdown_items()

    def __update_dropdown_items(self):
        self.__blocking_signals = True
        self.clear()

        for country_code, country_name in self.__country_names.items():
            if self.__filter == FilterType.BLACKLIST and country_code in self.__filtered_countries:
                continue
            if self.__filter == FilterType.WHITELIST and country_code not in self.__filtered_countries:
                continue

            if self.__flag_icons_enabled:
                self.addItem(self.__country_flags[country_code], country_name, userData=country_code)
            else:
                self.addItem(country_name, userData=country_code)

        self.model().sort(self.modelColumn(), Qt.SortOrder.AscendingOrder)
        self.setCurrentCountry(self.__current_country)
        self.__blocking_signals = False

    def __current_text_changed(self, text: str):
        if not self.__blocking_signals:
            self.__current_country = self.currentData()
            self.countryChanged.emit(self.__current_country)

    def __get_default_country_flags(self) -> dict[str, QIcon]:
        return {
            country_code: QIcon(OSUtils.get_current_directory() + '/flags/{}.png'.format(country_code))
            for country_code in countries.keys()
        }
