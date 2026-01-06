
import numpy as np
from utilities import svd_inv

from cobaya.likelihood import Likelihood
from cobaya.theory import Theory




class ErrorLikelihood(Likelihood):
    data = None
    eps = 1e-3

    def initialize(self):
        self.data = np.asarray(self.data)

    def get_requirements(self):
        return {'model': None}

    def logp(self, **params):
        model = self.provider.get_model()

        if not np.all(np.isfinite(model)):
            return -np.inf
        


        sigma = 0.2 * np.maximum(np.abs(self.data), self.eps)
        chi2 = np.sum((self.data - model)**2 / sigma**2)

        return -chi2
    


class FlareTheory(Theory):
    tvals = None # expect 1-d array of same size as data input to likelihood
    #########################################
    def initialize(self):
        self.tvals = np.asarray(self.tvals)


    #########################################

    #########################################
    def calculate(self, state,want_derived=False, **params):
        A = params["A"]
        tau = params["tau"]
        omega = params["omega"]
        C = params["C"]

        S = (
            A
            * np.exp(self.tvals)
            * (1 - np.tanh(2 * (self.tvals - tau)))
            * np.sin(omega * self.tvals)
        ) + C

        if not np.all(np.isfinite(S)):
            state["model"] = np.full_like(self.tvals, np.nan)
        else:
            state["model"] = S

    def get_model(self):
        return self.current_state["model"]

    def get_allow_agnostic(self):
        return True
    #########################################