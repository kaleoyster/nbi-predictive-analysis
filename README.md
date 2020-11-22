 # nbi-predictive-analysis
 The National Bridge Inventory (NBI) represents bridge data submitted annually to the Federal Highway Administration (FHWA) by the States, Federal agencies, and Tribal governments. FHWA is responsible for the maintenance of bridges in the USA. It uses NBI data to schedule regular maintenance of the bridges, and currently uses a flowchart-based process to schedule these maintenances. However, this procedure doesn't consider external factors such as precipitation, snowfall, freeze-thaw data, or other environmental factors.

The overall goal of this mini-project is to understand the influential factors that contribute to the deterioration of the bridges as measured by a provided ‘rating’ score and its fluctuation over time. Specifically, this project will use NBI and environmental data to build a Decision Tree for modeling bridge deterioration measured by this score. Factors identified through the Decision Tree can be used to improve the current maintenance routine, and the decision tree rules found by the applied algorithm will be compared against the existing maintenance rules to identify common factors and differences. The project is expected to identify environmental factors that can influence bridge health. These insights can then be used to augment maintenance routines and ideally lead to a predictive maintenance approach.

# Organization of the project
## File structure:
    1. data_process 
        1. preprocess
           The preprocess folder contains the files that clean and prepare dataset for the analysis.

            1. integrate.py

        2. post_analysis

            This folder contains files code that provides post analysis of the results from the analysis
            1. flow.py: Evaluates the bridges with respect to the flowchart 

            2. after_analysis.py

            3. quick_analysis.py 

            4. validation.py
        
    2. analysis
        R scripts that run models by taking into account the data prepared by the data processing scripts.

    3. notebook

# Project execution flow:

1. Prepare dataset (contains cleaning and preprocessing dataset) -> decision_tree_training.csv, decision_tree_testing.csv ->  assumed repair and reconstruction
2. run r scripts 
3. run post analysis scripts


# Order of execution

## processNdotMaintenanceRecords
    1. process_ndot_maintenance_records
    2.  integrate_all_results
