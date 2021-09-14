"""sqlalchemy tap class."""

from typing import List

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers
from singer_sdk.streams import SQLStream

TAP_NAME = "tap-sqlalchemy"

class SQLAlchemyStream(SQLStream):
    """Stream class for sqlalchemy streams."""

    @classmethod
    def get_sqlalchemy_url(cls, tap_config: dict) -> str:
        """Return the SQL Alchemy database URL as set by the user."""
        return tap_config["database_url"]


class TapSQLAlchemy(Tap):
    """SQLAlchemy tap class."""

    name = TAP_NAME
    default_stream_class = SQLAlchemyStream

    config_jsonschema = th.PropertiesList(
        th.Property("database_url", th.StringType, required=True),
    ).to_dict()
