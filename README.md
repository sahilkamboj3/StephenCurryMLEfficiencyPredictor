<!-- # Stephen Curry Career Analysis

This project analyzes and visualizes Stephen Curry's basketball career both by seasons and by individual games. I gathered the data by web scraping basketballreference.com. Using the requests, BeautifulSoup, and pandas libraries, I imported Stepehn Curry's season averages for each year he has played, except 2019-2020 since he was injured for most of the season, and his statistics for every game he has played.

In the data visualization, I visualized both the season averages and individual game statistics over his career. Using scatterplots, lineplots, violinplots, and more, I analyzed the distributions of the graphs and created some new features to paint a picture not just how Stephen Curry has changed his game over the years but how his game changes over the course of a season.

In the machine learning part of this project, I used Stephen Curry's individual game statistics over the course of his entire season to predict his +/- impact in the a game.

- The 2 machine learning iterations represent two parts of the data science and feature engineering.
  - The first iteration respresents the first round of feature engineering where I created features on my own through my own experimentation and research. I ran those features through various regression models and saved the best model, the SGD model which was able to predict the +/- within 7.08 points on average.
  - In the second iteration, I did further experimentation, adding a few features, and made a few adjustments to try to yield better results. Running them through the models again, I once again found the SGD Regression model yielded the best results, predicting the +/- within 6.86 points on average. -->

# Stephen Curry Career Analysis

<!-- <img src="../steph_curry_images/sc1.jpg" alt="Stephen Curry" width="300" style="margin: auto; display: block;" /> -->
<img src='https://upload.wikimedia.org/wikipedia/commons/b/b6/Stephen_Curry_shooting.jpg' alt='Stephen Curry' width='300' style="margin: auto; display: block;" />
<h2>Intro</h2>
<p>
    Stephen Curry, over the past years, has been one of the most popular players in the NBA and of the faces of the league. As he changed the game with his 3-point shooting, Curry has worked his way to 2 MVPs, 3 NBA Championships, 2 Gold Medals at the World Games, and countless records. 
</p>
<p>
    +/- rating - a statistic that measures the difference in one team's scoring and the opponent team's scoring while the player is in the game.
</p>

<img src="../steph_curry_images/sc2.jpg" alt="Stephen Curry Shooting" width="300" style="margin: auto; display: block;" />
<h2>Machine Learning</h2>
<p>
    The goal of this project is to use machine learning to predict the +/- rating for Curry's games based on various statistics such as points scored, PER, rebounds, fouls, blocks, and more. There are two machine learning iterations, which include two rounds of feature engineering, along with data science and feature selection, and training the machine learning models with these features and statistics.
</p>
<p>
    The feature engineering includes cross-referencing features to create new numerical features while also comparing those numerical features to certain thresholds to create categorical features. The features are evaluated based off their correlation with the target (+/-) feature and the p-value from ANOVA tests.
</p>
<p>
    The machine learning models I trained and tested were Linear Regression, Support Vector Machine, SGD Regression, Random Forest Regression, and more. The first machine learning iteration does not use PCA to reduce the dimensionality of the data while the second section does use it. 
</p>
<h3>Results</h3>
<p>
    In the first iteration, the best model was the SGD Regressor being able to predict Stephen Curry's plus minus in a game within 7.08 point on average. In the second iteration, after further research and experimentation, I created new features and tweeked a few settings/thresholds and ran the data through the machine learning models once again. I found that this time, SGD Regressor was once again the best model predicting Stephen Curry's plus minus in a game within 6.86 points on average.
</p>
<p>
It should be noted that +/- is not a complete representation of the performance of one player. Stephen Curry has played in the leauge for 11 years and played in many different rosters. With that, not only are his own teams very different, the teams he plays against also vary in skill and how their rosters are performing. Therefore, some of the error could be explained by the variance not just in Stephen Curry's own team but who he played against in the rest of the league. Therefore, even when he has an efficient game, having less skilled teammates may have led to a lower +/- rating or having the same statistics against  a team who isn't performing as well may lead to a higher +/- rating.
</p>

<h2>Data Collection</h2>
<p>
    The data was collected from Basketball Reference using BeautifulSoup, a Python package used for parsing HTML and XML documents. I also used the requests library to make HTTP requests and access Basketball Reference's websites as html files. Lastly, once I collected all the data, I stored it in a Pandas dataframe and converted it to a csv file.
</p>

<h2>Data Visualization</h2>
<p>
    The data visualization consists of two files - one file visualizing Stephen Curry's season averages and the second file visualizing Stephen Curry's individual game statistics. In these files, I visualized various features like points, 3 pointers made, steals, shooting percentages, and more. In addition to visualizing his statistics over his career, I also tried to see how his game changes over the course of his career aand how it changes over the course of a season. 
</p>
<p>
    To handle the visualizations, I used scatterplots, regplots, lineplots, violinplots, and more to try to find any interesting insights I could find.
</p>
