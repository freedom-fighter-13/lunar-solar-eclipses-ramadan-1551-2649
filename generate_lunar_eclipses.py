# generate_lunar_eclipses.py

from skyfield.api import load
from skyfield import almanac
import pandas as pd

START_YEAR = 1551
END_YEAR = 2649

def generate_lunar_eclipses(start_year, end_year):

    ts = load.timescale()
    eph = load('de440.bsp')

    earth = eph['earth']
    moon = eph['moon']
    sun = eph['sun']

    t0 = ts.utc(start_year, 1, 1)
    t1 = ts.utc(end_year, 12, 31)

    print("Finding full moons...")
    f = almanac.moon_phases(eph)
    times, phases = almanac.find_discrete(t0, t1, f)

    full_moons = times[phases == 2]

    print("Checking eclipse geometry...")

    data = []

    for t in full_moons:
        e = earth.at(t)
        m = e.observe(moon).apparent()
        s = e.observe(sun).apparent()

        separation = s.separation_from(m).degrees

        # Geometric approximation for lunar eclipse
        if abs(separation - 180) < 1.5:
            dt = t.utc_datetime()

            if abs(separation - 180) < 0.5:
                eclipse_type = "Total"
            elif abs(separation - 180) < 1.0:
                eclipse_type = "Partial"
            else:
                eclipse_type = "Penumbral"

            data.append({
                "eclipse_date": dt.strftime("%Y-%m-%d"),
                "year": dt.year,
                "type": eclipse_type
            })

    return pd.DataFrame(data)


if __name__ == "__main__":
    df = generate_lunar_eclipses(START_YEAR, END_YEAR)
    df.to_csv("lunar_eclipses_1551_2649.csv", index=False)
    print("Lunar eclipse dataset generated successfully.")
    print(df.head())
