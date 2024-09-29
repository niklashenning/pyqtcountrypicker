from qtpy.QtWidgets import QWidget, QComboBox
from qtpy.QtGui import QIcon
from qtpy.QtCore import Qt, Signal
from .countries import countries
from .os_utils import OSUtils


class CountryPicker(QComboBox):

    # Signal
    countryChanged = Signal(str)

    def __init__(self, parent: QWidget = None):
        """Create a new CountryPicker instance

        :param parent: parent widget
        """

        super(CountryPicker, self).__init__(parent)

        # Attributes
        self.__countries = set(countries.keys())
        self.__country_names = countries.copy()
        self.__country_flags = self.__get_default_country_flags()
        self.__country_flags_enabled = True

        self.__current_country = next(iter(self.__country_names.keys()))
        self.__blocking_signals = False

        # Init dropdown items
        self.__update_dropdown_items()
        self.currentTextChanged.connect(self.__current_text_changed)

    def getCurrentCountry(self) -> str:
        """Get the currently selected country

        :return: country code
        """

        return self.__current_country

    def setCurrentCountry(self, country_code: str):
        """Set the currently selected country

        :param country_code: country to select
        """

        country_code = country_code.lower()
        if country_code not in self.__country_names:
            return

        self.__current_country = country_code
        self.setCurrentIndex(self.findText(self.__country_names[country_code]))

    def getCountryName(self, country_code) -> str:
        """Get the name of a country by country code

        :param country_code: country code of the country
        :return: name of the country
        """

        country_code = country_code.lower()
        if country_code not in self.__country_names:
            return ''
        return self.__country_names[country_code]

    def setCountryName(self, country_code: str, country_name: str):
        """Set the name of a country by country code

        :param country_code: country code of the country
        :param country_name: new name of the country
        """

        country_code = country_code.lower()
        if country_code not in self.__country_names:
            return

        # Rename dropdown item and sort again
        item_index = self.findText(self.__country_names[country_code])
        self.setItemText(item_index, country_name)
        self.model().sort(self.modelColumn(), Qt.SortOrder.AscendingOrder)
        self.__country_names[country_code] = country_name

    def getCountryNames(self) -> dict[str, str]:
        """Get the country names

        :return: dict containing the country names by country code
        """

        return self.__country_names

    def setCountryNames(self, country_names: dict[str, str]):
        """Set the country names

        :param country_names: dict containing the country names by country code
        """

        # Rename all valid countries and update dropdown items
        for country_code, country_name in country_names.items():
            country_code = country_code.lower()
            if country_code not in self.__country_names:
                continue
            self.__country_names[country_code] = country_name

        self.__update_dropdown_items()

    def resetCountryNames(self):
        """Reset the country names to the default names"""

        self.__country_names = countries.copy()
        self.__update_dropdown_items()

    def isCountryFlagsEnabled(self) -> bool:
        """Get whether the country flag icons are enabled

        :return: whether the country flags are enabled
        """

        return self.__country_flags_enabled

    def setCountryFlagsEnabled(self, enabled: bool):
        """Set whether the country flag icons should be enabled

        :param enabled: whether the country flags should be enabled
        """

        self.__country_flags_enabled = enabled
        self.__update_dropdown_items()

    def getCountryFlag(self, country_code: str) -> QIcon:
        """Get the flag of a country by country code

        :param country_code: country code of the country
        :return: flag of the country
        """

        country_code = country_code.lower()
        if country_code not in self.__country_names:
            return QIcon()
        return self.__country_flags[country_code]

    def setCountryFlag(self, country_code: str, icon: QIcon):
        """Set the flag of a country by country code

        :param country_code: country code of the country
        :param icon: new flag of the country
        """

        country_code = country_code.lower()
        if country_code not in self.__country_names:
            return
        self.__country_flags[country_code] = icon
        self.__update_dropdown_items()

    def getCountryFlags(self) -> dict[str, QIcon]:
        """Get the country flags

        :return: dict containing the country flags by country code
        """

        return self.__country_flags

    def setCountryFlags(self, country_flags: dict[str, QIcon]):
        """Set the country flags

        :param country_flags: dict containing the country flags by country code
        """

        for country_code, flag_icon in country_flags.items():
            country_code = country_code.lower()
            if country_code not in self.__country_names:
                continue
            self.__country_flags[country_code] = flag_icon
        self.__update_dropdown_items()

    def resetCountryFlags(self):
        """Reset the country flags to the default flags"""

        self.__country_flags = self.__get_default_country_flags()
        self.__update_dropdown_items()

    def getCountries(self) -> list[str]:
        """Get the available countries

        :return: available countries
        """

        return list(self.__countries)

    def setCountries(self, countries: list[str]):
        """Set the available countries

        :param countries: new available countries
        """

        self.__countries = set(countries)
        self.__update_dropdown_items()

    def __update_dropdown_items(self):
        """Update the items of the dropdown by clearing and repopulating it"""

        self.__blocking_signals = True
        self.clear()

        # Add available countries
        for country_code, country_name in self.__country_names.items():
            if country_code not in self.__countries:
                continue

            # Only add country flag icons if enabled
            if self.__country_flags_enabled:
                self.addItem(self.__country_flags[country_code], country_name, userData=country_code)
            else:
                self.addItem(country_name, userData=country_code)

        # Sort dropdown and make sure previously selected country is selected again
        self.model().sort(self.modelColumn(), Qt.SortOrder.AscendingOrder)
        self.setCurrentCountry(self.__current_country)
        self.__blocking_signals = False

    def __current_text_changed(self, text: str):
        """Handle the currentTextChanged signal by emitting the
        countryChanged signal if the country has been manually changed

        :param text: text of currently selected item
        """

        if not self.__blocking_signals:
            self.__current_country = self.currentData()
            self.countryChanged.emit(self.__current_country)

    def __get_default_country_flags(self) -> dict[str, QIcon]:
        """Get a dict of the default country flag icons by country code

        :return: default country flag dict
        """

        return {
            country_code: QIcon(OSUtils.get_current_directory() + '/flags/{}.png'.format(country_code))
            for country_code in countries.keys()
        }
