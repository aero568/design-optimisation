import matplotlib.pyplot as plt
import numpy as np
import openmdao.api as om
from omxdsm import write_xdsm

from functions import f1p4 as f
from functions import g1, g2
from plotfun import set_plot

# build the model
prob = om.Problem()
prob.model.add_subsystem("function", f(), promotes=["*"])
prob.model.add_subsystem("constraint_1", g1(), promotes=["*"])
prob.model.add_subsystem("constraint_2", g2(), promotes=["*"])

# setup the optimization
prob.driver = om.ScipyOptimizeDriver()
prob.driver.options["optimizer"] = "SLSQP"
prob.model.add_design_var("x1", lower=0)
prob.model.add_design_var("x2", lower=0)
prob.model.add_constraint("g1", upper=1.0)
prob.model.add_constraint("g2", lower=0.0)
prob.model.add_objective("y")
prob.setup()

# run the optimization
prob.run_driver()

# minimum value
print(prob.get_val("function.y"))

# location of the minimum
x1_opt = prob.get_val("x1")
x2_opt = prob.get_val("x2")
print(x1_opt)
print(x2_opt)

# plot location of the minimum over contour
set_plot(f,g1,g2)
plt.plot(x1_opt, x2_opt, "bo")
#plt.show()
plt.savefig('two-dimensional.pdf')

# xsdm diagram
write_xdsm(
    prob,
    filename="two-dimensional-xdsm",
    out_format="pdf",
    show_browser=False,
    quiet=True,
    output_side="left",
    include_indepvarcomps=False,
    class_names=False,
    numbered_comps=False,
)
