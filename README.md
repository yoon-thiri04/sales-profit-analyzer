## 📈 Sales Profit Analyzer

An interactive Streamlit web app that helps users analyze monthly **sales**, **expenses**, and **profits** with clean input UI, charts, and data export features.

---

### 🧩 Features

✅ Manually input monthly sales and expenses <br>
✅ Upload CSV file instead of typing manually <br>
✅ Automatic calculation of profit per month <br>
✅ Interactive charts:

* 📊 Line chart
* 📊 Bar chart
* 🥧 Pie chart (only shows positive profit months)

✅ Download summarized data as Excel<br>
✅ Sidebar uploader

---

### 📂 Example CSV Format

To use the **file upload** feature, your CSV file should follow this format:

```csv
Month,Sales,Expenses
Jan,1200,600
Feb,1500,800
Mar,1800,900
...
```

* Column names **must** be: `Month`, `Sales`, and `Expenses`

---

### 🚀 How to Run

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

2. **Save the app code as `app.py`**

3. **Run the app**

```bash
streamlit run app.py
```

4. Open your browser to [http://localhost:8501](http://localhost:8501)

---
