# generate_ramadan_ranges.py

from convertdate import islamic
from datetime import date, timedelta
import pandas as pd

START_YEAR = 1551
END_YEAR = 2649

def generate_ramadan_ranges(start_year, end_year):
    data = []

    for g_year in range(start_year, end_year + 1):

        # Approximate Hijri year mapping
        h_year = int((g_year - 622) * 33 / 32)

        try:
            ramadan_start = islamic.to_gregorian(h_year, 9, 1)
            start_date = date(*ramadan_start)

            shawwal_start = islamic.to_gregorian(h_year, 10, 1)
            end_date = date(*shawwal_start) - timedelta(days=1)

            if start_date.year == g_year:
                data.append({
                    "year": g_year,
                    "ramadan_start": start_date.strftime("%Y-%m-%d"),
                    "ramadan_end": end_date.strftime("%Y-%m-%d")
                })

        except Exception:
            continue

    return pd.DataFrame(data)


if __name__ == "__main__":
    df = generate_ramadan_ranges(START_YEAR, END_YEAR)
    df.to_csv("ramadan_1551_2649.csv", index=False)
    print("Ramadan dataset generated successfully.")
    print(df.head())
