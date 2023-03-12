# LIVIVO_RW
## Dokumentation zu der Bachelorarbeit mit dem Thema: Anreicherung von bibliographischen Metadaten zur Sichtbarmachung zurückgezogener Artikel.  Erarbeitung am Beispiel des Suchportals LIVIVO und der "Retraction Watch Database".

### Hardware und Software
#### Für die VM wurde eine SimpleVM von de.NBI folgenden Spezifikationen gewählt:
- de.NBI medium + ephemeral: 14 VCPUs - 32 GB RAM - 50 GB root disk
- Image: Ubuntu 22.04 LTS de.NBI (2022-10-28)

#### Software
- Python
- PostgreSQL 15 & pgAdmin4

### Pipeline und Dokumentation
#### Pipeline

![image](https://user-images.githubusercontent.com/15416032/221816524-4a4598ae-700e-406e-8543-56eb7d459830.png)

#### Dokumentation
- Extraktion: Python Skript ```/src/harvest_lv_dio.py```
- PostgreSQL Dokumentation: ```/src/postgreSQL_cmds.txt```
