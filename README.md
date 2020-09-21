## Chandas

[![Build Status](https://travis-ci.org/sanskrit-coders/chandas.svg?branch=master)](https://travis-ci.org/sanskrit-coders/chandas)
[![Documentation Status](https://readthedocs.org/projects/chandas/badge/?version=latest)](http://chandas.readthedocs.io/en/latest/?badge=latest)
[![Actions Status](https://github.com/sanskrit-coders/chandas/workflows/Python%20package/badge.svg)](https://github.com/sanskrit-coders/chandas/actions)
[![PyPI version](https://badge.fury.io/py/chandas.svg)](https://badge.fury.io/py/chandas)

### Intro
This is a python package for Indic language (mostly sanskrit) metre identification and related tasks like syllabization. This module expects devanAgarI input, and currently produces IAST output.

## For users
* [Autogenerated Docs on readthedocs (might be broken)](http://chandas.readthedocs.io/en/latest/).
* Manually and periodically generated docs [here](https://sanskrit-coders.github.io/chandas/build/html/)
* For detailed examples and help, please see individual module files in this package.

### Installation or upgrade:
* `sudo pip install chandas -U`
* `sudo pip install git+https://github.com/sanskrit-coders/chandas/@master -U`
* [Web](https://pypi.python.org/pypi/chandas).


### Usage
For more examples, see tests.

#### Metre Identification
```
from chandas import identify
pattern_lines = identify.to_pattern_lines("निर्दिष्टाङ् कुलपतिना स पर्णशालाम् अध्यास्य प्रयतपरिग्रहद्वितीयः ।\nतच्छिष्याध्ययननिवेदितावसानां सव्ँविष्टः कुशशयने निशान् निनाय ॥".split("\n"))
id_result = identify.identifier.IdentifyFromPatternLines(pattern_lines)
assert id_result['exact'] == "Praharṣiṇī"
```

#### Syllabization
```
from chandas import syllabize
syllabize.get_syllables(u"ॐ मणि पद्मे ऽहम्") == "ओम् म णि पद् मे हम्"
syllabize.get_graphemes(u"बिक्रममेरोनामहो") == "बि क् र म मे रो ना म हो".split(" ")
```

### Shared test data
Please feel free to use test data published here to test your own modules:
- [syllabizationTests.json](https://github.com/sanskrit-coders/chandas/blob/master/src/test/data/syllabizationTests.json)

## For external collaborators
- We copy the data and identification code from [shreevatsa's repo](https://github.com/shreevatsa/sanskrit/). This code has been transformed a bit to conform to PEP conventions. 
- You may be interested in sharing and contributing to a common pool of test cases - see the chandas-id and syllabization tests under https://github.com/sanskrit-coders/chandas/tree/master/tests/data .

## For contributors
### Contact

Have a problem or question? Please head to [github](https://github.com/sanskrit-coders/chandas).

### Packaging

* ~/.pypirc should have your pypi login credentials.
```
python setup.py bdist_wheel
twine upload dist/* --skip-existing
```

### Build documentation
- sphinx html docs can be generated with `cd docs; make html`

### Testing
Run `pytest` in the root directory.

### Auxiliary tools
- [![Build Status](https://travis-ci.org/sanskrit-coders/chandas.svg?branch=master)](https://travis-ci.org/sanskrit-coders/chandas)
- [![Documentation Status](https://readthedocs.org/projects/indic-transliteration/badge/?version=latest)](http://indic-transliteration.readthedocs.io/en/latest/?badge=latest)
- [pyup](https://pyup.io/account/repos/github/sanskrit-coders/chandas/)

