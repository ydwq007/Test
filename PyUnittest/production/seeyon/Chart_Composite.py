# -*- coding: utf-8 -*-
"""
接口：组合图表
创建人：魏奇
更新人：魏奇
更新时间：2020-01-10 16:07
描述：
"""

from pyecharts import options as opts #引入配置项入口
from pyecharts.charts import Bar,Line,Grid,Page,Timeline,Scatter,Pie,EffectScatter #导入柱状图,折线图,并行多图，顺序多图，时间线轮播多图,散点图,饼状图,动态散点图
from pyecharts.render import make_snapshot #直接生成图片
from pyecharts.globals import ThemeType #内置主题类型可查看
from snapshot_selenium import snapshot
from pyecharts.faker import Faker


class chart_composite():

    def __init__(self,title,X,Y):
        self.title = title
        self.x = X
        self.y = Y

    #组合图表-Grid并行多图-上下
    def grid_updown(self):

        bar = Bar()
        bar.add_xaxis(self.x)
        for i in range(len(self.y)):
            bar.add_yaxis(
                self.y[i][0],self.y[i][-1]) #设置Y轴展示数据
        bar.set_global_opts(
            title_opts=opts.TitleOpts(title=self.title,subtitle="Grid-Bar"),
            xaxis_opts=opts.AxisOpts(
                name="省份"  #x轴名称
            ),
            yaxis_opts=opts.AxisOpts(
                name="万亿（元）" #Y轴名称
            )
            )

        line = Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        line.add_xaxis(self.x) #设置X轴展示数据
        for i in range(len(self.y)):
            line.add_yaxis(
                self.y[i][0],
                self.y[i][-1],
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")])
            ) #设置Y轴展示数据
        line.set_global_opts(
            title_opts=opts.TitleOpts(title=self.title,subtitle="Grid-Line",pos_top="48%"),
            legend_opts=opts.LegendOpts(pos_top="48%"), #图例配置项
            xaxis_opts=opts.AxisOpts(
                name="省份"  #x轴名称
            ),
            yaxis_opts=opts.AxisOpts(
                name="万亿（元）" #Y轴名称
            )
            )

        grid = (
            Grid()
                .add(bar,grid_opts=opts.GridOpts(pos_bottom="60%"))
                .add(line,grid_opts=opts.GridOpts(pos_top="60%"))
            )

        return grid.render("../../TestResults/HTML/chart_composite_grid_updown_001.html")

    #组合图表-Grid并行多图-左右
    def grid_about(self):

        scatter = EffectScatter(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        scatter.add_xaxis(self.x) #设置X轴展示数据
        for i in range(len(self.y)):
            scatter.add_yaxis(self.y[i][0],self.y[i][-1],symbol="pin") #设置Y轴展示数据
        scatter.set_global_opts(
            title_opts=opts.TitleOpts(title=self.title,subtitle="Grid-Scatter"), #设置标题和副标题
            legend_opts=opts.LegendOpts(pos_left="20%"),#图例配置项
            xaxis_opts=opts.AxisOpts(
                name="省份"  #x轴名称
            ),
            yaxis_opts=opts.AxisOpts(
                name="万亿（元）" #Y轴名称
            )
        )

        line = Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        line.add_xaxis(self.x) #设置X轴展示数据
        for i in range(len(self.y)):
            line.add_yaxis(
                self.y[i][0],
                self.y[i][-1],
                markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]),
                ) #设置Y轴展示数据
        line.set_global_opts(
            title_opts=opts.TitleOpts(title=self.title,subtitle="Grid-Line",pos_right="40%"),
            legend_opts=opts.LegendOpts(pos_right="10%"), #图例配置项
            xaxis_opts=opts.AxisOpts(
                name="省份"  #x轴名称
            ),
            yaxis_opts=opts.AxisOpts(
                name="万亿（元）" #Y轴名称
            )
        )

        grid = (
            Grid()
                .add(scatter,grid_opts=opts.GridOpts(pos_left="60%")) # 添加要展示的图表，并设置显示位置
                .add(line,grid_opts=opts.GridOpts(pos_right="60%"))
        )

        return grid.render("../../TestResults/HTML/chart_composite_grid_about_001.html")


    # def chart_overlap(self):


if __name__ == "__main__":

    title = "某商场销售情况"
    X = ["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"]
    Y = [["商家A",[120, 470, 432, 256, 767, 1356, 1622]],["商家B",[289, 390, 287, 707, 1056, 1522, 160]],
         ["商家C",[334, 230, 142, 566, 467, 856, 622]],["商家D",[412, 103, 399, 198, 536, 798, 1321]]]
    composite = chart_composite(title,X,Y)
    # composite.grid_updown()
    composite.grid_about()


