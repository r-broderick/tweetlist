# tweetlist

This is a Python module used to conveniently make repeated search requests to the Twitter API, aggregate the results in a pandas DataFrame, then use those results for analysis, drawing maps, or natural language ML training.

## Setup

### Dependencies

1) pandas
2) numpy
3) scipy
4) requests_oauthlib
5) sklearn
6) tensorflow
7) keras
8) matplotlib
9) plotly

### Installation

Install tweetlist by entering the following at the command line:
```
$ pip install git+https://github.com/r-broderick/tweetlist
```

## Features

The most import elements of the module are the following. See the docstring for each one for further information.

search_attempt: Send a single search request to the Twitter API, return a pandas DataFrame
repeated_search_loops: Send many requests over a specified number of hours, aggregating all in a pandas DataFrame
extract_tweets: Build a pandas DataFrame from a response object from a Twitter search
process_df: Infer local time, city, and/or state when possible and adds this information to the DataFrame
TweetList: A class for storing tweets on a given subject, drawing maps based on them, and training ML algorithms with them.

## Code example

Below is an example of using this module. First, we perform repeated requests to the Twitter API to find recent tweets about bagels.
Then we define a couple masking functions, corresponding to tweets from New York and tweets from any other known location. Then we build a TweetList object using two json files for dataframes containing tweets about bagels. We draw a state map to see which states produce a lot of tweets about bagels relative to their populations, then train the two default classification models on the two groups we defined and check the ROC for an ensemble of the resulting classifiers to see if we can accurately predict which tweets about bagels are written by New Yorkers. To see further examples and the output maps, open the demo notebook at https://github.com/r-broderick/tweetlist/blob/master/tweetlist_demo.ipynb. (Note that the maps are dynamic output, so they won't appear unless the notebook is viewed using nbviewer. An icon at the top right of the document will provide a link to this view.)

```python
import tweetlist as tl
tl.repeated_search_loops(tokens, 'bagels', 18, output_file = '~/bagels/bagel_tweets_6_1', process = True)    
not_ny_mask = lambda df : df.apply(lambda x : (x.city not in ['new york', None]) 
	or (x.state not in ['new york', None]), axis = 1)
ny_mask = lambda df : df.apply(lambda x : x.city == 'new york', axis = 1)
bagels_tl = tl.TweetList('~/bagels/bagel_search_results_6_1', 
	masks_for_groups = [ny_mask, not_ny_mask],
	cat_names = ['new york', 'not new york'])
bagels_tl.append('~/bagels/bagel_search_results_5_29')
tl.draw_state_map(filename = 'bagels_map.html')
tl.train_nn()
tl.train_nb()
tl.plot_roc(model = 'ens')
```

## Errors, bugs, and feature requests

If you would like to report a bug, suggest an improvement, or request a feature, please create an issue on the project's GitHub page: https://github.com/r-broderick/tweetlist/issues.

## Patches and pull requests

If you would like to make a contribution, please fork the project on GitHub, make your changes, then send a pull request with a detailed description of your work.

## Copyright and attribution

Copyright (c) 2018 Ryan Broderick. Released under the [MIT License](https://github.com/r-broderick/tweetlist/blob/master/LICENSE).
