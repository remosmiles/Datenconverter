import json
import csv
import os

class CarDataConverter:
    def __init__(self, input_file):
        self.input_file = input_file
        self.data = []

    def load_data(self):
        """Lädt die JSON-Daten aus einer Datei."""
        if not os.path.exists(self.input_file):
            print(f"Fehler: Datei {self.input_file} nicht gefunden.")
            return False
        
        with open(self.input_file, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        return True

    def clean_data(self):
        """Bereinigt die Daten: Kennzeichen zu Großbuchstaben, etc."""
        for entry in self.data:
            entry['kennzeichen'] = entry.get('kennzeichen', 'Unbekannt').upper()
            # Falls ein Wert fehlt, Standardwert setzen
            if 'personen' not in entry:
                entry['personen'] = 1
        print("Datenbereinigung abgeschlossen.")

    def to_csv(self, output_file):
        """Konvertiert die Daten in eine CSV-Datei."""
        if not self.data:
            print("Keine Daten zum Konvertieren vorhanden.")
            return

        keys = self.data[0].keys()
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.data)
        print(f"Erfolgreich konvertiert: {output_file}")

# --- Beispiel für die Nutzung ---
if __name__ == "__main__":
    # 1. Instanz erstellen
    converter = CarDataConverter('kontrollen.json')
    
    # 2. Daten laden und verarbeiten
    if converter.load_data():
        converter.clean_data()
        
        # 3. Speichern als CSV für Excel
        converter.to_csv('kontrollbericht_2026.csv')
