import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def month(x):
    # Converts "January" -> 0, "February" -> 1, ..., "December" -> 11
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(x)
def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    with open(filename, mode="r", newline='') as file:
        reader=csv.reader(file)
        next(reader)
        rows=list(reader)
        result=[]
        label=[]
        data=[int,float,int,float,int,float,float,float,float,float,month,int,int,int,int,lambda x: 1 if x=="Returning_Visitor" else 0, lambda x: 0 if x=="FALSE" else 1]
        for r in rows:
            temp=[c(v) for c,v in zip(data,r[:-1])]
            result.append(temp)
            label.append(1 if r[-1]=="TRUE" else 0)
        return (result, label)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    k=KNeighborsClassifier(
            n_neighbors=1,
    )
    return k.fit(evidence,labels)


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    p=0
    n=0
    ln,lp=0,0
    for x,y in zip(labels,predictions):
        if x==1:
            lp+=1
            if x==y:
                p+=1
        else:
            ln+=1
            if x==y:
                n+=1

    return (p/lp, n/ln)





if __name__ == "__main__":
    main()
