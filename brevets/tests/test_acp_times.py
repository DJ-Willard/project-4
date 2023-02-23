"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def 

def test_brevet_200km():
        brevet_dist = 200
        brevet_start_time = arrow.get('2023-01-01T00:00:00', 'YYYY-MM-DD HH:mm')
        checkpoints = {
                0: (brevet_start_time, brevet_start_time.shift(hours=1)),
               50: (brevet_start_time.shift(hours=1, minutes=28), brevet_start_time.shift(hours=3, minutes=30)),
              100: (brevet_start_time.shift(hours=2, minutes=56), brevet_start_time.shift(hours=6, minutes=40)),
              150: (brevet_start_time.shift(hours=4, minutes=25), brevet_start_time.shift(hours=10, minutes=00)),
              200: (brevet_start_time.shift(hours=5, minutes=53), brevet_start_time.shift(hours=13, minutes=30)),
                      }

        for km, times in checkpoints.items():
            start_time, end_time = times
            assert open_time(km, brevet_dist, brevet_start_time) == start_time
            assert close_time(km, brevet_dist, brevet_start_time) == end_time

def test_brevet_300km():
        brevet_dist = 300
        brevet_start_time = arrow.get('2023-01-01T00:00:00', 'YYYY-MM-DD HH:mm')
        checkpoints = {
                0: (brevet_start_time, brevet_start_time.shift(hours=1)),
              100: (brevet_start_time.shift(hours=2, minutes=56), brevet_start_time.shift(hours=6, minutes=40)),
              150: (brevet_start_time.shift(hours=4, minutes=25), brevet_start_time.shift(hours=10, minutes=00)),
              200: (brevet_start_time.shift(hours=5, minutes=53), brevet_start_time.shift(hours=13, minutes=20)),
              300: (brevet_start_time.shift(hours=9, minutes=00), brevet_start_time.shift(hours=20, minutes=00)),
                      }

        for km, times in checkpoints.items():
            start_time, end_time = times
            assert open_time(km, brevet_dist, brevet_start_time) == start_time
            assert close_time(km, brevet_dist, brevet_start_time) == end_time


def test_brevet_400km():
        brevet_dist = 400
        brevet_start_time = arrow.get('2023-01-01T00:00:00', 'YYYY-MM-DD HH:mm')
        checkpoints = {
                0: (brevet_start_time, brevet_start_time.shift(hours=1)),
              100: (brevet_start_time.shift(hours=2, minutes=56), brevet_start_time.shift(hours=6, minutes=40)),
              200: (brevet_start_time.shift(hours=5, minutes=53), brevet_start_time.shift(hours=13, minutes=20)),
              300: (brevet_start_time.shift(hours=9, minutes=00), brevet_start_time.shift(hours=20, minutes=00)),
              400: (brevet_start_time.shift(hours=12, minutes=8), brevet_start_time.shift(hours=27, minutes=00)),
                      }

        for km, times in checkpoints.items():
            start_time, end_time = times
            assert open_time(km, brevet_dist, brevet_start_time) == start_time
            assert close_time(km, brevet_dist, brevet_start_time) == end_time


def test_brevet_600km():
        brevet_dist = 600
        brevet_start_time = arrow.get('2023-01-01T00:00:00', 'YYYY-MM-DD HH:mm')
        checkpoints = {
                0: (brevet_start_time, brevet_start_time.shift(hours=1)),
              100: (brevet_start_time.shift(hours=2, minutes=56), brevet_start_time.shift(hours=6, minutes=40), 
              200: (brevet_start_time.shift(hours=5, minutes=53), brevet_start_time.shift(hours=13, minutes=20)),
              300: (brevet_start_time.shift(hours=9, minutes=00), brevet_start_time.shift(hours=20, minutes=00)),
              400: (brevet_start_time.shift(hours=12, minutes=8), brevet_start_time.shift(hours=26, minutes=40)),
              500: (brevet_start_time.shift(hours=15, minutes=28), brevet_start_time.shift(hours=33, minutes=20),
              600: (brevet_start_time.shift(hours=18, minutes=48), brevet_start_time.shift(hours=40, minutes=00)),
                      }

        for km, times in checkpoints.items():
            start_time, end_time = times
            assert open_time(km, brevet_dist, brevet_start_time) == start_time
            assert close_time(km, brevet_dist, brevet_start_time) == end_time


def test_brevet_1000km():
        brevet_dist = 1000
        brevet_start_time = arrow.get('2023-01-01T00:00:00', 'YYYY-MM-DD HH:mm')
        checkpoints = {
                0: (brevet_start_time, brevet_start_time.shift(hours=1)),
              100: (brevet_start_time.shift(hours=2, minutes=56), brevet_start_time.shift(hours=6, minutes=40)),
              200: (brevet_start_time.shift(hours=5, minutes=53), brevet_start_time.shift(hours=13, minutes=20)),
              300: (brevet_start_time.shift(hours=9, minutes=00), brevet_start_time.shift(hours=20, minutes=00)),
              400: (brevet_start_time.shift(hours=12, minutes=8), brevet_start_time.shift(hours=26, minutes=40)),
              500: (brevet_start_time.shift(hours=15, minutes=28), brevet_start_time.shift(hours=33, minutes=20)),
              600: (brevet_start_time.shift(hours=18, minutes=48), brevet_start_time.shift(hours=40, minutes=00)),
              900: (brevet_start_time.shift(hours=29, minutes=31), brevet_start_time.shift(hours=66, minutes=15)),
             1000: (brevet_start_time.shift(hours=33, minutes=5), brevet_start_time.shift(hours=75, minutes=00)),
                      }

        for km, times in checkpoints.items():
            start_time, end_time = times
            assert open_time(km, brevet_dist, brevet_start_time) == start_time
            assert close_time(km, brevet_dist, brevet_start_time) == end_time

