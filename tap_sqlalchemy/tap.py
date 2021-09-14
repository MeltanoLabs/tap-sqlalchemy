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

    # These two will be removed when this comment is resolved in the SDK:
    #    https://gitlab.com/meltano/sdk/-/merge_requests/44#note_676486579

    @property
    def catalog_dict(self) -> dict:
        if self.input_catalog:
            return self.input_catalog

        return SQLAlchemyStream.run_discovery(self.config)

    def discover_streams(self) -> List[SQLAlchemyStream]:
        """Return a list of discovered streams."""
        result: List[SQLAlchemyStream] = []
        for catalog_entry in self.catalog_dict["streams"]:
            result.append(SQLAlchemyStream(self, catalog_entry))

        return result
