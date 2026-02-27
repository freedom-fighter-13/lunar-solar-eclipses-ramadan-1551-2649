# generate_solar_eclipses.py

from skyfield.api import load
from skyfield import almanac
import pandas as pd

START_YEAR = 1551
END_YEAR = 2649

def generate_solar_eclipses(start_year, end_year):

    ts = load.timescale()
    eph = load('de440.bsp')

    earth = eph['earth']
    sun = eph['sun']
    moon = eph['moon']

    t0 = ts.utc(start_year, 1, 1)
    t1 = ts.utc(end_year, 12, 31)

    print("Finding new moons...")
    f = almanac.moon_phases(eph)
    times, phases = almanac.find_discrete(t0, t1, f)

    new_moons = times[phases == 0]

    data = []

    for t in new_moons:
        e = earth.at(t)
        s = e.observe(sun).apparent()
        m = e.observe(moon).apparent()

        separation = s.separation_from(m).degrees

        # Geometric approximation for solar eclipse
        if separation < 1.5:
            dt = t.utc_datetime()

            if separation < 0.3:
                eclipse_type = "Total"
            elif separation < 0.7:
                eclipse_type = "Annular"
            elif separation < 1.0:
                eclipse_type = "Hybrid"
            else:
                eclipse_type = "Partial"

            data.append({
                "eclipse_date": dt.strftime("%Y-%m-%d"),
                "year": dt.year,
                "type": eclipse_type
            })

    return pd.DataFrame(data)


if __name__ == "__main__":
    df = generate_solar_eclipses(START_YEAR, END_YEAR)
    df.to_csv("solar_eclipses_1551_2649.csv", index=False)
    print("Solar eclipse dataset generated successfully.")
    print(df.head())
