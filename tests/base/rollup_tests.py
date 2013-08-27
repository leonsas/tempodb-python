#!/usr/bin/env python
# encoding: utf-8

from unittest2 import TestCase

from tempodb import Rollup


class RollupTest(TestCase):

    def test_init(self):
        rollup = Rollup(interval="PT6H", function="avg", tz="UTC")
        self.assertEqual(rollup.interval, "PT6H")
        self.assertEqual(rollup.function, "avg")
        self.assertEqual(rollup.tz, "UTC")

    def test_from_json(self):
        json = {
                "interval":"PT6H",
                "function":"avg",
                "tz":"UTC"
                }
        rollup = Rollup.from_json(json)
        expected = Rollup(interval="PT6H", function="avg", tz="UTC")
        self.assertEqual(rollup, expected)