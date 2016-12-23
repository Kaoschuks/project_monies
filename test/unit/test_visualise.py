import os
import filecmp
import unittest

import datetime

import monies.monies.visualise as vis


def disabled(f):
    def _decorator():
        print(f.__name__ + ' has been disabled')
    return _decorator


class TestUnit(unittest.TestCase):

    def testQuery(self):

        inp = \
        {
            0: ["DATE", "BALANCE", "AMOUNT", "DESCRIPTION"],
            1: ["29/12/2012",
                "3472.63",
                "-10.45",
                "CARD PAYMENT TO WWW.JUST EAT.CO.UK,10.45 GBP, "
                "RATE 1.00/GBP ON 26-12-2012"],
            2: ["28/12/2012",
                "3483.08",
                "-10.00",
                "CARD PAYMENT TO WWW.JUST EAT.CO.UK,10.45 GBP, "
                "RATE 1.00/GBP ON 26-12-2012"],
            3: ["28/12/2011",
                "1344.08",
                "23.00",
                "CARD PAYMENT TO WWW.UCAS.COM,23.00 GBP, RATE 1.00/GBP ON "]
        }

        out = \
        {
            0: ["DATE", "BALANCE", "AMOUNT", "DESCRIPTION"],
            1: ["29/12/2012",
                "3472.63",
                "-10.45",
                "CARD PAYMENT TO WWW.JUST EAT.CO.UK,10.45 GBP, "
                "RATE 1.00/GBP ON 26-12-2012"],
            2: ["28/12/2012",
                "3483.08",
                "-10.00",
                "CARD PAYMENT TO WWW.JUST EAT.CO.UK,10.45 GBP, "
                "RATE 1.00/GBP ON 26-12-2012"],
        }

        self.assertDictEqual(vis.query(inp, "JUST EAT"), out)

    def testPreparePlotData(self):

        inp = \
        {
            0: ["DATE", "BALANCE", "AMOUNT", "DESCRIPTION"],
            1: ["29/12/2012",
                "3472.63",
                "-10.45",
                "CARD PAYMENT TO WWW.JUST EAT.CO.UK,10.45 GBP, "
                "RATE 1.00/GBP ON 26-12-2012"],
            2: ["28/12/2012",
                "3483.08",
                "-10.00",
                "CARD PAYMENT TO WWW.JUST EAT.CO.UK,10.45 GBP, "
                "RATE 1.00/GBP ON 26-12-2012"],
        }

        out = ([datetime.datetime(2012, 12, 29, 0, 0),
                datetime.datetime(2012, 12, 28, 0, 0)],
               [-10.45,
                -10.00])

        self.assertTupleEqual(vis.preparePlotData(inp), out)



class TestIntegration(unittest.TestCase):

    def testWriteData(self):
        data = \
        {
            0: ["DATE", "BALANCE", "AMOUNT", "DESCRIPTION"],
            1: ["29/12/2012",
                "3472.63",
                "-10.45",
                "CARD PAYMENT TO WWW.JUST EAT.CO.UK,10.45 GBP, "
                "RATE 1.00/GBP ON 26-12-2012"],
            2: ["28/12/2012",
                "3483.08",
                "-10.00",
                "CARD PAYMENT TO WWW.JUST EAT.CO.UK,10.45 GBP, "
                "RATE 1.00/GBP ON 26-12-2012"]
        }

        oPath = os.path.join("..", "res", "san_output.txt")
        ePath = os.path.join("..", "res", "san_expected.txt")

        vis.writeData(data, oPath)
        self.assertTrue(filecmp.cmp(oPath, ePath))


