
# coding: utf-8

# ### Comparing R2Scores for different Scaling Techniques in an MSE Linear Regression model

# #### The goal of this function is to choose the best scikit-learn scaling method for an MSE LR model. The function returns the training vs test R-squared values (it is common practice that the test r2S should be as equal as the training r2S as possible for a higher predictive confidence level)

# In[ ]:


def r2S(scaler, DataFrame, test_size=0.2, random_state=21):
    '''
    Computes the R2Score based on a selected scale and dataframe.
    Allows you to choose the best R2Score from a list of selected scaling techniques
    scale is the exact name of a scikit-learn scale, e.g. MinMaxScaler
    dfx is the DataFrame, assuming the last column is the target column
    A list of possible scikit-learn scalers are below
    RobustScaler
    MinMaxScaler
    MaxAbsScaler
    StandardScaler
    QuantileTransformer
    Normalizer
    
    Defaults used
    -------------
    Learning rate: 0.1
    LossType = Mean Squared Error
    Number of Epochs = 20
    Test_size (train_test_split) = 0.2
    
    Returns
    -------
    Returns the training r2Score and the test r2Scores as an array
    
    Examples
    --------
    >> df = pd.read_csv('sampledataFrame.csv')
    >> r2S(RobustScaler,df)
    [r2Score for training set, r2score for test set]
    '''
    get_ipython().run_line_magic('matplotlib', 'inline')
    import pandas as pd, numpy as np, matplotlib.pyplot as plt

    from sklearn.preprocessing import RobustScaler, MinMaxScaler, MaxAbsScaler, StandardScaler, QuantileTransformer, Normalizer
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import r2_score

    from keras.models import Sequential
    from keras.layers import Dense
    from keras.optimizers import Adam
    for i in DataFrame.columns:
        DataFrame[[i]] = scaler().fit_transform(DataFrame[[i]].values)
    X = DataFrame[DataFrame.columns[:-1]]
    y = DataFrame[DataFrame.columns[-1]]
    
    sq = Sequential()
    sq.reset_states()
    sq.add(Dense(1, input_shape=(len(DataFrame.columns)-1,)))
    sq.compile(Adam(lr=0.1), loss='mean_squared_error')
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    sq.fit(X, y, epochs=20, verbose=0)
    
    return [r2_score(y_train, sq.predict(X_train)),r2_score(y_test, sq.predict(X_test))]

