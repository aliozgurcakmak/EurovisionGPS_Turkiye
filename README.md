# Eurovision GPS: Turkey’s Voting Journey Through the Years

## Overview 📋
Welcome to the Eurovision GPS project! This repository delves into the voting patterns of Turkey in the Eurovision Song Contest from 1975 to 2019. This project is part of my data science journey and aims to analyze which countries have given the most points to Turkey, which countries Turkey has supported the most, and ultimately identify Turkey’s best friend on the Eurovision stage.

## Data Science Approach
In this project, I leveraged various data science techniques to extract insights from historical Eurovision voting data. By applying data preprocessing, exploratory data analysis, and advanced statistical methods, I aimed to uncover patterns and relationships in the voting behavior. The analysis involves data normalization, logarithmic scaling, and year-based weighting to ensure accurate and meaningful results.

### Key Objectives
- Data Collection: Using Datagraver’s Eurovision voting data from 1975 to 2019.
- Data Cleaning: Preparing and cleaning the dataset for analysis.
- Exploratory Data Analysis: Visualizing and understanding the data distribution and trends.
- Statistical Analysis: Applying mathematical techniques to quantify relationships and voting patterns.
- Result Interpretation: Drawing conclusions based on the analysis and identifying Turkey’s closest friend in Eurovision.

## Dataset and Analysis Methodology
For the analysis, I used Datagraver’s Eurovision voting data from 1975 to 2019. I separated the data into semi-final and final votes and applied various mathematical techniques such as score normalization, logarithmic scaling, and year-based weighting to accurately quantify the relationships.

## Data Preparation
I started by importing the necessary libraries and loading the dataset. I then cleaned and prepared the data for analysis by renaming columns and separating semi-final and final votes.

## Analysis
### 1. Countries That Gave Points to Turkey
I analyzed which countries have given the most points to Turkey during the Eurovision finals. I grouped the data by country, calculated the total score given by each country, and sorted the results.

First, I separated the votes given to Turkey into semi-final and final categories. Then, I analyzed the final votes given to Turkey. To determine the countries that gave the most points to Turkey, I grouped the data by country, calculated the total points given by each country, and sorted the results. This analysis provided a list of the countries that gave the most points to Turkey.

### 2. Countries Turkey Voted for the Most
I conducted a similar analysis to determine the countries that Turkey has given the most points to during the Eurovision finals. First, I created a data frame containing Turkey’s votes. I then grouped the data by country and calculated the total points given by Turkey to each country. This analysis helped me identify the countries that Turkey has supported the most.

### 3. Calculating Adjusted Togetherness Score
To account for the consistency of voting over the years, I calculated the Adjusted Togetherness Score using logarithmic operations and year-based weighting. First, I calculated the years Turkey competed together with each country. Then, I calculated the annual points given. Finally, I calculated the Adjusted Togetherness Score and sorted the results. These analyses allowed me to determine Turkey’s closest friend in the Eurovision Song Contest.

## Conclusion
My analysis showed that Azerbaijan stands out as Turkey’s closest friend in the Eurovision Song Contest, even though they have only competed together in five editions. This analysis goes beyond simple point totals and considers the distribution, continuity, and exchange of votes over the years.

## Libraries Used 📚
The following Python libraries were used in this project:
- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical operations and calculations.
- `matplotlib`: For data visualization.
- `scikit-learn`: For machine learning algorithms and calculations.

## References
- [Datagraver’s Eurovision voting data](https://www.kaggle.com/datasets/datagraver/eurovision-song-contest-scores-19752019)

## Future Work
This project will continue with new parts. With the Eurovision GPS format, as I improve my data science skills, I will find different applications, analyses, and reviews to share with you. Thank you for your review.

## Final Thoughts 💡
This project has been instrumental in enhancing my understanding of data analysis and statistical methods. By analyzing real-world data, I learned how to apply theoretical concepts to practical scenarios, making data-driven decisions more effectively. This repository serves as a comprehensive resource for anyone looking to deepen their knowledge of data science and Python programming. Please feel free to explore, experiment, and modify the examples to enhance your learning experience!

Thank you for visiting my repository. Happy coding! 😊
``` ▋
