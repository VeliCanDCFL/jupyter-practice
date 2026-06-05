# 🐼 Pandas Mastery — 7-Day Roadmap (8 Hours/Day)
# Goal: Use every function in pandas_cheatsheet.py at least once
# Strategy: Hands-on practice with a single dataset throughout the week

## 📋 PREP (30 min before Day 1)
- Download one dataset you'll use all week (suggested: [Titanic](https://www.kaggle.com/c/titanic/data), [House Prices](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset), or any CSV with mixed types)
- Create a folder `pandas-mission/` with 7 notebooks: `day1.ipynb` through `day7.ipynb`
- Keep `pandas_cheatsheet.py` open in a separate tab

---

## DAY 1 — Foundations: Creating & Inspecting Data (8 hours)

### Morning (4h)
| Time | Topic | Practice Tasks |
|------|-------|----------------|
| 0:00-0:30 | **Creating DataFrames** | Create DF from dict of lists, 2D list, `from_dict()`, Series, `date_range()` |
| 0:30-1:30 | **Reading Files** | Load CSV, Excel, JSON, SQL (`pd.read_csv`, `read_excel`, `read_json`, `read_sql`) |
| 1:30-2:00 | Break | ☕ |
| 2:00-3:00 | **Inspecting Data** | Use `head()`, `tail()`, `info()`, `describe()`, `describe(include='all')`, `shape`, `columns`, `dtypes`, `index`, `values`, `sample()`, `empty` |
| 3:00-4:00 | **Review** | Pick a random column — write its stats, first 5 rows, unique count, and dtype without looking at code. Check cheatsheet after. |

### Afternoon (4h)
| Time | Topic | Practice Tasks |
|------|-------|----------------|
| 4:00-5:30 | **Mini Challenge** | Load a NEW dataset from scratch using every creation method. Inspect it with every inspection function. |
| 5:30-6:00 | Break | ☕ |
| 6:00-7:30 | **Time Functions** | `pd.to_datetime()`, `pd.date_range()` — create date-indexed Series/DFs |
| 7:30-8:00 | **Reflection** | Write down 3 functions you forgot. Re-practice them tomorrow morning first. |

---

## DAY 2 — Selecting & Filtering Data (8 hours)

### Morning (4h)
| Time | Topic | Practice Tasks |
|------|-------|----------------|
| 0:00-1:00 | **Column Selection** | `df['col']`, `df[['col1','col2']]`, `.loc[]`, `.iloc[]`, `.at[]`, `.iat[]` |
| 1:00-2:00 | Break | ☕ |
| 2:00-3:30 | **Boolean Filtering** | `df[df['A'] > 5]`, multiple conditions with `& | ~`, `.query()`, `.isin()`, `.between()` |
| 3:30-4:00 | **Review** | Filter your dataset in 5 different ways. Compare results of `.loc` vs `.iloc`. |

### Afternoon (4h)
| Time | Topic | Practice Tasks |
|------|-------|----------------|
| 4:00-5:30 | **Sorting** | `sort_values()` (single/multi column, ascending/descending), `sort_index()` |
| 5:30-6:00 | Break | ☕ |
| 6:00-7:30 | **Challenge** | Filter → sort → select columns chain. Do it with `.loc`, `.query`, and boolean indexing. Compare syntax. |
| 7:30-8:00 | **Reflection** | Write down 3 functions you forgot. Re-practice them tomorrow morning first. |

---

## DAY 3 — Modifying & GroupBy (8 hours)

### Morning (4h)
| Time | Topic | Practice Tasks |
|------|-------|----------------|
| 0:00-1:00 | **Adding/Removing** | `df['new_col'] = ...`, `.drop()`, `.rename()`, `.set_index()`, `.reset_index()` |
| 1:00-2:00 | Break | ☕ |
| 2:00-3:00 | **Advanced Modify** | `.assign()`, `.astype()`, convert dtypes of multiple columns at once |
| 3:00-4:00 | **Review** | Add 3 new columns, rename 2, drop 1, change 2 dtypes. All in one chain. |

### Afternoon (4h)
| Time | Topic | Practice Tasks |
|------|-------|----------------|
| 4:00-5:30 | **GroupBy Basics** | `.groupby().sum()`, `.mean()`, `.count()`, `.size()`, `.first()`, `.last()` |
| 5:30-6:00 | Break | ☕ |
| 6:00-7:30 | **Advanced GroupBy** | `.agg()` with dict, `.pivot_table()`, groupby → filter chain (lambda) |
| 7:30-8:00 | **Reflection** | Write down 3 functions you forgot. Re-practice them tomorrow morning first. |

---

