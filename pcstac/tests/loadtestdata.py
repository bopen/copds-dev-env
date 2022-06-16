import os
from pathlib import Path

import orjson
from pypgstac.load import Loader, Methods, PgstacDB

DATA_DIR = os.path.join(os.path.dirname(__file__), "data-files")
collection = os.path.join(DATA_DIR, "reanalysis-era5-single-levels/collection.json")


def load_test_data() -> None:
    with PgstacDB() as conn:
        loader = Loader(db=conn)
        with open(collection, "rb") as f:
            c = orjson.loads(f.read())
            loader.load_collections([c], Methods.upsert)


load_test_data()
