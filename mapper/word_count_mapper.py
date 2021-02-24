from bson import Code

from mapper.config import client
from mapper.scripts.word_count_script import aggregation_pipeline_parm

word_collection = client.sentiment.word


def insert_words(word_list: list, timestamp: int):
    for word in word_list:
        word_collection.insert_one({
            "word": word,
            "time": timestamp
        })


def word_count(timestamp: int, size: int) -> dict:
    cursor = word_collection.aggregate(aggregation_pipeline_parm(timestamp, size))
    result = {}
    for i in cursor:
        print(i, type(i))


if __name__ == '__main__':
    '''
        map-reduce:
        db.word.mapReduce(function(){emit(this.word,1);},function(key,values){return Array.sum(values)},{query:{time:133},out:"word_count"})
    '''
    '''
        aggregate:
        db.word.aggregate([{$match:{time:{$gte:233}}},{$group:{_id:"$word",count:{$sum:1}}},{$sort:{count:-1}},{$limit:20}])
    '''

    """
    for t in word_collection.find():
        print(t)
    map_script = Code('''function(){emit(this.word,1);}''')
    reduce_script = Code('''function(key,values){return Array.sum(values)}''')
    res = word_collection.map_reduce(map_script, reduce_script, "tmp", True, query={'time': {'$gte': 233}}, jsMode=True)
    print(res)
    """
    word_count(233, 5)
