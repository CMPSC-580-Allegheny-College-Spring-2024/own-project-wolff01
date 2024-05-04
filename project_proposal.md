# Junior Seminar (CMPSC 580) Project Proposal

## Semester: Spring 2024

This document is to contain your project proposal. __As you complete each of the below sections in this document, please be sure to remove all preamble text so that it does not appear in your work.__

## GitHub Handle: wolff01

## Name: William Wolff

## Major: Computer Science

## Project Title: Swing Efficiency %

---

## Introduction

The project, Swing Efficiency %, is a tool that helps analyze the statistics of all qualified batters and what percent of the swings they took were truly efficient swings. In baseball, having the perfect swing is almost impossible to have consistently as it is tough from a physics standpoint. When looking at hitters in Major League Baseball, they have almost great swings and with analytic and metric tracking today, we are able to see what a hitter does on a regular basis. When we take a look at statistics, we see all these numbers that are very deeply thought out but a lot of the statistics do not use facts based around matric results. That is where the tool comes into play. The tool creates the merging factor between given metrics and statistics. It helps as well display who is a valuable hitter and how valuable they are and can be. The person with the more efficient swing should be brought to light and there are more ideas of what can be valued in trading and signing players in the off season. A tool of this type should be valued in the world of baseball to know more for what you can get out of a hitter. This adds another level of importance of what needs to be done when scouting baseball. Most statistics now are very valuable tools and a big part of a hitter to be scouted is consistency. This tool displays the consistency that a player has with his swing being perfect. When seeing other statistics that are used in baseball today, we see a trend of statistics becoming more intertwined with metrics. Metrics are all shown for how the player moves, how the ball goes off his bat. Merging statistics with metrics in baseball can give a better look into what general managers want in a player and using a tool like this can really drive value for players that are being traded. Managers in baseball can also benefit from using this by having the knowledge of who is statistically gonna have the swing to do damage in the line up. Many players can show results of growth and how they are producing in many ways but we can be given a tool that can help in ways that can be a big factor for the game of baseball.

## Literature Review

When reading on what can be beneficial for baseball and how statistics have a big impact on the game of baseball, I wanted to further understand what makes statistics valuable and what statistics are truly valued in the game. The article, “Evaluating Baseball Statistics by Predicting Playoff Teams”, by Rohan Nakra and Ryan Kimes explains the correlation of baseball statistics to how a team makes it to the postseason in baseball. The stats that they used and tried to display were mainly team on base percentage, slugging percentage, and earned run average but they could not find a true correlation but understanding the fact of these statistics having a correlation between each other brought a clear understanding of needing to have a correlation of statistics for creating an understanding. Other articles such as “The Relationship between Cognition, Preseason Hitting Assessments, and In-Game Batting Performance in Collegiate Baseball and Softball Players” as well as “Which Statistics in Baseball Are Most Important for Winning?” help gave more reassurance of what statistics and looking into each area more valuably, there was a clear understanding that more statistics can be clearly understood. “Using Real-Life Major League BaseballData in an Introductory Statistics Course” gave clear knowledge of statistical knowledge to be used in this field as well as “Disturbance in Hitting Accuracy by Professional and Collegiate Baseball Players due to Intentional Change of Target Position” which gave an explanation into the flaws of hitting. In addition to this, reading, “Evaluating plate discipline in Major League Baseball with Bayesian Additive Regression Trees”, this clears any confusion when wondering about how a hitter’s vision can affect how valuable his swing could be. Seeing a clear model for how the ball can be missed on the bat from being perfect was crucial and knowing that I had a clear gauge for the data that would be necessary to know before going about making the prototype clear and easy to process. After reading, the first step was to acquire the data that was needed to produce my statistical results. After reading more about what data is the most important and trustworthy, the option was to go with StatCast. Being a Major League Baseball used data tracker created by Google, there is a dashboard created in baseballsavant.com which gives the choice of what data can be used. After selecting the necessary parts of data, the next step was to use stream lit in order to display my results as well as use pandas too to display the final results.

## Prototype

When thinking about this project and how to go about creating this. First laying out a plan that was going to keep a clear mind set if the goal ahead. The first part of the plan was to make a mathematical equation that can give the correct output and be realistic. The first issue was here as there are so many statistics that exist that could be us but are not the most useful in this case. After trial and error and understanding each statistical measurement for where the statistics that were being used to contribute to this was found and how they were measured, the most efficient to be used in this case, and make the most impact on this were sweet spot percentage and hard hit percentage. Hard hit percentage is calculated as the percent of baseballs that were hit with an exit velocity of 95 miles an hour or harder off the bat. Sweet spot percentage is measured as baseballs that were hit off the bat at any angle between 8 degrees and 32 degrees. When taking a look at a hitter’s hard hit percentage, multiplying that number with the amount of balls hit in play, you get the total number of hard hit balls that a player had that were put in play. Then taking the total amount of swings a player takes in the strike zone and out of the strike zone. We then take that number and divide the amount of hard hit balls in play by total number of swings, we get the percentage of hard hit balls in play per total swings. Then doing that same process but using sweet spot percentage instead of hard hit percentage, we get the percentage of sweet spot hit balls in play per total swings. Taking those two percentages and multiplying the values together we are able to get the percentage of efficient swings a hitter has in a total season. Each part of the equation is clearly labeled when looking in the main.py file and they are all put into a streamlit table and you are given the option to sort the table by either the name of the player in descending order or by swing efficiency percentage in descending order as well. In the main we can see that the creation of each part is split up individually. This also is explained in each comment and docstring written that details every for loop, if statement, and function’s purpose.

## Preliminary Results and Outcomes

The result of the code came out to create a chart that is 134 lines long and as well display both the results of the math as well as the names of the player that correlates with the results. The outcome was to be expected as that was the intended goal was to display these metrics. The outputs when first creating this code were led to be in a different fashion as before the implementation of the stream lit function, the results were printed through running the python code. While working on this, there were several encounters of flaws in the code such as not being able to display the data properly and manipulating the code to run the correct mathematical equation. The mathematical portion was created in several different parts in order to know exactly how each part would behave in the running of this code. The parts being the addition, multiplication, and division. In the division though it includes the features of the results and how they will be displayed in the code. The more that was inputted into the code.The python code needed to be able to withstand a large inputted csv code from the downloaded baseball savant data. As shown in the example below, it shows the results of a small portion of the data

|---|------------------|--------------------|
|   |Names	           | Swing Efficiency % |
|---|------------------|--------------------|
|35	|Yoshida, Masataka |2.7721              |
|---|------------------|--------------------|
|97	|Yelich, Christian |1.9420              |
|---|------------------|--------------------|
|107|	Witt Jr., Bobby|2.3629              |
|---|------------------|--------------------|
|72	|Walker, Christian |1.6783              |
|---|------------------|--------------------|
|106|Wade Jr., LaMonte |2.2650              |
|---|------------------|--------------------|
|133|	Volpe, Anthony |1.7327              |
|---|------------------|--------------------|
|119|	Vierling, Matt |2.1328              |
|---|------------------|--------------------|
|99	|Verdugo, Alex	   |2.9859              |
|---|------------------|--------------------|

## Conclusions and Future Work

TODO: Summarize your work and outline future steps needed to complete to take the project to the next stage (for example, if you were to continue with this project in 600/610). You must also address ethical implications of your project, especially as pertains to the public release or use of your software or methods.

## References

TODO: Add references in the [ACM style](https://www.acm.org/publications/authors/reference-formatting). All references must be cited in the proposal.

Evaluating plate discipline in Major League Baseball with Bayesian Additive Regression Trees