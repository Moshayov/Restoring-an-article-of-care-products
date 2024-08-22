# Restoring-an-article-of-care-products
A-Introduction
The article highlights a significant problem facing consumers in today's beauty market: the difficulty of choosing the right natural beauty products amidst a vast and sweeping range of options.Over the past few years, the beauty industry has experienced rapid and expanding growth, introducing a growing range of products.Many of these products contain harsh chemicals that, while designed to improve the appearance of the skin, can actually lead to negative side effects, including irritation, allergic reactions, and long-term skin damage.This growing awareness of the potential dangers associated with chemical-laden skincare has pushed both manufacturers and consumers to shift their focus to natural beauty alternatives.

However, this shift towards natural products,despite good intentions,presented a new dilemma.The market is now flooded with an abundance of enhancers, each claiming to offer unique benefits.This abundance of options has left consumers stunned and uncertain about which product is really best for their specific skin type and needs.The challenge is further complicated by the reliance on customer reviews as a primary source of information for making purchase decisions. While reviews can provide valuable insights, they are often inconsistent, with some customers praising a product while others reporting disappointing results.This inconsistency creates confusion and makes it even more challenging for consumers to make informed choices, which can lead to the use of products that may not be appropriate or beneficial for their skin.



B. Methods – 
The method chosen for the solution is sentiment analysis, we will analyze customer reviews about the products and draw conclusions from them.
The solution to the problem of choosing the right natural beauty products is based on sentiment analysis, which leverages natural language processing (NLP) and text analysis to assess customer opinions, emotions and attitudes towards the products.Sentiment analysis is essential in this regard, as it helps businesses gain insights into whether the overall sentiment of reviews is positive, neutral or negative.
Stages of the study:
1.	Preliminary research,
2.	Data preparation
3.	,Pre-processing data
4.	Data analysis
5.	System architecture design,
6.	Interface design
7.	System development
8.	System testing and evaluation

Phase 1 Preliminary Research:
It starts with identifying the problem area and conducting a thorough investigation of its problems or problems. In this study, the issue of customer reviews about natural skin care products is addressed through the positives and negatives of reviews on the Internet.
Step2: Prepare the data:
Home page of the Sephora.com website was selected for data collection.
 The figure below shows the presented reviews Sephora. com.  This information will then be collected. The reviews collected are based on the most helpful reviews recognized by the user who has read them before. These reviews are the most reliable for collection.










Once we had all the necessary data and carried out the preparation and processing on it, we moved on to classification. 
We classified the data using:
•	Naïve Bayes 
•	KNN
•	SVM
•	Decision tree accuracy
•	Deep learning

Explanation of the classifiers:
Naïve Bayes Classifier 
The Bayes Theorem, based on Naive Bayes, assumes that all attributes, regardless of any 
relationships, independently contribute to the datasets' probability. In other words, the Naïve Bayes 
algorithm predicts a class given a set of features using probability.
The code: 
 

K-NN Classifier
 The following classification techniques used are K-nearest neighbors. KNN can be used both in regression and classification problems. The class of a red star is not decided yet. Make a circle first be the red star as the center. Assuming that K=3, the three closest points to the red star are all blue circles; hence, it can be decided that the red star is in a class of blue circles, as shown in the figure 
The code:







Support Vector Machine Classifier
 The Support Vector Machines Classifier (SVM), a discriminative classifier formally described by a separating hyperplane, created procedures for an ideal hyperplane using training datasets. SVM is frequently employed to solve classification and regression issues. The data points closest to the hyperplane are known as support vectors, as shown in the figure.
The code:

Decision Tree Classifier
 Decision Tree are supervised learning also used for classification and regression. Decision trees learn from data to approximate a sine curve with a set of if-then-else decision rules. The deeper the tree, the more complex the decision rules, and the fitter the model.
The code:
 

Deep Learning Classifier 
Deep Learning is based on a multi-layer feed-forward artificial neural network trained with stochastic gradient descent using back-propagation. The network can contain many hidden layers consisting of neurons with tanh, rectifier, and max-out activation functions.
The code: 
C. Data:
We collected the data from the SEPHORA website using a data mining tool called DATA Miner, with which you can collect data from a browser into an Excel file.We selected the brands on which the article is based and collected a quantity of reviews as indicated in the article.
The data we collected is divided across 4 brands
Number of reviews collected in the article	Number of reviews collected by us	brand
1802	1878	Drunk Elephant
2207	2207	Origins
1800	1808	Belief
2287	2206	Laneige

As you can see, the amount of data we collected is very similar to the amount of data collected in the article.
We collected the data through the data miner like this: 

Here's how the data is saved: 


After this process, we have the desired data as it exists in the article and can begin to do what is required.
Now, we can start with the data cleanup phase where we remove unnecessary words – link words and stop words, so that the text is narrow and easy to work with sentiment analysis.
The code for cleaning the data is code written in Python that uses the libraries:
 pandas, nltk, stopword

Here's how the data looks after cleaning:




Cleaning the data is important to ensure that the machine learning steps can be performed without errors,since in text analysis,the machine only reads text.
Now we have come to the part where the data is divided into training data and test data.
In the article, the data were randomly divided into ratios of 70% testing and 30% training.
But with us, because there was a problem (as detailed below), we took a sample of 10 random rows (we used Python code to select the random rows) from each brand = 40 in total and checked the percentage of positives and negatives there, and found that 85% of the responses were positive and 15% negative.
At this pointwe used aTEXTBLOB analyzer and got that its positive-to-negative ratio is 87 percent positive versus negative 13 which is quite close to what we got.
We performed sentiment analysis by TEXTBLOB on all data files so that each review had a positive/negative tag according to the sentiment of the review and analysis according to TEXTBLOB.
The code for analyzing sentiment:
 

