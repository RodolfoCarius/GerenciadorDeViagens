import pytest # type: ignore
import uuid
from src.models.settings.db_connection_handle import db_connection_handler
from .links_repository import LinksRepository

db_connection_handler.connect()

trip_id = str(uuid.uuid4())

# @pytest.mark.skip(reason="interacao com o banco")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    links_infos = {
        "id": trip_id,
        "trip_id": trip_id,
        "link": "olaMundo@email.com"
    }

    links_repository.registry_link(links_infos)

# @pytest.mark.skip(reason="interacao com o banco")
def test_find_links():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    links = links_repository.find_links(trip_id)
    print()
    print(links)
