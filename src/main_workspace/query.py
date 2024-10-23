"""
example simple use of databricks with python and SQL
"""

from dotenv import load_dotenv
from databricks import sql
import os


make_table_for_join = """
                            CREATE TABLE IF NOT EXISTS AvgSleepDurationByOccupation AS
                            SELECT 
                                Occupation, 
                                AVG(SleepDuration) AS AvgSleepDuration
                            FROM 
                                Person_Nathan
                            GROUP BY 
                                Occupation;
                        """

complexish_sql = """
                    SELECT 
                    p.Age,
                    p.Occupation,
                    a.AvgSleepDuration,
                    AVG(p.SleepDuration) / a.AvgSleepDuration AS sleep_duration_ratio
                FROM 
                    Person_Nathan p
                JOIN 
                    AvgSleepDurationByOccupation a 
                ON 
                    p.Occupation = a.Occupation
                GROUP BY 
                    p.Age, p.Occupation, a.AvgSleepDuration
                ORDER BY 
                    p.Age, p.Occupation;
                """


def query():
    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:
        with connection.cursor() as cursor:

            cursor.execute(make_table_for_join)
            cursor.execute(complexish_sql)
            result = cursor.fetchall()
            print(len(result))
            for row in result:
                print(row)
            connection.commit()
            cursor.close()
            connection.close()
            return 0


if __name__ == "__main__":
    query()
