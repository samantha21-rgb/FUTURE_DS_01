import pandas as pd

# Load the Superstore sales dataset
file_path = "data/Sample - Superstore.csv"

df = pd.read_csv(file_path, encoding="latin1")

# Display basic information about the dataset
print("SUPERSTORE SALES ANALYSIS")
print("-" * 40)

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset dimensions:")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nColumn names:")
print(df.columns.tolist())

print("\nDATA QUALITY CHECK")
print("-" * 40)

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nData types:")
print(df.dtypes)

# Convert date columns to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("\nUPDATED DATE TYPES")
print("-" * 40)
print(df[["Order Date", "Ship Date"]].dtypes)

print("\nOrder date range:")
print(df["Order Date"].min(), "to", df["Order Date"].max())


# CORE BUSINESS PERFORMANCE METRICS
print("\nCORE BUSINESS PERFORMANCE")
print("-" * 40)

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_units = df["Quantity"].sum()
average_order_value = total_sales / total_orders

print(f"Total Revenue: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Unique Orders: {total_orders:,}")
print(f"Units Sold: {total_units:,}")
print(f"Average Revenue per Order: ${average_order_value:,.2f}")

profit_margin = (total_profit / total_sales) * 100

print(f"Overall Profit Margin: {profit_margin:.2f}%")


# CATEGORY PERFORMANCE ANALYSIS
print("\nCATEGORY PERFORMANCE")
print("-" * 40)

category_performance = (
    df.groupby("Category")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Units_Sold=("Quantity", "sum"),
        Order_Count=("Order ID", "nunique")
    )
    .sort_values("Total_Sales", ascending=False)
)

category_performance["Profit_Margin_%"] = (
    category_performance["Total_Profit"]
    / category_performance["Total_Sales"] * 100
)

print(category_performance.round(2))


# SUB-CATEGORY PERFORMANCE ANALYSIS
print("\nSUB-CATEGORY PERFORMANCE")
print("-" * 40)

subcategory_performance = (
    df.groupby(["Category", "Sub-Category"])
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Units_Sold=("Quantity", "sum")
    )
)

subcategory_performance["Profit_Margin_%"] = (
    subcategory_performance["Total_Profit"]
    / subcategory_performance["Total_Sales"] * 100
)

print(
    subcategory_performance
    .sort_values("Total_Profit")
    .round(2)
)


# MONTHLY SALES AND PROFIT TRENDS
print("\nMONTHLY SALES AND PROFIT TRENDS")
print("-" * 40)

df["Order Month"] = df["Order Date"].dt.to_period("M")

monthly_performance = (
    df.groupby("Order Month")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Count=("Order ID", "nunique")
    )
)

print("\nFirst 12 months:")
print(monthly_performance.head(12).round(2))

print("\nHighest-revenue month:")
print(monthly_performance["Total_Sales"].idxmax())
print(
    f"Revenue: ${monthly_performance['Total_Sales'].max():,.2f}"
)

print("\nLowest-revenue month:")
print(monthly_performance["Total_Sales"].idxmin())
print(
    f"Revenue: ${monthly_performance['Total_Sales'].min():,.2f}"
)


import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# MONTHLY REVENUE TREND CHART
monthly_sales = monthly_performance.copy()
monthly_sales.index = monthly_sales.index.to_timestamp()

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    monthly_sales.index,
    monthly_sales["Total_Sales"],
    linewidth=2,
    marker="o",
    markersize=3
)

ax.set_title(
    "Monthly Sales Revenue (2014–2017)",
    fontsize=16,
    fontweight="bold",
    pad=15
)
ax.set_xlabel("Month")
ax.set_ylabel("Revenue ($)")
ax.yaxis.set_major_formatter(
    mtick.StrMethodFormatter("${x:,.0f}")
)

ax.grid(True, linestyle="--", alpha=0.3)
fig.tight_layout()

# Save the chart in the outputs folder
fig.savefig(
    "outputs/monthly_sales_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# REGIONAL SALES AND PROFIT ANALYSIS
print("\nREGIONAL PERFORMANCE")
print("-" * 40)

regional_performance = (
    df.groupby("Region")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Order_Count=("Order ID", "nunique")
    )
)

regional_performance["Profit_Margin_%"] = (
    regional_performance["Total_Profit"]
    / regional_performance["Total_Sales"] * 100
)

regional_performance = regional_performance.sort_values(
    "Total_Sales", ascending=False
)

print(regional_performance.round(2))



# DISCOUNT AND PROFITABILITY ANALYSIS
print("\nDISCOUNT AND PROFITABILITY ANALYSIS")
print("-" * 40)

discount_analysis = (
    df.groupby("Discount")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Transaction_Rows=("Row ID", "count")
    )
    .sort_index()
)

discount_analysis["Profit_Margin_%"] = (
    discount_analysis["Total_Profit"]
    / discount_analysis["Total_Sales"] * 100
)

print(discount_analysis.round(2))

print("\nCorrelation between discount and profit:")
print(df["Discount"].corr(df["Profit"]).round(3))



# PRODUCT-LEVEL PROFITABILITY ANALYSIS
print("\n10 LEAST PROFITABLE PRODUCTS")
print("-" * 40)

product_performance = (
    df.groupby(["Product ID", "Product Name", "Category", "Sub-Category"])
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Units_Sold=("Quantity", "sum")
    )
    .reset_index()
)

least_profitable = product_performance.sort_values(
    "Total_Profit", ascending=True
).head(10)

print(least_profitable.round(2).to_string(index=False))



# CHART: 10 LEAST PROFITABLE PRODUCTS
loss_products = least_profitable.sort_values("Total_Profit")

fig, ax = plt.subplots(figsize=(12, 7))

labels = loss_products["Product Name"].str.slice(0, 42)

ax.barh(
    labels,
    loss_products["Total_Profit"]
)

ax.set_title(
    "10 Least Profitable Products",
    fontsize=16,
    fontweight="bold",
    pad=15
)
ax.set_xlabel("Total Profit ($)")
ax.set_ylabel("Product")

ax.axvline(0, linewidth=1)
ax.grid(axis="x", linestyle="--", alpha=0.3)
fig.tight_layout()

fig.savefig(
    "outputs/least_profitable_products.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()



# TOP 10 MOST PROFITABLE PRODUCTS
print("\n10 MOST PROFITABLE PRODUCTS")
print("-" * 40)

most_profitable = product_performance.sort_values(
    "Total_Profit", ascending=False
).head(10)

print(most_profitable.round(2).to_string(index=False))
