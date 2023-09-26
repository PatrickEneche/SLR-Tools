# This is a simple python script that can be used to remove duplicates (both exact and fuzy types) from a list of items stored in .csv format.
# Ensure [pip install pandas], [pip install numpy] and [pip install fuzzywuzzy] are first initiated before proceeding with this tool.

import pandas as pd
import numpy as np
import fuzzywuzzy
from fuzzywuzzy import fuzz, process

t_value = int(input("Enter threshold value, preferably between 70 - 100: "))
# This is the threshold value for which the fuzy descrepancies will be removed


def Deduper(x):  # A simple function to remove exact and fuzzy duplicates from a long list of literature usually necessary in the systematic literature review
    df = pd.read_csv(x)
    Exact_Dedup = df.drop_duplicates(subset=["Title"])
    # This will drop duplicates based on title of papers. One of the columns in the csv file must be "Title"
    Exact_Dedup_doi = Exact_Dedup.drop_duplicates(subset=["Doi"])
    # This will further drop duplicates based on (unique) Digital Object Identifiers (Doi) of papers. One of the columns in the csv file must be "Doi" and contain the items.
    dedup_list = process.dedupe(Exact_Dedup_doi["Title"],
                                threshold=t_value)
    # This function will take care of the fuzy descripancies left from the previous Exact Deduplication processes
    new_df = pd.DataFrame(dedup_list)
    # This creates a new Dataframe with the list of of the result obtained from the removal of fuzy duplicates
    df2 = new_df.rename(columns={0: "Title"},
                        inplace=False)
    # final csv file with all duplicates removed
    Df3 = pd.merge(df2, Exact_Dedup_doi, on='Title', how='inner')
    # This creates a new DataFrame by merging the final result with other details as contained in the most recent exact-deduplicated file (based on Doi)
    Df3.to_csv("Deduplicated File.csv")


input = input("Please enter the name of the file ending with .csv: ")
Deduper(input)
