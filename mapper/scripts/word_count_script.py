def aggregation_pipeline_parm(timestamp: int, size: int) -> list:
    return [{'$match': {'time': {'$gte': timestamp}}}, {'$group': {'_id': "$word", 'count': {'$sum': 1}}},
            {'$sort': {'count': -1}}, {'$limit': size}]
