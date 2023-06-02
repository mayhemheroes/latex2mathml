#!/usr/bin/env python3
import atheris
import sys
import fuzz_helpers
from latex2mathml.exceptions import NoAvailableTokensError, MissingEndError, NumeratorNotFoundError, \
    DenominatorNotFoundError, DoubleSubscriptsError, InvalidStyleForGenfracError, InvalidAlignmentError, \
    InvalidWidthError, LimitsMustFollowMathOperatorError, MissingSuperScriptOrSubscriptError, \
    ExtraLeftOrMissingRightError

with atheris.instrument_imports():
    import latex2mathml.converter

def TestOneInput(data):
    #fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        latex2mathml.converter.convert(str(data, 'utf-8'))
    except (NoAvailableTokensError, MissingEndError, NumeratorNotFoundError, DenominatorNotFoundError, ExtraLeftOrMissingRightError,
            MissingSuperScriptOrSubscriptError, DoubleSubscriptsError, InvalidStyleForGenfracError, InvalidAlignmentError, InvalidWidthError,
            LimitsMustFollowMathOperatorError):
        return -1
    except (Exception):
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
