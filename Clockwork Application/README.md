# Clockwork
Clockwork Development

<h2>Contents</h2>
<li>Analyzed and gathered data from various recruiting projects through Clockwork’s SQL database using Days to Close and Closing Reason to determine business operations efficiency Used Python, Pandas, matplotlib, JSON, and the Clockwork SQL database to collect and analyze project data; HTML/CSS and Bootstrap to create templates, used D3 to make dynamic visualizations and waterfall diagram; Github/Heroku to deploy (was deployed, but no longer live)</li>

<h3>Project Analysis using D3</h3>

![alt text](https://github.com/kjordan18/kjordan18.github.io/blob/master/Clockwork%20Application/Screen%20Shot%202018-09-17%20at%209.04.08%20AM.png "D3 Pie Chart")

<li>This is a dynamic pie chart where the user can choose variables from the drop down menu ("Closing Reasons", "Industry", and "Seniority Level"). There was a hover that showed the average days to close for each section, showing which results/types of projects had high or low average days to close. A low days to close is good, it means these job postings are being filled quickly and (hopefully) efficiently with quality candidates.</li>

![alt text](https://github.com/kjordan18/kjordan18.github.io/blob/master/Clockwork%20Application/Screen%20Shot%202018-09-17%20at%209.04.37%20AM.png "D3 Scatter Plot")

<li>This is another chart created by D3 that shows more project analysis, specifically looking at each project individually based on their industry and how many days they've been open since October 2015. The user can change the axes to identify various trends in the projects.</li>
  
<h4>Waterfall Analysis</h4>

![alt text](https://github.com/kjordan18/kjordan18.github.io/blob/master/Clockwork%20Application/Screen%20Shot%202018-09-17%20at%209.05.32%20AM.png "Waterfall Plot")

<li> Based on a user-input firm and project ID, this chart shows a waterfall plot of candidates throughout the various steps of recruitment. This is valuable to a recruiting company as it allows them to see if each level of the recruiting process is being run in an efficient manner. You can see throughout the recruiting process how many candidates are "In", "Out" or "Current". </li>

<h5>Activity Analysis</h5>

<li>Each firm is assigned a unique ID and each user of the firm has a unique ID: user_id or actor_id. Events are triggered when there is a change in the project. Users can update the events or change the event depending on the task completed. While some users can create a project or close a project, not all users have access to such events. Depending on the rank and the type of the job, each user has certain administrative privileges on the kind of data and events they can access. Clockwork defined about 23 events in the project life cycle. In order to see user activity and the use of Clockwork Within, a firm can look into user activity on these 23 events. Most significant events such as Candidate creation, Project Creation, etc. are very specific and access to these events is restricted to very few users. We identified 9 of these events to determine the user activity.</li>

![alt text](https://github.com/kjordan18/kjordan18.github.io/blob/master/Clockwork%20Application/newplot%20(3).png "Activity Bar Plot")

![alt text](https://github.com/kjordan18/kjordan18.github.io/blob/master/Clockwork%20Application/newplot%20(4).png "Activity Pie Chart")
