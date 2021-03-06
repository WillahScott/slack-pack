# -*- coding: utf-8 -*-

"""Implementation of different distances to use for a geometry

Note
----
The following are in fact _similarities_ and not distances (a score of 1 means very similar, a score of 0 means very different)

.. module:: nlp.geometry.dist
   :platform: Unix, Windows
   :synopsis: Distances between message representations

.. |message| replace:: :class:`nlp.text.message.Message`
.. |tokenizer| replace:: :class:`nlp.text.grammar.tokenizer`
.. |sentgram| replace:: :class:`nlp.text.grammar.grammar_analyzer`

"""

import numpy as np
from scipy.stats import entropy


def cosine(repr1, repr2):
    """Calculate the `cosine similarity<https://en.wikipedia.org/wiki/Cosine_similarity>`_ between two object representations

    Parameters
    ----------
    repr1 : list[float]
        Representation of object 1
    repr2 : list[float]
        Representation of object 2

    Returns
    -------
    float
        Distance/Similarity between the two object representations
    """
    return (np.array(repr1) * np.array(repr2)).sum() / (np.linalg.norm(repr1) * np.linalg.norm(repr2))


def jensen_shannon(repr1, repr2):
    """Calculate the `Jensen-Shannon Divergence<https://en.wikipedia.org/wiki/Jensen%E2%80%93Shannon_divergence>`_ between two object representations

    Parameters
    ----------
    repr1 : list[float]
        Representation of object 1
    repr2 : list[float]
        Representation of object 2

    Returns
    -------
    float
        Distance/Similarity between the two object representations
    """
    _repr1 = repr1 / np.linalg.norm(repr1, ord=1)
    _repr2 = repr2 / np.linalg.norm(repr2, ord=1)
    mid_repr = 0.5 * (_repr1 + _repr2)

    return 0.5 * (entropy(_repr1, mid_repr) + entropy(_repr2, mid_repr))


def cross_entropy(repr1, repr2):
    """Calculate the cross-entropy (or `Kullback-Leibler Divergence<https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence>`_) between two object representations

    Parameters
    ----------
    repr1 : list[float]
        Representation of object 1
    repr2 : list[float]
        Representation of object 2

    Returns
    -------
    float
        Distance/Similarity between the two object representations
    """
    return entropy(repr1, repr2)


