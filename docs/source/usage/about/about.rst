=====
About
=====

Introduction
============

Natural Language Processing has created a new paradigm shift in both academia and industry today. With the cominig up of Transformers, the field has seen great growth and applications to fields which were previously unheard of.
Google's BERT has further accelerated the progress in the field. This paper can be considered as the backbone of modern NLP.
Multi-Modal systems utilize data from 2 or more modalities to make decisions. Our goal with this library is to provide an efficient, fast and reliable way to load and train models on multi-modal data.

With Tochmm, our goal is three-fold:
- To educate the user about Natural Language Processing and Multi-Modal Systems.

- Easy to understand implementations of State of the Multi-Modal Algorithms.
- Develop efficient pipelines of existing Algorithms.

.. Policies and Values
.. ===================
.. Modern research on Reinforcement Learning is majorly based on Markov Decision Processes. Policy and Value Functions are one of the core parts of such a problem formulation. And so, polices and values form one of the core parts of our library.

.. Trainers and Loggers
.. ====================

.. Trainers
.. --------

.. Most current algorithms follow a standard procedure of training. Considering a classification between On-Policy and Off-Policy Algorithms, we provide high level APIs through Trainers which can be coupled with Agents and Environments for training seamlessly.

.. Lets take the example of an On-Policy Algorithm, Proximal Policy Optimization. In our Agent, we make sure to define three methods: ``collect_rollouts``, ``get_traj_loss`` and finally ``update_policy``. 

.. .. literalinclude:: ../../../../genrl/deep/common/trainer.py
..    :lines: 507-511
..    :lineno-start: 507

.. The ``OnPolicyTrainer`` simply calls these functions and enables high level usage by simple defining of three methods.

.. Loggers
.. -------

.. At the moment, we support three different types of Loggers. ``HumanOutputFormat``, ``TensorboardLogger`` and ``CSVLogger``. Any of these loggers can be initialized really easily by the top level ``Logger`` class and specifying the individual formats in which logging should performed.

.. .. code-block:: python

..     logger = Logger(logdir='logs/', formats=['stdout', 'tensorboard'])

.. After which logger can perform logging easily by providing it with dictionaries of data. For e.g.

.. .. code-block:: python

..     logger.write({"logger":0})

.. Note: The Tensorboard logger requires an extra x-axis parameter, as it plots data rather than just show it in a tabular format.

.. Agent Encapsulation
.. ===================

.. WIP

.. Environments
.. ============
.. Wrappers
