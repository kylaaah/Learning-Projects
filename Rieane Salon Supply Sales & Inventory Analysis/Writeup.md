# Salon Supply Sales Analysis — Writeup

## The Business Scenario

The dataset represents a small, family-owned salon supply business serving parlors through a physical store, direct delivery, and online orders. Because its real transaction history isn't yet digitized, this project used a deliberately messy synthetic dataset — spanning 2019 through 2026 — to validate an analysis approach that can be applied directly once real point-of-sale data comes online.

## Core Business Questions

The analysis was built to answer two questions: How has revenue recovered since the pandemic, and what should the business expect in the near term? And, which products, if any, are underperforming relative to their own category and may need to be discontinued or repositioned?

## The Main Finding

The standout finding wasn't a business insight — it was catching a broken one before it shipped. An early forecast overstated near-term revenue by roughly 100x. Rather than presenting that number, I traced it back to a data-completeness gap in the four most recent months and rebuilt the model on a valid basis, turning a plausible-looking but wrong forecast into a usable one.

## The Execution

I cleaned the raw data column by column — dates, categories, channels, product IDs, units, prices, quantities, and line totals — documenting each fix in an issue log. On top of the cleaned data, I built a forecast and budget model, then a product-performance flag comparing each product to its own category average (an improvement on my first version, which compared products to their all-time peak and wrongly flagged 42 of 52 as declining). I built four EDA charts and a separate summary Dashboard, adjusting along the way when a chart type didn't render reliably. I closed the process with a full recalculation and cell-by-cell scan across all 12 sheets to confirm zero formula errors before calling it done.