## DAY 4 — Merging & Statistics (8 hours)

### Morning (4h)
| Time | Topic | Practice Tasks |
|------|-------|----------------|
| 0:00-1:00 | **Merge Types** | Create two small DFs. Merge with `inner`, `left`, `right`, `outer` on different keys |
| 1:00-2:00 | Break | ☕ |
| 2:00-3:00 | **Concat** | `pd.concat([df1, df2])` (vertical), `pd.concat([df1, df2], axis=1)` (horizontal) |
| 3:00-4:00 | **Review** | Merge two datasets the same way with all 4 join types. Note differences in row counts. |

### Afternoon (4h)
| Time | Topic | Practice Tasks |
|------|-------|----------------|
| 4:00-5:30 | **Statistics** | `.sum()`, `.mean()`, `.median()`, `.min()`, `.max()`, `.std()`, `.var()`, `.count()` — column-wise and overall |
| 5:30-6:00 | Break | ☕ |
| 6:00-7:30 | **Advanced Math** | `.cumsum()`, `.cummax()`, `.cummin()`, `.diff()`, `.pct_change()` — apply to your dataset |
| 7:30-8:00 | **Reflection** | Write down 3 functions you forgot. Re-practice them tomorrow morning first. |

---

## DAY 5 — Strings & Dates (8 hours)

### Morning (4h)
| Time | Topic | Practice Tasks |
|------|-------|----------------|
| 0:00-1:00 | **String Ops** | `.str.upper()`, `.lower()`, `.strip()`, `.contains()`, `.replace()`, `.split()`, `.len()` |
| 1:00-2:00 | Break | ☕ |
| 2:00-3:00 | **String Advanced** | `.str.extract(r'(\d+)')` — regex extraction on text column |
| 3:00-4:00 | **Review** | Clean a messy text column: strip whitespace, uppercase, replace values, extract numbers. All in one chain. |

### Afternoon (4h)
| Time | Topic | Practice Tasks |
|------|-------|----------------|
| 4:00-5:30 | **Date Ops** | `.dt.year/month/day/hour/minute/second`, `.dt.dayofweek`, `.day_name()`, `.month_name()` |
| 5:30-6:00 | Break | ☕ |
| 6:00-7:30 | **Advanced Dates** | `.to_period('M')`, `pd.Grouper(freq='D')` in groupby, convert with `pd.to_datetime()` |
| 7:30-8:00 | **Reflection** | Write down 3 functions you forgot. Re-practice them tomorrow morning first. |

---

## DAY 6 — Missing Data, Apply & Output (8 hours)

### Morning (4h)
| Time | Topic | Practice Tasks |
|------|-------|----------------|
| 0:00-1:00 | **Detecting NaN** | `.isna()`, `.isnull()`, `.notna()`, `.notnull()` — find missing data in every column |
| 1:00-2:00 | Break | ☕ |
| 2:00-3:00 | **Handling NaN** | `.dropna()`, `.fillna(value)`, `.fillna({'A': 0, 'B': 1})`, `.interpolate()`, fill with mean/median/mode |
| 3:00-4:00 | **Review** | Introduce NaN into your dataset. Detect → fill → verify zero NaNs. All in one chain. |

### Afternoon (4h)
| Time | Topic | Practice Tasks |
|------|-------|----------------|
| 4:00-5:30 | **Apply Functions** | `.apply(lambda)` on Series, row-wise with `axis=1`, `.applymap()` on DataFrame |
| 5:30-6:00 | Break | ☕ |
| 6:00-7:30 | **Deduplication & Output** | `.drop_duplicates()`, `.value_counts()`, `.nunique()`. Write to CSV, Excel, JSON, SQL, Parquet |
| 7:30-8:00 | **Reflection** | Write down 3 functions you forgot. Re-practice them tomorrow morning first. |

---

## DAY 7 — 🏆 Grand Challenge Day (8 hours)

### Morning (4h) — The Ultimate Pandas Pipeline
Build a complete data analysis pipeline from scratch using ALL functions:

```
1. Load data (3 different file formats) → read_csv, read_excel, read_json
2. Create a DataFrame manually → dict, list, from_dict
3. Inspect everything → head, tail, info, describe, shape, columns, dtypes, index, values, sample, empty
4. Clean data → dropna, fillna, replace, drop_duplicates, astype
5. Select/filter → loc, iloc, query, isin, between
6. Sort → sort_values (multi), sort_index
7. Modify → assign, rename, set_index, reset_index
8. GroupBy → groupby with sum/mean/count/size/first/last, agg with dict, pivot_table
9. Merge → merge (all 4 types), concat (both axes)
10. Math → sum/mean/median/min/max/std/var/cumsum/diff/pct_change
11. Strings → str.upper/lower/strip/contains/replace/split/len/extract
12. Dates → dt.year/month/day/hour/minute/second/dayofweek/day_name/month_name/to_period, Grouper
13. Apply → apply on Series, axis=1, applymap
14. Output → to_csv, to_excel, to_json, to_sql, to_parquet
```

