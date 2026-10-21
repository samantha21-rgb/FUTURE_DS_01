
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# =====================================================
# FIELD TERMINAL — FUTURE_DS_01
# =====================================================

st.set_page_config(
    page_title="FIELD TERMINAL | Sales Intelligence",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "Sample - Superstore.csv"

BG = "#090A09"
PANEL = "#101210"
PANEL2 = "#151815"
LINE = "#292C27"
TEXT = "#D8DAD3"
MUTED = "#858A7F"
ORANGE = "#E99A35"
ORANGE2 = "#B86D27"
GREEN = "#83B88A"
RED = "#E46D5D"

# =====================================================
# VISUAL SYSTEM
# =====================================================

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Inter:wght@400;500;600;700&display=swap');

    :root {{
        --bg: {BG};
        --panel: {PANEL};
        --line: {LINE};
        --text: {TEXT};
        --muted: {MUTED};
        --orange: {ORANGE};
    }}

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}

    .stApp {{
        background: var(--bg);
        color: var(--text);
    }}

    [data-testid="stHeader"] {{
        background: var(--bg);
    }}

    [data-testid="stSidebar"] {{
        background: #0D0F0D;
        border-right: 1px solid var(--line);
    }}

    [data-testid="stSidebar"] > div:first-child {{
        padding-top: 1rem;
    }}

    .block-container {{
        max-width: 1900px;
        padding: 1.1rem 1.35rem 2rem;
    }}

    h1, h2, h3, p, label {{
        color: var(--text);
    }}

    h1 {{
        font-size: 1.55rem !important;
        letter-spacing: -.04em !important;
        font-weight: 600 !important;
    }}

    h2 {{
        font-size: .95rem !important;
        font-weight: 600 !important;
    }}

    h3 {{
        font-size: .85rem !important;
    }}

    .terminal-head {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 12px;
        padding: 8px 0 12px;
        border-bottom: 1px solid var(--line);
        margin-bottom: 12px;
    }}

    .terminal-brand {{
        color: var(--orange);
        font-family: 'IBM Plex Mono', monospace;
        font-weight: 600;
        font-size: 1.15rem;
        letter-spacing: -.04em;
    }}

    .terminal-sub {{
        color: var(--muted);
        font-family: 'IBM Plex Mono', monospace;
        font-size: .63rem;
        letter-spacing: .04em;
        text-align: right;
    }}

    .ticker {{
        display: grid;
        grid-template-columns: repeat(5, minmax(0, 1fr));
        background: var(--panel);
        border: 1px solid var(--line);
        margin-bottom: 15px;
    }}

    .ticker-item {{
        padding: 12px 14px;
        min-width: 0;
        border-right: 1px solid var(--line);
    }}

    .ticker-item:last-child {{
        border-right: none;
    }}

    .ticker-label {{
        font-family: 'IBM Plex Mono', monospace;
        color: var(--muted);
        font-size: .61rem;
        text-transform: uppercase;
        letter-spacing: .08em;
        margin-bottom: 8px;
    }}

    .ticker-value {{
        font-family: 'IBM Plex Mono', monospace;
        color: var(--text);
        font-size: clamp(.95rem, 1.5vw, 1.35rem);
        font-weight: 600;
        white-space: nowrap;
    }}

    .ticker-foot {{
        color: var(--muted);
        font-size: .64rem;
        margin-top: 5px;
    }}

    .sectionbar {{
        display: flex;
        justify-content: space-between;
        gap: 10px;
        align-items: center;
        border-bottom: 1px solid var(--line);
        padding-bottom: 8px;
        margin: 17px 0 9px;
    }}

    .sectionbar-title {{
        font-weight: 600;
        font-size: .78rem;
        color: var(--text);
    }}

    .sectionbar-code {{
        font-family: 'IBM Plex Mono', monospace;
        font-size: .6rem;
        color: var(--muted);
    }}

    .panel-note {{
        background: var(--panel);
        border: 1px solid var(--line);
        padding: 11px 13px;
        font-size: .75rem;
        line-height: 1.65;
        color: var(--muted);
        margin-top: 8px;
    }}

    .panel-note strong {{
        color: var(--orange);
    }}

    .stPlotlyChart {{
        background: var(--panel);
    }}

    div[data-testid="stPlotlyChart"] {{
        background: var(--panel);
        border: 1px solid var(--line);
        padding: 3px;
    }}

    [data-testid="stDataFrame"] {{
        border: 1px solid var(--line);
    }}

    [data-testid="stMetric"] {{
        background: var(--panel);
        border: 1px solid var(--line);
        padding: 10px;
    }}

    [data-testid="stMetricLabel"] p {{
        color: var(--muted) !important;
        font-size: .65rem !important;
    }}

    [data-testid="stMetricValue"] {{
        color: var(--text) !important;
        font-size: 1.2rem !important;
    }}

    [data-testid="stExpander"] {{
        border: 1px solid var(--line);
        background: var(--panel);
    }}

    .stCaption, small {{
        color: var(--muted) !important;
    }}

    .stButton > button {{
        background: var(--orange);
        color: #111;
        border: 0;
        border-radius: 2px;
        font-weight: 600;
    }}

    hr {{
        border-color: var(--line);
    }}

    @media (max-width: 850px) {{
        .block-container {{
            padding: .8rem .65rem 1.5rem;
        }}
        .ticker {{
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }}
        .ticker-item {{
            border-bottom: 1px solid var(--line);
        }}
        .ticker-value {{
            font-size: 1rem;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# =====================================================
# DATA
# =====================================================

@st.cache_data
def load_data(path):
    df = pd.read_csv(path, encoding="latin1")

    for col in ["Order Date", "Ship Date"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    for col in ["Sales", "Profit", "Quantity", "Discount"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    required = [
        "Order Date", "Sales", "Profit", "Quantity",
        "Order ID", "Region", "Category", "Product Name",
    ]
    df = df.dropna(subset=required).copy()
    df["Month"] = df["Order Date"].dt.to_period("M").dt.to_timestamp()
    return df


if not DATA_PATH.exists():
    st.error("Missing data/Sample - Superstore.csv. Check your project folder.")
    st.stop()

df = load_data(str(DATA_PATH))

if df.empty:
    st.error("No usable records were found in the dataset.")
    st.stop()

# =====================================================
# FILTERS
# =====================================================

st.sidebar.markdown(
    "<div style='color:#E99A35;font-family:monospace;font-size:12px;'>"
    "FIELD TERMINAL / CONTROLS</div>",
    unsafe_allow_html=True,
)
st.sidebar.title("Analysis scope")

min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()

date_range = st.sidebar.date_input(
    "Order dates",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
)

regions = sorted(df["Region"].dropna().unique())
categories = sorted(df["Category"].dropna().unique())

selected_regions = st.sidebar.multiselect(
    "Regions", regions, default=regions
)
selected_categories = st.sidebar.multiselect(
    "Categories", categories, default=categories
)

if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = end_date = date_range[0]

d = df[
    df["Order Date"].dt.date.between(start_date, end_date)
    & df["Region"].isin(selected_regions)
    & df["Category"].isin(selected_categories)
].copy()

st.sidebar.divider()
st.sidebar.caption(f"{len(d):,} transaction rows in current scope")
st.sidebar.caption("Source: Sample Superstore CSV")

if d.empty:
    st.warning("No matching records. Change the filters.")
    st.stop()

# =====================================================
# CHART HELPER
# =====================================================

def chart_style(fig, height=285):
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=PANEL,
        plot_bgcolor=PANEL,
        height=height,
        font=dict(
            family="IBM Plex Mono, monospace",
            size=10,
            color=TEXT,
        ),
        title=dict(
            font=dict(size=12, color=TEXT),
            x=.02,
            xanchor="left",
        ),
        margin=dict(l=12, r=12, t=42, b=22),
        showlegend=False,
        coloraxis_colorbar=dict(
            tickfont=dict(color=MUTED, size=9),
            outlinewidth=0,
        ),
    )

    fig.update_xaxes(
        showgrid=False,
        linecolor=LINE,
        zerolinecolor=LINE,
        tickfont=dict(color=MUTED, size=9),
    )
    fig.update_yaxes(
        gridcolor=LINE,
        gridwidth=.5,
        zerolinecolor=LINE,
        tickfont=dict(color=MUTED, size=9),
    )
    return fig


def section(title, code):
    st.markdown(
        f"""
        <div class="sectionbar">
            <span class="sectionbar-title">{title}</span>
            <span class="sectionbar-code">{code}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =====================================================
# HEADER
# =====================================================

st.markdown(
    f"""
    <div class="terminal-head">
        <div>
            <div class="terminal-brand">FIELD<span style="color:#D8DAD3">
            / TERMINAL</span></div>
            <div style="font-size:10px;color:#858A7F;margin-top:4px">
            BUSINESS PERFORMANCE INTELLIGENCE
            </div>
        </div>
        <div class="terminal-sub">
            FUTURE_DS_01<br>
            DATASET / SUPERSTORE
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    "<h1>Sales Intelligence</h1>",
    unsafe_allow_html=True,
)
st.caption(
    f"PERIOD {start_date:%d %b %Y} — {end_date:%d %b %Y}"
    f"   /   REGIONS {len(selected_regions)}"
    f"   /   CATEGORIES {len(selected_categories)}"
)

# =====================================================
# TOP METRICS STRIP
# =====================================================

sales = d["Sales"].sum()
profit = d["Profit"].sum()
orders = d["Order ID"].nunique()
units = d["Quantity"].sum()
margin = profit / sales if sales else 0

section("Performance snapshot", "01 / KEY INDICATORS")

st.markdown(
    f"""
    <div class="ticker">
        <div class="ticker-item">
            <div class="ticker-label">Total sales</div>
            <div class="ticker-value">${sales:,.0f}</div>
            <div class="ticker-foot">Recorded revenue</div>
        </div>
        <div class="ticker-item">
            <div class="ticker-label">Total profit</div>
            <div class="ticker-value" style="color:{GREEN if profit >= 0 else RED}">
                ${profit:,.0f}
            </div>
            <div class="ticker-foot">Recorded profit</div>
        </div>
        <div class="ticker-item">
            <div class="ticker-label">Unique orders</div>
            <div class="ticker-value">{orders:,}</div>
            <div class="ticker-foot">Distinct order IDs</div>
        </div>
        <div class="ticker-item">
            <div class="ticker-label">Units sold</div>
            <div class="ticker-value">{units:,.0f}</div>
            <div class="ticker-foot">Total quantity</div>
        </div>
        <div class="ticker-item">
            <div class="ticker-label">Profit margin</div>
            <div class="ticker-value">{margin:.2%}</div>
            <div class="ticker-foot">Profit / sales</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =====================================================
# SALES + REGIONAL PROFITABILITY
# =====================================================

section("Revenue movement / regional risk", "02 / TIME SERIES + REGION")

left, right = st.columns([1.65, 1], gap="small")

monthly = (
    d.groupby("Month", as_index=False)
    .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
)

with left:
    trend = px.line(
        monthly,
        x="Month",
        y="Sales",
        labels={"Month": "Month", "Sales": "Sales ($)"},
    )
    trend.update_traces(
        line=dict(color=ORANGE, width=1.8),
        fill="tozeroy",
        fillcolor="rgba(233,154,53,0.09)",
        hovertemplate="%{x|%b %Y}<br>Sales: $%{y:,.0f}<extra></extra>",
    )
    trend.update_yaxes(tickprefix="$", tickformat=",.2s")
    trend.update_xaxes(nticks=7)
    trend.update_layout(title="Monthly sales trajectory")
    st.plotly_chart(
        chart_style(trend, 300),
        use_container_width=True,
        config={"displayModeBar": False},
    )

with right:
    region = (
        d.groupby("Region", as_index=False)
        .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
    )
    region["Margin"] = region["Profit"] / region["Sales"].replace(0, float("nan"))
    region = region.sort_values("Margin")

    rf = px.bar(
        region,
        x="Margin",
        y="Region",
        orientation="h",
        labels={"Margin": "Profit margin", "Region": ""},
        color_discrete_sequence=[ORANGE],
    )
    rf.update_traces(
        hovertemplate="%{y}<br>Margin: %{x:.2%}<extra></extra>"
    )
    rf.update_xaxes(tickformat=".0%")
    rf.update_layout(title="Regional margin comparison")
    st.plotly_chart(
        chart_style(rf, 300),
        use_container_width=True,
        config={"displayModeBar": False},
    )

# =====================================================
# CATEGORY MIX + DISCOUNT RISK
# =====================================================

section("Category allocation / discount exposure", "03 / MIX + RISK")

left, right = st.columns(2, gap="small")

category = (
    d.groupby("Category", as_index=False)
    .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
)
category["Margin"] = category["Profit"] / category["Sales"].replace(0, float("nan"))

with left:
    fig = go.Figure(
        go.Pie(
            labels=category["Category"],
            values=category["Sales"],
            hole=.60,
            sort=False,
            marker=dict(
                colors=[ORANGE, "#B86D27", "#777B6B"],
                line=dict(color=BG, width=2),
            ),
            textinfo="label+percent",
            textfont=dict(size=10, color=TEXT),
            hovertemplate="%{label}<br>Sales: $%{value:,.0f}<br>%{percent}<extra></extra>",
        )
    )
    fig.update_layout(title="Sales mix by category")
    st.plotly_chart(
        chart_style(fig, 280),
        use_container_width=True,
        config={"displayModeBar": False},
    )

with right:
    discounts = (
        d.groupby("Discount", as_index=False)
        .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
    )
    discounts["Margin"] = discounts["Profit"] / discounts["Sales"].replace(0, float("nan"))

    colors = [
        RED if value < 0 else ORANGE
        for value in discounts["Profit"]
    ]

    disc = go.Figure(
        go.Bar(
            x=discounts["Discount"],
            y=discounts["Profit"],
            marker_color=colors,
            hovertemplate="Discount: %{x:.0%}<br>Profit: $%{y:,.0f}<extra></extra>",
        )
    )
    disc.update_layout(
        title="Profit by discount level",
        xaxis_title="Discount",
        yaxis_title="Profit ($)",
    )
    disc.update_xaxes(tickformat=".0%")
    disc.update_yaxes(tickprefix="$", tickformat=",.2s")
    st.plotly_chart(
        chart_style(disc, 280),
        use_container_width=True,
        config={"displayModeBar": False},
    )

# =====================================================
# PRODUCT PROFIT AND DATA TABLE
# =====================================================

section("Product profitability", "04 / WINNERS + LOSSES")

products = (
    d.groupby("Product Name", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Units=("Quantity", "sum"),
    )
)

left, right = st.columns(2, gap="small")

with left:
    top = products.nlargest(7, "Profit").sort_values("Profit")
    fig = px.bar(
        top,
        x="Profit",
        y="Product Name",
        orientation="h",
        labels={"Profit": "Profit ($)", "Product Name": ""},
        color_discrete_sequence=[ORANGE],
    )
    fig.update_xaxes(tickprefix="$", tickformat=",.2s")
    fig.update_layout(title="Top products by profit")
    st.plotly_chart(
        chart_style(fig, 300),
        use_container_width=True,
        config={"displayModeBar": False},
    )

with right:
    bottom = products.nsmallest(7, "Profit").sort_values("Profit")
    fig = px.bar(
        bottom,
        x="Profit",
        y="Product Name",
        orientation="h",
        labels={"Profit": "Profit ($)", "Product Name": ""},
        color_discrete_sequence=[RED],
    )
    fig.update_xaxes(tickprefix="$", tickformat=",.2s")
    fig.update_layout(title="Lowest-profit products")
    st.plotly_chart(
        chart_style(fig, 300),
        use_container_width=True,
        config={"displayModeBar": False},
    )

section("Transaction intelligence", "05 / DETAIL TABLE")

with st.expander("Open product-level data"):
    product_table = products.sort_values("Profit").copy()
    st.dataframe(
        product_table,
        use_container_width=True,
        hide_index=True,
        height=320,
        column_config={
            "Product Name": st.column_config.TextColumn("Product"),
            "Sales": st.column_config.NumberColumn("Sales", format="$%.2f"),
            "Profit": st.column_config.NumberColumn("Profit", format="$%.2f"),
            "Units": st.column_config.NumberColumn("Units", format="%d"),
        },
    )

with st.expander("Open regional, category and discount breakdowns"):
    tab1, tab2, tab3 = st.tabs(["Regions", "Categories", "Discounts"])

    with tab1:
        st.dataframe(
            region,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Sales": st.column_config.NumberColumn(format="$%.2f"),
                "Profit": st.column_config.NumberColumn(format="$%.2f"),
                "Margin": st.column_config.NumberColumn(format="%.2%"),
            },
        )

    with tab2:
        st.dataframe(
            category,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Sales": st.column_config.NumberColumn(format="$%.2f"),
                "Profit": st.column_config.NumberColumn(format="$%.2f"),
                "Margin": st.column_config.NumberColumn(format="%.2%"),
            },
        )

    with tab3:
        st.dataframe(
            discounts,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Discount": st.column_config.NumberColumn(format="percent"),
                "Sales": st.column_config.NumberColumn(format="$%.2f"),
                "Profit": st.column_config.NumberColumn(format="$%.2f"),
                "Margin": st.column_config.NumberColumn(format="%.2%"),
            },
        )

# =====================================================
# INTERPRETATION
# =====================================================

section("Analyst notes", "06 / ACTIONABLE FINDINGS")

weak_cat = category.loc[category["Margin"].idxmin()]
weak_region = region.loc[region["Margin"].idxmin()]
loss_count = int((products["Profit"] < 0).sum())
negative_discount_count = int((discounts["Profit"] < 0).sum())

st.markdown(
    f"""
    <div class="panel-note">
    <strong>01 / CATEGORY</strong><br>
    {weak_cat["Category"]} has the lowest category margin in the current
    selection ({weak_cat["Margin"]:.2%}). Investigate pricing, costs,
    product mix and discount exposure.
    </div>
    <div class="panel-note">
    <strong>02 / REGION</strong><br>
    {weak_region["Region"]} has the lowest regional margin in the current
    selection ({weak_region["Margin"]:.2%}). Compare shipping costs,
    product mix and promotional activity.
    </div>
    <div class="panel-note">
    <strong>03 / PRODUCT</strong><br>
    {loss_count} products have negative total profit in the current
    selection. Review the largest losses and underlying costs before
    changing the assortment.
    </div>
    <div class="panel-note">
    <strong>04 / DISCOUNT</strong><br>
    {negative_discount_count} discount levels have negative aggregate profit
    in this selection. This association does not prove that discounting
    alone caused the losses; investigate orders and test pricing changes.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div style="border-top:1px solid {LINE};margin-top:25px;padding-top:12px;
    display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;
    color:{MUTED};font-family:monospace;font-size:10px;">
        <span>FIELD / TERMINAL</span>
        <span>FUTURE_DS_01</span>
        <span>SUPERSTORE / SALES ANALYSIS</span>
    </div>
    """,
    unsafe_allow_html=True,
)
