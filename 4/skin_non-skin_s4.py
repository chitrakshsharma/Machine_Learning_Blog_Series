# part - 4
# This part is in continuation with script_3
s_data = data[data[ : , 3] == 1]
ns_data = data[data[ : , 3] == 2]

print("Total Skin data: " + str(s_data.shape))
print("Total Non-Skin data: " + str(ns_data.shape))

folds = 5
total_score = 0
for i in range(0, folds):
    tr_s_data = sp.delete(s_data, [range( int(i*(len(s_data)/folds)), int((i+1)*(len(s_data)/folds)) )], 0)
    te_s_data = s_data[int(i*(len(s_data)/folds)) : int((i+1)*(len(s_data)/folds)), :]
    #print("te_s_data shape: " + str(te_s_data.shape))

    
    tr_ns_data = sp.delete(ns_data, [range( int(i*(len(ns_data)/folds)), int((i+1)*(len(ns_data)/folds)) )], 0)
    te_ns_data = ns_data[int(i*(len(ns_data)/folds)):int((i+1)*(len(ns_data)/folds)), :]
    #print("te_ns_data shape: " + str(te_ns_data.shape))

    
    tr_data = np.vstack((tr_s_data, tr_ns_data))
    te_data = np.vstack((te_s_data, te_ns_data))

    np.random.shuffle(tr_data)
    np.random.shuffle(te_data)

    #print("tr_data shape: " + str(tr_data.shape))
    #print("te_data shape: " + str(te_data.shape))


    tr_Y = tr_data[:, (len(tr_data[0]) - 1)]
    tr_X = tr_data[:, range(0, 3)]
    te_Y = te_data[:, (len(tr_data[0]) - 1)]
    te_X = te_data[:, range(0, 3)]
    
    predicted = NN_Classify(tr_X, tr_Y, te_X)
    score = NN_Score(te_Y, predicted)
    print("score in fold " + str(i) + ": " + str(score))
    total_score += score
    
avg_score = total_score / folds
print("for " + str(folds) + " folds cross validation, accuracy is: " + str(avg_score))
