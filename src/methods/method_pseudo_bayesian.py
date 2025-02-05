from mcsm_benchs.benchmark_utils import MethodTemplate
from mcsm_benchs.MatlabInterface import MatlabInterface
import os
import numpy as np
# import sys
# sys.path.append("methods")
# You must import the MethodTemplate abstract class and the MatlabInterface class.

# Create an interface with the matlab engine by passing the name of the function file 
# (without the .m extension). Then get the matlab function as:

# Paths to additional code for the method to add to Matlab path variable.

# paths = [   os.path.join('src','methods','pseudobay_method_utils'),
#             os.path.join('..','src','methods','pseudobay_method_utils')
#         ]

paths = [   os.path.join('src','methods','PB_method_utils'),
            os.path.join('..','src','methods','PB_method_utils')
        ]


mlint = MatlabInterface('pb_method', add2path=paths) 
matlab_function = mlint.matlab_function # A python function handler to the method.

class NewMethod(MethodTemplate):

    def __init__(self):
        self.id = 'pseudo_bayesian_method'
        self.task = 'denoising'
        

    def method(self, signal, nc=[], *params):
        """_summary_

        Args:
            signals (_type_): _description_
            params (_type_): _description_

        Returns:
            _type_: _description_
        """
        if nc == []:
            nc = signal.total_comps
            # nc = 10
        # xr = pb_method(x, Ncomp, use_sst, ds, beta, alpha, div, Pnei, PneiMask)
        signal_output = matlab_function(signal, nc, *params) # Only positional args.
        return signal_output

  # pb_method(x, Ncomp, use_sst, ds, beta, alpha, div, Pnei, PneiMask, M, L,return_comps, return_instf)
    def get_parameters(self):                       
        return (
            ([], [], [], 0.4, 0.4, [], [], [], [], []), # 
            ([], [], [], 0.4, 0.2, [], [], [], [], []), # 
            )    
    