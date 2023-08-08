import pandas as pd
from sklearn.model_selection import cross_val_score
import argparse
import json
import mlflow

from utils import load_datasets, load_target
from models.randomforest import train_and_predict


# Configの読み込み
parser = argparse.ArgumentParser()
parser.add_argument('--config', default='./configs/default.json')
options = parser.parse_args()
config = json.load(open(options.config))

# 特徴量、パラメータ、学習データの設定
feats = config['features']
ID_name = config['ID_name']
target_name = config['target_name']
params = config['params']
experiment_name = config['experiment_name']
model_name = config['model_name']
X_train_all, X_test = load_datasets(feats)
y_train_all = load_target(target_name)

# モデルの学習
y_pred, model = train_and_predict(X_train_all, y_train_all, X_test, params)
score = cross_val_score(model, X_train_all, y_train_all, scoring='accuracy', cv=5).mean()

# MLflow
is_recorded = False  # TrueにするとMLflowにrunが記録
run_id = None  # run_idを指定すると、runに結果が上書き

if(is_recorded):
    print('This run is recorded.')
    mlflow.set_experiment(experiment_name)
    if not run_id:
        mlflow.start_run(run_id=None)
        run_id = mlflow.active_run().info.run_id
    elif run_id:
        mlflow.start_run(run_id=run_id)

    mlflow.set_tag('model_name', model_name)
    mlflow.set_tag('target_name', target_name)
    mlflow.set_tag('features', feats)
    mlflow.log_params(params)
    mlflow.log_param('train_shape', X_train_all.shape)
    mlflow.log_param('test_shape', X_test.shape)
    mlflow.log_artifact('./configs/default.json')
    mlflow.log_artifact('./features/importances/importances_barh.png')
    mlflow.log_metric('accuracy', score)
    mlflow.sklearn.log_model(model, model_name)

    mlflow.end_run()

print('===CV score===')
print(score)

# 提出用ファイルの作成
sub = pd.DataFrame(pd.read_csv('./data/input/test.csv')[ID_name])
sub[target_name] = y_pred
sub.to_csv('./data/output/sub.csv', index=False)
print('./data/output/sub.csv is created.')
