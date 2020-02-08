# -*- coding: utf-8 -*-
"""
接口：柱状图
创建人：魏奇
更新人：魏奇
更新时间：2020-01-10 16:15
描述：X轴参数为列表一个，如：["衬衫", "毛衣"]，
     Y轴为参数列表中套列表，如：[["商家A",[20, 70]],["商家B",[59, 90]]]
"""

from pyecharts import options as opts #引入配置项入口
from pyecharts.charts import Bar #导入柱状图
from pyecharts.render import make_snapshot #直接生成图片
from pyecharts.globals import ThemeType #内置主题类型可查看
from snapshot_selenium import snapshot

# 柱状图
class chart_bar():

    #基本柱状图-正常XY轴（并列）
    def chart_bar_base(title,X,Y,subtitle=""):

        #构造图形对象，初始化配置项
        bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        bar.add_xaxis(X) #设置X轴展示数据
        for i in range(len(Y)):
            bar.add_yaxis(Y[i][0],Y[i][-1]) #设置Y轴展示数据
        bar.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle=subtitle)) #设置标题和副标题

        # bar.render_notebook() #直接展示
        bar.render(r"../../TestResults/HTML/chart_bar_base_001.html") #生成HTML页面
        make_snapshot(snapshot, bar.render(), r"../../TestResults/Picture/chart_bar_base_001.png") #导出图片

    #基本柱状图-翻转XY轴（并列）
    def chart_bar_flip(title,X,Y,subtitle=""):
        title_line = "%s-翻转XY轴" % title

        #构造图形对象，初始化配置项
        bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC)) #主题
        bar.add_xaxis(X) #设置X轴展示数据
        for i in range(len(Y)):
            bar.add_yaxis(Y[i][0],Y[i][-1]) #设置Y轴展示数据
        bar.reversal_axis() #翻转XY轴数据
        bar.set_series_opts(label_opts=opts.LabelOpts(position="right")) ##翻转xy轴需要得配置项
        bar.set_global_opts(title_opts=opts.TitleOpts(title=title_line,subtitle=subtitle)) #设置标题和副标题

        # bar.render_notebook() #直接展示
        bar.render(r"../../TestResults/HTML/chart_bar_flip_001.html") #生成HTML页面
        make_snapshot(snapshot, bar.render(), r"../../TestResults/Picture/chart_bar_flip_001.png") #导出图片

    #堆叠柱状图-正常XY轴
    def chart_bar_stack(title,X,Y,subtitle=""):
        title_line = "%s-堆叠数据" % title
        #构造图形对象，初始化配置项
        bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        bar.add_xaxis(X) #设置X轴展示数据
        for i in range(len(Y)):
            bar.add_yaxis(Y[i][0],Y[i][-1],stack="stack1") #设置Y轴展示数据

        bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False)) ##翻转xy轴需要得配置项
        bar.set_global_opts(title_opts=opts.TitleOpts(title=title_line,subtitle=subtitle)) #设置标题和副标题

        # bar.render_notebook() #直接展示
        bar.render(r"../../TestResults/HTML/chart_bar_stack_001.html") #生成HTML页面
        make_snapshot(snapshot, bar.render(), r"../../TestResults/Picture/chart_bar_stack_001.png") #导出图片

    #指定类型柱状图-正常XY轴
    def chart_bar_markpoint(title,X,Y,subtitle=""):
        title_line = "%s-指定类型" % title
        #构造图形对象，初始化配置项
        bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        bar.add_xaxis(X) #设置X轴展示数据
        for i in range(len(Y)):
            bar.add_yaxis(Y[i][0],Y[i][-1]) #设置Y轴展示数据

        bar.set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max",name="最大值"),
                    opts.MarkPointItem(type_="min",name="最小值"),
                    opts.MarkPointItem(type_="average",name="平均值"),
                ]
            )
        ) ##翻转xy轴需要得配置项
        bar.set_global_opts(title_opts=opts.TitleOpts(title=title_line,subtitle=subtitle)) #设置标题和副标题

        # bar.render_notebook() #直接展示
        bar.render(r"../../TestResults/HTML/chart_bar_markpoint_001.html") #生成HTML页面
        make_snapshot(snapshot, bar.render(), r"../../TestResults/Picture/chart_bar_markpoint_001.png") #导出图片

    #水平柱状图-正常XY轴
    def chart_bar_level(title,X,Y,subtitle=""):
        title_line = "%s-slider水平" % title
        #构造图形对象，初始化配置项
        bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        bar.add_xaxis(X) #设置X轴展示数据
        for i in range(len(Y)):
            bar.add_yaxis(Y[i][0],Y[i][-1]) #设置Y轴展示数据

        bar.set_global_opts(
            title_opts=opts.TitleOpts(title=title_line,subtitle=subtitle),
            datazoom_opts=opts.DataZoomOpts()
        ) #设置标题和副标题

        # bar.render_notebook() #直接展示
        bar.render(r"../../TestResults/HTML/chart_bar_level_001.html") #生成HTML页面
        make_snapshot(snapshot, bar.render(), r"../../TestResults/Picture/chart_bar_level_001.png") #导出图片

    #垂直柱状图-正常XY轴
    def chart_bar_vertical(title,X,Y,subtitle=""):
        title_line = "%s-slider垂直" % title
        #构造图形对象，初始化配置项
        bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        bar.add_xaxis(X) #设置X轴展示数据
        for i in range(len(Y)):
            bar.add_yaxis(Y[i][0],Y[i][-1]) #设置Y轴展示数据

        bar.set_global_opts(
            title_opts=opts.TitleOpts(title=title_line,subtitle=subtitle),
            datazoom_opts=opts.DataZoomOpts(orient="vertical")
        ) #设置标题和副标题

        # bar.render_notebook() #直接展示
        bar.render(r"../../TestResults/HTML/chart_bar_vertical_001.html") #生成HTML页面
        make_snapshot(snapshot, bar.render(), r"../../TestResults/Picture/chart_bar_vertical_001.png") #导出图片

if __name__ == "__main__":
    title = "某商场销售情况"
    X = ["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"]
    Y = [["商家A",[20, 70, 232, 256, 767, 1356, 1622]],["商家B",[59, 90, 287, 707, 1756, 1822,  60]],
         ["商家C",[34, 230, 42, 566, 467, 1856, 2622]],["商家D",[12, 43, 299, 198, 536, 1098, 1321]]]
    chart_bar.chart_bar_base(title,X,Y) #基本柱状图-正常XY轴（并列）
    chart_bar.chart_bar_flip(title,X,Y) #基本柱状图-翻转XY轴（并列）
    chart_bar.chart_bar_stack(title,X,Y) #堆叠柱状图-正常XY轴
    chart_bar.chart_bar_markpoint(title,X,Y) #指定类型柱状图-正常XY轴
    chart_bar.chart_bar_level(title,X,Y) #水平柱状图-正常XY轴
    chart_bar.chart_bar_vertical(title,X,Y) #垂直柱状图-正常XY轴


