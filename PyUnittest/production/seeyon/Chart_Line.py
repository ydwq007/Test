# -*- coding: utf-8 -*-
"""
接口：折线图
创建人：魏奇
更新人：魏奇
更新时间：2020-01-13 14:17
描述：
"""
from pyecharts import options as opts #引入配置项入口
from pyecharts.charts import Line #导入折线图
from pyecharts.render import make_snapshot #直接生成图片
from pyecharts.globals import ThemeType #内置主题类型可查看
from snapshot_selenium import snapshot

class Chart_Line():
    #折线图
    def chart_line_base(title,X,Y,subtitle="折线图"):

        #构造图形对象，初始化配置项
        bar = Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        bar.add_xaxis(X) #设置X轴展示数据
        for i in range(len(Y)):
            bar.add_yaxis(Y[i][0],Y[i][-1]) #设置Y轴展示数据
        bar.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle=subtitle)) #设置标题和副标题

        # bar.render_notebook() #直接展示
        bar.render(r"../../TestResults/HTML/chart_line_base_001.html") #生成HTML页面
        make_snapshot(snapshot, bar.render(), r"../../TestResults/Picture/chart_line_base_001.png") #导出图片

    #平滑折线图
    def chart_line_smooth(title,X,Y,subtitle="平滑折线图"):

        #构造图形对象，初始化配置项
        bar = Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        bar.add_xaxis(X) #设置X轴展示数据
        for i in range(len(Y)):
            bar.add_yaxis(Y[i][0],Y[i][-1],is_smooth=True) #设置Y轴展示数据
        bar.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle=subtitle)) #设置标题和副标题

        # bar.render_notebook() #直接展示
        bar.render(r"../../TestResults/HTML/chart_line_smooth_001.html") #生成HTML页面
        make_snapshot(snapshot, bar.render(), r"../../TestResults/Picture/chart_line_smooth_001.png") #导出图片

    #阶梯折线图
    def chart_line_step(title,X,Y,subtitle="阶梯折线图"):

        #构造图形对象，初始化配置项
        bar = Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        bar.add_xaxis(X) #设置X轴展示数据
        for i in range(len(Y)):
            bar.add_yaxis(Y[i][0],Y[i][-1],is_step=True) #设置Y轴展示数据
        bar.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle=subtitle)) #设置标题和副标题

        # bar.render_notebook() #直接展示
        bar.render(r"../../TestResults/HTML/chart_line_step_001.html") #生成HTML页面
        make_snapshot(snapshot, bar.render(), r"../../TestResults/Picture/chart_line_step_001.png") #导出图片

    #面积折线图
    def chart_line_area(title,X,Y,subtitle="面积折线图"):

        #构造图形对象，初始化配置项
        bar = Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        bar.add_xaxis(X) #设置X轴展示数据
        for i in range(len(Y)):
            bar.add_yaxis(Y[i][0],Y[i][-1],areastyle_opts=opts.AreaStyleOpts(opacity=0.5),is_smooth=True) #设置Y轴展示数据
        bar.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle=subtitle)) #设置标题和副标题

        # bar.render_notebook() #直接展示
        bar.render(r"../../TestResults/HTML/chart_line_area_001.html") #生成HTML页面
        make_snapshot(snapshot, bar.render(), r"../../TestResults/Picture/chart_line_area_001.png") #导出图片

    #面积折线图-紧贴Y轴
    def chart_line_area_y(title,X,Y,subtitle="面积折线图-紧贴Y轴"):

        #构造图形对象，初始化配置项
        bar = Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        bar.add_xaxis(X) #设置X轴展示数据
        for i in range(len(Y)):
            bar.add_yaxis(Y[i][0],Y[i][-1],areastyle_opts=opts.AreaStyleOpts(opacity=0.5),is_smooth=True) #设置Y轴展示数据
        bar.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle=subtitle),
                            xaxis_opts=opts.AxisOpts(
                                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                                is_scale=False,
                                boundary_gap=False
                            )

                            ) #设置标题和副标题

        # bar.render_notebook() #直接展示
        bar.render(r"../../TestResults/HTML/chart_line_area_y_001.html") #生成HTML页面
        make_snapshot(snapshot, bar.render(), r"../../TestResults/Picture/chart_line_area_y_001.png") #导出图片

    #折线图-平均值
    def chart_line_average(title,X,Y,subtitle="折线图-平均值"):

        #构造图形对象，初始化配置项
        bar = Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        bar.add_xaxis(X) #设置X轴展示数据
        for i in range(len(Y)):
            bar.add_yaxis(Y[i][0],Y[i][-1],markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")])) #设置Y轴展示数据
        bar.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle=subtitle),
                            xaxis_opts=opts.AxisOpts(
                                axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                                is_scale=False,
                                boundary_gap=False
                            )

                            ) #设置标题和副标题

        # bar.render_notebook() #直接展示
        bar.render(r"../../TestResults/HTML/chart_line_average_001.html") #生成HTML页面
        make_snapshot(snapshot, bar.render(), r"../../TestResults/Picture/chart_line_average_001.png") #导出图片

if __name__ == "__main__":
    title = "某商场销售情况"
    X = ["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"]
    Y = [["商家A",[20, 70, 232, 256, 767, 1356, 1622]],["商家B",[59, 90, 287, 707, 1756, 1822,  60]],
         ["商家C",[34, 230, 42, 566, 467, 1856, 2622]],["商家D",[12, 43, 299, 198, 536, 1098, 1321]]]
    Chart_Line.chart_line_base(title,X,Y) #折线图
    Chart_Line.chart_line_smooth(title,X,Y) #平滑折线图
    Chart_Line.chart_line_step(title,X,Y) #阶梯折线图
    Chart_Line.chart_line_area(title,X,Y) #面积折线图
    Chart_Line.chart_line_area_y(title,X,Y) #面积折线图-紧贴Y轴
    Chart_Line.chart_line_average(title,X,Y) #折线图-平均值