# -*- coding: utf-8 -*-
"""
接口：漏斗图
创建人：魏奇
更新人：魏奇
更新时间：2020-01-13 16:29
描述：
"""
from pyecharts import options as opts #引入配置项入口
from pyecharts.charts import Funnel #导入漏斗图
from pyecharts.render import make_snapshot #直接生成图片
from pyecharts.globals import ThemeType #内置主题类型可查看
from snapshot_selenium import snapshot

def chart_funnel_base(title,X,Y,subtitle="漏斗图"):

    #构造图形对象，初始化配置项
    funnel = Funnel()
    funnel.add(title,[list(z) for z in zip(X, Y)])

    funnel.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle=subtitle),
                        legend_opts=opts.LegendOpts(
                            orient="vertical",pos_top="15%",pos_left="2%"
                        )#图例设置
                        )
    # bar.render_notebook() #直接展示
    funnel.render(r"../../TestResults/HTML/chart_funnel_base_001.html") #生成HTML页面
    make_snapshot(snapshot, funnel.render(), r"../../TestResults/Picture/chart_funnel_base_001.png") #导出图片

def chart_funnel_sort(title,X,Y,subtitle="漏斗图"):

    #构造图形对象，初始化配置项
    funnel = Funnel()
    funnel.add(
        title,
        [list(z) for z in zip(X, Y)],
        sort_="ascending",
        label_opts=opts.LabelOpts(position="inside")
    )

    funnel.set_global_opts(
        title_opts=opts.TitleOpts(title=title,subtitle=subtitle),
        # legend_opts=opts.LegendOpts(
        # orient="vertical",pos_top="15%",pos_left="2%"
        #     )#图例设置
         )
    # bar.render_notebook() #直接展示
    funnel.render(r"../../TestResults/HTML/chart_funnel_sort_001.html") #生成HTML页面
    make_snapshot(snapshot, funnel.render(), r"../../TestResults/Picture/chart_funnel_sort_001.png") #导出图片

if __name__ == "__main__":
    title = "某商场销售情况"
    X = ["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"]
    Y = [20, 70, 232, 256, 767, 1356, 1622]
    chart_funnel_base(title,X,Y) #漏斗图
    chart_funnel_sort(title,X,Y) #漏斗图

