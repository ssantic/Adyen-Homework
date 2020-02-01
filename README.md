ADYEN DATA SCIENCE CHALLENGE README
===================================

This file purports to describe all the elements of the solution to Adyen's Supervised Learning Data Science Challenge
submitted by Srdjan Santic. The solution includes the following files:

* SupervisedChallenge__283_29.ipynb
* app.py
* request.py
* requirements.txt
* smote_rf.pickle
* README.md


SupervisedChallenge__283_29.ipynb
=================================

This file is a Jupyter notebook with the complete solution to the first part of the challenge. In order to work with the
notebook, the data file SupervisedChallenge.json is required. It is not provided as a part of the solution, due to the size,
and was originally provided by Adyen. The cells in the notebook are meant to be run in consecutive order. They provide the
exploratory data analysis, the feature engineering, the modeling and accuracy metrics, and export of the best model as a pickle file.


app.py
======

This file provides a minimum Flask server, and serves the model exported from the notebook through an API endpoint.
To run the server, use the following command at the terminal:

$ python app.py

The server listens on port 5000 by default, but this can be changed by modifying the file.


request.py
==========

This file provides a test request for the model served through Flask. It can be sent to the server by running:

$ python request.py


model/smote_rf.pickle
=====================

This is a pickle file of the best model from the solution. It can be exported through the notebook, and is required to
run the Flask web server.


requirements.txt
================

This file lists all the dependencies needed to run the project. They can be installed by running:

$ pip install -r requirements.txt
