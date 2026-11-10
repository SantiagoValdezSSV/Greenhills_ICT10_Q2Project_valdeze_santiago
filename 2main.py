from pyscript import document, display

elements = {
    "H":  "Symbol: H  | Element: Hydrogen    | Atomic Number: 1  | Atomic Mass: 1.008",
    "HE": "Symbol: He | Element: Helium      | Atomic Number: 2  | Atomic Mass: 4.0026",
    "C":  "Symbol: C  | Element: Carbon      | Atomic Number: 6  | Atomic Mass: 12.011",
    "N":  "Symbol: N  | Element: Nitrogen    | Atomic Number: 7  | Atomic Mass: 14.007",
    "O":  "Symbol: O  | Element: Oxygen      | Atomic Number: 8  | Atomic Mass: 15.999",
    "F":  "Symbol: F  | Element: Fluorine    | Atomic Number: 9  | Atomic Mass: 18.998",
    "NE": "Symbol: Ne | Element: Neon        | Atomic Number: 10 | Atomic Mass: 20.180",
    "P":  "Symbol: P  | Element: Phosphorus  | Atomic Number: 15 | Atomic Mass: 30.974",
    "S":  "Symbol: S  | Element: Sulfur      | Atomic Number: 16 | Atomic Mass: 32.06",
    "CL": "Symbol: Cl | Element: Chlorine    | Atomic Number: 17 | Atomic Mass: 35.45",
    "AR": "Symbol: Ar | Element: Argon       | Atomic Number: 18 | Atomic Mass: 39.948",
    "SE": "Symbol: Se | Element: Selenium    | Atomic Number: 34 | Atomic Mass: 78.971",
    "BR": "Symbol: Br | Element: Bromine     | Atomic Number: 35 | Atomic Mass: 79.904",
    "KR": "Symbol: Kr | Element: Krypton     | Atomic Number: 36 | Atomic Mass: 83.798",
    "I":  "Symbol: I  | Element: Iodine      | Atomic Number: 53 | Atomic Mass: 126.90",
    "XE": "Symbol: Xe | Element: Xenon       | Atomic Number: 54 | Atomic Mass: 131.29",
    "RN": "Symbol: Rn | Element: Radon       | Atomic Number: 86 | Atomic Mass: 222",
}

not_found_msg = "Element does not exist in the list."


def search_element(event=None):
    symbol = document.getElementById("symbol_input").value
    result = elements.get(symbol, not_found_msg)
    document.getElementById("result").innerHTML = result
