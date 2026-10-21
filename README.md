
# FIELD / Sales Intelligence

### FUTURE_DS_01 — Business Sales Performance Analytics

A data analytics project examining sales performance, profitability, product contribution, regional differences, and discount patterns using the Sample Superstore dataset.

The project combines Python-based analysis, interactive visualisation, and business recommendations to support evidence-based decision-making.

## Project objectives

- Analyse sales trends over time.
- Identify high-performing and low-performing product categories.
- Compare regional sales and profitability.
- Investigate product-level profit and loss.
- Examine discount patterns and their relationship with profitability.
- Present findings through an interactive dashboard and written report.

## Technology stack

- Python
- Pandas
- Matplotlib
- Streamlit
- Plotly

## Repository structure

```text
FUTURE_DS_01/
├── analysis.py
├── dashboard.py
├── report.md
├── README.md
├── requirements.txt
├── data/
│   └── Sample - Superstore.csv
└── outputs/
    ├── monthly_sales_trend.png
    └── least_profitable_products.png
```

## Key findings

The initial analysis of the 2014–2017 dataset identified:

| Metric | Result |
|---|---:|
| Total sales | $2,297,200.86 |
| Total profit | $286,397.02 |
| Unique orders | 5,009 |
| Units sold | 37,873 |
| Overall profit margin | 12.47% |

### Selected insights

- **Technology:** Approximately $836,154 in sales and $145,455 in profit.
- **Office Supplies:** Approximately $719,047 in sales and $122,491 in profit.
- **Furniture:** Approximately $742,000 in sales but only $18,451 in profit, indicating a comparatively low margin.
- **Regional performance:** The Central region recorded a profit margin of approximately 7.92% in the initial analysis.
- **Discounts:** Some high-discount groups recorded negative aggregate profit. This is an association requiring further investigation, not proof of causation.

See [`report.md`](report.md) for the methodology, detailed findings, limitations, and recommendations.

## Run the analysis

From the project root, install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the analysis script:

```bash
python analysis.py
```

## Run the interactive dashboard

Start Streamlit:

```bash
python -m streamlit run dashboard.py
```

The dashboard provides date, region, and category filters, along with interactive visualisations of sales, category performance, regional margins, product profitability, and discount patterns.

## Visual outputs

The analysis script generates the following charts:

- `outputs/monthly_sales_trend.png`
- `outputs/least_profitable_products.png`

## Business recommendations

1. Investigate the factors contributing to Furniture's low margin.
2. Examine product mix, costs, and discounting in the Central region.
3. Review products with persistent negative profit.
4. Evaluate discount practices using product-level evidence and controlled tests.
5. Monitor profitability alongside revenue when assessing business performance.

## Limitations

This is a descriptive analysis of historical data. The observed patterns do not establish causation, and the results should not be treated as a forecast of future performance.

## Project author

Prepared as part of the Future Interns Data Science & Analytics Internship, Task FUTURE_DS_01.
