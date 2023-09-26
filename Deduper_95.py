def Deduper(x):  # A simple function to remove exact and fuzzy duplicates from a long list of literature usually necessary in the systematic literature review
    import pandas as pd
    import numpy as np
    import fuzzywuzzy
    from fuzzywuzzy import fuzz, process

    df = pd.read_csv(x)
    Exact_Dedup = df.drop_duplicates(subset=["Title"])
    Exact_Dedup_doi = Exact_Dedup.drop_duplicates(subset=["ID_2"])
    dedup_list = process.dedupe(Exact_Dedup_doi["Title"],
                                threshold=95)
    new_df = pd.DataFrame(dedup_list)
    df2 = new_df.rename(columns={0: "Title"},
                        inplace=False)
    # final csv file with all duplicates removed
    Df3 = pd.merge(df2, Exact_Dedup_doi, on='Title', how='inner')
    Df3.to_csv("Deduplicated File")


input = input("Please enter the name of the file ending with .csv: ")
Deduper(input)
