from prml.bayesnet.probability_function import ProbabilityFunction
from prml.bayesnet.random_variable import RandomVariable
import numpy as np


class DiscreteVariable(RandomVariable):
    """
    Discrete random variable
    """

    def __init__(self, n_class: int):
        self.n_class = n_class
        self.parent = []
        self.message_from = {self: np.ones(n_class)}
        self.child = []
        self.is_observed = False
        self.posterior = None
        self.prior = None
        self.likelihood = None

    def add_parent(self, parent):
        self.parent.append(parent)

    def add_child(self, child):
        self.child.append(child)
        self.message_from[child] = np.ones(self.n_class)

    @property
    def probability(self):
        return self.posterior

    def receive_message(self, message, giver, prop_range):
        self.message_from[giver] = message
        self.summarize_message()
        self.send_message(prop_range, exclude=giver)

    def summarize_message(self):
        if self.is_observed:
            self.prior = self.message_from[self]
            self.likelihood = self.prior
            self.posterior = self.prior
            return

        self.prior = np.ones(self.n_class)
        for func in self.parent:
            self.prior *= self.message_from[func]
        self.prior /= np.sum(self.prior, keepdims=True)  # 正規化

        self.likelihood = np.copy(self.message_from[self])
        for func in self.child:
            self.likelihood *= self.message_from[func]

        self.posterior = self.prior * self.likelihood
        self.posterior /= self.posterior.sum()  # 正規化

    def send_message(self, prop_range=1, exclude=None):
        for func in self.parent:
            if func is not exclude:
                func.receive_message(self.likelihood, self, prop_range)
        for func in self.child:
            if func is not exclude:
                func.receive_message(self.prior, self, prop_range)

    def observe(self, data: int, prop_range=1):
        """
        set observed data for this variable.

        :param data: observed data of this variable.
        :param prop_range: Range to propagate the observation effect to the other random variable using belief propagation alg.
        """
        assert (0 <= data < self.n_class)
        self.is_observed = True
        self.receive_message(np.eye(self.n_class)[data], self, prop_range=prop_range)

    def __str__(self):
        tmp = f"DiscreteVariable("
        if self.is_observed:
            tmp += f"observed={self.probability})"
        else:
            tmp += f"probability={self.probability})"
        return tmp

    def __repr__(self):
        return self.__str__()


class DiscreteProbability(ProbabilityFunction):
    """
    Discrete probability function
    """

    def __init__(self, table: np.ndarray, *condition, out=None, name: str = None):
        """
        initialize discrete probability function
        :param table: probability table
        :param condition: tuple of DiscreteVariable, optional
        :param out: DiscreteVariable or list of DiscreteVariable, optional
        :param name: name of this discrete probability function
        """
        self.table = np.asarray(table)
        self.condition = condition
        if condition:
            for var in condition:
                var.add_child(self)
        self.message_from = {var: var.prior for var in condition}

        if out is None:
            self.out = [DiscreteVariable(len(table))]
        elif isinstance(out, DiscreteVariable):
            self.out = [out]
        else:
            self.out = out

        for i, random_variable in enumerate(self.out):
            random_variable.add_parent(self)
            self.message_from[random_variable] = np.ones(np.size(self.table, i))

        for random_variable in self.out:
            self.send_message_to(random_variable, prop_range=0)

        self.name = name

    def __str__(self):
        if self.name is not None:
            return self.name
        else:
            return super().__repr__()

    def __repr__(self):
        return self.__str__()

    def receive_message(self, message, giver, prop_range):
        self.message_from[giver] = message
        if prop_range:
            self.send_message(prop_range, exclude=giver)

    @staticmethod
    def expand_dims(x, n_dim, axis):
        shape = [-1 if i == axis else 1 for i in range(n_dim)]
        return x.reshape(*shape)

    def compute_message_to(self, destination):
        probability = np.copy(self.table)
        for i, random_variable in enumerate(self.out):
            if random_variable is destination:
                index = i
                continue
            message = self.message_from[random_variable]
            probability *= self.expand_dims(message, probability.ndim, i)
        for i, random_variable in enumerate(self.condition, len(self.out)):
            if random_variable is destination:
                index = i
                continue
            message = self.message_from[random_variable]
            probability *= self.expand_dims(message, probability.ndim, i)
        axis = list(range(probability.ndim))
        axis.remove(index)
        message = np.sum(probability, axis=tuple(axis))
        message /= np.sum(message, keepdims=True)
        return message

    def send_message_to(self, destination, prop_range=-1):
        message = self.compute_message_to(destination)
        destination.receive_message(message, self, prop_range)

    def send_message(self, prop_range, exclude=None):
        prop_range = prop_range - 1
        for random_variable in self.out:
            if random_variable is not exclude:
                self.send_message_to(random_variable, prop_range)

        if prop_range == 0:
            return

        for random_variable in self.condition:
            if random_variable is not exclude:
                self.send_message_to(random_variable, prop_range - 1)


def discrete(table, *condition, out=None, name=None):
    """
    discrete probability function
    """
    function = DiscreteProbability(table, *condition, out=out, name=name)
    if len(function.out) == 1:
        return function.out[0]
    else:
        return function.out