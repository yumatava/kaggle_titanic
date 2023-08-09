# Analytics Titanic Competition
===
- [Kaggle Titanic](https://www.kaggle.com/competitions/first-competition-titanic) のコンペに自動Submitするためのサンプルモデル。
- Azure Pipelineを使ってcsvファイルのparquet変換、特徴量作成、モデルの訓練、Submissionファイルのアップロードを実行可能。

## Structures
```
.
├── configs
│   ├── default.json
│   └── kaggle.json
├── data
│   ├── input
│   │   ├── train.csv
│   │   └── test.csv
│   └── output
│   └── convert_to_parquet.py
├── features
│   ├── importances
│   ├── __init__.py
│   ├── base.py
│   └── create.py
├── kaggle
│   └── submit_to_competition.py
├── mlruns
├── models
│   └── randomforest.py
├── notebooks
├── utils
│   └── __init__.py
├── .flake8
├── .gitignore
├── azure-pipelines.yml
├── README.md
├── requirements.txt
├── run.py
```
## Commands


### Convert data to parquet format 

```
python data/convert_to_parquet.py
```
`./data/input/`に`train.csv`、`test.csv`を格納したうえで実行。

### Create features

```
python features/create.py
```
特徴量を作成する場合。

### Run

```
python run.py
```
実行が終わると`./data/output/`に提出用ファイル`sub.csv`が作成されます。

### Submit to Kaggle

```
python kaggle/submit_to_competition.py
```
[Setting | Kaggle](https://www.kaggle.com/settings)から**Create New Token**で新しいトークンを取得し、`./configs/kaggle.json`に置き換えてください。

### MLflow

```
mlflow ui
```

### flake8

```
flake8 .
```

## References
- [ml-competition-template-titanic](https://github.com/upura/ml-competition-template-titanic)
