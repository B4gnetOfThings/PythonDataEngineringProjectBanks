# Largest Banks Market Capitalization – Data Engineering Project

## 📌 Project Overview

A multi-national firm has hired a data engineer to access, process, transform, and store financial data for managerial reporting across multiple countries.

This project compiles the **Top 10 largest banks in the world ranked by market capitalization (USD)**, transforms the data into multiple currencies, and stores the processed information both as a **CSV file** and in a **relational database**. Managers from different regions can query the database to view market capitalization values in their local currency.

---

## 🎯 Objectives

The project performs the following tasks:

1. Extract tabular data from a public web source under the heading **“By Market Capitalization”**
2. Transform the extracted data by converting market capitalization values from USD to:
   - GBP
   - EUR
   - INR  
   (rounded to 2 decimal places using exchange rates from a CSV file)
3. Store the transformed data:
   - Locally as a CSV file
   - In a relational SQL database
4. Execute SQL queries to support regional reporting needs
5. Log progress throughout execution for traceability and debugging

---

## 🧩 Functional Requirements

### Data Extraction
- Extract the **Top 10 largest banks by market capitalization** from the given URL
- Load the extracted data into a Pandas DataFrame

### Data Transformation
- Read exchange rate information from a CSV file
- Add the following columns:
  - `MC_GBP_Billion`
  - `MC_EUR_Billion`
  - `MC_INR_Billion`
- Round all transformed values to **2 decimal places**

### Data Loading
- Save the transformed DataFrame to:
  - A CSV file (local storage)
  - A SQL database table

### Database Queries
Run the following queries on the database table:

a. **London Office**  
   - Retrieve: `Name`, `MC_GBP_Billion`

b. **Berlin Office**  
   - Retrieve: `Name`, `MC_EUR_Billion`

c. **New Delhi Office**  
   - Retrieve: `Name`, `MC_INR_Billion`

### Logging
- Maintain a log file that records:
  - Start and completion of each major task
  - Data extraction, transformation, loading, and query execution steps

---

## 🛠️ Technologies Used

- **Python**
- **BeautifulSoup** – Web scraping
- **Pandas** – Data manipulation
- **SQLite** – Relational database
- **Requests** – HTTP requests
- **Datetime** – Logging timestamps

---


---

## 🚀 How to Run

1. Install required dependencies:
   ```bash
   pip install pandas requests beautifulsoup4

## ⚖️ Acknowledgement & Disclaimer

This project is an academic and educational exercise based on a data engineering activity
designed by **IBM Skills Network** as part of the **IBM Data Engineering curriculum**.

The original problem statement, learning objectives, and workflow design are credited to **IBM**.
This repository contains an independent implementation created for learning and academic
submission purposes only.

All data sources used are publicly available. No proprietary IBM materials are reproduced or redistributed.

## Jomel C. Felix, CCpE
Learner
