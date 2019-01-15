# MVP Machine Learning Predictions

<h2>Contents</h2>
<li>Worked independently to create a predictive model using gradient boosting classifiers for this season’s Most Valuable Player award. Model generated probabilities for the testing data. Used Python, Pandas to structure the data properly, used 20 previous seasons to train the model, which generated perfect predictions. Used matplotlib to visualize.</li>

<h3>Results</h3>
<br/>
<h4> AL MVP Predictions </h4>
<br/>

![alt text](https://github.com/kjordan18/kjordan18.github.io/blob/master/MVP%20Machine%20Learning%20Predictions/Screen%20Shot%202019-01-14%20at%205.04.48%20PM.png "AL MVP Predictions")

<li>This shows the top 5 model generated probabilities for the American League MVP this season. The model predicts with a 99.999% likelihood that Mookie Betts will win the award, and has all 3 finalists represented in the top 5 (Manny Machado is ineligable to win the award). This seems to be a two man race, with Mike Trout representing the only significant chance of topping Betts. </li>
<br/>
<h4> NL MVP Predictions </h4>
<br/>

![alt text](https://github.com/kjordan18/kjordan18.github.io/blob/master/MVP%20Machine%20Learning%20Predictions/Screen%20Shot%202019-01-14%20at%205.04.39%20PM.png "NL MVP Predictions")

<li>This shows the top 5 probabilities for the National League MVP award. The model predicts with a 100% likelihood that Christian Yelich will win the award, with Javier Baez and Trevor Story coming in 2nd and 3rd, respectively. Nolan Arenado is the only finalist not represented in the top 5 of predictions (12th). </li>
<br/>
<h4> Feature Importance of Training Data</h4>
<br/>

![alt text](https://github.com/kjordan18/kjordan18.github.io/blob/master/MVP%20Machine%20Learning%20Predictions/Screen%20Shot%202019-01-14%20at%205.05.51%20PM.png "Feature Importance of Training Data")

<li>This shows the feature importance score for each explanatory variable from the training dataset. This score determines how impactful each variable is towards winning the MVP award. We see that Home Runs (HR) represents the largest impact, followed by Winning Percentage and Batting Avereage (BA). I was surprised to see WAR and other player evaluation stats so low in the importance rankings. These are metrics that more accurately represent a players' ability than most of the other stats used. However, this best represents the criteria in which the voters make their decisions for this award. Clearly, hitting home runs and playing for a winning team are the most important features for the voters. </li>
<br/>
<h4> Feature Importance of Testing Data</h4>
<br/>

![alt text](https://github.com/kjordan18/kjordan18.github.io/blob/master/MVP%20Machine%20Learning%20Predictions/Screen%20Shot%202019-01-14%20at%205.06.04%20PM.png "Feature Importance of Testing Data")

<li>This shows the feature importance score for each explanatory variable from the test dataset. The graph looks much different than the testing data. Here we see Slugging Percentage (SLG) as the most important feature, followed by RBI and Batting Average. I was surprised to see BA in the top 3 for both training and testing data. The way players are evaluated has changed dramatically from 1998 to 2018. Another major impact to the findings of this study is the first 10 years of the era studied was amidst the steroid era. This may explain a bit why the feature importances are different for the training and testing data. </li>
