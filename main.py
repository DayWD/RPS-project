import generators as gen
import tests
import histograms

"""Linear congruential generator"""
# print(gen.G(100))
histograms.G(200000)

"""Generator J for the range from 0 to 1, but we can choose [a,b] interval"""
# print(gen.J(0, 1, 100))
# print(gen.J(4, 13, 100))
histograms.J(0, 1, 200000)

"""Coin Toss Distribution. We receive only 0 and 1 with p chance."""
# print(gen.B(0.5, 100))
# print(gen.B(0.2, 100))
histograms.B(0.5, 10000)
histograms.B(0.2, 10000)

"""Binomial Distribution"""
histograms.D(0.5, 10000)

"""Poisson Distribution"""
histograms.P(1000)

"""Exponential Distribution"""
histograms.W(10000)

"""Normal Distribution"""
histograms.N(1000)

"""Run Test"""
tests.runs_test(1000)
