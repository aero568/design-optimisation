import openmdao.api as om

class g1(om.ExplicitComponent):

    def setup(self):

        # global design variables
        self.add_input("x1", val=0.0)
        self.add_input("x2", val=0.0)

        # output setup
        self.add_output("g1", val=0.0)

    def setup_partials(self):

        # finite difference all partials
        self.declare_partials("*", "*", method="fd")

    def compute(self, inputs, outputs):

        # evaluate example 1.4 function
        x1 = inputs["x1"]
        x2 = inputs["x2"]

        outputs["g1"] = x1**2 + x2**2


class g2(om.ExplicitComponent):

    def setup(self):

        # global design variables
        self.add_input("x1", val=0.0)
        self.add_input("x2", val=0.0)

        # output setup
        self.add_output("g2", val=0.0)

    def setup_partials(self):

        # finite difference all partials
        self.declare_partials("*", "*", method="fd")

    def compute(self, inputs, outputs):

        # evaluate example 1.4 function
        x1 = inputs["x1"]
        x2 = inputs["x2"]

        outputs["g2"] = x1 - 3 * x2 + 0.5


class f1p4(om.ExplicitComponent):

    def setup(self):

        # global design variables
        self.add_input("x1", val=0.0)
        self.add_input("x2", val=0.0)

        # output setup
        self.add_output("y", val=1.0)

    def setup_partials(self):

        # finite difference all partials
        self.declare_partials("*", "*", method="fd")

    def compute(self, inputs, outputs):

        # evaluate example 1.4 function
        x1 = inputs["x1"]
        x2 = inputs["x2"]

        outputs["y"] = (1 - x1) ** 2 + (1 - x2) ** 2 + 0.5 * (2 * x2 - x1**2) ** 2
