# GameZone Orders — Data Cleaning, EDA & Business Insights

## 📖 Project Overview & Scenario
**The Problem:** GameZone, an online gaming-equipment retailer (consoles, monitors, laptops, accessories), had raw order-level export data — but it was full of inconsistent date formats, duplicate categories, missing values, and unresolved duplicate order IDs. No one could confidently answer: *how is revenue trending across products, regions, and marketing channels, and what should Finance, Sales, and Marketing actually do about it?*

**The Solution:** This project applies a structured, repeatable data-cleaning framework (Conceptualize → Locate → Evaluate → Augment → Document) to ~21,900 raw order rows, then runs a stakeholder-driven EDA process (the SCAN framework) to turn a cleaned dataset into department-specific, actionable recommendations. The result: **$6.15M in tracked revenue** analyzed across products, regions, and marketing channels, with findings routed directly to Finance, Sales, and Marketing.

##  Tools & Technical Approach
* **Excel (Advanced):** Full data-cleaning workflow using formulas (`DATE`, `IF`, lookups), a structured issue log, and separate `_CLEANED` columns kept alongside raw columns for auditability.
* **PivotTables:** Built multi-dimensional pivot summaries (revenue by product × month × year) to surface trends and ranges, with sparklines for at-a-glance movement.
* **Data Cleaning Framework:** A 5-step process — *Conceptualize* the grain/metrics/dimensions, *Locate* solvable issues (formats, categorization, nulls, duplicates), *Evaluate* unsolvable issues (true nulls, outliers, business-logic violations), *Augment* the dataset with new dimensions/metrics/time grains, and *Document* every decision in a resolution log.
* **SCAN Framework for EDA:** Stakeholder goals → Columns & coverage → Aggregates & anomalies → Notable segments, used to keep exploratory analysis tied to real business questions instead of open-ended poking around.
* **Business Logic Validation:** Added calculated columns (e.g. time-to-ship, a ship-before-purchase flag) to catch violations a simple null/duplicate check would miss.

##  Challenges & Solutions
* **Challenge:** The raw data mixed inconsistent date formats, near-duplicate category labels (e.g. product names differing only by spelling), and blank values across several columns.
  **Solution:** Built a formal issue log (table, column, issue, row count, magnitude, solvable Y/M/N, resolution) before making any changes, so every fix is traceable and repeatable rather than ad hoc.
* **Challenge:** Some "missing" or "unknown" values looked like data errors at first glance, but on closer inspection were legitimate business categories (e.g. a system-assigned "unknown" account-creation method) rather than broken data.
  **Solution:** Cross-checked raw values before deciding on a resolution, and only imputed values ("unknown category" bucket) where there was no reliable way to recover the true value — following the rule of never imputing without a real source of truth.
* **Challenge:** A duplicate-order-ID check surfaced 145 order IDs appearing more than once, which conflicted with the original assumption that each row represented one unique order.
  **Solution:** Flagged this directly in the issue log as an open item requiring a grain decision, rather than silently aggregating around it — a reminder to validate grain assumptions against the data itself, not just the stated business question.
* **Challenge:** A summary pivot table's reported trend window needs to actually match the underlying data's real date coverage, or every downstream conclusion inherits the error.
  **Solution:** Went back and reconciled the derived time-grain columns against the raw purchase-date column to confirm the reporting window was accurate before finalizing any insights — a core sanity check now baked into the process.

##  Impact & What I Learned
* **Why It Matters:** This process turns a messy raw export into a trustworthy source of truth that different teams can act on immediately — Finance gets revenue trends and forecasting inputs, Sales gets product-performance data to guide bundling and inventory decisions, and Marketing gets channel-level data to reduce over-reliance on any single acquisition source.
* **Key Findings:**
  * **$6.15M** in total revenue tracked across **~21,900 order rows**.
  * **27in 4K Gaming Monitor** was the top-performing product (~$1.97M), while a handful of products (e.g. one gaming headset SKU) showed unusually low revenue — flagged for follow-up with the product team rather than taken at face value, since it looked more like a data-completeness issue than a true sales signal.
  * Direct traffic was the dominant marketing channel by a wide margin, informing a recommendation to diversify acquisition channels rather than depend on one.
* **What I Learned:** I learned that data cleaning isn't a checklist to rush through — it's where most of the actual judgment in analytics happens: deciding what's a real error versus a legitimate business value, when to fix something yourself versus escalate to a stakeholder, and how to verify that a summary table's headline numbers actually match what the raw data supports before writing conclusions from it. That last habit — tracing a finding back to its source before presenting it — is the one I now treat as non-negotiable.

---
**Author:** Kyla Cathrine Hernandez
**Portfolio:** [https://kylahernandez-portfolio.vercel.app/](https://kylahernandez-portfolio.vercel.app/)
