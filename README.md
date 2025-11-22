# Parser for Arera fees and tarifs
A script to parse energy tarifs and fees from an excel file.

A parser to download the most up-to-date “rates and charges” from the Arera website (publicly available), search for the necessary parameters, and save them neatly in a JSON file. 

The script is provided as-is without any warranty. No “production ready” checks have been performed at the time of the publication, and therefore the use of the file is at your own discretion and responsibility, both for the technical aspect and for the data actually downloaded. 
We accept no responsibility for any eventuality arising from use other than purely educational purposes.

Pull requests and contributions are welcome. In this case, please open an Issues first.

Script tested last at 22 Nov 2025

## Sample data
## Abitazioni di residenza anagrafica — EN €/kWh

### PE
| Fascia | Valore |
|--------|--------|
| F0     | 0.12032 |
| F1     | 0.12348 |
| F23    | 0.11874 |

### Materia energia
| Fascia        | Valore |
|---------------|--------|
| Fascia unica  | 0.14256 |
| F1            | 0.14572 |
| F23           | 0.14098 |

### Altri valori
| Voce                           | Valore    |
|--------------------------------|-----------|
| PD                             | 0.01779   |
| PCV                            | —         |
| DISPbt                         | —         |
| PPE                            | 0.00445   |
| σ1                             | —         |
| σ2                             | —         |
| σ3                             | 0.01189   |
| UC3                            | 0.00156   |
| UC6                            | 0.00007   |
| Trasporto e gestione contatore | 0.01352   |
| ASOS                           | 0.02968   |
| ARIM                           | 0.00164   |
| Oneri di sistema               | 0.03132   |



