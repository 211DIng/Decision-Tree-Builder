# Decision Tree Builder

This is an implementation of [Hunt's decision tree algorithm](http://www.hypertextbookshop.com/dataminingbook/working_version/contents/chapters/chapter001/section003/blue/page004.html) in Python.
It uses the [Gini index](https://en.wikipedia.org/wiki/Decision_tree_learning#Gini_impurity) as it's impurity measure.

It takes as input a csv file of attribute tuples and their class labels in the following form --

```
Attribute 1, Attribute 2,.... Attribute n, Class Label
Attribute 1, Attribute 2,.... Attribute n, Class Label
Attribute 1, Attribute 2,.... Attribute n, Class Label
Attribute 1, Attribute 2,.... Attribute n, Class Label
```

Please note that both attributes and their associated class labels must be numeric (integers specifically)

For example an acceptable dataset might look like this --
```
1,1,1,2,2
1,1,1,1,2
2,1,1,2,1
3,2,1,2,1
3,3,2,2,1
3,3,2,1,2
2,3,2,1,1
1,2,1,2,2
1,3,2,2,1
3,2,2,2,1
1,2,2,1,1
2,2,1,1,1
2,1,2,2,1
3,2,1,1,2
```

The output decision tree will look like this - 

```
|’root’
	|-‘child 1 of root’
		|--‘child of child 1’
		|--
		|--
		And so on...
	|-‘child 2 of root’
		|--‘child of child 2’
		|--
		|--
		And so on...
	|-
	And so on...

```

For example, the output produced by the above example dataset is the following --

```
|'Attribute 0'
	|-'Attribute 2'
		|--'Label 2'
		|--'Label 1'
	|-'Label 1'
	|-'Attribute 3'
		|--'Label 2'
		|--'Label 1'
```

DTree_Driver.py is the driver program that parses a specified input csv file and write the produced decision tree to a specified output text file.

Usage:

```
$ DTree_Driver.py input.csv output.txt
```
