import numpy as np
import openmdao.api as om
from bokeh.models import inputs


def f1p2(x1, x2):
    y = x1**3 + 2 * x1 * x2**2 - x2**3 - 20 * x1
    return y


def g1(x1, x2):
    y = x1**2 + x2**2
    return y


class f1p4(om.ExplicitComponent):

    def setup(self):

        #global design variables
        self.add_input("x", val=np.ones(2))

        #output setup
        self.add_output("y", val=1.0)

    def setup_partials(self):

        # finite difference all partials
        self.declare_partials("*", "*", method="fd")

    def compute(self, inputs, outputs):

        # evaluate example 1.4 function
        x1 = inputs["x"][0]
        x2 = inputs["x"][1]

        outputs["y"] = (1 - x1) ** 2 + (1 - x2) ** 2 + 0.5 * (2 * x2 - x1**2) ** 2
