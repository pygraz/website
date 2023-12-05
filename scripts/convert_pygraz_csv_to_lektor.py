import csv
import pathlib
from datetime import datetime

from slugify import slugify

CSV_FOLDER = pathlib.Path(__file__).parent / "data"
BLOG_FOLDER = pathlib.Path(__file__).parent.parent / "blog"

csv_names = [
    "meetups_location.csv",
    "meetups_meetup.csv",
    "meetups_session.csv",
    "meetups_sessiontype.csv",
]


def csv_id_to_rows(basename: str) -> dict[str, list[dict]]:
    result = {}
    with open(CSV_FOLDER / basename, newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            result[row["id"]] = row
    return result


data = {basename: csv_id_to_rows(basename) for basename in csv_names}


def convert():
    # print(data)
    # keys = {k:mydata[0].keys() for k, mydata in data.items()}
    # pprint(keys)
    sessions = data["meetups_session.csv"]
    meetups = data["meetups_meetup.csv"]
    for session_id, session in sessions.items():
        meetup_id = session["meetup_id"]
        if meetup_id == "":
            print("warning, sesson ohne meetup:", session_id)
            continue

        meetup = meetups[meetup_id]

        # chase date
        start_date_as_string = meetup["start_date"].replace(" ", "T") + ":00"
        start_date = datetime.fromisoformat(start_date_as_string)
        date_as_string = start_date.date().isoformat()

        # create folder
        content_directory = (
            BLOG_FOLDER / f"{date_as_string}-{slugify(session['title'])}"
        )
        content_directory.mkdir(parents=True, exist_ok=True)

        # make content-file
        with open(content_directory / "contents.lr", "w") as f:
            f.write(f"body: \n{session['abstract']}\n")
            f.write("---\n")
            f.write("author: TODO\n")
            f.write("---\n")
            f.write(f"title: {session['title']}\n")

    print(CSV_FOLDER)


if __name__ == "__main__":
    convert()
