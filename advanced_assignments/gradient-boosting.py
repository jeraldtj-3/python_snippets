from sklearn.datasets import make_regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

X,y = make_regression(random_state = 0)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=13
)

params = {
    "n_estimators": 80,
    "max_depth": 5,
    "min_samples_split": 5,
    "learning_rate": 0.02,
    "random_state":1,
    "verbose":2
}

reg = GradientBoostingRegressor(**params)

parameters = reg.get_params()
print(f'parameters = {parameters}')

reg.fit(X,y)

model_score = reg.score(X,y)
# features_imp = reg.feature_importance_


# boosting deviance graph
def plot_deviance():

    test_score = np.zeros((params["n_estimators"],), dtype=np.float64)

    #staged_predict allows monitoring(error on testing set after each stage)
    for i, y_pred in enumerate(reg.staged_predict(X_test)):
        test_score[i] = reg.loss_(y_test, y_pred)

    fig = plt.figure(figsize=(6, 6))
    plt.subplot(1, 1, 1)
    plt.title("Deviance")
    plt.plot(
        np.arange(params["n_estimators"]) + 1,
        reg.train_score_,
        "b-",
        label="Training Set Deviance",
    )
    plt.plot(
        np.arange(params["n_estimators"]) + 1, test_score, "r-", label="Test Set Deviance"
    )
    plt.legend(loc="upper right")
    plt.xlabel("Boosting Iterations")
    plt.ylabel("Deviance")
    fig.tight_layout()
    plt.show()


print(f'model score = {model_score}')
plot_deviance()
