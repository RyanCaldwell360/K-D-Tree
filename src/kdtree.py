import numpy as np
import pandas as pd
from datetime import datetime

class Node:
    """
    k-d tree node for data assignment
    This class assigns data to Node object for tree construction.

    Parameters
    ----------
    file : ndarray
        Numpy array of records in subfile
    """
    def __init__(self, file):
        self.file = file
        self.file_size = file.shape[0]
        self.left = None
        self.right = None
        self.discriminator = None
        self.partition = None

class KDTree:
    """
    kd-tree for quick nearest-neighbor lookup
    This class builds a k-d tree for quick nearest neighbors lookup.

    Parameters
    ----------
    file : ndarray
        Numpy array of records to build out tree
    bucket_size : int
        The number of records in a subfile where tree depth
        stops and creates a terminal leaf

    Notes
    -----
    The algorithm used is described in Friedman et el 1975. The paper
    has been revised in Dec 1975 and July 1976.
    """
    def __init__(self, file, bucket_size):
        self.file = file
        self.bucket_size = bucket_size
        self.n_keys = file.shape[1]

    def build_tree(self, node):
        if node.file_size <= self.bucket_size:
            return

        node.discriminator = self.spreadest(node.file)
        node.partition = np.median(node.file[:,node.discriminator])
        left_split, right_split = self.split_array(node.discriminator,
                                                   node.partition,
                                                   node.file)
        node.left = Node(left_split)
        node.right = Node(right_split)

        self.build_tree(node.left)
        self.build_tree(node.right)

    def split_array(self, discriminator, partition, file):
        """Returns tuple of arrays for left and right splits.

           Parameters
           ----------
           discriminator : int
               The discriminating key for subfile split
           partition : float
               The optimal split value for the discriminator
           file : ndarray
               The numpy array of values for each key in subfile

           Returns
           -------
           tuple : ndarray
               tuple of left and right splits
        """
        indexes = file[:,discriminator] <= partition
        left_array = file[indexes]
        right_array = file[~indexes]

        return (left_array,right_array)

    def spreadest(self, file):
        """Returns the range of each key in the subfile.

           Parameters
           ----------
           file : ndarray
               The numpy array of values for each key in subfile

           Returns
           -------
           int
               index at key with largest range
        """
        min_ = np.min(file, axis=0)
        max_ = np.max(file, axis=0)
        max_range_key = np.argmax(max_ - min_)

        return max_range_key

    def search(self):
        pass

    def ball_within_bounds(self):
        pass

    def bounds_overlap_ball(self):
        pass

    def coordinate_distance(self):
        pass

    def dissimilarity(self):
        pass
