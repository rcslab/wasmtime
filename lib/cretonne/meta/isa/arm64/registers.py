"""
Aarch64 register banks.
"""
from __future__ import absolute_import
from cdsl.registers import RegBank, RegClass
from .defs import ISA


# The `x31` regunit serves as the stack pointer / zero register depending on
# context. We reserve it and don't model the difference.
IntRegs = RegBank(
        'IntRegs', ISA,
        'General purpose registers',
        units=32, prefix='x')

FloatRegs = RegBank(
        'FloatRegs', ISA,
        'Floating point registers',
        units=32, prefix='v')

GPR = RegClass(IntRegs)
FPR = RegClass(FloatRegs)

RegClass.extract_names(globals())
