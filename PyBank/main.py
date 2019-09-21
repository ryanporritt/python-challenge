import pandas as pd

file = "Resources/budget_data.csv"
# Create a datafile
df_original = pd.read_csv(file)


# The total number of months included in the dataset
Months = df_original["Date"].count()
Total_Months = str(Months)


# The net total amount of "Profit/Losses" over the entire period
ProfitLosses_Total = df_original["Profit/Losses"].sum()
Net_Total = str(ProfitLosses_Total)


# The average of the changes in "Profit/Losses" over the entire period
ProfitLosses_mean = df_original["Profit/Losses"].mean()
Average_Change = str(format(ProfitLosses_mean,'9.2f'))


# The greatest increase in profits (date and amount) over the entire period
ProfitLosses_max = df_original["Profit/Losses"].max()
Greatest_Increase = str(ProfitLosses_max)

# Location of the greates profit
loc_Greatest_Increase = df_original.loc[df_original["Profit/Losses"] == ProfitLosses_max]
Greatest_Increase_Date = df_original.iloc[25, 0]


# The greatest decrease in losses (date and amount) over the entire period
ProfitLosses_min = df_original["Profit/Losses"].min()
Greatest_Decrease = str(ProfitLosses_min)

# Location of the greatest deficit
loc_Greatest_Decrease = df_original.loc[df_original["Profit/Losses"] == ProfitLosses_min]
Greatest_Decrease_Date = df_original.iloc[44, 0]

# Create a new dataframe to house the analysis
df_new = pd.DataFrame({
    "Financial Analysis": ["2010-2017"],
    "Total Months": [Total_Months],
    "Net Total": [("$" + Net_Total)],
    "Average Change": [("$" + Average_Change)],
    "Greatest Increase in Profits": [(Greatest_Increase_Date + " $" + Greatest_Increase)],
    "Greatest Decrease in Profits": [(Greatest_Decrease_Date + " $" + Greatest_Decrease)]
    
})

df = df_new.set_index("Financial Analysis")

# Export dataframe to excel
df.to_excel("output/Financial_Analysis.xlsx")



# Output
print("Financial Analysis")
print("==================================")
print("Total Months: " + Total_Months)
print("Total: $" + Net_Total)
print("Average Change: $" + Average_Change)
print("Greatest Increase in Profits: " + Greatest_Increase_Date + "  ($" + Greatest_Increase + ")")
print("Greatest Decrease in Profits: " + Greatest_Decrease_Date + "  ($" + Greatest_Decrease + ")")