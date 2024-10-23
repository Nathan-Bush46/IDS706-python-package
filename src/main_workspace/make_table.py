"""
example simple use of databricks with python and SQL
"""

from dotenv import load_dotenv
from databricks import sql
import os
import csv

init_table = """CREATE TABLE IF NOT EXISTS person_nathan (PersonID INT,
                                    Gender STRING,
                                    Age INT,
                                    Occupation STRING,
                                    SleepDuration FLOAT,
                                    QualityOfSleep INT,
                                    PhysicalActivityLevel INT,
                                    StressLevel INT,
                                    BMICategory STRING,
                                    BloodPressure STRING,
                                    HeartRate INT,
                                    DailySteps INT,
                                    SleepDisorder STRING
                                    );
                                    """


def load(data="src/main_workspace/data/Sleep_health_and_lifestyle_dataset.csv"):
    payload = csv.reader(open(data, newline="", encoding="utf-8"), delimiter=",")
    next(payload)  # skip header
    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(init_table)  # make table if not already
            cursor.execute("SELECT * FROM person_nathan")  # check table
            result = cursor.fetchall()
            if len(result) != 374:  # see if table has full data, if not re-make it
                cursor.execute(
                    "DROP TABLE IF EXISTS person_nathan"
                )  # if table not full nuke it
                cursor.execute(init_table)  # remake it
                # Insert data into the Person table
                # this is slow and should use copy into but I am not sure if I have permision to create files on the server
                insert_query = """
                INSERT INTO Person_Nathan (
                    PersonID, Gender, Age, Occupation, SleepDuration, QualityOfSleep, 
                    PhysicalActivityLevel, StressLevel, BMICategory, BloodPressure, 
                    HeartRate, DailySteps, SleepDisorder
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """
                cursor.executemany(insert_query, payload)
                # Execute insert for each row in the CSV
            # Commit the transaction and close the connection
            connection.commit()
            cursor.close()
            connection.close()
            return 0  # all good


if __name__ == "__main__":
    load()
