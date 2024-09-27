# PyQt Country Picker

[BADGES]

A simply, yet highly customizable country picker widget for PyQt and PySide

[GIF]


## Features
- Supports 235 countries and territories
- Supports only showing certain countries
- Fully customizable country names and flags
- Works with `PyQt5`, `PyQt6`, `PySide2`, and `PySide6`


## Installation
```
pip install pyqtcountrypicker
```


## Usage
Import the `CountryPicker` class and instantiate it like a normal widget:

```python
from PyQt6.QtWidgets import QMainWindow
from pyqtcountrypicker import CountryPicker


class Window(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)
        
        # Init country picker
        self.country_picker = CountryPicker(self)
```


To get and set the currently selected country, you can use the `getCurrentCountry()` and `setCurrentCountry()` methods:
```python
country_picker.setCurrentCountry('us')

selected_country = country_picker.getCurrentCountry()  # 'us'
```


To get notified when the selected country changes, you can subscribe to the `countryChanged` signal:
```python
country_picker.countryChanged.connect(lambda country_code: print('country changed to ' + country_code))
```


## Customization

* **Limiting the countries that can be selected:**
```python
eu_countries = [
    'at', 'be', 'bg', 'hr', 'cy', 'cz', 'dk', 'ee', 'fi',
    'fr', 'de', 'gr', 'hu', 'ie', 'it', 'lt', 'lu', 'lv',
    'mt', 'nl', 'pl', 'pt', 'ro', 'sk', 'si', 'es', 'se'
]

country_picker.setCountries(eu_countries)
```


* **Changing the country names:**
```python
# Setting a single country name
country_picker.setCountryName('af', 'Islamic Emirate of Afghanistan')

# Setting multiple country names at once
new_country_names = {
    'us': 'United States of America',
    'de': 'Federal Republic of Germany',
    'uk': 'England'
}
country_picker.setCountryNames(new_country_names)

# Resetting the country names
country_picker.resetCountryNames()
```


* **Changing the country flags:**

```python
# Setting a single flag
country_picker.setCountryFlag('af', QIcon('af_new_flag.png'))

# Setting multiple flags at once
new_country_flags = {
    'us': QIcon('us_alt.png'),
    'de': QIcon('de_alt.png'),
    'uk': QIcon('uk_alt.png')
}
country_picker.setCountryFlags(new_country_flags)

# Resetting the flags
country_picker.resetCountryFlags()
```


* **Enabling or disabling the country flags:**

```python
country_picker.setCountryFlagsEnabled(False)  # Default: True
```


## License
This software is licensed under the [MIT license](https://github.com/niklashenning/pyqtcountrypicker/blob/master/LICENSE).
