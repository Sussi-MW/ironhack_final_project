<img src="https://github.com/Sussi-MW/ironhack_final_project/blob/master/image/deshboard.gif">

## Project: Real State Predictor MEXICO CITY
### by Susana Martin Wanton

### Goal: Ironhack final project. A system that connects Big Query with Python and Tableau, capable of obtaining and processing information for analysis and visualization.

### Result: Single-web-application that uses multiple trained machine learning models to predict property price from interactive data.



### Procedure:

#### Start up

Use of Tableau for data analysis and visualization. 
We establish the connection with Google BigQuery.


- BigQuery public datasets: Mexico Real Estate Listings:
	This dataset includes rent and sales data for properties in Mexico since 2016. 

- Due to the large volume of data in BigQuery, Tableau made the connection in real time.

#### Data Analysis

```bash
**Cleaning and reorganizing the database:**
[data_preparation.ipynb](https://github.com/Sussi-MW/ironhack_final_project/tree/master/notebook) 
```

- Exploring the data sets
- Handle Categorical Data
- Evaluation of the level of collinearity of the data.
- Normalize data
- Prediction Model Trainings 

```bash
	- **Scikit-learn imported models:**
	- Ridge, Lasso, SGDRegressor, GradientBoostingRegressor, RandomForestRegressor,         DecisionTreeRegressor, MLPRegressor
```

#### Machine Learning Platform: H2O.ai 

We use H2O that allows us to interactively execute machine learning workflows and provides a visualization of those models in a business analysis environment.

<img src="https://github.com/Sussi-MW/ironhack_final_project/blob/master/h2o.ai/03%20Visualize.JPG">

[H2O documentation can be found here](https://github.com/Sussi-MW/ironhack_final_project/tree/master/h2o.ai) 


#### Montaje de App Web:

Using Streamlit as an app framework to create a website that predicts the prices of the indicated property, entering the data related to the location and surface.

<img src="https://github.com/Sussi-MW/ironhack_final_project/blob/master/image/single_web_application.JPG">


---
### Resources used

* [scikit-learn Machine Learning in Python] (https://scikit-learn.org/stable/index.html]
* [Python Functional Programming How To Documentation](https://docs.python.org/3.7/howto/functional.html]
* [Python Errors and Exceptions Documentation](https://docs.python.org/3/tutorial/errors.html]
* [StackOverflow String Operation Questions](https://stackoverflow.com/questions/tagged/string+python]
* [https://en.wikipedia.org/wiki/Sentiment_analysis]
* [BigQuery public datasets](https://cloud.google.com/bigquery/public-data)
* [Tableau](https://www.tableau.com/es-es/support/help)
* [H2O 3](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/welcome.html)
* [Streamlit](https://docs.streamlit.io/en/stable/)


