# Spectrochemical Energy Converter

## Description
Command-line tool written in python that allows scientists to quickly and easily convert common energy units used.

## Project Status
This project has been expanded to be used on mobile platforms as opposed to being used as a command line tool. This project will be updated with added units that are included or added to the mobile app.

## Installation
Must have python installed on PC/linux and the EnergyConversions.py saved in parent directory to use conversions.

## Usage
The project can be used as a command-line tool:

```bash
python EnergyConversions.py
```

or the conversions can be run as standalone functions:

```python 
import EnergyConversions

#converts 5 eV to wavenumbers
EnergyConversions.convert2wavenumber('eV', 5)

#converts 200 nm to eV
EnergyConversions.convert2eV('nm', 200)
```

## Support
Contact the author at mmfahey92@gmail.com

## Roadmap
No planned updates.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

# Authors and Acknowledgment
Mackenzie Fahey

mmfahey Programming

mmfahey92@gmail.com

https://mmfahey-portfolio-app.herokuapp.com/

https://github.com/mmfahey

## License
[MIT](https://choosealicense.com/licenses/mit/)