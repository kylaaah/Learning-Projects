# Global FX & Payment Operations Dashboard

## 📖 Project Overview & Scenario
**The Problem:** A company was losing money on international transfers because payment processors were secretly adding hidden fees and using bad exchange rates. 

**The Solution:** This project is an automated data pipeline and Power BI dashboard built to solve that problem. It tracks cross-border payments, finds hidden fees (known as cost leakage), and automatically flags high-risk transactions for managers to review. In this sample, the dashboard successfully tracked $3.74 million in payments and found $91,011 in hidden fees.

##  Tools & Technical Architecture
*   **Python (Pandas, Requests):** Wrote a script to pull real-time European Central Bank exchange rates using the Frankfurter API and generate a sample dataset of international transactions.
*   **SQL (SQLite3):** Cleaned and saved the processed data into a structured relational database (`fx_operations.db`) to show enterprise-level data handling.
*   **Business Logic (Python):** Used Python rules to automatically tag risky transactions. For example, it flags payments over $10,000 as "REVIEW: HIGH VALUE" and provider markups over 3% as "REVIEW: HIGH SPREAD".
*   **Power BI:** Built a dashboard with executive summaries, trend lines to track daily losses, and an interactive queue for managers to easily filter and review flagged transactions.

##  Challenges & Solutions
*   **Challenge:** I needed to show real-world financial losses, but I didn't have access to a real company's private payment data.
*   **Solution:** I wrote a Python function that applied random hidden fees (1% to 4%) to live market exchange rates[. This accurately copied how real payment processors hide their fees.
*   **Challenge:** Making sure the dashboard was a useful daily tool for a manager, not just a static picture.
*   **Solution:** I added an interactive "Compliance Queue" filter. Managers can simply click "REVIEW: HIGH SPREAD" to instantly see exactly which transactions need their attention that day.

##  Impact & What I Learned
*   **Why It Matters:** This tool gives businesses clear visibility into their payment flows. It protects company profits by showing exactly which currencies (like PHP, AUD, or JPY) are costing the most in hidden fees.
*   **What I Learned:** I learned how to connect data engineering (APIs, Python, SQL) with real business needs. I successfully turned raw data into a functional tool that helps finance teams make faster, better decisions.

---
**Author:** Kyla Cathrine Hernandez  
**Portfolio:** [https://kylahernandez-portfolio.vercel.app/](https://kylahernandez-portfolio.vercel.app/)
