# lambdadata

WHAT IS IT?
Lambdata is a repository of helper functions meant to make data science tasks easier. It is primarily a pedagogical exercise, with limited actual usefulness.

FUNCTIONS
All functions are found in the helper_functions.py file.

null_count(df) - this function takes a dataframe, and returns the number of null values in it, as a single integer.

train_test_split(df, frac) - this function takes a dataframe and a fraction, and returns a split of the data into a training and a test set, with frac being the amount of the data to include in the training set. It is essentially a wrapper of scikit-learn's train_test_split function, which checks that frac is in [0, 1], and restricts the user to default values for all other parameters.

Abbreviations.abbr_2_st(state_series, abbr_2_st=True) - this method maps a series of state abbreviations to a series of state names, or vice versa if the second argument is False. It does not currently include DC or any of the territories, this may be changed in the future.

DEPENDENCIES
Lambdata uses numpy, pandas, ans scikit-learn. All must be installed.

TESTING
There is a helper_functions_tester.py file, which contains a unit test of the null_count function, and may in the future be expanded to test other functions.

LICENSE
This code is released under the MIT license, see LICENSE file for details.

CONTRIBUTORS
This code is written by River Bellamy.
