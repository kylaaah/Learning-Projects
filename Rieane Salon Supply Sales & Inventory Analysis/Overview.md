# Salon Supply Sales Analysis — Overview

## Project Overview & Scenario

This project analyzes six years (2019–2026) of transaction data from a family-run salon supply business that sells haircare, nail care, PPE, and salon-essential products to parlors — through walk-in retail, salon delivery, and (in later years) an online channel. Since the business's real point-of-sale records aren't digitized yet, I built a synthetic dataset that mirrors exactly what a real data export would look like — mixed formats, entry errors, and all — to design and pressure-test a full cleaning-to-reporting pipeline *before* pointing it at the real thing.

## Tools & Technical Architecture

Built entirely in Excel workbook: raw and cleaned transaction tables kept side by side for auditability, a `Lookup_Tables` sheet for unit standardization, a `Forecasting_Budgeting` tab (actual revenue, trailing 3-month budget, variance, linear-trend forecast), a `Product_Performance` tab benchmarking all 52 products against their own category peers, an `EDA` tab with four exploratory charts, a stakeholder-facing `Dashboard`, and an `Insights` tab documenting the issue log and findings. Core techniques: SEARCH-based text normalization, TRIM, VLOOKUP, SUMIF/SUMIFS, INDEX/MATCH, SMALL, and FORECAST.

## Challenges & Solutions

Nearly every column had its own break-fix story: four different raw date formats parsed by pattern; inconsistent category/channel text normalized with SEARCH; 439 negative quantities corrected with `ABS()` instead of dropped; 2,346 rows where Line Total didn't actually equal Price × Quantity, recomputed from cleaned values (a net +₱1,034,355 correction); and 44 raw unit variants collapsed into ~30 real units via a dedicated lookup table.

The hardest problem, though, wasn't a formatting bug — it was the forecast. A first-pass model projected ~₱330K for Q1 2027 while the last four months of actuals looked near zero. Checking transaction *volume* behind those numbers (rather than trusting revenue alone) revealed the real cause: those months had only 1–4 recorded transactions each, versus a normal 500–700 — a data-completeness gap, not a business collapse. Rebuilding the forecast to exclude the incomplete months brought it back in line with reality (₱389K–396K).

## Impact & What I Learned

The corrected analysis surfaced three actionable findings: three of 52 products declining meaningfully faster than their category peers and worth discontinuing or repositioning; a lasting shift toward online sales (1.6% of revenue in 2019 to ~16–18% by 2026, well above the pre-pandemic baseline); and a forecast that's now trustworthy enough to actually plan around.

The bigger lesson was about judgment, not formulas: a plausible, technically-correct number isn't automatically a meaningful one, and the habit that catches the difference is checking the data *behind* a metric before trusting it. I also learned to design for two different audiences — an EDA tab for my own working analysis, and a separate Dashboard for someone with 30 seconds — rather than assuming one chart set can serve both.

---
**Author:** Kyla Cathrine Hernandez  
**Portfolio:** [https://kylahernandez-portfolio.vercel.app/](https://kylahernandez-portfolio.vercel.app/)
