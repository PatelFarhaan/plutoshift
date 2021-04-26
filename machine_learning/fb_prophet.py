import json
import pandas as pd
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error


def generate_csv(data):
    """
    Generating csv from the input data
    """

    csv_path = "data.csv"
    json_path = "data.json"

    _sub_key = list(data.get("target", {}).keys())
    sub_key = _sub_key[0] if _sub_key else None
    forecast_data = data.get("target", {}).get(sub_key, [])
    forecast_length = int(data.get("forecast_length").replace("D", ""))
    if not forecast_data:
        return {
            "result": False,
            "message": "no data found",
            "data": None
        }

    with open(json_path, "w") as out_file:
        json.dump(forecast_data, out_file, indent=4)

    df = pd.read_json(json_path)
    df.to_csv(csv_path, index=False, header=["ds", "y"])
    return csv_path, forecast_length


def convert_df_to_json(dataframe):
    return json.dumps(json.loads(dataframe.to_json(orient="records")))


def fit_the_model(data):
    """
    Initializing Prophet machine_learning for data fitting
    """

    prediction_data, forecast_length = generate_csv(data)
    prediction_df = pd.read_csv(prediction_data)
    model = Prophet()
    model.fit(prediction_df)
    future = model.make_future_dataframe(periods=forecast_length)
    forecast = model.predict(future)
    y_pred = forecast["yhat"][:prediction_df.shape[0]]
    y_true = prediction_df["y"]
    mse = mean_squared_error(y_true, y_pred)
    str_data = convert_df_to_json(forecast)
    return str_data, mse
