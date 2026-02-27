# Ramadan Eclipse Analysis (1551–2649 CE)

## Overview

This repository contains a computational and astronomical analysis of the recurrence of a specific eclipse configuration:

- A lunar eclipse occurring during the first half of Ramadan  
- A solar eclipse occurring during the second half of the same Ramadan  

The study evaluates whether this configuration is historically unique within the Gregorian years 1551–2649 CE.

The analysis is strictly astronomical and computational. It does **not** assess theological interpretation, textual authenticity, or doctrinal implications.

---

## Motivation

In contemporary discussions, it is sometimes asserted that the above eclipse configuration is singular or unprecedented. Given the availability of high-precision astronomical datasets and modern computational tools, such claims can be evaluated empirically.

This project tests recurrence, not interpretation.

---

## Temporal Scope

The interval 1551–2649 CE was selected because it falls within the stable computational range supported by the JPL DE440 planetary ephemeris model.

Within this range:

- Eclipse timing calculations are reliable
- Orbital integration error is minimal
- Recurrence analysis is computationally robust

---

## Methodology Summary

### 1. Lunar Eclipse Detection

Using Skyfield and JPL DE440:

- Full moons were computed
- Sun–Moon angular separation was evaluated
- Eclipse candidates were identified when:

```
|separation − 180°| < 1.5°
```

Classification was approximated using tighter angular thresholds.

---

### 2. Solar Eclipse Detection

- New moons were computed
- Sun–Moon angular separation evaluated
- Eclipse candidates identified when:

```
separation < 1.5°
```

---

### 3. Ramadan Date Generation

Ramadan start and end dates were generated using a tabular Islamic calendar model:

- 30-year leap cycle
- Ramadan = 9th Hijri month
- Dates exported in ISO format (YYYY-MM-DD)

---

### 4. SQL-Based Temporal Matching

All datasets were imported into MySQL with native DATE types.

Matching conditions:

**Full Ramadan:**
```
eclipse_date BETWEEN ramadan_start AND ramadan_end
```

**First Half (Days 1–15):**
```
eclipse_date BETWEEN ramadan_start
AND DATE_ADD(ramadan_start, INTERVAL 14 DAY)
```

**Second Half (Days 16–End):**
```
eclipse_date BETWEEN DATE_ADD(ramadan_start, INTERVAL 15 DAY)
AND ramadan_end
```

A qualifying year required:

- Lunar eclipse in first half
- Solar eclipse in second half
- Both within same Ramadan year

---

## Results

Across the interval 1551–2649 CE:

**102 qualifying Ramadan years** satisfied both conditions.

The full dataset is available here:

https://docs.google.com/spreadsheets/d/17ks2BvVFlOpYD2R9jYb6lEpUnybuSTDwZkB8hPIx4t8

---

## Conclusion

Within the analyzed interval (1551–2649 CE), the specified eclipse configuration occurs multiple times.

Under a literal astronomical interpretation that assumes historical uniqueness, the configuration is therefore not unique within the tested timeframe.

This conclusion is purely computational and astronomical.

---

## Reproducibility

To reproduce the analysis:

1. Install dependencies:

```bash
pip install skyfield pandas numpy
```

2. Run Python notebooks in `/python/`
3. Import CSV files into MySQL using scripts in `/sql/`
4. Execute `analysis_queries.sql`

---

## Limitations

- Eclipse detection is threshold-based (not full shadow-cone modeling)
- Tabular Islamic calendar used (not observational sighting)
- No regional visibility constraints applied
- Analysis limited to 1551–2649 CE

---

## License

This project is released under the MIT License.

---

## Citation

If referencing this work:

> Ramadan Eclipse Analysis (1551–2649 CE), GitHub Repository.
