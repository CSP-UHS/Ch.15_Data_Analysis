'''
------------------------
CREATING YOUR LINE CHART
------------------------

HINTS:
------
You will need to import the numpy library and use polyfit and poly1d to draw a
trendline and retrieve the slope and y-intercept. Use the following line of code:

coefficients = np.polyfit(x,y,1)

This will do a 1st order polynomial fit on the x and y data. An example of a
first order polynomial would look like y = 3x + 2. The variable coefficients 
would be a list of the coefficients. In this case 3 and 2 which would be the 
slope and the y-intercept. Therefore the next two lines of code will give you 
the slope and the y-intercept.

slope = coefficients[0]
yint = coefficients[1]

Now how do I plot the best fit line? We can use the poly1d in the following line of code.

best_fit = np.poly1d(coefficients)

This basically makes a function or an equation with the given coefficients. 
So for above, best_fit would be equal to 3x + 2 and if you pass the x data 
into the best_fit function you would have a new set of y values. 
Therefore we could plot a best fit line as follow:

plt.plot(x, best_fit(x), '--b')

This graphs a black dashed line using data set x and the new y values when you pass the 
x data into the best_fit function. If this is confusing ask your instructor.

To incorporate the coefficient values into the title, first format them to the tenths place.
Reformatting,these variables will change their type and allow them to be concatenated. 
If you don't reformat them you will have some errors. You must concatenate the string 
and variables with plus(+) signs rather than commas. Please change to your last name.

"Hermon's Line Chart m="+slope+" b="+yint

To change the background color of the graph you could call the method,
get current axis (gca) and then call the method set_facecolor as follows:

plt.gca().set_facecolor('cornsilk')

Use plt.xlim and plt.ylim to set limits on the axes.

Here is the data that needs to be used:
x = [0,1,2.5,3,4.7, 5, 6, 7.3, 8.6, 9, 10]
y = [.1,9.1,17.4,29.3,40,48,62,68,84,90,97]

This will make your graph slightly different than the picture and have different slope
and y-intercept values.
'''

import matplotlib.pyplot as plt


























plt.show()
