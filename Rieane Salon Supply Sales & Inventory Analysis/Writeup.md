# Salon Supply Sales Analysis — Writeup

### The Business Scenario
The business is a salon supply distributor selling across three channels (Walk-in Store, Online, Salon Delivery) to two customer segments (Retail Customers and Salon/Parlor Partners), spanning categories like Hair Treatment, Hair Color & Bleaching, Nail Care, Makeup Essentials, PPE & Salon Essentials, Shampoo & Conditioner, and Styling Tools & Accessories. The dataset runs January 2019 through December 2026 — squarely spanning the pre-pandemic period, the pandemic itself, and years of recovery — which makes it a genuinely useful case study for understanding how a real small business absorbed and adapted to that shock.

### Core Business Questions
Two questions framed the whole analysis:
1. **What are the sales trends across these years — and did the pandemic affect sales?**
2. **Are there products that need to be replaced? If so, which ones, and why?**

### The Main Finding
**On the pandemic:** revenue collapsed from ~₱1.4M/month (January 2020) to ~₱46K/month (June 2020) — a ~97% drop — in just four months. It recovered gradually and returned to roughly pre-pandemic monthly levels by 2022. But the business's **annual** total never recovered to its 2019 peak: ₱14.1M in 2019 versus ₱3.5M in 2026 (complete months only). Nearly every one of the 52 products individually peaked in 2019, which turned out to be the key complication for the second question (see below).

**On channel behavior**, a pattern worth knowing on its own: Online's share of revenue jumped from 1.6% (2019) to a peak of 29.6% (2021) during pandemic restrictions on in-person shopping, then settled back to ~16–18% post-pandemic — still roughly 10x its pre-pandemic share. Walk-in Store never recovered its former share (27.7% → ~19%). Salon Delivery stayed dominant throughout (60–70% of revenue) and was comparatively resilient during the pandemic itself.

**On products needing replacement:** comparing every product to its own all-time peak was misleading, since that comparison mostly just re-measured the pandemic — nearly all 52 peaked pre-pandemic and the whole business hadn't recovered. Instead, each product's most recent two-year revenue trend (2024→2025→2026) was benchmarked against the **average trend of other products in its own category** over the same period. Every category had declined substantially in that window (roughly -35% to -46% on average) — a broadly difficult two years across the board. Within that context, three products stood out as declining meaningfully faster than their own category peers: **Oze Hair Reborn** (Hair Treatment: -58.9% vs. a category average of -45.7%), **Tail Comb/Rat-tail** (Styling Tools & Accessories: -51.5% vs. -40.9%), and **Disposable Cape** (PPE & Salon Essentials: -58.8% vs. -45.7%) — each declining 10–13 percentage points faster than their peers, not just riding the general downturn.

### The Execution
1. **Diagnosed the raw data.** Audited both source tables (Sales_Transactions, Inventory_PriceList) for structural issues before writing a single cleaning formula — checking distinct value counts, blank rates, and format patterns column by column rather than assuming what was wrong.
2. **Built a raw-vs-cleaned column structure.** Every messy field got a parallel `_Cleaned` column driven by a live formula, so the original data stays intact and every transformation is auditable and explainable.
3. **Cleaned systematically, verifying after each fix.** After each formula change, forced a full recalculation and scanned for formula errors and leftover "Unknown" values — then traced every remaining "Unknown" back to its source to confirm it was a genuine blank, not a missed edge case.
4. **Built the forecasting and budgeting model.** Monthly revenue rollup, a trailing 3-month-average budget, variance and variance %, and a linear-regression forecast — then stress-tested the forecast against reality (checking it against actual trailing months) rather than trusting the formula output at face value, which is what surfaced the data-completeness bug.
5. **Built the product-performance analysis**, including redesigning it after the first version produced an obviously-wrong result (42 of 52 products flagged) — diagnosing *why* it was wrong before rebuilding it, rather than just tweaking the threshold until the output looked better.
6. **Built the reporting layer** — an EDA tab for exploratory charts and a separate Dashboard tab for the at-a-glance, stakeholder-facing summary (KPIs, two headline charts, a flagged-products table) — deliberately kept as two different tools for two different audiences rather than one crowded tab.
7. **Documented everything** in an issue log with real, verified resolutions and magnitudes for every fix, so the whole process is explainable and defensible, not just a finished file with no paper trail behind it.
---
**Author:** Kyla Cathrine Hernandez  
**Portfolio:** [https://kylahernandez-portfolio.vercel.app/](https://kylahernandez-portfolio.vercel.app/)
