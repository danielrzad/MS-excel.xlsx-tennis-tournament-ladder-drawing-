from pathlib import Path
from datetime import datetime


# Settings file for drawing tennis_tournamend_drawing.py and excel_fill.py.
# Don't change anything in files above.
# All the changes needs to be done here.
paths = {
	"players_data_path": Path.cwd() / "players_data_input_file.txt",
	"torunamets_samples_path": Path.cwd() / "tournaments_structures_samples",
	"created_excel_files_path": Path.cwd() / "filled_files",
}


config = {
	"tournament_name": "VI GPSWA",
	"tournament_category": "MS OPEN",
	"tournament_arbiter": "Tomasz Adamowicz",
	"tournament_city": "Stalowa Wola",
	"tournament_date": "20.03.2020",
	"tournament_size": 32,
	"tournament_type": "cup",
	"tournament_drawing_date": datetime.now().strftime("%d-%m-%Y, %H:%M"),
	"draw_witnesses_1": "Daniel Rząd",
	"draw_witnesses_2": "Edward Banaś",
}
