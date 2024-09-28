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


## Countries

| Country name                   | Country code | Country flag                                                   |
|--------------------------------|--------------|----------------------------------------------------------------|
| Afghanistan                    | af           | <img src="src/pyqtcountrypicker/flags/af.png" width="20px">    |
| Albania                        | al           | <img src="src/pyqtcountrypicker/flags/al.png" width="20px">    |
| Algeria                        | dz           | <img src="src/pyqtcountrypicker/flags/dz.png" width="20px">    |
| American Samoa                 | as           | <img src="src/pyqtcountrypicker/flags/as.png" width="20px">    |
| Andorra                        | ad           | <img src="src/pyqtcountrypicker/flags/ad.png" width="20px">    |
| Angola                         | ao           | <img src="src/pyqtcountrypicker/flags/ao.png" width="20px">    |
| Anguilla                       | ai           | <img src="src/pyqtcountrypicker/flags/ai.png" width="20px">    |
| Antigua and Barbuda            | ag           | <img src="src/pyqtcountrypicker/flags/ag.png" width="20px">    |
| Argentina                      | ar           | <img src="src/pyqtcountrypicker/flags/ar.png" width="20px">    |
| Armenia                        | am           | <img src="src/pyqtcountrypicker/flags/am.png" width="20px">    |
| Aruba                          | aw           | <img src="src/pyqtcountrypicker/flags/aw.png" width="20px">    |
| Ascension Island               | sh-ac        | <img src="src/pyqtcountrypicker/flags/sh-ac.png" width="20px"> |
| Australia                      | au           | <img src="src/pyqtcountrypicker/flags/au.png" width="20px">    |
| Austria                        | at           | <img src="src/pyqtcountrypicker/flags/at.png" width="20px">    |
| Azerbaijan                     | az           | <img src="src/pyqtcountrypicker/flags/az.png" width="20px">    |
| Bahamas                        | bs           | <img src="src/pyqtcountrypicker/flags/bs.png" width="20px">    |
| Bahrain                        | bh           | <img src="src/pyqtcountrypicker/flags/bh.png" width="20px">    |
| Bangladesh                     | bd           | <img src="src/pyqtcountrypicker/flags/bd.png" width="20px">    |
| Barbados                       | bb           | <img src="src/pyqtcountrypicker/flags/bb.png" width="20px">    |
| Belarus                        | by           | <img src="src/pyqtcountrypicker/flags/by.png" width="20px">    |
| Belgium                        | be           | <img src="src/pyqtcountrypicker/flags/be.png" width="20px">    |
| Belize                         | bz           | <img src="src/pyqtcountrypicker/flags/bz.png" width="20px">    |
| Benin                          | bj           | <img src="src/pyqtcountrypicker/flags/bj.png" width="20px">    |
| Bermuda                        | bm           | <img src="src/pyqtcountrypicker/flags/bm.png" width="20px">    |
| Bhutan                         | bt           | <img src="src/pyqtcountrypicker/flags/bt.png" width="20px">    |
| Bolivia                        | bo           | <img src="src/pyqtcountrypicker/flags/bo.png" width="20px">    |
| Bosnia and Herzegovina         | ba           | <img src="src/pyqtcountrypicker/flags/ba.png" width="20px">    |
| Botswana                       | bw           | <img src="src/pyqtcountrypicker/flags/bw.png" width="20px">    |
| Brazil                         | br           | <img src="src/pyqtcountrypicker/flags/br.png" width="20px">    |
| British Indian Ocean Territory | io           | <img src="src/pyqtcountrypicker/flags/io.png" width="20px">    |
| British Virgin Islands         | vg           | <img src="src/pyqtcountrypicker/flags/vg.png" width="20px">    |
| Brunei                         | bn           | <img src="src/pyqtcountrypicker/flags/bn.png" width="20px">    |
| Bulgaria                       | bg           | <img src="src/pyqtcountrypicker/flags/bg.png" width="20px">    |
| Burkina Faso                   | bf           | <img src="src/pyqtcountrypicker/flags/bf.png" width="20px">    |
| Burundi                        | bi           | <img src="src/pyqtcountrypicker/flags/bi.png" width="20px">    |
| Cambodia                       | kh           | <img src="src/pyqtcountrypicker/flags/kh.png" width="20px">    |
| Cameroon                       | cm           | <img src="src/pyqtcountrypicker/flags/cm.png" width="20px">    |
| Canada                         | ca           | <img src="src/pyqtcountrypicker/flags/ca.png" width="20px">    |
| Cape Verde                     | cv           | <img src="src/pyqtcountrypicker/flags/cv.png" width="20px">    |
| Caribbean Netherlands          | bq           | <img src="src/pyqtcountrypicker/flags/bq.png" width="20px">    |
| Cayman Islands                 | ky           | <img src="src/pyqtcountrypicker/flags/ky.png" width="20px">    |
| Central African Republic       | cf           | <img src="src/pyqtcountrypicker/flags/cf.png" width="20px">    |
| Chad                           | td           | <img src="src/pyqtcountrypicker/flags/td.png" width="20px">    |
| Chile                          | cl           | <img src="src/pyqtcountrypicker/flags/cl.png" width="20px">    |
| China                          | cn           | <img src="src/pyqtcountrypicker/flags/cn.png" width="20px">    |
| Colombia                       | co           | <img src="src/pyqtcountrypicker/flags/co.png" width="20px">    |
| Comoros                        | km           | <img src="src/pyqtcountrypicker/flags/km.png" width="20px">    |
| Congo - Brazzaville            | cg           | <img src="src/pyqtcountrypicker/flags/cg.png" width="20px">    |
| Congo - Kinshasa               | cd           | <img src="src/pyqtcountrypicker/flags/cd.png" width="20px">    |
| Cook Islands                   | ck           | <img src="src/pyqtcountrypicker/flags/ck.png" width="20px">    |
| Costa Rica                     | cr           | <img src="src/pyqtcountrypicker/flags/cr.png" width="20px">    |
| Côte d'Ivoire                  | ci           | <img src="src/pyqtcountrypicker/flags/ci.png" width="20px">    |
| Croatia                        | hr           | <img src="src/pyqtcountrypicker/flags/hr.png" width="20px">    |
| Cuba                           | cu           | <img src="src/pyqtcountrypicker/flags/cu.png" width="20px">    |
| Curaçao                        | cw           | <img src="src/pyqtcountrypicker/flags/cw.png" width="20px">    |
| Cyprus                         | cy           | <img src="src/pyqtcountrypicker/flags/cy.png" width="20px">    |
| Czechia                        | cz           | <img src="src/pyqtcountrypicker/flags/cz.png" width="20px">    |
| Denmark                        | dk           | <img src="src/pyqtcountrypicker/flags/dk.png" width="20px">    |
| Djibouti                       | dj           | <img src="src/pyqtcountrypicker/flags/dj.png" width="20px">    |
| Dominica                       | dm           | <img src="src/pyqtcountrypicker/flags/dm.png" width="20px">    |
| Dominican Republic             | do           | <img src="src/pyqtcountrypicker/flags/do.png" width="20px">    |
| Ecuador                        | ec           | <img src="src/pyqtcountrypicker/flags/ec.png" width="20px">    |
| Egypt                          | eg           | <img src="src/pyqtcountrypicker/flags/eg.png" width="20px">    |
| El Salvador                    | sv           | <img src="src/pyqtcountrypicker/flags/sv.png" width="20px">    |
| Equatorial Guinea              | gq           | <img src="src/pyqtcountrypicker/flags/gq.png" width="20px">    |
| Eritrea                        | er           | <img src="src/pyqtcountrypicker/flags/er.png" width="20px">    |
| Estonia                        | ee           | <img src="src/pyqtcountrypicker/flags/ee.png" width="20px">    |
| Eswatini                       | sz           | <img src="src/pyqtcountrypicker/flags/sz.png" width="20px">    |
| Ethiopia                       | et           | <img src="src/pyqtcountrypicker/flags/et.png" width="20px">    |
| Falkland Islands               | fk           | <img src="src/pyqtcountrypicker/flags/fk.png" width="20px">    |
| Faroe Islands                  | fo           | <img src="src/pyqtcountrypicker/flags/fo.png" width="20px">    |
| Fiji                           | fj           | <img src="src/pyqtcountrypicker/flags/fj.png" width="20px">    |
| Finland                        | fi           | <img src="src/pyqtcountrypicker/flags/fi.png" width="20px">    |
| France                         | fr           | <img src="src/pyqtcountrypicker/flags/fr.png" width="20px">    |
| French Guiana                  | gf           | <img src="src/pyqtcountrypicker/flags/gf.png" width="20px">    |
| French Polynesia               | pf           | <img src="src/pyqtcountrypicker/flags/pf.png" width="20px">    |
| Gabon                          | ga           | <img src="src/pyqtcountrypicker/flags/ga.png" width="20px">    |
| Gambia                         | gm           | <img src="src/pyqtcountrypicker/flags/gm.png" width="20px">    |
| Georgia                        | ge           | <img src="src/pyqtcountrypicker/flags/ge.png" width="20px">    |
| Germany                        | de           | <img src="src/pyqtcountrypicker/flags/de.png" width="20px">    |
| Ghana                          | gh           | <img src="src/pyqtcountrypicker/flags/gh.png" width="20px">    |
| Gibraltar                      | gi           | <img src="src/pyqtcountrypicker/flags/gi.png" width="20px">    |
| Greece                         | gr           | <img src="src/pyqtcountrypicker/flags/gr.png" width="20px">    |
| Greenland                      | gl           | <img src="src/pyqtcountrypicker/flags/gl.png" width="20px">    |
| Grenada                        | gd           | <img src="src/pyqtcountrypicker/flags/gd.png" width="20px">    |
| Guadeloupe                     | gp           | <img src="src/pyqtcountrypicker/flags/gp.png" width="20px">    |
| Guam                           | gu           | <img src="src/pyqtcountrypicker/flags/gu.png" width="20px">    |
| Guatemala                      | gt           | <img src="src/pyqtcountrypicker/flags/gt.png" width="20px">    |
| Guinea                         | gn           | <img src="src/pyqtcountrypicker/flags/gn.png" width="20px">    |
| Guinea-Bissau                  | gw           | <img src="src/pyqtcountrypicker/flags/gw.png" width="20px">    |
| Guyana                         | gy           | <img src="src/pyqtcountrypicker/flags/gy.png" width="20px">    |
| Haiti                          | ht           | <img src="src/pyqtcountrypicker/flags/ht.png" width="20px">    |
| Honduras                       | hn           | <img src="src/pyqtcountrypicker/flags/hn.png" width="20px">    |
| Hong Kong                      | hk           | <img src="src/pyqtcountrypicker/flags/hk.png" width="20px">    |
| Hungary                        | hu           | <img src="src/pyqtcountrypicker/flags/hu.png" width="20px">    |
| Iceland                        | is           | <img src="src/pyqtcountrypicker/flags/is.png" width="20px">    |
| India                          | in           | <img src="src/pyqtcountrypicker/flags/in.png" width="20px">    |
| Indonesia                      | id           | <img src="src/pyqtcountrypicker/flags/id.png" width="20px">    |
| Iran                           | ir           | <img src="src/pyqtcountrypicker/flags/ir.png" width="20px">    |
| Iraq                           | iq           | <img src="src/pyqtcountrypicker/flags/iq.png" width="20px">    |
| Ireland                        | ie           | <img src="src/pyqtcountrypicker/flags/ie.png" width="20px">    |
| Israel                         | il           | <img src="src/pyqtcountrypicker/flags/il.png" width="20px">    |
| Italy                          | it           | <img src="src/pyqtcountrypicker/flags/it.png" width="20px">    |
| Jamaica                        | jm           | <img src="src/pyqtcountrypicker/flags/jm.png" width="20px">    |
| Japan                          | jp           | <img src="src/pyqtcountrypicker/flags/jp.png" width="20px">    |
| Jordan                         | jo           | <img src="src/pyqtcountrypicker/flags/jo.png" width="20px">    |
| Kazakhstan                     | kz           | <img src="src/pyqtcountrypicker/flags/kz.png" width="20px">    |
| Kenya                          | ke           | <img src="src/pyqtcountrypicker/flags/ke.png" width="20px">    |
| Kiribati                       | ki           | <img src="src/pyqtcountrypicker/flags/ki.png" width="20px">    |
| Kosovo                         | xk           | <img src="src/pyqtcountrypicker/flags/xk.png" width="20px">    |
| Kuwait                         | kw           | <img src="src/pyqtcountrypicker/flags/kw.png" width="20px">    |
| Kyrgyzstan                     | kg           | <img src="src/pyqtcountrypicker/flags/kg.png" width="20px">    |
| Laos                           | la           | <img src="src/pyqtcountrypicker/flags/la.png" width="20px">    |
| Latvia                         | lv           | <img src="src/pyqtcountrypicker/flags/lv.png" width="20px">    |
| Lebanon                        | lb           | <img src="src/pyqtcountrypicker/flags/lb.png" width="20px">    |
| Lesotho                        | ls           | <img src="src/pyqtcountrypicker/flags/ls.png" width="20px">    |
| Liberia                        | lr           | <img src="src/pyqtcountrypicker/flags/lr.png" width="20px">    |
| Libya                          | ly           | <img src="src/pyqtcountrypicker/flags/ly.png" width="20px">    |
| Liechtenstein                  | li           | <img src="src/pyqtcountrypicker/flags/li.png" width="20px">    |
| Lithuania                      | lt           | <img src="src/pyqtcountrypicker/flags/lt.png" width="20px">    |
| Luxembourg                     | lu           | <img src="src/pyqtcountrypicker/flags/lu.png" width="20px">    |
| Macao                          | mo           | <img src="src/pyqtcountrypicker/flags/mo.png" width="20px">    |
| Madagascar                     | mg           | <img src="src/pyqtcountrypicker/flags/mg.png" width="20px">    |
| Malawi                         | mw           | <img src="src/pyqtcountrypicker/flags/mw.png" width="20px">    |
| Malaysia                       | my           | <img src="src/pyqtcountrypicker/flags/my.png" width="20px">    |
| Maldives                       | mv           | <img src="src/pyqtcountrypicker/flags/mv.png" width="20px">    |
| Mali                           | ml           | <img src="src/pyqtcountrypicker/flags/ml.png" width="20px">    |
| Malta                          | mt           | <img src="src/pyqtcountrypicker/flags/mt.png" width="20px">    |
| Marshall Islands               | mh           | <img src="src/pyqtcountrypicker/flags/mh.png" width="20px">    |
| Martinique                     | mq           | <img src="src/pyqtcountrypicker/flags/mq.png" width="20px">    |
| Mauritania                     | mr           | <img src="src/pyqtcountrypicker/flags/mr.png" width="20px">    |
| Mauritius                      | mu           | <img src="src/pyqtcountrypicker/flags/mu.png" width="20px">    |
| Mexico                         | mx           | <img src="src/pyqtcountrypicker/flags/mx.png" width="20px">    |
| Micronesia                     | fm           | <img src="src/pyqtcountrypicker/flags/fm.png" width="20px">    |
| Moldova                        | md           | <img src="src/pyqtcountrypicker/flags/md.png" width="20px">    |
| Monaco                         | mc           | <img src="src/pyqtcountrypicker/flags/mc.png" width="20px">    |
| Mongolia                       | mn           | <img src="src/pyqtcountrypicker/flags/mn.png" width="20px">    |
| Montenegro                     | me           | <img src="src/pyqtcountrypicker/flags/me.png" width="20px">    |
| Montserrat                     | ms           | <img src="src/pyqtcountrypicker/flags/ms.png" width="20px">    |
| Morocco                        | ma           | <img src="src/pyqtcountrypicker/flags/ma.png" width="20px">    |
| Mozambique                     | mz           | <img src="src/pyqtcountrypicker/flags/mz.png" width="20px">    |
| Myanmar                        | mm           | <img src="src/pyqtcountrypicker/flags/mm.png" width="20px">    |
| Namibia                        | na           | <img src="src/pyqtcountrypicker/flags/na.png" width="20px">    |
| Nauru                          | nr           | <img src="src/pyqtcountrypicker/flags/nr.png" width="20px">    |
| Nepal                          | np           | <img src="src/pyqtcountrypicker/flags/np.png" width="20px">    |
| Netherlands                    | nl           | <img src="src/pyqtcountrypicker/flags/nl.png" width="20px">    |
| New Caledonia                  | nc           | <img src="src/pyqtcountrypicker/flags/nc.png" width="20px">    |
| New Zealand                    | nz           | <img src="src/pyqtcountrypicker/flags/nz.png" width="20px">    |
| Nicaragua                      | ni           | <img src="src/pyqtcountrypicker/flags/ni.png" width="20px">    |
| Niger                          | ne           | <img src="src/pyqtcountrypicker/flags/ne.png" width="20px">    |
| Nigeria                        | ng           | <img src="src/pyqtcountrypicker/flags/ng.png" width="20px">    |
| Niue                           | nu           | <img src="src/pyqtcountrypicker/flags/nu.png" width="20px">    |
| Norfolk Island                 | nf           | <img src="src/pyqtcountrypicker/flags/nf.png" width="20px">    |
| North Korea                    | kp           | <img src="src/pyqtcountrypicker/flags/kp.png" width="20px">    |
| North Macedonia                | mk           | <img src="src/pyqtcountrypicker/flags/mk.png" width="20px">    |
| Northern Mariana Islands       | mp           | <img src="src/pyqtcountrypicker/flags/mp.png" width="20px">    |
| Norway                         | no           | <img src="src/pyqtcountrypicker/flags/no.png" width="20px">    |
| Oman                           | om           | <img src="src/pyqtcountrypicker/flags/om.png" width="20px">    |
| Pakistan                       | pk           | <img src="src/pyqtcountrypicker/flags/pk.png" width="20px">    |
| Palau                          | pw           | <img src="src/pyqtcountrypicker/flags/pw.png" width="20px">    |
| Palestine                      | ps           | <img src="src/pyqtcountrypicker/flags/ps.png" width="20px">    |
| Panama                         | pa           | <img src="src/pyqtcountrypicker/flags/pa.png" width="20px">    |
| Papua New Guinea               | pg           | <img src="src/pyqtcountrypicker/flags/pg.png" width="20px">    |
| Paraguay                       | py           | <img src="src/pyqtcountrypicker/flags/py.png" width="20px">    |
| Peru                           | pe           | <img src="src/pyqtcountrypicker/flags/pe.png" width="20px">    |
| Philippines                    | ph           | <img src="src/pyqtcountrypicker/flags/ph.png" width="20px">    |
| Poland                         | pl           | <img src="src/pyqtcountrypicker/flags/pl.png" width="20px">    |
| Portugal                       | pt           | <img src="src/pyqtcountrypicker/flags/pt.png" width="20px">    |
| Puerto Rico                    | pr           | <img src="src/pyqtcountrypicker/flags/pr.png" width="20px">    |
| Qatar                          | qa           | <img src="src/pyqtcountrypicker/flags/qa.png" width="20px">    |
| Réunion                        | re           | <img src="src/pyqtcountrypicker/flags/re.png" width="20px">    |
| Romania                        | ro           | <img src="src/pyqtcountrypicker/flags/ro.png" width="20px">    |
| Russia                         | ru           | <img src="src/pyqtcountrypicker/flags/ru.png" width="20px">    |
| Rwanda                         | rw           | <img src="src/pyqtcountrypicker/flags/rw.png" width="20px">    |
| Samoa                          | ws           | <img src="src/pyqtcountrypicker/flags/ws.png" width="20px">    |
| San Marino                     | sm           | <img src="src/pyqtcountrypicker/flags/sm.png" width="20px">    |
| São Tomé & Príncipe            | st           | <img src="src/pyqtcountrypicker/flags/st.png" width="20px">    |
| Saudi Arabia                   | sa           | <img src="src/pyqtcountrypicker/flags/sa.png" width="20px">    |
| Senegal                        | sn           | <img src="src/pyqtcountrypicker/flags/sn.png" width="20px">    |
| Serbia                         | rs           | <img src="src/pyqtcountrypicker/flags/rs.png" width="20px">    |
| Seychelles                     | sc           | <img src="src/pyqtcountrypicker/flags/sc.png" width="20px">    |
| Sierra Leone                   | sl           | <img src="src/pyqtcountrypicker/flags/sl.png" width="20px">    |
| Singapore                      | sg           | <img src="src/pyqtcountrypicker/flags/sg.png" width="20px">    |
| Sint Maarten                   | sx           | <img src="src/pyqtcountrypicker/flags/sx.png" width="20px">    |
| Slovakia                       | sk           | <img src="src/pyqtcountrypicker/flags/sk.png" width="20px">    |
| Slovenia                       | si           | <img src="src/pyqtcountrypicker/flags/si.png" width="20px">    |
| Solomon Islands                | sb           | <img src="src/pyqtcountrypicker/flags/sb.png" width="20px">    |
| Somalia                        | so           | <img src="src/pyqtcountrypicker/flags/so.png" width="20px">    |
| South Africa                   | za           | <img src="src/pyqtcountrypicker/flags/za.png" width="20px">    |
| South Korea                    | kr           | <img src="src/pyqtcountrypicker/flags/kr.png" width="20px">    |
| South Sudan                    | ss           | <img src="src/pyqtcountrypicker/flags/ss.png" width="20px">    |
| Spain                          | es           | <img src="src/pyqtcountrypicker/flags/es.png" width="20px">    |
| Sri Lanka                      | lk           | <img src="src/pyqtcountrypicker/flags/lk.png" width="20px">    |
| St. Barthélemy                 | bl           | <img src="src/pyqtcountrypicker/flags/bl.png" width="20px">    |
| St. Helena                     | sh-hl        | <img src="src/pyqtcountrypicker/flags/sh-hl.png" width="20px"> |
| St. Kitts & Nevis              | kn           | <img src="src/pyqtcountrypicker/flags/kn.png" width="20px">    |
| St. Lucia                      | lc           | <img src="src/pyqtcountrypicker/flags/lc.png" width="20px">    |
| St. Martin                     | mf           | <img src="src/pyqtcountrypicker/flags/mf.png" width="20px">    |
| St. Pierre & Miquelon          | pm           | <img src="src/pyqtcountrypicker/flags/pm.png" width="20px">    |
| St. Vincent & Grenadines       | vc           | <img src="src/pyqtcountrypicker/flags/vc.png" width="20px">    |
| Sudan                          | sd           | <img src="src/pyqtcountrypicker/flags/sd.png" width="20px">    |
| Suriname                       | sr           | <img src="src/pyqtcountrypicker/flags/sr.png" width="20px">    |
| Sweden                         | se           | <img src="src/pyqtcountrypicker/flags/se.png" width="20px">    |
| Switzerland                    | ch           | <img src="src/pyqtcountrypicker/flags/ch.png" width="20px">    |
| Syria                          | sy           | <img src="src/pyqtcountrypicker/flags/sy.png" width="20px">    |
| Taiwan                         | tw           | <img src="src/pyqtcountrypicker/flags/tw.png" width="20px">    |
| Tajikistan                     | tj           | <img src="src/pyqtcountrypicker/flags/tj.png" width="20px">    |
| Tanzania                       | tz           | <img src="src/pyqtcountrypicker/flags/tz.png" width="20px">    |
| Thailand                       | th           | <img src="src/pyqtcountrypicker/flags/th.png" width="20px">    |
| Timor-Leste                    | tl           | <img src="src/pyqtcountrypicker/flags/tl.png" width="20px">    |
| Togo                           | tg           | <img src="src/pyqtcountrypicker/flags/tg.png" width="20px">    |
| Tokelau                        | tk           | <img src="src/pyqtcountrypicker/flags/tk.png" width="20px">    |
| Tonga                          | to           | <img src="src/pyqtcountrypicker/flags/to.png" width="20px">    |
| Trinidad & Tobago              | tt           | <img src="src/pyqtcountrypicker/flags/tt.png" width="20px">    |
| Tunisia                        | tn           | <img src="src/pyqtcountrypicker/flags/tn.png" width="20px">    |
| Türkiye                        | tr           | <img src="src/pyqtcountrypicker/flags/tr.png" width="20px">    |
| Turkmenistan                   | tm           | <img src="src/pyqtcountrypicker/flags/tm.png" width="20px">    |
| Turks & Caicos Islands         | tc           | <img src="src/pyqtcountrypicker/flags/tc.png" width="20px">    |
| Tuvalu                         | tv           | <img src="src/pyqtcountrypicker/flags/tv.png" width="20px">    |
| U.S. Virgin Islands            | vi           | <img src="src/pyqtcountrypicker/flags/vi.png" width="20px">    |
| Uganda                         | ug           | <img src="src/pyqtcountrypicker/flags/ug.png" width="20px">    |
| Ukraine                        | ua           | <img src="src/pyqtcountrypicker/flags/ua.png" width="20px">    |
| United Arab Emirates           | ae           | <img src="src/pyqtcountrypicker/flags/ae.png" width="20px">    |
| United Kingdom                 | gb           | <img src="src/pyqtcountrypicker/flags/gb.png" width="20px">    |
| United States                  | us           | <img src="src/pyqtcountrypicker/flags/us.png" width="20px">    |
| Uruguay                        | uy           | <img src="src/pyqtcountrypicker/flags/uy.png" width="20px">    |
| Uzbekistan                     | uz           | <img src="src/pyqtcountrypicker/flags/uz.png" width="20px">    |
| Vanuatu                        | vu           | <img src="src/pyqtcountrypicker/flags/vu.png" width="20px">    |
| Vatican City                   | va           | <img src="src/pyqtcountrypicker/flags/va.png" width="20px">    |
| Venezuela                      | ve           | <img src="src/pyqtcountrypicker/flags/ve.png" width="20px">    |
| Vietnam                        | vn           | <img src="src/pyqtcountrypicker/flags/vn.png" width="20px">    |
| Wallis & Futuna                | wf           | <img src="src/pyqtcountrypicker/flags/wf.png" width="20px">    |
| Yemen                          | ye           | <img src="src/pyqtcountrypicker/flags/ye.png" width="20px">    |
| Zambia                         | zm           | <img src="src/pyqtcountrypicker/flags/zm.png" width="20px">    |
| Zimbabwe                       | zw           | <img src="src/pyqtcountrypicker/flags/zw.png" width="20px">    |


## License
This software is licensed under the [MIT license](https://github.com/niklashenning/pyqtcountrypicker/blob/master/LICENSE).
