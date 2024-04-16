import pysftp
import pandas as pd
import argparse
import logging
import json
from google.oauth2 import service_account
import pandas_gbq


# Read json file
def read_config(json_file):

    with open(json_file, "r") as f:
        data = json.load(f)
    return data


def connect_sftp(config_sftp, file_name):

    try:
        conn = pysftp.Connection(
            host=config_sftp.get("host"), 
            port=config_sftp.get("port"), 
            username=config_sftp.get("username"), 
            password=config_sftp.get("password")
        )
        print("connection established successfully")x
    except:
        print('failed to establish connection to targeted server')

    current_dir = conn.pwd
    print('our current working directory is: ', current_dir)

    with conn.cd('xepelin_data/orders/'):
        conn.get(file_name)


def load_data(project_id, table_id, df_news, date):

    # path to JSON credentials file
    credentials = service_account.Credentials.from_service_account_file('path/to/key.json')

    # get historic data excluding new date data
    sql = """
    SELECT customer_id, date, total_amount, avg_amount, median_amount
    FROM `{}.{}`
    WHERE date =! '{}'
    """.format(project_id, table_id, date)

    df_data = pandas_gbq.read_gbq(
        sql, 
        project_id=project_id, 
        credentials=credentials
    )

    # union historic data with news
    data = [df_data, df_news]
    df_final = pd.concat(data)

    # insert data in bigquery table, if table not exists, create it
    pandas_gbq.to_gbq(
        df_final, 
        table_id, 
        project_id=project_id, 
        credentials=credentials, 
        if_exists='replace'
    )

    print(
        "Created and loaded table {}.{}".format(project_id, table_id)
    )


def transpose_df(df):

    df_transposed = df.T
    header = df_transposed.iloc[0]
    df_transposed = df_transposed[1:]
    df_transposed.columns = header

    return df_transposed


def transform_data(df_transposed):

    df_transposed["amount"] = pd.to_numeric(df_transposed["amount"])
    df_final = df_transposed.groupby(['customerId', 'createdAt'])['amount'].agg(["sum", "mean" , "median"])
    df_final= df_final.rename(columns={"mean": "avg_amount", "sum": "total_amount", "median": "median_amount", "customerId": "customer_id", "createdAt": "date"})

    return df_final


def xepelin_test(date):

    config_sftp = read_config("sftp_config_example.json")
    print("Config File Read")

    file_name = 'orders_{}.csv'.format(date)

    connect_sftp(config_sftp, file_name)

    df = pd.read_csv(file_name)
    print(df)

    df_transposed = transpose_df(df)
    df_final = transform_data(df_transposed)

    project_id = "xepelin_data"
    # dataset_id.table_name
    table_id = "landing.test_xepelin_mj"

    load_data(project_id, table_id, df_final)


if __name__ == "__main__":

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", help="Date in format yyyy-mm-dd", required=True)
    args = parser.parse_args()

    xepelin_test(args.date)