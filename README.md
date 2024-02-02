# BiFeO<sub>3</sub> sol-gel thin film text mining

Dataset and associated model training / analysis scripts for __Text-mining the literature to inform experiments and rationalize impurity phase formation for BiFeO<sub>3</sub>__.

Curated and validated dataset is found in ```/data/bfo_df_20221019.csv```, along with a version without syntheses leading an amorphous product. 

```df_prep.ipynb``` processes the dataset into appropriate dataframes for EDA and modeling
* If you want to generate the separate dataframe for predicting results on the published experiments for replication, you currently need to run the full notebook twice: once to generate all of the "regular" dataframes and again (with ```for_prediction = True```) to generate the prediction dataset (__to be improved in next version__)

```df_decision_tree.ipynb``` trains a collection of decision tree models based on the produced dataframes
* Similarly, if you want to train models without considering the data left out to pred


```python

```
