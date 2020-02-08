# -*- coding: utf-8 -*-
"""
接口：词云图
创建人：魏奇
更新人：魏奇
更新时间：2020-01-15 15:52
描述：
"""
from pyecharts import options as opts #引入配置项入口
from pyecharts.charts import WordCloud #导入词云图
from pyecharts.render import make_snapshot #直接生成图片
from pyecharts.globals import SymbolType
from snapshot_selenium import snapshot

#词云图
def chart_wordclod_base(title,words,word_size_range):

    wordclod = (
        WordCloud()
        .add(
            "",
            words,
            word_size_range=word_size_range,
            shape=SymbolType.DIAMOND
        )
        .set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle="词云图"))
    )

    # bar.render_notebook() #直接展示
    wordclod.render(r"../../TestResults/HTML/chart_wordclod_base_001.html") #生成HTML页面
    make_snapshot(snapshot, wordclod.render(), r"../../TestResults/Picture/chart_wordclod_base_001.png") #导出图片

if __name__ == "__main__":
    title = "2019热门词汇"
    word_size_range = [20,100]
    words =[
        ("Sam S Club", 10000),
        ("Macys", 6181),
        ("Amy Schumer", 4386),
        ("Jurassic World", 4055),
        ("Charter Communications", 2467),
        ("Chick Fil A", 2244),
        ("Planet Fitness", 1868),
        ("Pitch Perfect", 1484),
        ("Express", 1112),
        ("Home", 865),
        ("Johnny Depp", 847),
        ("Lena Dunham", 582),
        ("Lewis Hamilton", 555),
        ("KXAN", 550),
        ("Mary Ellen Mark", 462),
        ("Farrah Abraham", 366),
        ("Rita Ora", 360),
        ("Serena Williams", 282),
        ("NCAA baseball tournament", 273),
        ("Point Break", 265)
    ]
    chart_wordclod_base(title,words,word_size_range)