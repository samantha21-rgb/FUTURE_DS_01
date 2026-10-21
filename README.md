# Superstore Sales Performance Analytics

**Future Interns — Data Science & Analytics Internship | Task 1 (2026)**

## Project Overview

This project analyzes retail sales transactions to evaluate business performance, identify profitable and loss-making products, examine regional differences, and investigate the relationship between discounts and profitability.

The objective is to transform raw sales data into actionable business insights that can support better commercial decisions.

## Business Questions

- Which products generate the highest and lowest profits?
- How do sales and profits change over time?
- Which product categories and regions perform best?
- How are discounts associated with profitability?
- What actions could improve business performance?

## Tools and Technologies

- Python
- pandas — data preparation and analysis
- Matplotlib — data visualization
- Git and GitHub — project version control and documentation

## Dataset

**Dataset:** Sample - Superstore

The dataset contains retail transaction information, including order dates, shipping dates, customers, geographical regions, product categories, sales, quantities, discounts, and profit.

The analyzed order dates range from January 2014 to December 2017.

The dataset is used for educational and analytical purposes. Refer to the original dataset provider for its licensing and usage conditions.

## Methodology

1. **Data inspection:** Examined column names, data types, missing values, and duplicate rows.
2. **Data preparation:** Converted order and shipping dates into datetime values for time-based analysis.
3. **Business performance analysis:** Calculated total sales, total profit, unique orders, units sold, average revenue per order, and overall profit margin.
4. **Category and sub-category analysis:** Compared sales, profit, unit volumes, and profit margins.
5. **Time-series analysis:** Aggregated sales and profit by month and identified the highest- and lowest-revenue months.
6. **Regional analysis:** Compared sales, profit, order counts, and profit margins across regions.
7. **Product profitability analysis:** Identified the ten most profitable and ten least profitable products.
8. **Discount analysis:** Compared profitability across discount levels and calculated the correlation between discount and profit.

## Key Findings

- **Overall performance:** Total sales were $2,297,200.86, with recorded profit of $286,397.02 and an overall profit margin of 12.47%.
- **Category performance:** Technology generated the highest sales at $836,154.03 and the highest category profit at $145,454.95.
- **Furniture profitability:** Furniture generated $741,999.80 in sales but had a profit margin of only 2.49%.
- **Loss-making sub-categories:** Tables recorded a loss of $17,725.48, while Bookcases recorded a loss of $3,472.56.
- **Regional performance:** West generated the highest sales at $725,457.82 and the highest regional profit at $108,418.45.
- **Product profitability:** The Canon imageCLASS 2200 Advanced Copier had the highest total product profit among the products analyzed, at $25,199.93.
- **Discount relationship:** The correlation between discount and profit was -0.219, indicating a weak negative linear association in this dataset.
- **Monthly sales:** November 2017 was the highest-revenue month at $118,447.82, while February 2014 was the lowest at $4,519.89.

## Business Recommendations

1. **Investigate loss-making products:** Review pricing, costs, and discounting for loss-making Tables, Bookcases, and individual machine products before making pricing or assortment decisions.
2. **Review discount policies:** Evaluate high-discount transactions to understand whether discount levels are commercially sustainable.
3. **Protect strong category performance:** Examine the products and customer segments contributing to Technology's strong profitability.
4. **Investigate regional differences:** Review product mix, discounting, and other relevant factors in Central, where the observed profit margin was lower than in the other regions.
5. **Monitor performance over time:** Track monthly sales and profit together to identify sustained changes rather than relying on individual high- or low-performing months.

These recommendations are preliminary and should be validated with further transaction-level analysis before implementation.

## Project Outputs

The `outputs/` directory contains generated visualizations, including:

- `monthly_sales_trend.png`
- `least_profitable_products.png`

## Limitations

- The analysis is descriptive and does not establish causal relationships.
- Correlation between discounts and profit does not prove that discounts cause lower profits.
- The dataset does not necessarily represent current retail market conditions.
- Additional investigation is needed to determine the causes of product-level and regional profitability differences.

## How to Run

1. Install Python.
2. Install the required libraries:

   `python -m pip install pandas matplotlib`

3. Place the dataset at `data/Sample - Superstore.csv`.
4. Run the analysis:

   `python analysis.py`

## Conclusion

This project demonstrates how data analysis can support business decisions by identifying sales patterns, measuring profitability, and highlighting areas that warrant further investigation. It combines data preparation, descriptive analysis, visualization, and business-focused recommendations in response to the Future Interns Task 1 brief.

---

**Prepared for:** Future Interns Data Science & Analytics Internship  
**Task:** Business Sales Performance Analytics  
**Repository:** `future-ds-task1`