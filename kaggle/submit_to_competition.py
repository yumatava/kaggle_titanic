import pathlib
import json

from kaggle.api.kaggle_api_extended import KaggleApi


SUBMISSION_FILE_PATH = './data/output/sub.csv'
MESSAGE = 'Auto-submission'
COMPETITION_ID = 'first-competition-titanic'

# Kaggle API credentials
creds = json.load(open('./configs/kaggle.json'))
cred_path = pathlib.Path('~/.kaggle/kaggle.json').expanduser()
if not cred_path.exists():
    cred_path.parent.mkdir(exist_ok=True)
    cred_path.write_text(json.dumps(creds))
    cred_path.chmod(0o600)

# Kaggle API
api = KaggleApi()
api.authenticate()
api.competition_submit(SUBMISSION_FILE_PATH, MESSAGE, COMPETITION_ID)
