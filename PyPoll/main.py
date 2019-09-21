import pandas as pd
file = "Resources/election_data.csv"

# Create a datafile
df_original = pd.read_csv(file)



# Key variables
Total_Votes = df_original["Candidate"].count()

Number_Votes = df_original["Candidate"].value_counts()

Winner_Vote_Total = max(Number_Votes)
Winner_Vote_Total = str(Winner_Vote_Total)


# Khan 
#=======================================================
# Create a dataframe for only Khan
Khan_df = df_original.loc[df_original["Candidate"] == "Khan", :]

# Count only his votes
Khan_Votes = Khan_df["Candidate"].count()
Khan_Votes_Total = str(Khan_Votes)

# Determin Khan's percentage of all votes
Khan_Percent = Khan_Votes / Total_Votes
Khan_Percent = format(Khan_Percent, "5.2%")
#=======================================================


# Correy
#=======================================================
Correy_df = df_original.loc[df_original["Candidate"] == "Correy", :]

Correy_Votes = Correy_df["Candidate"].count()
Correy_Votes_Total = str(Correy_Votes)
Correy_Percent = Correy_Votes / Total_Votes
Correy_Percent = format(Correy_Percent, "5.2%")
#=======================================================


# Li
#=======================================================
Li_df = df_original.loc[df_original["Candidate"] == "Li", :]

Li_Votes = Li_df["Candidate"].count()
Li_Votes_Total = str(Li_Votes)
Li_Percent = Li_Votes / Total_Votes
Li_Percent = format(Li_Percent, "5.2%")
#=======================================================


# O'Tooley
#=======================================================
OTooley_df = df_original.loc[df_original["Candidate"] == "O'Tooley", :]

OTooley_Votes = OTooley_df["Candidate"].count()
OTooley_Votes_Total = str(OTooley_Votes)
OTooley_Percent = OTooley_Votes / Total_Votes
OTooley_Percent = format(OTooley_Percent, "5.2%")
#=======================================================

# Calculate the winner using variables
CalcWinner = pd.DataFrame({
    "Candidate": ["Khan", "Correy", "Li", "O'Tooley"],
    "Total Votes": [Khan_Votes_Total, Correy_Votes_Total, Li_Votes_Total, OTooley_Votes_Total]
})

loc_Winner = CalcWinner.loc[CalcWinner["Total Votes"] == Winner_Vote_Total]

Winner = CalcWinner.iloc[0, 0]


# Create a new dataframe to house the analysis
df_new = pd.DataFrame({
    "Election Results": ["Election Data"],
    "Total Votes": [Total_Votes],
    "Khan": [(Khan_Percent + " " + Khan_Votes_Total)],
    "Correy": [(Correy_Percent + " " + Correy_Votes_Total)],
    "Li": [(Li_Percent + " " + Li_Votes_Total)],
    "O'Tooley": [(OTooley_Percent + " " + OTooley_Votes_Total)],
    "Winner": [Winner]
    
})

df = df_new.set_index("Election Results")

# Export dataframe to excel
df.to_excel("output/Election_Analysis.xlsx")



# Output
print("Election Results")
print("==================================")
print("Total Votes: " + str(Total_Votes))
print("Khan: " + Khan_Percent + " " + Khan_Votes_Total)
print("Correy: " + Khan_Percent + " " + Khan_Votes_Total)
print("Li: " + Khan_Percent + " " + Khan_Votes_Total)
print("O'Tooley: " + Khan_Percent + " " + Khan_Votes_Total)
print("==================================")
print("Winner: " + Winner)
print("==================================")


