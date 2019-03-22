from datastore import json_datastore

if __name__ == "__main__":

    x = [
        'great', 'buy', 'ill', 'wait', 'jefferies', 'maintains', 'rating',
        'hold', 'setting', 'target', 'price', 'usd', 'verdict', 'buy', 'heard',
        'guy', 'know', 'someone', 'think', 'somebody', 'know', 'something',
        'stocktwits', 'reveal', 'drop', 'warren', 'buffet', 'taking',
        'position', 'bear', 'reason', 'pay', 'attention', 'ok', 'good',
        'dropping', 'price', 'weekend', 'lol', 'daily', 'chart', 'need', 'get',
        'back', 'drop', 'per', 'week', 'spike', 'news', 'month', 'back', 'bo',
        'bingo', 'odds'
    ]
    y = [
        'amp', 'utm_campaign', 'social_tracking', 'mnk', 'key', 'c', 'adc',
        'cbe', 'b', 'f', 'fb', 'today', 'insight', 'five', 'year', 'baba',
        'apple', 'next', 'week', 'ahhhhhhhhhhhhhhhhhhhhh', 'short', 'sale',
        'volume', 'short', 'interest', 'via', 'raytheon', 'valuation',
        'profitability', 'dividend', 'safety', 'score', 'analysis', 'trending',
        'get', 'riiiiiiiiiich', 'sooooon', 'buuuuls', 'looooove', 'fucking',
        'drunk', 'get', 'going', 'make', 'new', 'low', 'pay', 'dividend',
        'gapping', 'monday', 'short', 'ratio', 'short', 'float', 'via',
        'jefferies', 'maintains', 'rating', 'hold', 'setting', 'target',
        'price', 'usd', 'verdict', 'buy', 'warbey', 'parker', 'b', 'prep',
        'apple', 'glass', 'seen', 'watch', 'apple', 'focus', 'fashion', 'tech',
        'wrt', 'wearable', 'look', 'like', 'sbux', 'paying', 'full', 'sex',
        'change', 'employee', 'hit', 'bottom', 'line', 'weekly', 'recap',
        'price', 'moved', 'since', 'post', 'expect', 'run', 'trade',
        'included', 'hsy', 'uri', 'sonc', 'dri', 'kmx', 'wynn', 'akam', 'b',
        'enterprise', 'value', 'v', 'b', 'market', 'cap', 'b', 'difference',
        'actual', 'asset', 'v', 'market', 'value', 'big', 'spread', 'way',
        'undervalued', 'million', 'share', 'added', 'june', 'dont', 'wait',
        'think', 'amazon', 'become', 'monopoly', 'dipping', 'everything',
        'amazon', 'airline', 'possibility', 'miss', 'breakout', 'buy', 'stop',
        'stop', 'loss', 'suggested', 'chartmill', 'analyzer', 'utm_medium',
        'ta', 'amp', 'utm_content', 'tradingsetup', 'amp', 'utm_campaign',
        'social_tracking', 'amd', 'key', 'eb', 'b', 'efcd', 'ba', 'de', 'f',
        'short', 'sale'
    ]
    data = json_datastore(y, do='go')
    print(data)
