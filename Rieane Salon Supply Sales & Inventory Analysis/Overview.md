# Salon Supply Sales Analysis — Data Cleaning & Forecasting

## Overview

### Project Overview & Scenario
Digitized point-of-sale records for the business weren't available yet, so a synthetic dataset was built using the business's actual product categories (tail combs, gloves, nail products, foundation, eyelash products, eyelash glue) to validate an analysis approach before applying it to the real records once they're digitized. The dataset covers 89,247 transaction rows across 52 products and 96 months (January 2019–December 2026), and was deliberately built messy — mixed date formats, inconsistent text casing, currency-formatted prices, negative quantities — to mirror what a real exported dataset actually looks like.

The goal: turn that raw export into a trustworthy, analysis-ready workbook that could answer two real business questions — how did the pandemic affect sales, and which products need replacing — and build the reporting infrastructure (forecast, budget, dashboard) the business could keep using once real data comes in.

### Tools & Technical Architecture
Built entirely in Google Sheets/Excel, using:
- **SEARCH()** for case/spacing-insensitive text normalization (channel, customer type, category)
- **TRIM()** to catch a whitespace bug that was silently breaking product lookups
- **VLOOKUP** against a purpose-built reference table for unit normalization (44 raw variants → 30 canonical units) and to backfill missing 2026 prices from the current price list
- **SUMIFS / COUNTIF / AVERAGEIF** for the monthly revenue rollups, transaction-count checks, and category-relative benchmarking
- **FORECAST()** (linear regression) for the revenue forecast
- Native Excel/Sheets charts (line, bar) for the EDA and Dashboard tabs

Final workbook structure (10 tabs): raw and cleaned versions of the two source tables, a `Lookup_Tables` reference sheet, a `Forecasting_Budgeting` model, a `Product_Performance` analysis, an `EDA` tab, a `Dashboard`, and a documentation/issue-log tab.

### Challenges & Solutions
- **Four different date formats mixed in one column** (DD-MM-YYYY, MM/DD/YYYY, YYYY/MM/DD, "Mon DD, YYYY") — solved by detecting each pattern and parsing it with its correct rule, rather than one blanket conversion.
- **A stale Year column** that wasn't actually derived from the Date column, producing phantom years (2018, 2027) outside the dataset's real range — rebuilt as a live formula off the corrected date.
- **Exact-string text matching silently failing on real-world variants** — `'WALK-IN STORE'`, `' Online'`, `'on-line'` weren't catching under simple equality checks. Rebuilt with normalized SEARCH()-based matching, which cut "Unknown" categorizations down to only genuinely blank source cells.
- **A raw "Line Total" column that looked reliable but wasn't** — recomputing it from cleaned Price × Quantity uncovered 2,346 rows where the original figure simply didn't match the math, independent of any formatting issue. Net correction: +₱1M.
- **A whitespace bug that broke ~30 products' price lookups** — stray leading/trailing spaces in Product IDs (`' SKU-011 '` vs `'SKU-011'`) were silently failing VLOOKUP matches against the price list. Fixed with TRIM(), which then made it possible to correctly backfill 66 blank 2026 prices.
- **A product-performance metric that was technically correct but practically useless on the first pass** — comparing every product to its 2019 (pre-pandemic) peak flagged 42 of 52 products as "declining," because the *entire business* never recovered to 2019 levels. Redesigned to compare each product's recent trend against its own category's average instead, which correctly isolated 3 products declining for their own reasons rather than the shared macro shock.
- **A forecast that was ~100x too high** — tracing it back, the model was fitting a straight line across all 96 months, letting the old pre-pandemic peak drag the projection way up. Digging further into *why* the most recent months looked like a business collapse (revenue near-zero) revealed the real cause: those months had only 1–4 recorded transactions versus a normal ~600/month — a data-completeness gap, not a real decline. The forecast was rebuilt to exclude those incomplete months from its basis.

### Impact & What I Learned
The cleaning work corrected a net +₱1M in misstated revenue and made 66 previously-blank 2026 prices usable. The forecast and product-performance analysis are both now built on a verified, error-checked foundation rather than numbers that merely looked plausible.

The bigger lesson: a metric or a chart that runs without errors isn't the same as a metric that's *right*. Several of the real findings in this project only surfaced because I went back and checked a "working" result against a second source of truth — checking transaction counts, not just revenue, is what caught the forecast bug; checking the category-level baseline, not just the product's own history, is what caught the flawed first-pass underperformance metric. That habit — verify before you trust a clean-looking output — was the actual skill this project built.

---
**Author:** Kyla Cathrine Hernandez  
**Portfolio:** [https://kylahernandez-portfolio.vercel.app/](https://kylahernandez-portfolio.vercel.app/)
