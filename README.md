# SQL-Python-Package

[![Docker Image CI Main](https://github.com/Nathan-Bush46/IDS706-python-package/actions/workflows/main.yml/badge.svg)](https://github.com/Nathan-Bush46/IDS706-python-package/actions/workflows/main.yml)

[![Docker Image CI Lint](https://github.com/Nathan-Bush46/IDS706-python-package/actions/workflows/lint.yml/badge.svg)](https://github.com/Nathan-Bush46/IDS706-python-package/actions/workflows/lint.yml)

[![Docker Image CI Test](https://github.com/Nathan-Bush46/IDS706-python-package/actions/workflows/test.yml/badge.svg)](https://github.com/Nathan-Bush46/IDS706-python-package/actions/workflows/test.yml)

[![Docker Image CI Format](https://github.com/Nathan-Bush46/IDS706-python-package/actions/workflows/format.yml/badge.svg)](https://github.com/Nathan-Bush46/IDS706-python-package/actions/workflows/format.yml)

[![Docker Image CI Install](https://github.com/Nathan-Bush46/IDS706-python-package/actions/workflows/install.yml/badge.svg)](https://github.com/Nathan-Bush46/IDS706-python-package/actions/workflows/install.yml)


## User Guide for `run-databricks-query`

## Easy one step install and .env setup: 

* pip install databricks-tool
* Note: only tested with python 3.10 (should not use current python versions as databricks-sql-connector will not work)

*  Create a `.env` file where you want to run sql query. This file Must contain your Databricks credentials in the formate:
   ```
   DATABRICKS_SERVER_HOSTNAME=your-server-hostname
   DATABRICKS_HTTP_PATH=your-http-path
   DATABRICKS_TOKEN=your-access-token
   ```

   Replace `your-server-hostname`, `your-http-path`, and `your-access-token` with your actual Databricks credentials.

## Usage Instructions

1. **Running a Query**

   To execute a SQL query using the tool, use the command format below in your terminal:

   ```bash
   run-databricks-query "SELECT * FROM Person_Nathan"
   ```
   Must run with .env file in current directory 

2. **Understanding Output**

   The tool will connect to your Databricks instance, execute the provided SQL query, and print the results to the console.

3. **Common Issues and Troubleshooting**

    - **Environment Variables**: Ensure that your `.env` file is correctly configured and located in the directory from which you run the command.
    - **Network Issues**: Verify that you have network access to your Databricks instance.
    - **Permissions**: Ensure that your access token has sufficient permissions to execute queries.

### **Additional Information**

- **Dependencies**: The tool requires `python-dotenv` and `databricks-sql-connector`. These are automatically installed when you run `pip install .`.

### Alternative install
1. **Clone the Repository**
   Start by cloning this repository 

2. **Set Up Environment Variables**

   Create a `.env` file in the root directory of the cloned project. This file Must contain your Databricks credentials in the formate:
   ```
   DATABRICKS_SERVER_HOSTNAME=your-server-hostname
   DATABRICKS_HTTP_PATH=your-http-path
   DATABRICKS_TOKEN=your-access-token
   ```

   Replace `your-server-hostname`, `your-http-path`, and `your-access-token` with your actual Databricks credentials.

3. **Install the Package**

   Use pip to install the package locally. Run this command in the root directory (src/databricks_tool/setup.py) where`setup.py` is located:
   ```bash
   pip3.10 install .
   ```

   Note: must use old version of python for databricks-sql-connector, python 3.10 works


## Explanation of other things in Repository 

* databricks_tool is a package that lets you run sql querys using databricks on the commond line.

* workspace and test folders show examples of python scripts running sql on a databricks database.

* See [`video`](https://www.youtube.com/watch?v=rTuY1ctXtiI) for walkthrough run using databricks with python code.

* Python files that create, query, and test a databricks table using Python and SQL.
    * [`create table`](src/main_workspace/make_table.py): Creates a basic table from data found ['here'](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset?resource=download)
        * Shows use of some SQL queries
    * [`query`](src/main_workspace/query.py): Creates a table from the other table. Then joins them to create a more intersting table.
    * [`Test`](src/tests/tests.py): Does a basic testing using Python. This tests that the operations on a database behave as expected. 

## Set up instructions using VS code + Docker: 
### Docker
1. For Windows, Mac, and maybe Linux, you download Docker Desktop. links can be found [here](https://docs.docker.com/engine/install/). Follow set up instructions and start the application.

2. In vs code add Dev Containers and Docker extensions 

3. clone repo, restart vs code, and open repo in vs code.

4. should see a pop up to (re)open in devcontainer. Click it and let it run. It takes a bit of time for the first run but is much faster after that. Done.

#### Alternatives to Docker
If you choose not to run docker, use a python virtual environment to prevent conflict with local packages and run the makefile.
 
## Testing

### makefile  
* install

* testing:

    tests all "\*test\*.py" files in src/test/ using py.test then tests all files using py.test --nbval-lax

* lint

* format

* all 

### VS code testing  
1. Can also use the VS-code testing menu in the same way.

## Things included are:

* [`Makefile`](Makefile)

* `Pylint` and `Ruff` for lintning

* `.env`, used to ensure constient imports and give DB info

* `.devcontainer` with [`Dockerfile`](/.devcontainer/Dockerfile), [`postinstall.sh`](/.devcontainer/postinstall.sh), and [`devcontainer.json`](/.devcontainer/devcontainer.json)`

*  [`settings.json`](.vscode/settings.json) for testing

*  A base set of libraries in [`requirements.txt`](requirements.txt)
