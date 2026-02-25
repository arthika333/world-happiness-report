# World Happiness Report Prediction for 2025 using Ridge Regression
As of 22nd February 2026, the official World Happiness Report 2026 has not yet been published. 
This project uses historical data from 2018–2024 to train a Ridge Regression model that forecasts projected Ladder Scores and rankings for 2025. The project demonstrates the complete workflow including data preprocessing, feature scaling, regression modeling, evaluation, and visualization.

## Dataset Overview
The dataset was compiled from historical World Happiness Reports (2018–2024).
The Ladder Score is calculated using data from the Gallup World Poll and is based on the following features:
* Log GDP per capita
* Social support
* Healthy life expectancy
* Freedom to make life choices
* Generosity
* Perceptions of corruption
These variables were used as predictors in the regression model.

## Data Visualization and Exploratory Analysis
The cleaned datasets were used to build interactive Tableau dashboards to explore:
* Global happiness distribution
* Top 10 country rankings
* Ladder score trends
* Relations between dataset parameters

 <img width="1919" height="1087" alt="image" src="https://github.com/user-attachments/assets/86cc6c62-4d41-4296-b9aa-a8b605b602fe" />

 <img width="1919" height="1090" alt="image" src="https://github.com/user-attachments/assets/ba90884d-2336-4487-8807-777da3ddaedb" />

## Data Pre-processing
Rows containing all null values were removed. Rows that had missing values were imputed using Simple Imputer and mean strategy. Data was scaled using MinMaxScaler and split based on years. 
* Training: 2018-2022
* Testing: 2023-2024

## Model Structure
A simple ridge ression model wih alpha=10. The chosen value resulted in improved the model's performance and prevented extreme values. An alpha value of 10 provided more stable and realistic predictions.

## Model Evaluation
Performance was evaluated using the R² (coefficient of determination) metric.
* Training R²: 0.72
* Testing R²: 0.57
  
So the model explains 72% of the variance in training data and 57% of the variance in unseen future data. The moderate gap between training and testing performance suggests acceptable generalization without severe overfitting.

## 2025 Predictions
Using 2024 feature values, the trained model was used to forecast projected 2025 Ladder Scores.. The predictions were sorted to generate a projected top 10 ranking for 2025.

<img width="1919" height="1093" alt="image" src="https://github.com/user-attachments/assets/eff57ac2-9f9f-4b50-bc12-3cd44c4b779c" />

Most of the predicted countries consistently stayed within the top 10 in previous years. This shows that the model is making realistic predictions.

<img width="843" height="604" alt="image" src="https://github.com/user-attachments/assets/5f4dd7b9-ae22-47a0-9826-1f35a5a5e60e" />

One notable outlier is Singapore, which is projected to rise significantly compared to its previous year's ranking.

## Technologies Used:
* Python
* Pandas
* NumPy
* Scikit-learn
* TensorFlow (for experimentation)
* Tableau

## Resources
Every source that has been used for this project is listed below:
* https://scikit-learn.org/
* https://www.youtube.com/watch?v=VMbaOcyDtsQ
* https://youtu.be/jO0P-HTyYiw
* https://www.worldhappiness.report/ed/2025/#appendices-and-data

## Interactive Dashboards:
* https://public.tableau.com/app/profile/arthika.p2281/vizzes
