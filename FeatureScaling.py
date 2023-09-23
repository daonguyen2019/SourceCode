_related to gradient descent
_some ML Algos where scaling wont have an effect

Feature scaling caveats:
-always scale new unseen data
-interpretability of feature coefs

Feature scaling benefits:
-lead to great increases in performance
-need for some models
-no real downside to scaling feature

Two main ways to scale features:
    -Standardization ~ Z-score normalization
        Rescales data to have a mean of 0 and standard deviation of 1
    -Normalization
        Rescales all data values to be between 0-1:
                    (X - min(X))/(max(X)-min(X))

.fit()  --> method call simply calculates the necessary statistics (Xmin, Xmax, mean, standard deviation)
.transform()  --> scales data and returns the new scaled version of data


Few important notes:
--> fit to training data only
--> calculate statistical information should only come from training data.
--> dont assume prior knowledge of the test set

data leakage --> calculate statistic from full data leads to some information of the test set

Feature scaling process:
-perform train test split
-fit to training feature data
-transform training feature data
-transform test feature data

--> dont apply feature scaling for the label/target


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
scaled_X_train = scaler.transform(X_train)
scaled_X_test = scaler.transform(X_test)

    












