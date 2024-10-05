# PyQt Country Picker

[![PyPI](https://img.shields.io/badge/pypi-v1.0.0-blue)](https://pypi.org/project/pyqtcountrypicker/)
[![Python](https://img.shields.io/badge/python-3.7+-blue)](https://github.com/niklashenning/pyqtcountrypicker)
[![Build](https://img.shields.io/badge/build-passing-neon)](https://github.com/niklashenning/pyqtcountrypicker)
[![Coverage](https://img.shields.io/badge/coverage-100%25-green)](https://github.com/niklashenning/pyqtcountrypicker)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/niklashenning/pyqtcountrypicker/blob/master/LICENSE)

A simply, yet highly customizable country picker widget for PyQt and PySide

![pyqtcountrypicker](https://github.com/user-attachments/assets/3d3ed4d4-c593-4f2a-a170-89715a3714e1)


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
        
        # Create country picker
        self.country_picker = CountryPicker(self)
```


To get and set the currently selected country, you can use the `getCurrentCountry()` and `setCurrentCountry()` methods:
```python
# Set current country
country_picker.setCurrentCountry('us')

# Get current country
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
    'gb': 'England'
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
    'gb': QIcon('gb_alt.png')
}
country_picker.setCountryFlags(new_country_flags)

# Resetting the flags
country_picker.resetCountryFlags()
```


* **Enabling or disabling the country flags:**

```python
country_picker.setCountryFlagsEnabled(False)  # Default: True
```


## Countries

| Country name                   | Country code | Country flag                                                                                                                   |
|--------------------------------|--------------|--------------------------------------------------------------------------------------------------------------------------------|
| Afghanistan                    | af           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/af.png" width="20px"> |
| Albania                        | al           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/al.png" width="20px"> |
| Algeria                        | dz           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/dz.png" width="20px"> |
| American Samoa                 | as           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/as.png" width="20px"> |
| Andorra                        | ad           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ad.png" width="20px"> |
| Angola                         | ao           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ao.png" width="20px"> |
| Anguilla                       | ai           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ai.png" width="20px"> |
| Antigua and Barbuda            | ag           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ag.png" width="20px"> |
| Argentina                      | ar           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ar.png" width="20px"> |
| Armenia                        | am           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/am.png" width="20px"> |
| Aruba                          | aw           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/aw.png" width="20px"> |
| Ascension Island               | sh-ac        | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/sh-ac.png" width="20px"> |
| Australia                      | au           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/au.png" width="20px"> |
| Austria                        | at           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/at.png" width="20px"> |
| Azerbaijan                     | az           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/az.png" width="20px"> |
| Bahamas                        | bs           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/bs.png" width="20px"> |
| Bahrain                        | bh           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/bh.png" width="20px"> |
| Bangladesh                     | bd           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/bd.png" width="20px"> |
| Barbados                       | bb           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/bb.png" width="20px"> |
| Belarus                        | by           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/by.png" width="20px"> |
| Belgium                        | be           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/be.png" width="20px"> |
| Belize                         | bz           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/bz.png" width="20px"> |
| Benin                          | bj           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/bj.png" width="20px"> |
| Bermuda                        | bm           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/bm.png" width="20px"> |
| Bhutan                         | bt           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/bt.png" width="20px"> |
| Bolivia                        | bo           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/bo.png" width="20px"> |
| Bosnia and Herzegovina         | ba           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ba.png" width="20px"> |
| Botswana                       | bw           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/bw.png" width="20px"> |
| Brazil                         | br           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/br.png" width="20px"> |
| British Indian Ocean Territory | io           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/io.png" width="20px"> |
| British Virgin Islands         | vg           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/vg.png" width="20px"> |
| Brunei                         | bn           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/bn.png" width="20px"> |
| Bulgaria                       | bg           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/bg.png" width="20px"> |
| Burkina Faso                   | bf           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/bf.png" width="20px"> |
| Burundi                        | bi           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/bi.png" width="20px"> |
| Cambodia                       | kh           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/kh.png" width="20px"> |
| Cameroon                       | cm           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/cm.png" width="20px"> |
| Canada                         | ca           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ca.png" width="20px"> |
| Cape Verde                     | cv           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/cv.png" width="20px"> |
| Caribbean Netherlands          | bq           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/bq.png" width="20px"> |
| Cayman Islands                 | ky           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ky.png" width="20px"> |
| Central African Republic       | cf           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/cf.png" width="20px"> |
| Chad                           | td           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/td.png" width="20px"> |
| Chile                          | cl           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/cl.png" width="20px"> |
| China                          | cn           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/cn.png" width="20px"> |
| Colombia                       | co           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/co.png" width="20px"> |
| Comoros                        | km           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/km.png" width="20px"> |
| Congo - Brazzaville            | cg           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/cg.png" width="20px"> |
| Congo - Kinshasa               | cd           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/cd.png" width="20px"> |
| Cook Islands                   | ck           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ck.png" width="20px"> |
| Costa Rica                     | cr           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/cr.png" width="20px"> |
| Côte d'Ivoire                  | ci           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ci.png" width="20px"> |
| Croatia                        | hr           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/hr.png" width="20px"> |
| Cuba                           | cu           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/cu.png" width="20px"> |
| Curaçao                        | cw           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/cw.png" width="20px"> |
| Cyprus                         | cy           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/cy.png" width="20px"> |
| Czechia                        | cz           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/cz.png" width="20px"> |
| Denmark                        | dk           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/dk.png" width="20px"> |
| Djibouti                       | dj           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/dj.png" width="20px"> |
| Dominica                       | dm           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/dm.png" width="20px"> |
| Dominican Republic             | do           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/do.png" width="20px"> |
| Ecuador                        | ec           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ec.png" width="20px"> |
| Egypt                          | eg           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/eg.png" width="20px"> |
| El Salvador                    | sv           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/sv.png" width="20px"> |
| Equatorial Guinea              | gq           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/gq.png" width="20px"> |
| Eritrea                        | er           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/er.png" width="20px"> |
| Estonia                        | ee           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ee.png" width="20px"> |
| Eswatini                       | sz           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/sz.png" width="20px"> |
| Ethiopia                       | et           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/et.png" width="20px"> |
| Falkland Islands               | fk           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/fk.png" width="20px"> |
| Faroe Islands                  | fo           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/fo.png" width="20px"> |
| Fiji                           | fj           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/fj.png" width="20px"> |
| Finland                        | fi           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/fi.png" width="20px"> |
| France                         | fr           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/fr.png" width="20px"> |
| French Guiana                  | gf           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/gf.png" width="20px"> |
| French Polynesia               | pf           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/pf.png" width="20px"> |
| Gabon                          | ga           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ga.png" width="20px"> |
| Gambia                         | gm           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/gm.png" width="20px"> |
| Georgia                        | ge           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ge.png" width="20px"> |
| Germany                        | de           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/de.png" width="20px"> |
| Ghana                          | gh           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/gh.png" width="20px"> |
| Gibraltar                      | gi           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/gi.png" width="20px"> |
| Greece                         | gr           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/gr.png" width="20px"> |
| Greenland                      | gl           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/gl.png" width="20px"> |
| Grenada                        | gd           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/gd.png" width="20px"> |
| Guadeloupe                     | gp           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/gp.png" width="20px"> |
| Guam                           | gu           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/gu.png" width="20px"> |
| Guatemala                      | gt           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/gt.png" width="20px"> |
| Guinea                         | gn           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/gn.png" width="20px"> |
| Guinea-Bissau                  | gw           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/gw.png" width="20px"> |
| Guyana                         | gy           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/gy.png" width="20px"> |
| Haiti                          | ht           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ht.png" width="20px"> |
| Honduras                       | hn           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/hn.png" width="20px"> |
| Hong Kong                      | hk           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/hk.png" width="20px"> |
| Hungary                        | hu           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/hu.png" width="20px"> |
| Iceland                        | is           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/is.png" width="20px"> |
| India                          | in           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/in.png" width="20px"> |
| Indonesia                      | id           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/id.png" width="20px"> |
| Iran                           | ir           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ir.png" width="20px"> |
| Iraq                           | iq           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/iq.png" width="20px"> |
| Ireland                        | ie           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ie.png" width="20px"> |
| Israel                         | il           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/il.png" width="20px"> |
| Italy                          | it           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/it.png" width="20px"> |
| Jamaica                        | jm           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/jm.png" width="20px"> |
| Japan                          | jp           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/jp.png" width="20px"> |
| Jordan                         | jo           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/jo.png" width="20px"> |
| Kazakhstan                     | kz           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/kz.png" width="20px"> |
| Kenya                          | ke           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ke.png" width="20px"> |
| Kiribati                       | ki           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ki.png" width="20px"> |
| Kosovo                         | xk           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/xk.png" width="20px"> |
| Kuwait                         | kw           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/kw.png" width="20px"> |
| Kyrgyzstan                     | kg           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/kg.png" width="20px"> |
| Laos                           | la           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/la.png" width="20px"> |
| Latvia                         | lv           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/lv.png" width="20px"> |
| Lebanon                        | lb           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/lb.png" width="20px"> |
| Lesotho                        | ls           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ls.png" width="20px"> |
| Liberia                        | lr           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/lr.png" width="20px"> |
| Libya                          | ly           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ly.png" width="20px"> |
| Liechtenstein                  | li           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/li.png" width="20px"> |
| Lithuania                      | lt           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/lt.png" width="20px"> |
| Luxembourg                     | lu           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/lu.png" width="20px"> |
| Macao                          | mo           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/mo.png" width="20px"> |
| Madagascar                     | mg           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/mg.png" width="20px"> |
| Malawi                         | mw           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/mw.png" width="20px"> |
| Malaysia                       | my           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/my.png" width="20px"> |
| Maldives                       | mv           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/mv.png" width="20px"> |
| Mali                           | ml           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ml.png" width="20px"> |
| Malta                          | mt           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/mt.png" width="20px"> |
| Marshall Islands               | mh           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/mh.png" width="20px"> |
| Martinique                     | mq           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/mq.png" width="20px"> |
| Mauritania                     | mr           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/mr.png" width="20px"> |
| Mauritius                      | mu           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/mu.png" width="20px"> |
| Mexico                         | mx           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/mx.png" width="20px"> |
| Micronesia                     | fm           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/fm.png" width="20px"> |
| Moldova                        | md           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/md.png" width="20px"> |
| Monaco                         | mc           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/mc.png" width="20px"> |
| Mongolia                       | mn           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/mn.png" width="20px"> |
| Montenegro                     | me           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/me.png" width="20px"> |
| Montserrat                     | ms           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ms.png" width="20px"> |
| Morocco                        | ma           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ma.png" width="20px"> |
| Mozambique                     | mz           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/mz.png" width="20px"> |
| Myanmar                        | mm           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/mm.png" width="20px"> |
| Namibia                        | na           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/na.png" width="20px"> |
| Nauru                          | nr           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/nr.png" width="20px"> |
| Nepal                          | np           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/np.png" width="20px"> |
| Netherlands                    | nl           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/nl.png" width="20px"> |
| New Caledonia                  | nc           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/nc.png" width="20px"> |
| New Zealand                    | nz           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/nz.png" width="20px"> |
| Nicaragua                      | ni           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ni.png" width="20px"> |
| Niger                          | ne           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ne.png" width="20px"> |
| Nigeria                        | ng           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ng.png" width="20px"> |
| Niue                           | nu           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/nu.png" width="20px"> |
| Norfolk Island                 | nf           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/nf.png" width="20px"> |
| North Korea                    | kp           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/kp.png" width="20px"> |
| North Macedonia                | mk           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/mk.png" width="20px"> |
| Northern Mariana Islands       | mp           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/mp.png" width="20px"> |
| Norway                         | no           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/no.png" width="20px"> |
| Oman                           | om           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/om.png" width="20px"> |
| Pakistan                       | pk           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/pk.png" width="20px"> |
| Palau                          | pw           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/pw.png" width="20px"> |
| Palestine                      | ps           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ps.png" width="20px"> |
| Panama                         | pa           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/pa.png" width="20px"> |
| Papua New Guinea               | pg           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/pg.png" width="20px"> |
| Paraguay                       | py           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/py.png" width="20px"> |
| Peru                           | pe           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/pe.png" width="20px"> |
| Philippines                    | ph           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ph.png" width="20px"> |
| Poland                         | pl           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/pl.png" width="20px"> |
| Portugal                       | pt           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/pt.png" width="20px"> |
| Puerto Rico                    | pr           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/pr.png" width="20px"> |
| Qatar                          | qa           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/qa.png" width="20px"> |
| Réunion                        | re           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/re.png" width="20px"> |
| Romania                        | ro           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ro.png" width="20px"> |
| Russia                         | ru           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ru.png" width="20px"> |
| Rwanda                         | rw           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/rw.png" width="20px"> |
| Samoa                          | ws           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ws.png" width="20px"> |
| San Marino                     | sm           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/sm.png" width="20px"> |
| São Tomé & Príncipe            | st           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/st.png" width="20px"> |
| Saudi Arabia                   | sa           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/sa.png" width="20px"> |
| Senegal                        | sn           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/sn.png" width="20px"> |
| Serbia                         | rs           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/rs.png" width="20px"> |
| Seychelles                     | sc           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/sc.png" width="20px"> |
| Sierra Leone                   | sl           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/sl.png" width="20px"> |
| Singapore                      | sg           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/sg.png" width="20px"> |
| Sint Maarten                   | sx           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/sx.png" width="20px"> |
| Slovakia                       | sk           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/sk.png" width="20px"> |
| Slovenia                       | si           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/si.png" width="20px"> |
| Solomon Islands                | sb           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/sb.png" width="20px"> |
| Somalia                        | so           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/so.png" width="20px"> |
| South Africa                   | za           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/za.png" width="20px"> |
| South Korea                    | kr           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/kr.png" width="20px"> |
| South Sudan                    | ss           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ss.png" width="20px"> |
| Spain                          | es           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/es.png" width="20px"> |
| Sri Lanka                      | lk           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/lk.png" width="20px"> |
| St. Barthélemy                 | bl           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/bl.png" width="20px"> |
| St. Helena                     | sh-hl        | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/sh-hl.png" width="20px"> |
| St. Kitts & Nevis              | kn           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/kn.png" width="20px"> |
| St. Lucia                      | lc           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/lc.png" width="20px"> |
| St. Martin                     | mf           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/mf.png" width="20px"> |
| St. Pierre & Miquelon          | pm           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/pm.png" width="20px"> |
| St. Vincent & Grenadines       | vc           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/vc.png" width="20px"> |
| Sudan                          | sd           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/sd.png" width="20px"> |
| Suriname                       | sr           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/sr.png" width="20px"> |
| Sweden                         | se           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/se.png" width="20px"> |
| Switzerland                    | ch           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ch.png" width="20px"> |
| Syria                          | sy           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/sy.png" width="20px"> |
| Taiwan                         | tw           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/tw.png" width="20px"> |
| Tajikistan                     | tj           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/tj.png" width="20px"> |
| Tanzania                       | tz           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/tz.png" width="20px"> |
| Thailand                       | th           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/th.png" width="20px"> |
| Timor-Leste                    | tl           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/tl.png" width="20px"> |
| Togo                           | tg           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/tg.png" width="20px"> |
| Tokelau                        | tk           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/tk.png" width="20px"> |
| Tonga                          | to           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/to.png" width="20px"> |
| Trinidad & Tobago              | tt           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/tt.png" width="20px"> |
| Tunisia                        | tn           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/tn.png" width="20px"> |
| Türkiye                        | tr           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/tr.png" width="20px"> |
| Turkmenistan                   | tm           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/tm.png" width="20px"> |
| Turks & Caicos Islands         | tc           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/tc.png" width="20px"> |
| Tuvalu                         | tv           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/tv.png" width="20px"> |
| U.S. Virgin Islands            | vi           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/vi.png" width="20px"> |
| Uganda                         | ug           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ug.png" width="20px"> |
| Ukraine                        | ua           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ua.png" width="20px"> |
| United Arab Emirates           | ae           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ae.png" width="20px"> |
| United Kingdom                 | gb           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/gb.png" width="20px"> |
| United States                  | us           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/us.png" width="20px"> |
| Uruguay                        | uy           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/uy.png" width="20px"> |
| Uzbekistan                     | uz           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/uz.png" width="20px"> |
| Vanuatu                        | vu           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/vu.png" width="20px"> |
| Vatican City                   | va           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/va.png" width="20px"> |
| Venezuela                      | ve           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ve.png" width="20px"> |
| Vietnam                        | vn           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/vn.png" width="20px"> |
| Wallis & Futuna                | wf           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/wf.png" width="20px"> |
| Yemen                          | ye           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/ye.png" width="20px"> |
| Zambia                         | zm           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/zm.png" width="20px"> |
| Zimbabwe                       | zw           | <img src="https://raw.githubusercontent.com/niklashenning/pyqtcountrypicker/refs/heads/master/src/pyqtcountrypicker/flags/zw.png" width="20px"> |

The flag icons used are modified versions of the icons available in [this repository](https://github.com/lipis/flag-icons).


## License
This software is licensed under the [MIT license](https://github.com/niklashenning/pyqtcountrypicker/blob/master/LICENSE).
