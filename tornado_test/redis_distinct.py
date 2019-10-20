# -*- coding: utf-8 -*- 
import redis
from public_code import logger, redis_ip, redis_db, redis_pw, redis_zset_name, \
    move_file_lm, redis_zset_clean_date

pool = redis.ConnectionPool(host=redis_ip, db=redis_db, password=redis_pw)
# pool = redis.ConnectionPool(db=6, password=redis_pw)
rr = redis.Redis(connection_pool=pool)  # # 客户端StrictRedis=Redis 合并了
pipe = rr.pipeline(transaction=True)  # 批量操作


def distinct_md5(date, eml_md5, eml_path, redis_fail_path):
    try:
        # pipe.zadd(redis_zset_name, eml_md5, md5_date)
        # pipe.zadd(redis_zset_name, {date: eml_md5}, nx=True)
        # pipe.zadd(redis_zset_name, {date: eml_md5})
        pipe.zadd(redis_zset_name, {eml_md5: date})
        return pipe.execute()[0]  # 1 添加, 0 没添加

    except Exception as e:
        move_file_lm(eml_path, redis_fail_path, "md5去重", e)
        return -1


# pipe.zcard('eml_md5_zset')  # 查看总个数


def del_redis_md5(n, m):  # 按照分数值进行删除
    try:
        pipe.zremrangebyscore(redis_zset_name, n, m)
    except Exception as e:
        logger.warning("删除Redis缓存中md5值失败: {},".format(e))
        return
    pipe.execute()


# 	return
# return pipe.execute()[0]


def clean_redis_zset(md5_score):
    if md5_score <= redis_zset_clean_date:
        md5_score += 31
    md5_clean_score = md5_score - redis_zset_clean_date
    del_redis_md5(md5_clean_score - 0.5, md5_clean_score + 0.5)  # 清理Redis上的md5  闭区间


# print(distinct_md5(redis_zset_name, "qwe", 2, "sdfsd", "sdfsdf"))
# print(distinct_md5(redis_zset_name, "qweqwe", 2, "sdfsd", "sdfsdf"))
# print(del_redis_md5(redis_zset_name, 1, 10))
clean_redis_zset(5)
