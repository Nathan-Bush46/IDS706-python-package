from make_table import load
from query import query

from dotenv import load_dotenv
from databricks import sql
import os


def test_make_table():
    assert load() == 0  # function has testing built in


def test_query():
    assert query() == 0  # function is somewhat simple
    load_dotenv()
    with sql.connect(  # just test that extra table is made
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM AvgSleepDurationByOccupation")
            result = cursor.fetchall()
            assert (result) is not None
            cursor.close()
            connection.close()


if __name__ == "__main__":
    test_make_table()
    test_query()
