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

>> Research Objectives

* Classify waste images into various categories using machine learning algorithms.
* Predict the impact of climate on organic waste decomposition.
* Analyze waste composition and climate data to develop sustainable waste management insights.

>> Project Milestones

* Week 1-2: Set up the GitHub repository, collect datasets, perform initial data preprocessing.
* Week 3-4: Train machine learning models (CNN for waste classification, Linear Regression for climate prediction).
* Week 5-6: Visualize the results, validate model performance, update README with results and milestones.

>> Dataset Sources

* Garbage Classification Dataset: UNEP Waste Management Resources.
* Climate Dataset: Historical climate data for various countries, source: Kaggle Climate Data Repository.
* Pollution Dataset: Waste composition data for various countries, sourced from open data repositories.

>> How to Run the Data Preparation Pipeline

* Garbage Dataset:
  1. Upload the dataset folder under garbage_classification.
  2. Run preprocess_garbage_data.py to process and train the data.
  3. Analyze processed data with analyze_garbage_data.py. Trained models will be available in the model folder.

>> Climate Dataset:
  1. Upload the dataset folder under climate_analysis.
  2. Run preprocess_climate_data.py to process data.
  3. Visualize processed data using analyze_climate_data.py. Results will be stored in the results folder.

>> Application Setup:
  1. Run app.py to start a local server for garbage image classification.

>> Project Deliverables

  * Garbage Classification using CNN: The model uses a convolutional neural network to classify images into 12 categories (e.g., plastic, 
    organic, glass). Source Code.
  * Climate Prediction using Linear Regression: Predict organic waste levels based on climate data. Source Code.

>> GitHub Repository Structure

  ->additionals
    |_app.py
    |_preprocess_and_train.py
    |_visualization.py
    |_visualize_log.py
    
  ->climate_analysis
     |->analysis
       |_analyze_climate_data.py  
     |->dataset
       |_climate_data.csv 
     |->preprocessing
       |_preprocess_climate_data.py
  
  ->combined_analysis
    |->analysis
      |_combined_analysis.py
      |_waste_prediction.py
    |->scripts
      |_combined_analysis.py

  ->garbage_classification
    |->analysis
       |_analyze_garbage_data.py
    |->dataset (images dataset)
    |->models
       |_train_garbage_model.py
    |->preprocessing
       |_preprocess_garbage_data.py

   ->pollution_analysis
     |->analysis
        |_analyze_pollution_data.py
     |->dataset
        |_pollution_data.csv
     |->preprocessing
        |_preprocess_pollution_data.py

   * README.md: Project overview and data pipeline description.
    

>> Running the Application

> Our Project have 3 Datasets each dataset is plased in the repective folders.

 > Garbage Classification
   1. Run Preprocess_garbage_data.py to train the CNN model.
   2. Run train_garbage_model.py to train the model after preprocessing.
   3. Run analyze_garbage_data.py by taking the results from trained model
   4. Results will be stored in the ressults folder

 > Climate Data Analysis
   1. Run preprocess_climate_data.py to prepare data.
   2. Execute analyze_climate_data.py to visualize results.
   3. Results will be stored in the ressults folder
 
 > Pollution Data Analysis
   1. Run preprocess_pollution_data.py to process the data.
   2. Execute analyze_pollution_data.py to get the results in .csv format

 > Combined Analysis
   1. Run combined_analysis.py collecting all the results from other analysis to get merged climate pollution data.
   2. Execute waste_prediction.py to get visual chart of actual vs predicted organic waste.
  
 > Additionals
   1. Run Preprocessing_and_train.py to train the CNN model.
   2. Execute visualization.py to generate visual charts.
   3. Start the local server with app.py to classify waste images.

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

**Garbage Dataset Instructions:**
Dataset Location:
Place the dataset folder under the garbage_classification directory.

Preprocess and Train the Data:
Run preprocess_garbage_data.py to preprocess the images and train the model:

This will normalize the image data, apply data augmentation, and save the trained CNN model.
Analyze Processed and Trained Data:
Run analyze_garbage_data.py to analyze the results of the processed and trained data:

This script uses the trained model to classify garbage into categories.
Model and Results Location:

The trained CNN model is saved in the model folder.
The classification results, including predictions, can be found in the results folder.

======================================================

**Climate Dataset Instructions:**
Dataset Location:
Place the dataset folder under the climate_analysis directory.

Preprocess Climate Data:
Run preprocess_climate_data.py to process the dataset:

This script calculates the yearly average temperature for each country and normalizes the values.
The preprocessed data will be saved as a CSV file in the results folder inside climate_analysis.
Analyze Processed Data:
Run analyze_climate_data.py to analyze the processed data:

This script generates a visual representation of temperature trends for selected countries.
The analysis results will include:
A CSV file of analyzed data saved in the results folder.
A line plot visualizing the normalized average temperature trends for specified countries.
Visualization and Output:

The line plot displays the climate trends for selected countries using normalized average temperatures.
The results folder contains the processed and analyzed data in CSV format and any saved visualizations.

=========================================================
**Pollution Dataset Instructions**
Dataset Location:
Place the dataset folder under the pollution_analysis directory.

Preprocess Pollution Data:
Run preprocess_pollution_data.py to:

Filter and clean relevant columns (e.g., waste generation, composition percentages).
Normalize TotalWasteGenerated and convert waste composition percentages to decimals.
Save the preprocessed data as preprocessed_pollution_data.csv in the results folder.
Analyze Pollution Data:
Run analyze_pollution_data.py to:

Generate a bar plot for the top 10 countries by total waste generated.
Analyze and visualize waste composition for a selected country.
Results Location:
Preprocessed data and visualizations are stored in the results folder inside pollution_analysis.

=========================================================
**Combined Analysis**
Saving Merged Data for Reference:

The merged climate and pollution dataset is saved as merged_climate_pollution_data.csv in the combined_analysis/results/ folder to ensure easy access and reproducibility.

Analysis of Merged Data:

The merged dataset is analyzed to explore correlations between variables like average temperature, total waste generated, and waste composition (organic, plastic, glass). A correlation matrix is computed and visualized using a heatmap to highlight variable relationships.

Steps:

Load climate and pollution datasets.
Merge datasets by country name to create a combined dataset.
Save the merged dataset in combined_analysis/results/.
Compute and visualize a correlation matrix to analyze variable dependencies.
