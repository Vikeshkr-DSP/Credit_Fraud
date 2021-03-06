# Credit Card Fraud Detection
## Introduction
The use credit cards is increasing day by day, so there is more opprtunity for fraudsters to do fraud transaction and thus increasing the burden on credit card companies to identify  and block such transactiins so that their customers are not charged for any transactions which is not done by them. It can be easily understood how important it is to prevent any fraud transaction for both - for credit card company as weel as for their customers. This problem is all about predicting a transaction to be fraud or legitimate based on some features of that transaction so that the credir card compamies can take important step to prevent such transactions.
## DataSource
Different machine learning algorithms are trained to classify a transaction to be legitimate or a fraud. The data needed to train the model is collected from Machine Learning Group - ULB which is shared publically and can be gathered from Kaggle. This dataset have all the transaction details done in September 2013 by European cardholders. The dataset have 30 features - Time, Amount, V1 to V28 where V1 to V28 are PCA trasformed data and other two features are TIme and Amount where Time contains the seconds elapsed between each transaction and the first transaction in the dataset and Amount is the transaction Amount. There are 492 frauds out of 284,807 transactions. This dataset is highly imbalanced which can be seen by the no of fraud transaction which only accounts for 0.172% transactions. Output of this problem is to predict the transaction type as 1 for fraud transactions or 0 for legitimate transactionn. We need not to work on the data as it is already pre-processed except for Time and Amount.
## Model Training
Machine Learning model has been trained using different algorithms. AUC (Area Under the Curve) is used as the evaluation metric for measuring the performance of the model. Model with best AUC score will be used for creating the model.
### Random Forest
Firstly, Random Forest was trained with its default parameters and obtained AUC score was 0.9631 on validation data. After using all the features for model training, insignificant features (features having importance value less than 0.0125) were removed and the model was retrained on default parameters and AUC score of 0.9513 was obtained on validation data. Since all the features are PCA transformed, it is difficult to decide insignificant features. Removing any features with very less importance value is resulting towards worsening in the prediction or reduction in AUC score.
### XGBoost
XGBoost was firstly trained with its default parameters and AUC score obtained on validation data was 0.9760. As we have experienced reduction is AUC score after removing some features in Random Forest, so any feature is not removed for training XGBoost. HPT (Hyperparameter Tuning) was done considering all the independent feature and AUC score of 0.9871 was obtained which is the best so far. After upsampling the minority class using SMOTE gives an AUC score of 0.9834 on validation data which is less than the previous.
### Logistic Regression
As we know Logistic Regression is a distance based algorithm and all tha features needs to scaled before being used for model training. Only two features, Time and Amount needs to be rescaled as all the features are akready scaled. After rescaling the features, it was used to train Logistic Regression with default parameters and AUC score of 0.7588 was obtained which is very less. As we know this is a imbalanced class problem, so SMOTE (Upsampling) was used to create some random observation which will make the training data balanced. After SMOTE, Logistic Regression gives an AUC score of 0.9350 which is improved a lot but is less than the AUC score of Random Forest and XGBoost.

XGBoost got the best AUC score of 0.9871 and will be used for deployment and app creation.
## Web App
Wep app has been created and deployed using Flask on Azure which can be accessed at https://credit-fraud.azurewebsites.net/ and looks like:
![image](https://user-images.githubusercontent.com/66907101/123978162-45624500-d9dd-11eb-90fd-f0e26db9464b.png)
You need to provide all the details asked and select Submit button. The web app will predict whether the transaction is fraud or legitimate depending upon the values passed.
## Technology Used
* Jupyter Notebook (Python 3.8)
* Spyder (creating app.py)
* VS Code (creating front end web page)
* Azure and Github (for deployment)
