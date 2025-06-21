import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title="Sale Profit Analyzer", layout="centered")

st.title("📈 Sales Profit Analyzer")

# File Upload

st.sidebar.header("📤 Upload Your Data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaed successfully!")

    expected_columns ={"Month","Sales","Expenses"}

    if not expected_columns.issubset(df.columns):
        st.error("CSV must have columns: Month, Sales, Expeneses")

    else:
        df = df[["Month","Sales","Expenses"]]
        df["Profit"] = df["Sales"] - df["Expenses"]

else:
    st.info("No file uploaded. You can manually enter data below!")


    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    sales,expenses = [],[]
    for row in range(2):
        cols =st.columns(6)
        for i, month in enumerate(months[row*6:(row+1)*6]):
            with cols[i]:
                s = st.number_input(f"{month} Sales", min_value=0, step=100, value=1000,key=f"sales_{month}")
                e = st.number_input(f"{month} Expenses", min_value=0, step=100, value=1000,key=f"exp_{month}")
                sales.append(s)
                expenses.append(e)


    df = pd.DataFrame(
        {
            "Month":months,
            "Sales":sales,
            "Expenses":expenses
        }
    )

    df["Profit"]= df["Sales"]-df["Expenses"]


#Display Data Table

st.subheader("📋 Monthly Summary")
st.dataframe(df.set_index("Month"))


from io import BytesIO

output= BytesIO()
df.to_excel(output, index=False, sheet_name="Sales Summary")
st.download_button(
    label= " Download as Excel",
    data = output.getvalue(),
    file_name="sales_summary.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# Visualizations
st.header("📊 Visualize Your Data")

chart_type = st.selectbox("Choose Chart Type", ["Line Chart","Bar Chart","Pie Chart (Profit Distribution)"])

if chart_type=="Line Chart":
    st.line_chart(df.set_index("Month")[["Sales","Expenses","Profit"]])

elif chart_type=="Bar Chart":
    st.bar_chart(df.set_index("Month")[["Sales","Expenses","Profit"]])

elif chart_type=="Pie Chart (Profit Distribution)":
    fig, ax = plt.subplots()

    ax.pie(df["Profit"], labels=df["Month"], autopct="%1.1f%%")
    ax.set_title("Profit by Month")
    st.pyplot(fig)




# Summary Stats
st.subheader("Summary Stats")
st.write(f"**Total Sales:** ${df["Sales"].sum():,.2f}")
st.write(f"**Total Expenses:**${df["Expenses"].sum():,.2f}")
st.write(f"**Total Profit:** ${df["Profit"].sum():,.2f}")


##comment