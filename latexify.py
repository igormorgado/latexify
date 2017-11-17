#!/usr/bin/env python

from collections.abc import Sequence
from IPython.display import Latex


def matrix(M, type='matrix'):
    """Return the latex representation of matrix"""
    lines = str(M).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{' + type + r'}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv += [r'\end{' + type + r'}']
    return '\n'.join(rv)


def bmatrix(M):
    """Return the latex representation of bmatrix"""
    return matrix(M, type='bmatrix')    


def pmatrix(M):
    """Return the latex representation of bmatrix"""
    return matrix(M, type='pmatrix')    


def vector(v, separator, type='matrix'):
    elements = str(v).replace('[', '').replace(']', '').split()
    rv = [r'\begin{' + type + r'}']
    rv += [ (' '+separator+' ').join(elements) ]
    rv += [r'\end{' + type + r'}']
    return ' '.join(rv)
    

def colvector(v, type='pmatrix'):
    """Return the latex representation of column vector"""
    return vector(v, separator=r'\\', type=type)
    

def rowvector(v, type='pmatrix'):
    """Return the latex representation of row vector"""
    return vector(v, separator=r'&', type=type)


def Lprint(latexinput, block='$$'):
    """Return a string with full latex surrounded by block"""

    if isinstance(latexinput, Sequence):
        latexstr = ''.join(map(str,latexinput))
    elif isinstance(latexinput, six.string_types):
        latexstr = latexinput
    else:
        latexstr = str(latexinput)

    # Surround with correct latex scope
    if block == '$$' or block == '$':
        begin = block
        end = block
    elif block == r'\[':
        begin = block
        end = r'\]'
    else:
        begin = r'\begin{' + block + r'}'
        end = r'\end{' + block + r'}'

    return Latex(begin + latexstr + end)
