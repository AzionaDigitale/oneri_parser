# Parser for Arera fees and tarifs
A script to parse energy tarifs and fees from an excel file.

A parser to download the most up-to-date “rates and charges” from the Arera website (publicly available), search for the necessary parameters, and save them neatly in a JSON file. 

The script is provided as-is without any warranty. No “production ready” checks have been performed at the time of the publication, and therefore the use of the file is at your own discretion and responsibility, both for the technical aspect and for the data actually downloaded. 
We accept no responsibility for any eventuality arising from use other than purely educational purposes.

Pull requests and contributions are welcome. In this case, please open an Issues first.

Script tested last at 05 Sept 2025

## Sample data
 "Abitazioni di residenza anagrafica": [<br>
        {<br>
            "descrizione": "EN €/kWh",<br>
            "valori": {<br>
                "PE": {<br>
                    "F0": 0.13463,<br>
                    "F1": 0.14352,<br>
                    "F23": 0.13002<br>
                },<br>
                "Materia energia": 0.16412,<br>
                "PD": 0.02393,<br>
                "PCV": "- ",<br>
                "DISPbt": "- ",<br>
                "PPE": 0.00556,<br>
                "σ2": "- ",<br>
                "σ3": 0.01189,<br>
                "UC3": 0.00156,<br>
                "UC6": 7e-05,<br>
                "Trasporto e gestione del contatore": 0.01352,<br>
                "ASOS": 0.02968,<br>
                "ARIM": 0.00164,<br>
                "Oneri di sistema": 0.03132<br>
            }<br>


