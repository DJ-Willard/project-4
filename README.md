# UOCIS322 - Project 4 #
We learn how to write test cases and test your code, along with more JQuery.

## Overview

We reimplement RUSA ACP controle time calculator with Flask and AJAX.
> That's *"controle"* with an *e*, because it's French, although "control" is also accepted. Controls are points where a rider must obtain proof of passage, and control[e] times are the minimum and maximum times by which the rider must arrive at the location.

### ACP controle times Info

This project consists of a web application that is based on RUSA's online calculator. The algorithm for calculating controle times is described here [https://rusa.org/pages/acp-brevet-control-times-calculator](https://rusa.org/pages/acp-brevet-control-times-calculator). Additional background information is given here [https://rusa.org/pages/rulesForRiders](https://rusa.org/pages/rulesForRiders). The description is ambiguous, but the examples help. Part of finishing this project is clarifying anything that is not clear about the requirements, and documenting it clearly. 

We are essentially replacing the calculator here [https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html). We can also use that calculator to clarify requirements and develop test data. 

## Tasks Completed

* Implement the logic in `acp_times.py` based on the algorithm form the websites listed above.

* Created test cases using the original websites created data, and we wrote 5 test suites for the project.
	* We based our tests on what was discussed in the lecture, created test cases on the edge cases, tested them in the original website, and checked if the created functions correctly calculate the times listed.
	* This will effectively replicate the calulator listed in the website.

* Edit the template and Flask app so that the required remaining arugments are passed along.
	* Currently the miles to kilometers (and some other basic stuff) is implemented with AJAX. 
	* We passed start date/time and brevet distance.

* As always, revise the README file for the points of course
	* **NOTE: form Professor** This time, you should outline the application, the algorithm, and how to use start (docker instructions, web app instructions). **Make sure you're thorough, otherwise you may not get all the points.**
    * In this application we have an AJAX interation with the calc.html template which pass values to the python API flask in the flask_brevet.py.
    * Then the api calls acp_times.py to get the start and end times by the given.
    * In the Algorithm I created two tupled lists Min and Max
    * I then ran if cases to prevent oddities cases
    * Then i calulate total time per control distance and then divided by the match tuple min/ max speed then mupliplied by time  in minutes
    * To use the program you must frist `docker build -t imagename .`
    * then `docker run -p 5001:5000 imagename`
    * then open a boswer at http://localhost:5001/
    * then use the website in the same way you did before, but you can only put in whole km and not miles.
    * the website will calculate data

* As always, I submit `credentials.ini` through Canvas. It should contain my name and git repo URL.

### Testing

A suite of nose test cases is a requirement of this project. Design the test cases based on an interpretation of rules here [https://rusa.org/pages/acp-brevet-control-times-calculator](https://rusa.org/pages/acp-brevet-control-times-calculator). Be sure to test your test cases: You can use the current brevet time calculator [https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html) to check that your expected test outputs are correct. While checking these values once is a manual operation, re-running your test cases should be automated in the usual manner as a Nose test suite.

To make automated testing more practical, your open and close time calculations should be in a separate module. Because I want to be able to use my test suite as well as yours, I will require that module be named `acp_times.py` and contain the two functions I have included in the skeleton code (though revised, of course, to return correct results).

We should be able to run your test suite by changing to the `brevets` directory and typing `nosetests`. All tests should pass. You should have at least 5 test cases, and more importantly, your test cases should be chosen to distinguish between an implementation that correctly interprets the ACP rules and one that does not.


## Authors

Daniel Willard