Credit Card Fraud Detection: Capstone Project

In recent times, the number of fraud transactions has increased drastically due to which credit card companies are facing a lot of challenges. For many banks, retaining high profitable customers is the most important business goal. Banking fraud, however, poses a significant threat to this goal. In terms of substantial financial loss, trust, and credibility, banking fraud is a concerning issue for both banks and customers alike. With the rise in digital payment channels, the number of fraudulent transactions is also increasing as fraudsters are finding new and different ways to commit such crimes.

 

Now, let’s watch the upcoming video as Thejasvee sheds light on fraud analytics, some common types of fraud happening across different industries and the different ways in which you can deal with it using machine learning.

As you learnt in the video above, credit card fraud is an inclusive term for fraud that is committed using a payment card, such as a credit card or a debit card, by stealing the card information through skimmers. The Federal Trade Commission (US) has estimated that around 10 million people become victims of credit card theft each year. Credit card companies lose close to $50 billion per year to fraud.

 

Finex is a leading financial service provider based out of Florida, US. It offers a wide range of products and business services to customers through different channels, ranging from in-person banking and ATMs to online banking. Over the last few years, Finex has observed that a significantly large number of unauthorised transactions are being made, due to which the bank has been facing a huge revenue and profitability crisis. Many customers have been complaining about unauthorised transactions being made through their credit/debit cards. It has been reported that fraudsters use stolen/lost cards and hack private systems to access the personal and sensitive data of many cardholders. They also indulge in ATM skimming at various POS terminals such as gas stations, shopping malls, and ATMs that do not send alerts or do not have OTP systems through banks. Such fraudulent activities have been reported to happen during non-peak and odd hours of the day leaving no room for suspicion.

 

In most cases, customers get to know of such unauthorised transactions happening through their cards quite late as they are unaware of such ongoing credit card frauds or they do not monitor their bank account activities closely. This has led to late complaint registration with Finex and by the time the case is flagged fraudulent, the bank incurs heavy losses and ends up paying the lost amount to the cardholders.

 

Now, Finex is also not really equipped with the latest financial technologies, and it is becoming difficult for the bank to track these data breaches on time to prevent further losses. The Branch Manager is worried about the ongoing situation and wants to identify the possible root causes and action areas to come up with a long-term solution that would help the bank generate high revenue with minimal losses.

 

Reading Material:

Go through the links provided below to understand how credit card frauds happen, the different ways of fraud and the techniques involved in making fraud transactions.

Credit Card Fraud
How Credit Card Skimming Works
Now, suppose you are consulting Finex for solving the issue of the rise in unauthorised transactions made through credit cards/debit cards. As the first step to solving this problem, you are required to understand the pipeline for a typical transaction and the challenges at each of these steps of the transaction process so that you can make appropriate interventions to solve the problem. Based on the background information and the reading links provided above, apply a basic framework to understand the business and subsequently dig deeper into the problem.

 Understanding and Defining Fraud

Credit card fraud is any dishonest act or behaviour to obtain information without the proper authorisation of the account holder for financial gain. Among the different ways of committing fraud, skimming is the most common one. Skimming is a method used for duplicating information located on the magnetic stripe of the card.  Apart from this, other ways of making fraudulent transactions are as follows:

Manipulation or alteration of genuine cards
Creation of counterfeit cards
Stolen or lost credit cards
Fraudulent telemarketing

Data Understanding

This is a simulated data set taken from the Kaggle website and contains both legitimate and fraudulent transactions. You can download the data set using this link.

 

The data set contains credit card transactions of around 1,000 cardholders with a pool of 800 merchants from 1 Jan 2019 to 31 Dec 2020. It contains a total of 18,52,394 transactions, out of which 9,651 are fraudulent transactions. The data set is highly imbalanced, with the positive class (frauds) accounting for 0.52% of the total transactions. Now, since the data set is highly imbalanced, it needs to be handled before model building. The feature 'amt' represents the transaction amount. The feature 'is_fraud' represents class labelling and takes the value 1 the transaction is a fraudulent transaction and 0, otherwise.

 

Since the data set is huge, it will be difficult for you to work on it offline. You are advised to download the raw dataset in your Google Drive and use Google Colab to write your Python code. Create a separate folder in your Google Drive to save any code/CSV files (processed data) and the colab notebooks that you create during this project.

Project Pipeline
The project pipeline can be briefly summarised in the following steps:

 

Understanding Data: In this step, you need to load the data and understand the features present in it. This will help you choose the features that you need for your final model.

 

Exploratory data analytics (EDA): Normally, in this step, you need to perform univariate and bivariate analyses of the data, followed by feature transformations, if necessary. You can also check whether or not there is any skewness in the data and try to mitigate it, as skewed data can cause problems during the model-building phase.

 

Train/Test Data Splitting: In this step, you need to split the data set into training data and testing data in order to check the performance of your models with unseen data. You can use the stratified k-fold cross-validation method at this stage. For this, you need to choose an appropriate k value such that the minority class is correctly represented in the test folds.

 

Model Building or Hyperparameter Tuning: This is the final step, at which you can try different models and fine-tune their hyperparameters until you get the desired level of performance out of the model on the given data set. Ensure that you start with a baseline linear model before going towards ensembles. You should check if you can get a better performance out of the model by using various sampling techniques.

 

Model Evaluation: Evaluate the performance of the models using appropriate evaluation metrics. Note that since the data is imbalanced, it is important to identify which transactions are fraudulent transactions more accurately than identifying non-fraudulent transactions. Choose an appropriate evaluation metric that reflects this business goal.

 

Business Impact: After the model has been built and evaluated with the appropriate metrics, you need to demonstrate its potential benefits by performing a cost-benefit analysis which can then be presented to the relevant business stakeholders. 

 

To perform this analysis, you need to compare the costs incurred before and after the model is deployed. Earlier, the bank paid the entire transaction amount to the customer for every fraudulent transaction which accounted for a heavy loss to the bank.

Cost-Benefit Analysis
Let us take a look at what you need to do in order to perform the cost-benefit analysis step by step.

 

Part I: Analyse the dataset and find the following figures:

Average number of transactions per month 
Average number of fraudulent transactions per month
Average amount per fraudulent transaction 

Part II: Compare the cost incurred per month by the bank before and after the model deployment:

Cost incurred per month before the model was deployed = Average amount per fraudulent transaction * Average number of fraudulent transactions per month
Cost incurred per month after the model is built and deployed: <Use the test metric from the model evaluation part and the calculations performed in Part I to compute the values given below>
 

Let TF be the average number of transactions per month detected as fraudulent by the model and let the cost of providing customer executive support per fraudulent transaction detected by the model = $1.5

Total cost of providing customer support per month for fraudulent transactions detected by the model = 1.5 * TF.
Let FN be the average number of transactions per month that are fraudulent but not detected by the model 

Cost incurred due to these fraudulent transactions left undetected by the model = Average amount per fraudulent transaction * FN
Therefore, the cost incurred per month after the model is built and deployed = 1.5*TF + Average amount per fraudulent transaction * FN
Final savings = Cost incurred before - Cost incurred after.


## 🛠 Skills
python,machine learning


## 🔗 Links
dataset = https://drive.google.com/drive/folders/11FAugABNbAk38HgEkgVAbPJb7KnCLP5b?usp=drive_link

