# -*- coding: utf-8 -*-
"""
接口：散点图
创建人：魏奇
更新人：魏奇
更新时间：2020-01-13 14:24
描述：
"""
from pyecharts import options as opts #引入配置项入口
from pyecharts.charts import Scatter,EffectScatter #导入散点图,动态散点图
from pyecharts.render import make_snapshot #直接生成图片
from pyecharts.globals import ThemeType #内置主题类型可查看
from snapshot_selenium import snapshot

class Chart_Scatter():

    #基础散点图
    def chart_scatter_base(title,X,Y,subtitle=""):
        title_line = "%s-基础" % title
        #构造图形对象，初始化配置项
        bar = Scatter(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        bar.add_xaxis(X) #设置X轴展示数据
        for i in range(len(Y)):
            bar.add_yaxis(Y[i][0],Y[i][-1]) #设置Y轴展示数据
        bar.set_global_opts(title_opts=opts.TitleOpts(title=title_line,subtitle=subtitle)) #设置标题和副标题

        # bar.render_notebook() #直接展示
        bar.render(r"../../TestResults/HTML/chart_scatter_base_001.html") #生成HTML页面
        make_snapshot(snapshot, bar.render(), r"../../TestResults/Picture/chart_scatter_base_001.png") #导出图片

    #动态散点图
    def chart_scatter_effect(title,X,Y,subtitle=""):
        title_line = "%s-动态" % title

        #构造图形对象，初始化配置项
        bar = EffectScatter(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        bar.add_xaxis(X) #设置X轴展示数据
        for i in range(len(Y)):
            bar.add_yaxis(Y[i][0],Y[i][-1],symbol="pin") #设置Y轴展示数据,symbol:pin,rect,roundRect,diamond,arrow,triangle
        bar.set_global_opts(title_opts=opts.TitleOpts(title=title_line,subtitle=subtitle)) #设置标题和副标题

        # bar.render_notebook() #直接展示
        bar.render(r"../../TestResults/HTML/chart_scatter_effect_001.html") #生成HTML页面
        make_snapshot(snapshot, bar.render(), r"../../TestResults/Picture/chart_scatter_effect_001.png") #导出图片

if __name__ == "__main__":
    title = "某商场销售情况"
    X = ["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"]
    Y = [["商家A",[20, 70, 232, 256, 767, 1356, 1622]],["商家B",[59, 90, 287, 707, 1756, 1822,  60]],
         ["商家C",[34, 230, 42, 566, 467, 1856, 2622]],["商家D",[12, 43, 299, 198, 536, 1098, 1321]]]
    Chart_Scatter.chart_scatter_base(title,X,Y) #基础散点图
    Chart_Scatter.chart_scatter_effect(title,X,Y) #动态散点图