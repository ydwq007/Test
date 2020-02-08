# -*- coding: utf-8 -*-
"""
接口：水球图
创建人：魏奇
更新人：魏奇
更新时间：2020-01-13 16:07
描述：
"""
from pyecharts import options as opts #引入配置项入口
from pyecharts.charts import Liquid #导入水球图
from pyecharts.render import make_snapshot #直接生成图片
from pyecharts.globals import ThemeType #内置主题类型可查看
from snapshot_selenium import snapshot

class Chart_Liquid():

    #水球图
    def chart_liquid_base(title,liquid,per,subtitle="水球图"):

        #构造图形对象，初始化配置项
        bar = Liquid(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        bar.add(liquid,per)
        bar.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle=subtitle)) #设置标题和副标题

        # bar.render_notebook() #直接展示
        bar.render(r"../../TestResults/HTML/chart_liquid_base_001.html") #生成HTML页面
        make_snapshot(snapshot, bar.render(), r"../../TestResults/Picture/chart_liquid_base_001.png") #导出图片

    #水球图-方形
    def chart_liquid_square(title,liquid,per,subtitle="水球图-方形"):

        #构造图形对象，初始化配置项
        bar = Liquid(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        bar.add(liquid,per, shape='diamond')
        bar.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle=subtitle)) #设置标题和副标题

        # bar.render_notebook() #直接展示
        bar.render(r"../../TestResults/HTML/chart_liquid_square_001.html") #生成HTML页面
        make_snapshot(snapshot, bar.render(), r"../../TestResults/Picture/chart_liquid_square_001.png") #导出图片

if __name__ == "__main__":
    title = "水球百分比"
    per = [[0.6],[0.6, 0.5, 0.4, 0.3]]
    Chart_Liquid.chart_liquid_base(title,"测试",per[0]) #水球图-单一
    Chart_Liquid.chart_liquid_base(title,"测试",per[1]) #水球图-多层
    Chart_Liquid.chart_liquid_square(title,"测试",per[1]) #水球图-方形
