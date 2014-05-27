#!/usr/bin/env ruby

require 'csv'
require 'rspec'

class BayesBuy

  attr_accessor :buydata, :students, :incomes, :credit, :ages

  def initialize(filename)
    @buydata = CSV::table(filename)
    @buys  = 0
    @nobuys = 0
    @buydata[:buy].each do |p|
      if p == "yes"
        @buys += 1
      else
        @nobuys += 1
      end
    end
    compute_student
    compute_income
    compute_credit
    compute_age
  end

  def compute_student
    @students = []
    @buydata.each do |b|
      if b[:student] == 'yes'
        @students << b[:buy]
      end
    end
    print @students, "\n"
  end

  def compute_age
    @ages = []
    @buydata.each do |b|
      ages << [ b[:age], b[:buy] ]
    end
    print @ages, "\n"
  end

  def compute_income
    @incomes = []
    @buydata.each do |b|
      incomes << [ b[:income], b[:buy] ]
    end
    print @incomes, "\n"
  end

  def compute_credit
    @credit = []
    @buydata.each do |b|
      @credit << [ b[:credit], b[:buy] ]
    end
    print @credit, "\n"
  end

  def print_stats

    print "buys: ", @buys, "\n"
    print "nobuys: ", @nobuys, "\n"
    total = @buys + @nobuys
    print "total: ", total, "\n"

    p_buy = @buys/total
    print "p_buy: ", p_buy, "\n"
    p_buy = Float(@buys/total)
    print "p_buy: ", p_buy, "\n"
    p_buy = @buys/total.to_f
    print "p_buy: ", p_buy, "\n"

    p_nobuy = @nobuys/total.to_f
    print "p_nobuy: ", p_nobuy, "\n"

    print "total p: ", p_buy + p_nobuy, "\n"
  end

  # boundary, adding elements to the training set
  # These methods need to have argument checking
  #def add_buyer
  #def add_nonbuyer
  # If private, no need for argument checking
  #def add_record # should be private and called from add_buyer and add_nonbuyer?

end

b = BayesBuy.new('buy.csv')
b.print_stats

describe BayesBuy do

  before(:all) do
    @b = BayesBuy.new('buy.csv')
  end

  xit "computes probabilities for buy classification" do
  end

  it "reads all the records from the example data" do
    @b.buydata.size.should == 14
  end

  it "counts the students" do
    @b.students.size.should         == 7
    @b.students.count('yes').should == 6
    @b.students.count('no').should  == 1
  end

  it "counts the incomes" do
    @b.incomes.size.should                    == 14
    @b.incomes.count(['low','yes']).should    == 3
    @b.incomes.count(['medium','yes']).should == 4
    @b.incomes.count(['high','yes']).should   == 2
    @b.incomes.count(['low','no']).should     == 1
    @b.incomes.count(['medium','no']).should  == 2
    @b.incomes.count(['high','no']).should    == 2
  end

  it "counts the age" do
    @b.ages.size.should                         == 14
    @b.ages.count(['youth','yes']).should       == 2
    @b.ages.count(['middle-aged','yes']).should == 4
    @b.ages.count(['senior','yes']).should      == 3
    @b.ages.count(['youth','no']).should        == 3
    @b.ages.count(['middle-aged','no']).should  == 0
    @b.ages.count(['senior','no']).should       == 2
  end


  it "counts the credit" do
    @b.credit.size.should                       == 14
    @b.credit.count(['fair','yes']).should      == 6
    @b.credit.count(['excellent','yes']).should == 3
    @b.credit.count(['fair','no']).should       == 2
    @b.credit.count(['excellent','no']).should  == 3
  end

  it "updates the counts when a new record is added"
  it "rejects records which are incorrect" # probably should be a describe block here.

end
