
# Business Sales Performance Analytics

**Programme:** Future Interns — Data Science & Analytics Internship  
**Task:** FUTURE_DS_01 — Business Sales Performance Analytics  
**Dataset:** Sample Superstore  
**Tools:** Python, Pandas, Matplotlib, Streamlit, Plotly

## 1. Executive Summary

This project examines sales performance, profitability, product contribution, regional differences, and discount patterns using the Sample Superstore dataset.

The dataset covers orders from January 2014 to December 2017. The analysis focuses on identifying where revenue is generated, where profitability is weak, and which areas warrant further investigation by business decision-makers.

The dataset records approximately $2.30 million in sales and $286,397 in profit. However, profitability varies considerably across categories, regions, products, and discount levels. This demonstrates why sales volume alone is insufficient for evaluating business performance.

## 2. Business Objectives

The analysis addresses five objectives:

1. Examine sales trends over time.
2. Compare sales and profitability across product categories and regions.
3. Identify high-performing and loss-making products.
4. Investigate the relationship between discounts and profit.
5. Develop practical recommendations supported by the observed data.

## 3. Dataset and Preparation

The Sample Superstore dataset contains transaction-level sales records and fields relating to orders, dates, products, categories, regions, quantities, discounts, sales, and profit.

Preparation and validation included:

- Loading the CSV dataset with Pandas.
- Converting order and shipping dates into datetime values.
- Converting sales, profit, quantity, and discount fields into numeric values.
- Checking missing values and duplicate records during the initial inspection.
- Removing records with missing values in fields required for the dashboard analysis.

The initial inspection found no missing values and no exact duplicate rows in the original dataset.

The analysis uses the supplied dataset and does not claim that the records represent current commercial activity.

## 4. Methodology

The project uses descriptive data analysis.

- **Sales trends:** Aggregate sales by month to examine changes over time.
- **Category analysis:** Aggregate sales and profit by product category.
- **Regional analysis:** Compare sales, profit, and profit margin across regions.
- **Product analysis:** Rank products by total profit to identify strong and weak contributors.
- **Discount analysis:** Compare aggregate profit and margin at different discount levels.

Profit margin is calculated as:

Profit Margin = Total Profit / Total Sales × 100

The dashboard provides interactive date, region, and category filters. Metrics and visualisations are recalculated from the selected records.

## 5. Key Performance Indicators

| Metric | Result |
|---|---:|
| Total sales | $2,297,200.86 |
| Total profit | $286,397.02 |
| Unique orders | 5,009 |
| Units sold | 37,873 |
| Overall profit margin | 12.47% |
| Analysis period | 2014–2017 |

These indicators establish the overall performance baseline for the dataset.

## 6. Key Findings

### 6.1 Category Performance

Technology generated approximately $836,154 in sales and $145,455 in profit, with a profit margin of approximately 17.40%.

Office Supplies generated approximately $719,047 in sales and $122,491 in profit, with a margin of approximately 17.04%.

Furniture generated approximately $742,000 in sales but only $18,451 in profit, producing a margin of approximately 2.49%.

**Interpretation:** Furniture's comparatively weak margin warrants investigation. The figures alone do not establish whether pricing, product mix, discounts, shipping, or other costs explain the difference.

### 6.2 Regional Performance

The West recorded approximately $725,458 in sales and $108,418 in profit, with a margin of approximately 14.94%.

The East generated approximately $678,781 in sales and $91,523 in profit, with a margin of approximately 13.48%.

The Central region generated approximately $501,240 in sales and $39,706 in profit, with a margin of approximately 7.92%.

The South generated approximately $391,722 in sales and $46,749 in profit, with a margin of approximately 11.93%.

**Interpretation:** The Central region has the lowest regional margin among the four regions. Further analysis should investigate product mix, delivery costs, discounting, and other potential contributors.

### 6.3 Product Profitability

The Canon imageCLASS 2200 Advanced Copier was the highest-profit product identified in the initial analysis, generating approximately $25,200 in profit.

Loss-making products included the Cubify CubeX 3D Printer Double Head Print, which recorded approximately $8,880 in negative profit, and the Lexmark MX611dhe Monochrome Laser Printer, which recorded approximately $4,590 in negative profit.

**Interpretation:** Product-level profitability can differ substantially. Business decisions should consider costs, sales volume, strategic importance, and customer demand before changing product availability.

### 6.4 Discount Patterns

The initial analysis found that records with no discount had an aggregate profit margin of approximately 29.51%.

Some high-discount groups recorded negative aggregate profit. For example, the 70% discount group recorded approximately $40,075 in negative profit.

The initial analysis also found a correlation of approximately -0.219 between discount and profit.

**Interpretation:** The observed correlation indicates a negative association in the analysed data, but it does not prove that discounts alone cause lower profits. Product mix, costs, order characteristics, and other factors may contribute.

### 6.5 Monthly Sales Trends

Monthly aggregation reveals substantial variation in sales over the four-year period. The highest-sales month in the initial analysis was November 2017, with approximately $118,448 in sales.

Monthly patterns should be examined across multiple years before concluding that a particular peak reflects a recurring seasonal effect.

## 7. Business Recommendations

### Recommendation 1: Investigate Furniture profitability

Review Furniture's product-level margins, discount exposure, costs, and pricing. Prioritise the products contributing most to the category's weak profitability.

### Recommendation 2: Examine Central region performance

Compare the Central region's product mix, discount patterns, and fulfilment costs with stronger-performing regions. Use the findings to identify practical opportunities for improvement.

### Recommendation 3: Introduce product-level profitability reviews

Investigate products with persistent negative profit. Evaluate pricing, cost structure, sales conditions, and business importance before deciding whether to reprice, renegotiate costs, or change the assortment.

### Recommendation 4: Review discount policies

Examine the transactions and products associated with high-discount losses. Test proposed discount limits or approval thresholds against a baseline before implementing changes.

### Recommendation 5: Monitor performance regularly

Use the dashboard to review sales, profit, margins, and product performance over consistent reporting periods. Investigate significant changes rather than relying on revenue alone.

## 8. Deliverables

The project includes:

- `analysis.py` — Python-based data inspection and analysis.
- `dashboard.py` — Interactive business intelligence dashboard.
- `data/Sample - Superstore.csv` — Source dataset.
- `outputs/monthly_sales_trend.png` — Monthly sales visualisation.
- `outputs/least_profitable_products.png` — Least-profitable-products visualisation.
- `report.md` — Written analysis and business recommendations.

## 9. Limitations

This project is a descriptive analysis of the supplied historical dataset.

The findings do not establish causal relationships between discounts, regional performance, and profitability. Additional cost, customer, inventory, and operational data would be needed to investigate the underlying causes more rigorously.

The historical results should not be treated as a forecast of future sales or profits.

## 10. Conclusion

The analysis demonstrates that strong revenue does not necessarily translate into strong profitability. Furniture's comparatively low margin, the Central region's weaker margin, product-level losses, and negative profit in some discount groups identify areas for further investigation.

The interactive dashboard makes these patterns easier to explore and supports more evidence-based business decisions.

The project combines data preparation, descriptive analysis, visualisation, and actionable recommendations to address the objectives of FUTURE_DS_01.
