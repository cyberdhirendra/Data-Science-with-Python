from sklearn import tree
#[height,weight,shoe_size]
x = [[180,44,34],[178,55,56],[189,56,33],[180,56,23],[167,45,35],[183,46,56],[181,60,45]]
y = ['male','female','male','male','female','male','female']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
prediction = clf.predict([[181,43,55]])
print(prediction)
