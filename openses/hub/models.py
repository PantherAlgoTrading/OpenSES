from datetime import datetime
from pathlib import Path
from uuid import uuid4

from peewee import SqliteDatabase, Model, FloatField, UUIDField

from openses.config import get_config


OPENSES_HIDDEN_FOLDER: Path = Path.cwd() / ".openses"
SQLITE3_FILE_PATH: Path = OPENSES_HIDDEN_FOLDER / "datastore.db"

db = SqliteDatabase(SQLITE3_FILE_PATH)


class BaseModel(Model):
    class Meta:
        database = db


# TODO: Add models here and add them to create_tables


# class User(BaseModel):
#     uuid = UUIDField(primary_key=True, default=uuid4)
#     fund_amount = FloatField(default=get_config().default_fund_amount)


def initialize_db_tables() -> None:
    with db:
        db.create_tables([])


if __name__ == "__main__":
    pass
