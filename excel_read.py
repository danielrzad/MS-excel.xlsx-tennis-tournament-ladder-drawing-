from openpyxl import load_workbook
from datetime import datetime
from pathlib import Path

key = 1
rank_row = 8
seed_num_row = 8
seed_positions = [1, 8, 9, 16, 17, ]
name_row = 8

while key != 32:
    key += 1
    rank_row, seed_num_row, name_row += 2
    dct = {
        "rank": "C" + f"{str(rank_row)}"
        "seed_num": "D" + f"{str(seed_num_row)}"
        "name": "R" + f"{str(name_row)}"
    }
    


    positions32[key][]
positions32 = {
    1: {"rank": "C8", "seed_num": "D8", "name": "E8"}
}








def write_excel(
    tournament_size, tournament_name, torunament_category, torunament_date, draw_witnesses
):
    if tournament_size == 32:
        path = Path.cwd() / "tournament_structure_samples" / "cup32.xlsx"
    elif tournament_size == 16:
        path = Path.cwd() / "tournament_structure_samples" / "cup16.xlsx"
    wb = load_workbook(filename=path)
    ws = wb.active
    print(ws)




write_excel(
    tournament_size=32,
    tournament_name="VI GPSWA",
    torunament_category="MS OPEN",
    torunament_date=f"{datetime.now().strftime('%d.%m.%Y ')}",
    draw_witnesses="Daniel Rząd"
)