This is a function that removes english stop words from a tweet. A pandas dataframe is taken as as input and the sentences are tokenised according to the definition in function 6. 
The stopwords are then removed from the tokenised list. These stopwords were defined in the stop_words_dict variable at the top of the notebook.
The resulting tokenised list is then placed in a column named "Without Stop Words" while also modifying the input dataframe.
The function returns the dataframe as modified.