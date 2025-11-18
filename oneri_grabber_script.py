```
# === DOWNLOAD FILE FROM WEB IF AVAILABLE ===
	import requests
	from typing import Optional
	from bs4 import BeautifulSoup
	from urllib.parse import urljoin
	import os

	BASE_URL = "https://www.arera.it/area-operatori/prezzi-e-tariffe"
	PATTERN = "smt.xlsx"

	TIMEOUT = 30 # managing timeout

	# Fetch function
	def fetch_html(url: str) -> str:
		response = requests.get(url, timeout=TIMEOUT)
		response.raise_for_status()
		return response.text

	# Find function
	def find_excel_link(html: str, base_url: str, pattern: str) -> Optional[str]:
		soup = BeautifulSoup(html, "html.parser")
		link_tag = soup.find("a", href=lambda x: x and pattern in x)
		if not link_tag:
			return None
		return urljoin(base_url, link_tag["href"])

	# Download function
	def download_file(url: str, output_path: str) -> None:
		response = requests.get(url, timeout=TIMEOUT)
		response.raise_for_status()

		with open(output_path, "wb") as f:
			f.write(response.content)


	def main():
		# print("Fetching HTML...")
		html = fetch_html(BASE_URL)

		# print("Searching for Excel link...")
		file_url = find_excel_link(html, BASE_URL, PATTERN)

		if not file_url:
			print(f"No file found containing '{PATTERN}'")
			return

		file_name = os.path.basename(file_url)

		#print(f"Downloading file: {file_name} ...")
		download_file(file_url, file_name)

		print(f"Download completed: {file_name}")


	if __name__ == "__main__":
		main()
```

```
# === DOWNLOAD DATA FROM LOCAL XLS FILE ===

import pandas as pd
import json
from numbers import Number

# === COSTANTI ===
EXCEL_FILE = "E2025-3_smt.xlsx"
SHEET_NAME = 0  # foglio indicato da indice o nome
HEADER_ROW = 16  # riga di intestazione (zero-based)
COLS = list(range(2, 21))  # colonne da C a U (zero-based)

# mapping righe valori
RESIDENTIAL_ROWS = {
    "EN €/kWh": 19,
    "FIX €/Y": 20,
    "POT €/kW/Y": 21
}
NON_RESIDENTIAL_ROWS = {
    "EN €/kWh": 28,
    "FIX €/Y": 29,
    "POT €/kW/Y": 30
}

# chiavi fisse per i gruppi di colonne
PE_KEYS = ["F0", "F1", "F23"]
ME_KEYS = ["Monorario", "F1", "F23"]


def load_raw_data(file_path, sheet, header_row, cols):
    """Carica il file excel senza intestazioni e ritorna dataframe e intestazioni delle colonne."""
    df = pd.read_excel(file_path, sheet_name=sheet, header=None)
    headers = df.iloc[header_row, cols].astype(str).str.strip().tolist()
    return df, headers


def extract_grouped_data(df, rows_map, cols, headers):
    """
    Estrae i dati da df seguendo le righe specificate in rows_map.
    Ricostruisce i gruppi PE, PD_PPE, ME e il resto.
    Rimuove la chiave 'TOTALE' se presente (case sens).
    """
    PD_TO_PPE_KEYS = headers[3:8]
    rest_keys = headers[11:]

    extracted = []
    for descrizione, row_idx in rows_map.items():
        values = df.iloc[row_idx, cols].tolist()

        pe = dict(zip(PE_KEYS, values[0:3]))
        pd_ppe = dict(zip(PD_TO_PPE_KEYS, values[3:8]))
        me = dict(zip(ME_KEYS, values[8:11]))
        rest = dict(zip(rest_keys, values[11:]))

        row_dict = {"PE": pe, "Materia energia": me}
        row_dict.update(pd_ppe)
        row_dict.update(rest)

        # Rimuove eventuale chiave TOTALE (case-insensitive)
        row_dict = {k: v for k, v in row_dict.items() if str(k).strip().upper() != "TOTALE"}

        extracted.append({"descrizione": descrizione, "valori": row_dict})

    return extracted


def round_values(obj, decimals=5):
    """
    Ricorsivamente arrotonda tutti i valori numerici in obj a 'decimals' cifre decimali.
   
    """
    if isinstance(obj, dict):
        return {k: round_values(v, decimals) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [round_values(elem, decimals) for elem in obj]
    elif isinstance(obj, Number):
        return round(obj, decimals)
    else:
        return obj


def save_json(data, filename):
    """Salva i dati in formato JSON leggibile."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"File JSON salvato in {filename}")


def main():
    df_raw, headers = load_raw_data(EXCEL_FILE, SHEET_NAME, HEADER_ROW, COLS)
    residential_data = extract_grouped_data(df_raw, RESIDENTIAL_ROWS, COLS, headers)
    non_residential_data = extract_grouped_data(df_raw, NON_RESIDENTIAL_ROWS, COLS, headers)

    final_result = {
        "Abitazioni di residenza anagrafica": residential_data,
        "Abitazioni diverse dalla residenza anagrafica": non_residential_data,
    }

    # Arrotonda tutti i valori numerici a 5 decimali prima di salvare
    final_result = round_values(final_result, decimals=5)

    save_json(final_result, "output.json")


if __name__ == "__main__":
    main()
```