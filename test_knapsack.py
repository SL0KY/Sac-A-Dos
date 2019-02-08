import os
import time
import csv 
from knapsack import *
from generate_input import *


def check_and_print_result(t0, file_in, file_out, size_bag, bag_value, bag_used_weight, my_bag_count):
    #  print
    print('-- result, my bag     value[{}] weight[{}] nb[{}]'.format(bag_value, bag_used_weight, my_bag_count))
    t1 = time.time()
    print('-- time : ', t1 - t0)

    #  check
    assert os.path.exists(file_out)

    # TODO read file and check what's inside the student file

def test_greedy_small_knapsack():
    print('\ntest_greedy_small_knapsack -- big capacity')
    filepath_in = 'petit_sac.csv'
    filepath_out = 'petit_sac_output.csv'
    size_bag = 100

    t0 = time.time()
    bag_value, bag_used_weight, my_bag_count = greedy(filepath_in, filepath_out, size_bag)

    check_and_print_result(t0, filepath_in, filepath_out, size_bag, bag_value, bag_used_weight, my_bag_count)
    assert my_bag_count is 15

    print('test_greedy_small_knapsack -- avg capacity')
    t0 = time.time()
    size_bag = 30
    bag_value, bag_used_weight, my_bag_count = greedy(filepath_in, filepath_out, size_bag)

    check_and_print_result(t0, filepath_in, filepath_out, size_bag, bag_value, bag_used_weight, my_bag_count)
    assert my_bag_count < 15
    assert int(bag_value) is 42
    assert int(bag_used_weight) is 30
    assert my_bag_count is 11

    print('test_greedy_small_knapsack -- impossible capacity')
    t0 = time.time()
    size_bag = 0
    bag_value, bag_used_weight, my_bag_count = greedy(filepath_in, filepath_out, size_bag)

    check_and_print_result(t0, filepath_in, filepath_out, size_bag, bag_value, bag_used_weight, my_bag_count)
    assert bag_value + bag_used_weight + my_bag_count is 0


def test_greedy_generated_bag():
    print('\ntest_greedy_generated_bag :')
    filepath_in = 'generated_bag.csv'
    filepath_out = 'generated_bag_output.csv'
    size_bag = 100
    generate_input(filepath_in, 150, 20, 100)

    t0 = time.time()
    bag_value, bag_used_weight, my_bag_count = greedy(filepath_in, filepath_out, size_bag)

    check_and_print_result(t0, filepath_in, filepath_out, size_bag, bag_value, bag_used_weight, my_bag_count)
    assert my_bag_count is not 0


def test_greedy_generated_super_big_bag():
    print('\ntest_greedy_generated_super_big_bag :')
    filepath_in = 'generated_bag.csv'
    filepath_out = 'generated_bag_output.csv'
    size_bag = 100
    # TODO for student : just add some 0 here to generated a mega file !!!
    generate_input(filepath_in, 20000, 20, 100)

    t0 = time.time()
    bag_value, bag_used_weight, my_bag_count = greedy(filepath_in, filepath_out, size_bag)

    check_and_print_result(t0, filepath_in, filepath_out, size_bag, bag_value, bag_used_weight, my_bag_count)
    assert my_bag_count is not 0

test_greedy_small_knapsack()
