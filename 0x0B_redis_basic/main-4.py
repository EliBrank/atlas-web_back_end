#!/usr/bin/env python3
""" Main file """

import exercise

cache = exercise.Cache()

cache.store("foo")
cache.store("bar")
cache.store(42)

exercise.replay(cache.store)
