from typing import Dict, Tuple, List
from sqlite3 import Connection

class LinksRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_link(self, link_info: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO links
                (id, trip_id, link)
            VALUES
                (?, ?, ?)
            ''', (
                link_info["id"],
                link_info["trip_id"],
                link_info["link"],
                
            )
        )
        self.__conn.commit()

    def find_links(self, trip_id: str) -> List[Tuple]: 
        cursor = self.__conn.cursor()
        cursor.execute(
            '''SELECT * FROM links where trip_id = ?''', (trip_id,)
        )
        links = cursor.fetchall()
        return links