#!/usr/bin/env ruby

# This code doesn't yet do anything.

require 'rspec'

class BayesTheorem

  attr_accessor :prior, :posterior, :evidence, :likelihood

  def initialize(*options)
    @prior      == Float::NAN
    @posterior  == Float::NAN
    @likelihood == Float::NAN
    @evidence   == Float::NAN
  end

  def prior=(p)
    @prior = p
    return if @posterior == Float::NAN
    return if @likelihood == Float::NAN
    return if @evidence == Float::NAN
    # else recompute bayes
  end

end

bt = BayesTheorem.new
