from PyQt6.QtGui import QIcon
from src.pyqtcountrypicker import CountryPicker
from src.pyqtcountrypicker.countries import countries


def test_initial_values(qtbot):
    """Test setting the initial values"""

    country_picker = CountryPicker()
    qtbot.addWidget(country_picker)

    assert country_picker.getCurrentCountry() == 'af'
    assert country_picker.getCountries() == list(countries.keys())
    assert country_picker.isCountryFlagsEnabled() == True
    assert country_picker.getCountryNames() == countries


def test_set_countries(qtbot):
    """Test setting the available countries"""

    country_picker = CountryPicker()
    qtbot.addWidget(country_picker)

    country_picker.setCountries(['de', 'us', 'ro', 'fr', 'bs', 'hu'])
    assert country_picker.getCountries() == ['de', 'us', 'ro', 'fr', 'bs', 'hu']
    assert country_picker.count() == 6


def test_set_current_country(qtbot):
    """Test setting the current country"""

    country_picker = CountryPicker()
    qtbot.addWidget(country_picker)

    country_picker.setCurrentCountry('de')
    assert country_picker.getCurrentCountry() == 'de'


def test_set_country_name(qtbot):
    """Test setting a country name"""

    country_picker = CountryPicker()
    qtbot.addWidget(country_picker)

    country_picker.setCountryName('de', 'Federal Republic of Germany')
    assert country_picker.getCountryName('de') == 'Federal Republic of Germany'


def test_set_country_names(qtbot):
    """Test setting multiple country names"""

    country_picker = CountryPicker()
    qtbot.addWidget(country_picker)

    new_country_names = {
        'de': 'Federal Republic of Germany',
        'gb': 'England'
    }

    country_picker.setCountryNames(new_country_names)
    country_names = country_picker.getCountryNames()
    assert country_names['de'] == 'Federal Republic of Germany'
    assert country_names['gb'] == 'England'


def test_reset_country_names(qtbot):
    """Test resetting the country names"""

    country_picker = CountryPicker()
    qtbot.addWidget(country_picker)

    new_country_names = {
        'de': 'Federal Republic of Germany',
        'gb': 'England'
    }

    country_picker.setCountryNames(new_country_names)
    country_picker.resetCountryNames()
    country_names = country_picker.getCountryNames()
    assert country_names['de'] == 'Germany'
    assert country_names['gb'] == 'United Kingdom'


def test_set_country_flag(qtbot):
    """Test setting a country flag"""

    country_picker = CountryPicker()
    qtbot.addWidget(country_picker)

    new_icon = QIcon()
    country_picker.setCountryFlag('de', new_icon)
    assert country_picker.getCountryFlag('de') == new_icon


def test_set_country_flags(qtbot):
    """Test setting multiple country flags"""

    country_picker = CountryPicker()
    qtbot.addWidget(country_picker)

    new_country_flags = {
        'de': QIcon(),
        'gb': QIcon()
    }

    country_picker.setCountryFlags(new_country_flags)
    country_flags = country_picker.getCountryFlags()
    assert country_flags['de'] == new_country_flags['de']
    assert country_flags['gb'] == new_country_flags['gb']


def test_reset_country_flags(qtbot):
    """Test resetting the country flags"""

    country_picker = CountryPicker()
    qtbot.addWidget(country_picker)

    new_country_flags = {
        'de': QIcon(),
        'gb': QIcon()
    }

    old_country_flags = country_picker.getCountryFlags().copy()
    country_picker.setCountryFlags(new_country_flags)
    country_picker.resetCountryFlags()
    country_flags = country_picker.getCountryFlags()
    assert country_flags['de'].pixmap(50, 50).toImage() == old_country_flags['de'].pixmap(50, 50).toImage()
    assert country_flags['gb'].pixmap(50, 50).toImage() == old_country_flags['gb'].pixmap(50, 50).toImage()


def test_set_country_flags_enabled(qtbot):
    """Test disabling the country flags"""

    country_picker = CountryPicker()
    qtbot.addWidget(country_picker)

    assert not country_picker.itemIcon(0).isNull()

    country_picker.setCountryFlagsEnabled(False)
    assert country_picker.itemIcon(0).isNull()


def test_invalid_country_codes(qtbot):
    """Test calling methods with invalid country codes as arguments"""

    country_picker = CountryPicker()
    qtbot.addWidget(country_picker)

    # Current country
    current_country = country_picker.getCurrentCountry()
    country_picker.setCurrentCountry('invalid')
    assert country_picker.getCurrentCountry() == current_country

    # Country names
    country_names = country_picker.getCountryNames()
    country_picker.setCountryName('invalid', 'country does not exist')
    country_picker.setCountryNames({'abcd': 'abcd'})
    assert country_names == country_picker.getCountryNames()
    assert country_picker.getCountryName('invalid') == ''

    # Country flags
    country_flags = country_picker.getCountryFlags()
    country_picker.setCountryFlag('invalid', QIcon())
    country_picker.setCountryFlags({'abcd': QIcon()})
    assert country_flags == country_picker.getCountryFlags()
    assert country_picker.getCountryFlag('invalid').isNull()
