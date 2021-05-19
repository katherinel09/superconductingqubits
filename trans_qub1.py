import numpy as np
import scqubits as scq

transmon = scq.Transmon(
    EJ=30.0,
    EC=1.2,
    ng=0.3,
    ncut=31
)

tmon = scq.Transmon.create()

transmon.eigenvals(evals_count=12)

ng_list = np.linspace(-2, 2, 220)
transmon.plot_evals_vs_paramvals('ng', ng_list, evals_count=5, subtract_ground=False);

evals, evecs = transmon.eigensys()

EJvals = np.linspace(0.1, 35, 100)
tmon.plot_dispersion_vs_paramvals('ng', 'EJ', EJvals, ref_param='EC', levels=(0,1,2));