from collections import Counter
from itertools import product, chain

import pandas as pd
from IPython.display import display

pd.set_option('display.max_columns', None)

a_max = 50_000
v_max = 5_000

from functools import cache

distances = [0, 10, 20, 40, 45, 50, 100, 200, 249, 250, 251, 300, 400, 450, 499, 500, 501, 1000, 2000, 5000]
velocities = [0, 1, 50] + list(range(250, v_max, 250)) + [v_max - 1, v_max]


@cache
def limits():
    """Return a list of (x,v_0, v_1) tuples for use in testing. """

    return list(enumerate(product(distances, velocities, velocities)))


def report(sl):
    from IPython.display import HTML

    h = (f"""
    <table>
    <tr>
        <td><b>N Discont</b></td>  <td>{len(list(sl.discontinuities()))}</td>
        <td><b>N Replans</b></td>  <td>{sum([b.replans for b in sl.blocks])}</td>
        <td><b>Errors</b></td>     <td>{Counter(chain(*[b.errors for b in sl.blocks])).most_common(10)}</td>
    </tr>
    <tr>
        <td><b>Reductions</b></td> <td>{Counter(chain(*[b.reductions for b in sl.blocks])).most_common(10)}</td>
        <td><b>Replans</b></td>    <td>{Counter(sl.replans).most_common(10)}</td>
        <td><b>Time Err</b></td>     <td>{sum([s.times_e_rms for s in sl]):2.4f}</td>
    </tr>

    </table>""")

    display(HTML(h))
