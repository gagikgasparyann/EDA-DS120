# EDA-DS120
exploratory data analysis - group project for DS120 programming for data science course

DS 120C GROUP PROJECT REPORT - NYC VEHICLE COLLISIONS TO PERSON
Due Date: May, 10, 2026
Group Members: Arshak Mahtesyan, Gagik Gasparyan, Hayk Yesayan
1. Objective of the Analysis
The primary goal of this project is to build a structured Python pipeline to analyze traffic collision data in
New York City. The analysis focuses on identifying patterns in how accidents happen, who is involved,
and what factors most strongly correlate with serious injuries or fatalities. By organizing the code through
Object-Oriented Programming (OOP), we ensure the analysis is modular and can be easily updated
with new data.
2. Dataset Description
The project utilizes a real-world dataset containing detailed records of NYC traffic collisions.
●​ Source: A public Google Sheets export containing collision metrics.
●​ Features: The data includes categorical information (e.g., PERSON_TYPE,
SAFETY_EQUIPMENT, PED_ROLE) and numerical/temporal data (e.g., PERSON_AGE,
CRASH_DATE, CRASH_TIME).
●​ Preprocessing: We performed extensive cleaning, including handling missing values in age and
safety equipment, correcting logical errors (e.g., removing "helmet" labels from pedestrians), and
merging date/time columns into a single CRASH_DATE_TIME object for better time-series
analysis.
3. Overview of Code Structure
The project is organized into four main Python modules to maintain clean code and follow PEP8
standards:
●​ data○​ Contains our dataset in excel sheet in case the link to the dataset fails to load
●​ sources
○​ data_cleaning.py: Handles raw data loading and systematic cleaning of all columns.
○​ analyzer.py: Contains the Analyzer class, which performs all mathematical and statistical
calculations.
○​ visualization.py: Contains the Visualization class, which takes data from the Analyzer to
create plots.
●​ main.py: The entry point that executes the full pipeline.
4. Key Insights
Our analysis revealed several meaningful trends in the collision data:
●​ Temporal Patterns: By analyzing crashes by month, we identified specific times of the year with
higher incident rates.
●​ Demographic Breakdown: A pie chart of "Person Types" showed the proportion of drivers
versus pedestrians involved, while age statistics revealed differences in average age between male
and female victims.
●​ Safety & Risk Correlations:
○​ Emotional Status: We found a measurable correlation between a person's emotional state
and the severity of their injury.
○​ Contributing Factors: The analysis highlighted the top 10 most dangerous contributing
factors that lead to accidents.
○​ Role vs. Injury: Heatmaps demonstrate how a person's role (e.g., passenger vs. cyclist)
relates to specific injury types.
Summary of Technical Requirements Met
●​ Python Libraries: NumPy, Pandas, Matplotlib, and Seaborn.
●​ OOP Design: Implemented at least two classes (Analyzer and Visualization).
●​ Visualizations: Includes bar charts, pie charts, stem plots, and heatmaps.
●​ Documentation: All classes and methods include descriptive docstrings.
