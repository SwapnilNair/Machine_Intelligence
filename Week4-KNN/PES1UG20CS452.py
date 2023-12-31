import numpy as np


class KNN:
    """
    K Nearest Neighbours model
    Args:
        k_neigh: Number of neighbours to take for prediction
        weighted: Boolean flag to indicate if the nieghbours contribution
                  is weighted as an inverse of the distance measure
        p: Parameter of Minkowski distance
    """

    def __init__(self, k_neigh, weighted=False, p=2):
        self.weighted = weighted
        self.k_neigh = k_neigh
        self.p = p

    def fit(self, data, target):
        """
        Fit the model to the training dataset.
        Args:
            data: M x D Matrix( M data points with D attributes each)(float)
            target: Vector of length M (Target class for all the data points as int)
        Returns:
            The object itself
        """
        self.data = data
        self.target = target.astype(np.int64)

        return self
        
    def mink(self,A,B):
        n = len(A)
        sum = 0
        for i in range(n):
            sum += abs(A[i]-B[i])**self.p
        k = sum**(1/self.p)
        return k
        
    def find_distance(self, x):
        """
        Find the Minkowski distance to all the points in the train dataset x
        Args:
            x: N x D Matrix (N inputs with D attributes each)(float)
        Returns:
            Distance between each input to every data point in the train dataset
            (N x M) Matrix (N Number of inputs, M number of samples in the train dataset)(float)
        """       
        KNN = []

        for point in x:
            knn = []
            for point2 in self.data:
                knn.append(self.mink(point,point2))
            KNN.append(knn)
        return KNN
        
    def k_neighbours(self, x):
        """
        Find K nearest neighbours of each point in train dataset x
        Note that the point itself is not to be included in the set of k Nearest Neighbours
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            k nearest neighbours as a list of (neigh_dists, idx_of_neigh)
            neigh_dists -> N x k Matrix(float) - Dist of all input points to its k closest neighbours.
            idx_of_neigh -> N x k Matrix(int) - The (row index in the dataset) of the k closest neighbours of each input

            Note that each row of both neigh_dists and idx_of_neigh must be SORTED in increasing order of distance
        """

        k = list(map(lambda x: (sorted(x))[:self.k_neigh],self.find_distance(x)))
        k2 = self.find_distance(x)
        next = [[] for i in k]
        for i in range(len(k)):
            for j in k[i]:
                next[i].append(k2[i].index(j))
        return [k,next]

    def predict(self, x):
        """
        Predict the target value of the inputs.
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            pred: Vector of length N (Predicted target value for each input)(int)
        """
        next = self.k_neighbours(x)[1]
        weights = list(map(lambda x : self.target[x],next))
        preds = list(map(lambda x:np.bincount(x).argmax(),weights))
        
        return preds
        

    def evaluate(self, x, y):
        """
        Evaluate Model on test data using 
            classification: accuracy metric
        Args:
            x: Test data (N x D) matrix(float)
            y: True target of test data(int)
        Returns:
            accuracy : (float.)
        """
        exp = self.predict(x)
        total = len(exp)
        success = [int(exp[i] == y[i]) for i in range(total)]
        ratio = sum(success)/total
        return ratio*100
