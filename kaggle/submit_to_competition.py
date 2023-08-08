import pathlib
import json


submission_file_path = './data/output/sub.csv'
message = 'Auto-submission'
competition_id = 'first-competition-titanic'

# jsonファイルの配置
creds = json.load(open('./configs/kaggle.json'))
cred_path = pathlib.Path('~/.kaggle/kaggle.json').expanduser()
if not cred_path.exists():
    cred_path.parent.mkdir(exist_ok=True)
    cred_path.write_text(json.dumps(creds))
    cred_path.chmod(0o600)

from kaggle.api.kaggle_api_extended import KaggleApi

# Kaggle API
api = KaggleApi()
api.authenticate()
api.competition_submit(submission_file_path, message, competition_id)
