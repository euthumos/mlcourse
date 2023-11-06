# **Binary Prediction of Smoker Status using Bio-Signals**  
  
## **Problem Description**   
   
The problem is to build a model that can accurately classify patients into two categories: smokers and non-smokers. To achieve this, we're utilizing gradient boosting decision trees from LGBM. Trained machine learning model has been implemented as a web service and deployed on the Google Cloud Platform.

The data for this project is sourced from the [Kaggle competition](https://www.kaggle.com/competitions/playground-series-s3e24/overview); it's important to note that it is synthetic data.  
   
## **Structure of the repository**    
   
The repository contains the next files and folders:
* `data/train.csv` - labeled dataset    
* `data/test.csv` - unlabeled dataset for testing on Kaggle
* `data/sample_submission.csv` - unlabeled dataset for submition on Kaggle
* `notebook.ipynb` - notebook with EDA and ML model training    
* `model.pkl` - saved final GBDT model    
* `Pipfile` and `Pipfile.lock` - configuration files that specify the project's dependencies 
* `train.py` - script for model training 
* `preprocessing.py` - feature engeneering
* `predict.py` - script for deploying a web service (Flask) using the final model    
* `Dockerfile` - encapsulating the Flask application within a container.
* `request_cloud.py` - script for generating predictions using the deployed application on GCP
* `request_local.py` - script for generating predictions using the deployed application (whether encapsulated in a container or not)   
* `images` - folder with images  
* `README.md` - project documentation 
   
## **Dataset description**    
   
Dataset source: https://www.kaggle.com/competitions/playground-series-s3e24/data 

- train.csv - the training dataset; smoking is the binary target
- test.csv - the test dataset; your objective is to predict the probability of positive smoking
- sample_submission.csv - a sample submission file in the correct format

Training dataset contains 159k patient records with biological parameters and smoking status.

Testing dataset contains 106k similar records without smoking status.

22 columns with biological parameters are listed in notebook.ipynb.

## **Environment**   
   
The project's virtual environment is established with Pipenv. To install Pipenv use the command:
   
`pip install pipenv`   
   
To install all the specified dependencies:  
   
`pipenv install`  

To activate virtual environment:

`pipenv shell`   
 


## **Running a web service in a local server**   
      
The final model has been implemented in a web service, and to run it, the following steps are required:

- Install Docker: Docker can be obtained from the official website at https://www.docker.com/.

- Access the Dockerfile: In the current repository or a cloned repository on your local machine, you will find a Dockerfile containing all the specifications required to build the container. This includes Python, the virtual environment, scripts, the model file, and other dependencies.

- To construct the container, initiate Docker on your system, launch a terminal or command window and input the following command:
   
`docker build -t proj_smoking .`   
   
To run the image: 
   
`docker run -d -p 8080:8080 --name smoke_container_new  test_proj_1 proj_smoking`   
   
Run a script `request_local.py`:    
    
`pipenv run request_local.py`   

   
## **Running a web service in a cloud**   
   
To push the image on GCP repository, you need to input the following commands (after completing all the necessary steps for registration and SDK installation): 
      
`docker tag proj_smoking gcr.io/axiomatic-skill-404020/smoke_proj_repo`  (axiomatic-skill-404020 is GCP project id)
   
`docker push gcr.io/axiomatic-skill-404020/smoke_proj_repo`   
   

And then use Cloud Run to deploy the image.

<br />
      
<img src="images/Cloud_Run.png" alt="container_image"/>
     
<br />

<br />
      
<img src="images/deployed.png" alt="container_image"/>
     
<br />   

To test deployed application:

`pipenv python request_cloud.py`