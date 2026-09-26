import pandas as pd


def calculate_profitability(revenue: float, cost: float) -> float:
    """Возвращает рентабельность в процентах."""
    if revenue == 0:
        return 0.0
    return (revenue - cost) / revenue * 100


def main():
    data = {
        "Месяц": ["Январь", "Февраль", "Март"],
        "Выручка": [120000, 150000, 135000],
        "Затраты": [80000, 100000, 95000],
    }
    df = pd.DataFrame(data)
    print(df)
    print("Средняя выручка:", df["Выручка"].mean())

    for _, row in df.iterrows():
        profit = calculate_profitability(row["Выручка"], row["Затраты"])
        print(f"{row['Месяц']}: рентабельность = {profit:.1f}%")


if __name__ == "__main__":
    main()