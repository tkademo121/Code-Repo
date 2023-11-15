import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Step 1: Creating Sample Financial Data
np.random.seed(42)

data = {
    'Client_Name': ['CompanyA', 'CompanyB', 'CompanyC'] * 10,
    'Industry': ['Technology', 'Finance', 'Healthcare'] * 10,
    'Revenue': np.random.randint(100000, 500000, 30),
    'Expenses': np.random.randint(50000, 200000, 30),
}

df = pd.DataFrame(data)

# Step 2: Preprocessing and Wrangling (You can customize this based on your data)
# Example: Convert strings to lowercase, handle missing values, etc.
df['Client_Name'] = df['Client_Name'].str.lower()

# Step 3: Model the Code (Not specified in the question, so a placeholder)
# Placeholder for modeling using scikit-learn or any other library

# Step 4: Use Metrics to Evaluate the Model (Not specified in the question, so a placeholder)
# Placeholder for model evaluation metrics

# Step 5: Create a Report using Plotly
fig = make_subplots(rows=1, cols=3, subplot_titles=['Technology', 'Finance', 'Healthcare'])

for industry, col in zip(['Technology', 'Finance', 'Healthcare'], ['blue', 'orange', 'green']):
    industry_data = df[df['Industry'] == industry]
    fig.add_trace(
        go.Bar(x=industry_data['Client_Name'], y=industry_data['Revenue'], name='Revenue', marker_color=col),
        row=1, col=1
    )
    fig.add_trace(
        go.Bar(x=industry_data['Client_Name'], y=industry_data['Expenses'], name='Expenses', marker_color=col),
        row=1, col=2
    )
    fig.add_trace(
        go.Bar(x=industry_data['Client_Name'], y=industry_data['Revenue'] - industry_data['Expenses'],
               name='Profit', marker_color=col),
        row=1, col=3
    )

fig.update_layout(title_text='Financial Data by Industry', showlegend=False)
fig.update_xaxes(title_text='Client Name', row=1, col=1)
fig.update_xaxes(title_text='Client Name', row=1, col=2)
fig.update_xaxes(title_text='Client Name', row=1, col=3)
fig.update_yaxes(title_text='Amount', row=1, col=1)
fig.update_yaxes(title_text='Amount', row=1, col=2)
fig.update_yaxes(title_text='Amount', row=1, col=3)

fig.show()
