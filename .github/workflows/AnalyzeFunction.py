
def extract_municipality_hashtags(df):

    ''' This function takes a DataFrame and outputs a new DataFrame with a column called 'municipality' 
    which are values contained in a municipality dictionary ,
     those vales are matched to the keys contained in within the dictionary.
    The functin also extracts hashtags and places them in a new column
     '''
     
    import pandas as pd
    import numpy as np
    g = df['Tweets'].str.findall(r'@.*?(?=\s|$)')                                                   # Finds all words that begin with @.
    df['municipality'] = g.apply(lambda x: [mun_dict[g] for g in mun_dict.keys() if g in x])        # Matches values in the dictionary and creates a municipality column
    df["municipality"]= df['municipality'].apply(lambda x: ''.join(x) if len(x) > 0 else np.nan)    # converts lists into strings in the municipality column
    df['hashtags'] = df['Tweets'].str.findall(r'#.*?(?=\s|$)')                                      # finds all hashtags in the Tweets column and places them in a hashtag colum
    df["hashtags"]= df['hashtags'].apply(lambda x: ','.join(x).lower().split(',') if len(x) > 0 else np.nan)    #creates list of hashtags with lower case letter
    
    return df
