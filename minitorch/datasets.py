import math
import random
from dataclasses import dataclass
from typing import List, Tuple


def make_pts(N: int) -> List[Tuple[float, float]]:
    """Generate N random points in a 2D space.

    Args:
    ----
        N (int): Number of points to generate.

    Returns:
    -------
        List[Tuple[float, float]]: List of generated points.

    """
    X = []
    for i in range(N):
        x_1 = random.random()
        x_2 = random.random()
        X.append((x_1, x_2))
    return X


@dataclass
class Graph:
    """Data structure to hold a graph of points and their labels.

    Attributes
    ----------
        N (int): Number of points.
        X (List[Tuple[float, float]]): List of points.
        y (List[int]): List of labels for the points.

    """

    N: int
    X: List[Tuple[float, float]]
    y: List[int]


def simple(N: int) -> Graph:
    """Generate a simple dataset where points are labeled based on their x-coordinate.

    Args:
    ----
        N (int): Number of points to generate.

    Returns:
    -------
        Graph: Generated graph with points and labels.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def diag(N: int) -> Graph:
    """Generate a dataset where points are labeled based on their position relative to the diagonal.

    Args:
    ----
        N (int): Number of points to generate.

    Returns:
    -------
        Graph: Generated graph with points and labels.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < x_2 else 0
        y.append(y1)
    return Graph(N, X, y)


def split(N: int) -> Graph:
    """Generate a dataset where points are labeled based on their x-coordinate with a split.

    Args:
    ----
        N (int): Number of points to generate.

    Returns:
    -------
        Graph: Generated graph with points and labels.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.2 or x_1 > 0.8 else 0
        y.append(y1)
    return Graph(N, X, y)


def xor(N: int) -> Graph:
    """Generate a dataset where points are labeled based on XOR of their coordinates.

    Args:
    ----
        N (int): Number of points to generate.

    Returns:
    -------
        Graph: Generated graph with points and labels.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if ((x_1 < 0.5 and x_2 > 0.5) or (x_1 > 0.5 and x_2 < 0.5)) else 0
        y.append(y1)
    return Graph(N, X, y)


def circle(N: int) -> Graph:
    """Generate a dataset where points are labeled based on their distance from the center.

    Args:
    ----
        N (int): Number of points to generate.

    Returns:
    -------
        Graph: Generated graph with points and labels.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        x1, x2 = (x_1 - 0.5, x_2 - 0.5)
        y1 = 1 if x1 * x1 + x2 * x2 > 0.1 else 0
        y.append(y1)
    return Graph(N, X, y)


def spiral(N: int) -> Graph:
    """Generate a dataset where points are labeled based on a spiral pattern.

    Args:
    ----
        N (int): Number of points to generate.

    Returns:
    -------
        Graph: Generated graph with points and labels.

    """

    def x(t: float) -> float:
        return t * math.cos(t) / 20.0

    def y(t: float) -> float:
        return t * math.sin(t) / 20.0

    X = [
        (x(10.0 * (float(i) / (N // 2))) + 0.5, y(10.0 * (float(i) / (N // 2))) + 0.5)
        for i in range(5 + 0, 5 + N // 2)
    ]
    X = X + [
        (y(-10.0 * (float(i) / (N // 2))) + 0.5, x(-10.0 * (float(i) / (N // 2))) + 0.5)
        for i in range(5 + 0, 5 + N // 2)
    ]
    y2 = [0] * (N // 2) + [1] * (N // 2)
    return Graph(N, X, y2)


datasets = {
    "Simple": simple,
    "Diag": diag,
    "Split": split,
    "Xor": xor,
    "Circle": circle,
    "Spiral": spiral,
}
