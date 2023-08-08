from sklearn.ensemble import RandomForestClassifier

from utils import visualize_features_by_barh


def train_and_predict(X_train, y_train, X_test, rf_params):
    # モデルを学習する
    model = RandomForestClassifier(**rf_params)
    model.fit(X_train, y_train)

    # テストデータを予測する
    y_pred = model.predict(X_test)

    # Feature Importanceの保存
    labels = X_train.columns
    importances = model.feature_importances_
    visualize_features_by_barh(labels, importances)

    return y_pred, model
