# These commands are run after the docker image is built.
pip install -r requirements.txt
#python -m nltk.downloader punkt
python -m pip install --upgrade pip setuptools wheel