# 📁 Google Stock Prices (2004 - Today)

![Project](https://img.shields.io/badge/Project-Type%3A%20Data%20Visualization-blue)
![Dataset](https://img.shields.io/badge/Dataset-Google%20Daily%20Stock%20Prices-green)
![Language](https://img.shields.io/badge/Language-Python-yellow)
![Charts](https://img.shields.io/badge/Charts-Bar%20%26%20Scatter-critical)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-✔️-150?style=flat-square&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-📊-green?style=flat-square&logo=python)
![GitHub Repo stars](https://img.shields.io/github/stars/turki013/Google-stock-by-year?style=social)
![GitHub forks](https://img.shields.io/github/forks/turki013/Google-stock-by-year?style=social)
![GitHub issues](https://img.shields.io/github/issues/turki013/Google-stock-by-year)
![GitHub pull requests](https://img.shields.io/github/issues-pr/turki013/Google-stock-by-year)
![GitHub last commit](https://img.shields.io/github/last-commit/turki013/Google-stock-by-year)
![GitHub repo size](https://img.shields.io/github/repo-size/turki013/Google-stock-by-year)
![License](https://img.shields.io/github/license/turki013/Google-stock-by-year)
---

## 🧠 Project Description

This project explores the **historical daily stock prices of Google** from 2004 to today. It aims to visualize how trading volume evolved year by year using Python libraries such as **Pandas** and **Matplotlib**.

The charts make it easier to understand stock activity trends and uncover potential market patterns by summarizing large volumes of raw data into readable visual formats.

---

## 📂 File Structure

```
GOOGLE STOCK PRICES (2004 - TODAY)/
├── Data/
│   └── googl_daily_prices.csv         # Raw dataset
├── Doc/
│   └── Analysis.md                    # Visual insight summary
├── src/
│   ├── config.py                      # Configuration for labels, font size, title, etc.
│   └── main.py                        # Core code to process and plot the data
├── README.md                          # Project overview and setup guide
```

---

## 🧰 Technologies Used

* **Python 3.11**
* **Pandas**: for data handling
* **Matplotlib**: for plotting
* **VS Code**: development environment

---

## 📈 Visualizations

Two main types of charts are included:

* **Bar Chart**: Displays total trading volume by year using a color-coded scheme.
* **Scatter Plot**: Shows individual volume points per year for deeper visual clarity.

Both charts help in identifying:

* Surges in activity (e.g. 2004-2008, 2020s)
* Periods of stagnation or low volume
* Potential market reaction to historical events

> 📌 Full interpretation available in `Doc/Analysis.md`

---

## 🚀 How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/your-repo-name.git
cd your-repo-name
```

2. Install required packages:

```bash
pip install pandas matplotlib
```

3. Run the project:

```bash
python src/main.py
```

---

## 📌 Notes

* Make sure the dataset path is correct: `Data/googl_daily_prices.csv`
* Chart labels and styles can be customized in `config.py`
* Press `S` while viewing the plot to save an image of the chart (custom save logic implemented)

---

## 📜 License

This project is for academic and educational use. You are free to modify and adapt it.

---

> Built by a Data Science student exploring Python and data visualization as part of their AI engineering journey.
