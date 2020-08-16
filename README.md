# Stephen Curry Career Analysis

This project analyzes and visualizes Stephen Curry's basketball career both by seasons and by individual games. I gathered the data by web scraping basketballreference.com. Using the requests, BeautifulSoup, and pandas libraries, I imported Stepehn Curry's season averages for each year he has played, except 2019-2020 since he was injured for most of the season, and his statistics for every game he has played.

In the data visualization, I visualized both the season averages and individual game statistics over his career. Using scatterplots, lineplots, violinplots, and more, I analyzed the distributions of the graphs and created some new features to paint a picture not just how Stephen Curry has changed his game over the years but how his game changes over the course of a season.

In the machine learning part of this project, I used Stephen Curry's individual game statistics over the course of his entire season to predict his +/- impact in the a game.

- The 2 machine learning iterations represent two parts of the data science and feature engineering.
  - The first iteration respresents the first round of feature engineering where I created features on my own through my own experimentation and research. I ran those features through various regression models and saved the best model, the SGD model which was able to predict the +/- within 7.08 points on average.
  - In the second iteration, I did further experimentation, adding a few features, and made a few adjustments to try to yield better results. Running them through the models again, I once again found the SGD Regression model yielded the best results, predicting the +/- within 6.86 points on average.