### Afternoon (4h)
| Time | Topic | Practice Tasks |
|------|-------|----------------|
| 4:00-6:00 | **New Dataset Challenge** | Pick a completely new dataset. Do the full pipeline without looking at cheatsheet. |
| 6:00-6:30 | Break | ☕ |
| 6:30-7:30 | **Cheatsheet Check** | Open your cheatsheet. For each section, rate yourself: ✅ Know it / ⚠️ Shaky / ❌ Forgot it. Fix the ❌ ones. |
| 7:30-8:00 | **Final Reflection** | What are your top 5 most-used functions now? What are your top 5 weakest? Plan next steps. |

---

## 📊 PROGRESS TRACKER

Mark each function as you practice it:

### Day 1 — Creating & Inspecting
- [ ] `pd.DataFrame()` from dict
- [ ] `pd.DataFrame()` from list
- [ ] `pd.Series()`
- [ ] `pd.read_csv()`
- [ ] `pd.read_excel()`
- [ ] `pd.read_json()`
- [ ] `pd.read_sql()`
- [ ] `pd.DataFrame.from_dict()`
- [ ] `pd.date_range()`
- [ ] `pd.to_datetime()`
- [ ] `.head()`, `.tail()`, `.info()`, `.describe()`
- [ ] `.describe(include='all')`
- [ ] `.shape`, `.columns`, `.dtypes`, `.index`, `.values`
- [ ] `.sample()`, `.empty`

### Day 2 — Selecting & Filtering
- [ ] `df['col']`, `df[['col1','col2']]`
- [ ] `.loc[]`, `.iloc[]`
- [ ] Boolean filter, multiple conditions
- [ ] `.query()`
- [ ] `.isin()`, `.between()`
- [ ] `.sort_values()` (single + multi)
- [ ] `.sort_index()`

### Day 3 — Modifying & GroupBy
- [ ] `df['new_col'] = ...`
- [ ] `.drop()` (rows + cols)
- [ ] `.rename()`, `.set_index()`, `.reset_index()`
- [ ] `.assign()`, `.astype()`
- [ ] `.groupby().sum/mean/count/size/first/last`
- [ ] `.agg()` with dict
- [ ] `.pivot_table()`

### Day 4 — Merging & Statistics
- [ ] `pd.merge()` (inner, left, right, outer)
- [ ] `pd.concat()` (vertical + horizontal)
- [ ] `.sum/mean/median/min/max/std/var/count`
- [ ] `.cumsum/cummax/cummin`
- [ ] `.diff()`, `.pct_change()`

### Day 5 — Strings & Dates
- [ ] `.str.upper/lower/strip/contains/replace/split/len`
- [ ] `.str.extract()` (regex)
- [ ] `.dt.year/month/day/hour/minute/second`
- [ ] `.dt.dayofweek`, `.day_name()`, `.month_name()`
- [ ] `.to_period()`, `pd.Grouper(freq=)`

### Day 6 — Missing Data, Apply & Output
- [ ] `.isna()/isnull()/notna()/notnull()`
- [ ] `.dropna()`, `.fillna()` (scalar + dict)
- [ ] `.interpolate()`
- [ ] `.apply()` (Series + axis=1)
- [ ] `.applymap()`
- [ ] `.drop_duplicates()`, `.value_counts()`, `.nunique()`
- [ ] `.to_csv/to_excel/to_json/to_sql/to_parquet`

### Day 7 — Grand Challenge
- [ ] Full pipeline without cheatsheet ✅
- [ ] Rate all sections: ✅ / ⚠️ / ❌

---

## 💡 TIPS FOR RETENTION
1. **Never copy-paste** — type every function manually to build muscle memory
2. **Before checking the cheatsheet**, try to remember the syntax first
3. **Write comments** in your notebooks explaining what each function does
4. **At the end of each day**, write down 5 functions you forgot — re-practice them next morning
5. **Day 7 is the real test** — if you can complete the pipeline without looking, you've mastered it

## 🎯 SUCCESS CRITERIA
By Day 7 evening, you should be able to:
- ✅ Write pandas code from memory for common tasks
- ✅ Know which function to reach for without checking docs
- ✅ Understand every line in the cheatsheet without hesitation
- ✅ Build a complete data pipeline in under 30 minutes
