# Waste-Classification-Climate-Prediction

> Group Name: Dubai_PG 13

> Project Title:
Machine Learning for Environmental Sustainability: Waste Classification and Climate Prediction

> Group Members:
Adarsh Kumar (H00462142)
Gagan Lokanath Shetty (H00461958)
Kiran Narayana (H00461871)
Neha Giliyar Nagaraj (H00461957)
Sanjana Koujalgi (H00462014)

> Research Objectives

* Classify waste images into various categories using machine learning algorithms.
* Predict the impact of climate on organic waste decomposition.
* Analyze waste composition and climate data to develop sustainable waste management insights.

> Project Milestones

* Week 1-2: Set up the GitHub repository, collect datasets, perform initial data preprocessing.
* Week 3-4: Train machine learning models (CNN for waste classification, Linear Regression for climate prediction).
* Week 5-6: Visualize the results, validate model performance, update README with results and milestones.

> Dataset Sources

* Garbage Classification Dataset: UNEP Waste Management Resources.
* Climate Dataset: Historical climate data for various countries, source: Kaggle Climate Data Repository.
* Pollution Dataset: Waste composition data for various countries, sourced from open data repositories.

> How to Run the Data Preparation Pipeline

* Garbage Dataset:
  1. Upload the dataset folder under garbage_classification.
  2. Run preprocess_garbage_data.py to process and train the data.
  3. Analyze processed data with analyze_garbage_data.py. Trained models will be available in the model folder.

> Climate Dataset:
  1. Upload the dataset folder under climate_analysis.
  2. Run preprocess_climate_data.py to process data.
  3. Visualize processed data using analyze_climate_data.py. Results will be stored in the results folder.

> Application Setup:
  1. Run app.py to start a local server for garbage image classification.

> Project Deliverables

  * Garbage Classification using CNN: The model uses a convolutional neural network to classify images into 12 categories (e.g., plastic, organic, glass). Source Code.

  * Climate Prediction using Linear Regression: Predict organic waste levels based on climate data. Source Code.

GitHub Repository Structure

data/: Contains datasets used for training and analysis.

notebooks/: Jupyter notebooks for data analysis and modelling.

scripts/: Python scripts for data preprocessing, model training, and evaluation.

documentation/: Project documentation and weekly updates.

week1/, week2/, etc.: Detailed weekly progress.

README.md: Project overview and data pipeline description.


>> Running the Application

 > Waste Classification
   1. Run Preprocessing_and_train.py to train the CNN model.
   2. Execute visualization.py to generate visual charts.
   3. Start the local server with app.py to classify waste images.

 > Climate Data Analysis
   1. Run preprocess_climate_data.py to prepare data.
   2. Execute analyze_climate_data.py to visualize results.


>> Weekly Updates

* Week 1: Data collected, GitHub set up.
* Week 2: Data preprocessing completed.
* Week 3: Model training underway, challenges with overfitting addressed.

>> Formatting and Documentation

* All files are documented using GitHub Markdown.
* Jupyter Notebooks used for exploratory data analysis and documentation of results.

>> Data Management

* bRaw Data: Stored separately to maintain reproducibility.
* Preprocessed Data: Processed for model training, ensuring consistent input formats.


# Waste-Classification-Climate-Prediction-

1. Garbage Dataset 
2. run Preprocessing_and _train.py to traing the model using CNN
3. Once completed run visulization.py to visualize the chart 
4. run app.py wherein we have a local server running and images can be uploaded to clasify based on garbage type.
5. Come back and check logs.

=====================================================

Garbage Dataset

1. Uploaded the dataset folder under garbage classification
2. Run preprocess_garbage_data.py to process and train the data first
3. Run analyze_garbage_data.py to analyse the proccessed and trained data.
4. Please check model folder for the trained CNN model.
5. Once this is run please check the results folder for classification of garbage based on category.

======================================================

Climate Dataset

1. Uploaded the dataset folder under climate analysis
2. Run preprocess_climate_data.py to process the data based on avergae temperature
3. Run analyze_climate_dat.py to analyse the processed data 
4. once run please check the results folder for both processed as well as analysed data in csv.
5. As updated now once we run the analysis_climate.py we see a visual representation of plot using climate average temperature of countries we mention. 
6. Analysed data will be gereated in a csv file in rsults folder inside climate_analysis.