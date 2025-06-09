import os
import pandas as pd
import matplotlib.pyplot as plt
import config as cfg


def is_ci():
    return os.getenv("GITHUB_ACTIONS") == "true"

def data():
    try:
        df = pd.read_csv("Data/googl_daily_prices.csv")
        return df
    except FileNotFoundError:
        print("Oops! We couldn't find the file you're looking for. Please double-check the file path and try again.")
    except Exception as e:
        print(f"An unexpected error occurred while trying to read the file:\n{e}\nPlease contact support or try again later")

 

def bar(df):
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year 
    summary = df.groupby("year")[["1. open", "2. high", "3. low", "4. close", "5. volume"]].sum()
    summary["total"] = summary.sum(axis=1)
    summary = summary.sort_values("total").drop(columns="total")
    cmap = plt.cm.get_cmap("Accent", len(summary))
    colors = [cmap(i) for i in range(len(summary))]
    summary["5. volume"].plot(kind="bar", color=colors)
    plt.title(cfg.Title , fontsize=cfg.main_font_size , fontweight=cfg.font_weight )
    plt.xlabel(cfg.X_label , fontsize=cfg.font_size , fontweight=cfg.font_weight)
    plt.ylabel(cfg.Y_label , fontsize=cfg.font_size , fontweight=cfg.font_weight)
    plt.xticks(rotation=45)
    plt.tight_layout()
    if not is_ci():
        plt.show()

def scatter(df):
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year 
    volume_by_year = df.groupby("year")["5. volume"].sum().reset_index()
    plt.scatter(volume_by_year["year"], volume_by_year["5. volume"])
    plt.title(cfg.Title , fontsize=cfg.main_font_size , fontweight=cfg.font_weight )
    plt.xlabel(cfg.X_label , fontsize=cfg.font_size , fontweight=cfg.font_weight)
    plt.ylabel(cfg.Y_label , fontsize=cfg.font_size , fontweight=cfg.font_weight)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    
    if not is_ci():
        plt.show()
        plt.close()

if __name__ == "__main__":
    df = data()
    if is_ci():
        print("CI detected: generating all charts automatically...")
        bar(df)
        scatter(df)
    else:
        print("Welcome to Google stock prices")
        while True:
            print("1. Bar")
            print("2. Scatter")
            print("3. Exit")
            user = input("Enter your choice: ")
            if user == "1":
                bar(df)
            elif user == "2":
                scatter(df)
            elif user == "3":
                print("Exiting the app...\nGoodbye")
                break
            else:
                print("Invalid choice, please try again.")
