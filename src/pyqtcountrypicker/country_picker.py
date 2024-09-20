from qtpy.QtWidgets import QWidget, QComboBox
from qtpy.QtGui import QIcon
from .countries import countries
from .os_utils import OSUtils


class CountryPicker(QComboBox):

    def __init__(self, parent: QWidget = None):
        """Create a new CountryPicker instance

        :param parent: parent widget
        """

        super(CountryPicker, self).__init__(parent)

        self.countries = countries.copy()

        for country_code, country_name in countries.items():
            self.addItem(
                QIcon(OSUtils.get_current_directory() + '/flags/' + country_code + '.png'),
                country_name
            )

    def getCurrentCountry(self) -> str:
        pass

    def setCurrentCountry(self):
        pass

    def getCountryName(self, country_code) -> str:
        pass

    def setCountryName(self, country_code: str, country_name: str):
        pass

    def setCountryNames(self, country_names: dict[str, str]):
        pass
