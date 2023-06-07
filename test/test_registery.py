from fastcrawler.core.registery import Crawler
from fastcrawler.core.spider import Spider


def test_crawler_instances():
    obj_a = Crawler('arg1')
    obj_b = Crawler('arg2', keyword_arg='key_arg1')
    all_objs = Crawler.get_all_objects()
    assert obj_a in all_objs
    assert obj_b in all_objs
    assert all_objs[obj_a] == (('arg1',), {})
    assert all_objs[obj_b] == (('arg2',), {'keyword_arg': 'key_arg1'})


def test_crawler_with_task():
    class cls_A(Spider):
        pass

    class cls_B(Spider):
        pass

    class cls_C(Spider):
        pass

    obj = Crawler(cls_A >> cls_B >> cls_C)
    assert [cls_A, cls_B, cls_C] == obj.task.instances