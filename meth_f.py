import numpy as np

#Confirm how many donors have both methylation and RNA data
#==============================================================================
def print_count(curr_meth, curr_rna):
#==============================================================================
    """
    This function prints the number of donors with both methylation and RNA data.
    Inputs:
        curr_meth: dataframe of methylation data
        curr_rna: dataframe of RNA data

    """

    curr_meth = curr_meth['Sample ID']
    curr_rna = curr_rna.columns
    print('Total donors with methylation data: {}'.format(len(curr_meth)))
    print('Total donors with RNA data: {}'.format(len(curr_rna)))
    print('Total donors with both methylation and RNA data: {}'.format(len(np.intersect1d(curr_meth, curr_rna))))