Classification of data:
Once our data is divided into training and test data, we can classify them.
We used 5 types of classifiers, in each of which we took 30 percent of the data for testing and 70 percent for training.
Here arethe accuracy results we received from each of the grooming companies:






1.	NAÏVE BAYSE 
% Correctness in our study	% Article correctness	Beauty Brand
88	71	Laneige
83	80	Drunk Elephant
86	62	Origins
92	83	Belif

2.	KNN
% Correctness in our study	% Article correctness	Beauty Brand
84	82	Laneige
73	84	Drunk Elephant
83	70	Origins
90	89.98	Belif

3.	SVM
% Correctness in our study	% Article correctness	Beauty Brand
88	82	Laneige
85	85	Drunk Elephant
87	75	Origins
91	88.36	Belif

4.	Decision tree accuracy
% Correctness in our study	% Article correctness	Beauty Brand
87	82.84	Laneige
85	88	Drunk Elephant
86	71.38	Origins
89	88.36	Belif






5.	Deep learning
% Correctness in our study	% Article correctness	Beauty Brand
89	80.89	Laneige
86	85.9	Drunk Elephant
87	73.62	Origins
92	89.29	Belif

In summary: we ran all the classifieds, in some cases we got exactly the same as in thearticleand some slightly different.
Probably because the data we worked on were slightly different, even though the way the information was collected was like theirs, but in practice time passes and the data changes (new comments are added that affect the result).


 	 
 	 
Results:


Conclusion:
We have accepted that a decision tree and deep learning bring the best results.
Recommendation for balanced brands:
Considering both the positive and negative reaction data and the performance of the models, the two most balanced brands with good results are LANEIGE and ORIGIN.
LANEIGE: It has high positive responses (90%) and high model accuracy (around 89.55%).
ORIGIN: It has positive responses of 85% and relatively good accuracy (88%).
Both of these brands present a good balance between positive reactions and performance results, so they are recommended


Problems we encountered:

•	STARTING WITH OBTAINING THE DATA – WE FOUND DATA THAT DIDN'T MATCH WHAT WE NEEDED AND HAD TO START FROM SCRATCH, WE USED A TOOL CALLED DATA MINER TO GET THE DATA WE NEEDED.
•	We had trouble finding a brand that we looked at in the article because we no longer make products from the brand, so we just did without it.
•	In order to perform sentiment analysis in the article, they used rapid MINER and we got in trouble and couldn't and got stuck. We thought about splitting the training part ourselves and checked the positives and negatives of the reviews manually and it was exhausting.
We received advice from the lecturer to perform sentiment analysis using Python libraries, and we did, and we succeeded.



Bibliography:
References Atikah, N., Wavi, N., Suhaida, N., Fahmi, M., Yusof, M., Iskandar, M., … Rahim, M. (2017). THE FACTORS THAT INFLUENCE THE CONSUMPTION OF LOCAL COSMETIC PRODUCTS AMONG CONSUMERS IN KOTA BHARU, KELANTAN. Ben-Noun (Nun), L. (2016). BEAUTY OF HUMANS. Jhawar, N., Schoenberg, E., & Wang, J. V. (2018). US CR. Clinics in Dermatology #pagerange#. Johnsy, G., S. Davidson Sargunam, and V. Kaviyarasan., 4, 1.
Vol.2022:12 Krishnan, S., Safia Amira, N., Nur Atilla, U., Syafawani, S., & Hafiz, M. (2017). The Usage of Cosmetic in Malaysia: Understanding the Major Factors that Affect the Users. Management, 2017(1), 48–51. Retrieved from http://journal.sapub.org/mm Masłowska, E., Malthouse, E., & Bernritter, S. (2017). The Effect of Online Customer Reviews' Characteristics on Sales. https://doi.org/10.1007/978-3-658-15220-8_8 Mawazi, S., Ann, J., Othman, N., Khan, J., Alolayan, S., thagfan, S., & Kaleemullah, M. (2022). A Review of MoisturizersMoisturizers; CharacterizationCharacterization and Applications. History, Cosmetics, Preparation, 9, 61. https://doi.org/10.3390/cosmetics9030061 Nanjwade, B. (2017). DEVELOPMENT OF COSMECEUTICALS. World Journal of Pharmacy and Pharmaceutical Sciences, 643–691. https://doi.org/10.20959/wjpps20174-8927 Nilforoushzadeh, M., Amirkhani, M., Zarrintaj, P., Moghaddam, A., Mehrabi, T., Alavi, S., & Mollapour, M. (2018). Skin care and rejuvenation by cosmeceutical facial mask. Journal of Cosmetic Dermatology, 17. https://doi.org/10.1111/jocd.12730 Osei-Frimpong, K., Donkor, G., & Owusu‐ Frimpong, N. (2019). The Impact of Celebrity Endorsement on Consumer Purchase Intention: An Emerging Market Perspective. The Journal of Marketing Theory and Practice, 27, 103–121. https://doi.org/10.1080/10696679.2018.1534070 Shankar, P. R., & Palaian, S. (2007). Fair skin in South Asia: An obsession? Journal of Pakistan Association of Dermatologists, 17. Waldron, M. (2014). Why is Sentiment Analysis important from a business perspective? Retrieved from http://blog.aylien.com/why-is-sentiment-analysis-important-from-a/


We took the data from SEPHORA.com site
We took them out using https://dataminer.io/






