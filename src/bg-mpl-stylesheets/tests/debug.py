#!/usr/bin/env python
##############################################################################
#
# (c) 2024 The Trustees of Columbia University in the City of New York.
# All rights reserved.
#
# File coded by: Billinge Group members and community contributors.
#
# See GitHub contributions for a more detailed list of contributors.
# https://github.com/Billingegroup/bg-mpl-stylesheets/graphs/contributors
#
# See LICENSE.rst for license information.
#
##############################################################################

"""
Convenience module for debugging the unit tests using

python -m bg-mpl-stylesheets.tests.debug

Exceptions raised by failed tests or other errors are not caught.
"""


if __name__ == "__main__":
    import sys

    from bg-mpl-stylesheets.tests import testsuite

    pattern = sys.argv[1] if len(sys.argv) > 1 else ""
    suite = testsuite(pattern)
    suite.debug()


# End of file