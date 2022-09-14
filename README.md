### Hexlet tests and linter status:
[![Actions Status](https://github.com/dmitriy-ga/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/dmitriy-ga/python-project-lvl2/actions)
[![CI](https://github.com/dmitriy-ga/python-project-lvl2/actions/workflows/CI.yml/badge.svg)](https://github.com/dmitriy-ga/python-project-lvl2/actions/workflows/CI.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/85027d0cb2f13901b6ff/maintainability)](https://codeclimate.com/github/dmitriy-ga/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/85027d0cb2f13901b6ff/test_coverage)](https://codeclimate.com/github/dmitriy-ga/python-project-lvl2/test_coverage)

### Description
Difference Generator (gendiff) - CLI-tool for comparing two configuration files. Accepts json and yaml files in any combination.
Implemented formatting output styles:

| Style   | Description                 |
|---------|-----------------------------|
| stylish | Line by line view (default) |
| plain   | Human-readable changelog    |
| json    | Standard json output        |
 
### Minimum requirements
- Python (3.10 or newer)
- PyYAML (6.0 or newer)

### Additional dev-dependencies
- flake8 (5.0.4 or newer)
- pytest (7.1.2 or newer)
- pytest-cov (3.0.0 or newer)

### Installing (from source)
1. In terminal navigate to desired folder to extract
2. Clone the repo `git clone git@github.com:dmitriy-ga/python-project-lvl2.git`
3. Open downloaded folder `cd python-project-lvl2`
4. Run `make build`
5. Run `make package-install`

### Usage
`gendiff [-h] [-f {stylish,plain,json}] first_file second_file`

Also tool can be imported and called by `generate_diff(first_file, second_file, style)`

### Asciinema demo:
[![asciicast](https://asciinema.org/a/TQ2XR1wxid6bR4GeBzFx3gBKg.svg)](https://asciinema.org/a/TQ2XR1wxid6bR4GeBzFx3gBKg)