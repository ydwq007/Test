# -*- coding: utf-8 -*-
"""
接口：饼状图
创建人：魏奇
更新人：魏奇
更新时间：2020-01-13 14:41
描述：
"""
from pyecharts import options as opts #引入配置项入口
from pyecharts.charts import Pie #导入饼状图
from pyecharts.render import make_snapshot #直接生成图片
from pyecharts.globals import ThemeType #内置主题类型可查看
from snapshot_selenium import snapshot

class Chart_Pie():

    #饼状图
    def chart_pie_base(title,X,Y,subtitle="饼状图"):

        #构造图形对象，初始化配置项
        # bar = Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        pie = Pie()
        pie.add(
            "",
            [list(z) for z in zip(X, Y)] #字典

        ) #设置X轴展示数据

        pie.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle=subtitle))
        pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))#格式化标签输出内容
        # bar.render_notebook() #直接展示
        pie.render(r"../../TestResults/HTML/chart_pie_base_001.html") #生成HTML页面
        make_snapshot(snapshot, pie.render(), r"../../TestResults/Picture/chart_pie_base_001.png") #导出图片

    #饼状图-圆环
    def chart_pie_radius(title,X,Y,subtitle="饼状图-玫瑰花"):

        #构造图形对象，初始化配置项
        # bar = Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        pie = Pie()
        pie.add(
            "",
            [list(z) for z in zip(X, Y)], #字典
            radius=["40%", "75%"] #饼图的半径,扇区圆心角展现数据的百分比，半径展现数据的大小

        ) #设置X轴展示数据

        pie.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle=subtitle),
                            legend_opts=opts.LegendOpts(
                                orient="vertical",pos_top="15%",pos_left="2%"
                            )
                        )
        pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))#格式化标签输出内容

       # bar.render_notebook() #直接展示
        pie.render(r"../../TestResults/HTML/chart_pie_radius_001.html") #生成HTML页面
        make_snapshot(snapshot, pie.render(), r"../../TestResults/Picture/chart_pie_radius_001.png") #导出图片

    #饼状图-玫瑰花
    def chart_pie_rose(title,X,Y,subtitle="饼状图-玫瑰花"):

        #构造图形对象，初始化配置项
        # bar = Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        pie = Pie()
        pie.add(
            "",
            [list(z) for z in zip(X, Y)], #字典
            radius=["20%", "65%"], #饼图的半径,扇区圆心角展现数据的百分比，半径展现数据的大小
            center=["35%","60%"],#图标中心位置
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=False)
        ) #设置X轴展示数据
        pie.add(
            "",
            [list(z) for z in zip(X, Y)], #字典
            radius=["20%", "65%"], #饼图的半径,扇区圆心角展现数据的百分比，半径展现数据的大小
            center=["75%","60%"],#图标中心位置
            rosetype="area"
        ) #设置X轴展示数据


        pie.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle=subtitle)
                            # legend_opts=opts.LegendOpts(
                            #     orient="vertical",pos_top="15%",pos_left="2%"
                            # )

        pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))#格式化标签输出内容
        # bar.render_notebook() #直接展示
        pie.render(r"../../TestResults/HTML/chart_pie_rose_001.html") #生成HTML页面
        make_snapshot(snapshot, pie.render(), r"../../TestResults/Picture/chart_pie_rose_001.png") #导出图片

    #饼状图-多饼图
    def chart_pie_multiple(title,X,Y,subtitle="饼状图-玫瑰花"):

        #构造图形对象，初始化配置项
        # bar = Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        pie = Pie()
        pie.add(
            "",
            [list(z) for z in zip(X, Y)], #字典
            radius=["10%", "30%"], #饼图的半径,扇区圆心角展现数据的百分比，半径展现数据的大小
            center=["30%", "30%"] #图标中心位置
        ) #设置X轴展示数据
        pie.add(
            "",
            [list(z) for z in zip(X, Y)], #字典
            radius=["10%", "30%"], #饼图的半径,扇区圆心角展现数据的百分比，半径展现数据的大小
            center=["70%", "30%"] #图标中心位置
        ) #设置X轴展示数据
        pie.add(
            "",
            [list(z) for z in zip(X, Y)], #字典
            radius=["10%", "30%"], #饼图的半径,扇区圆心角展现数据的百分比，半径展现数据的大小
            center=["30%", "80%"] #图标中心位置
        ) #设置X轴展示数据
        pie.add(
            "",
            [list(z) for z in zip(X, Y)], #字典
            radius=["10%", "30%"], #饼图的半径,扇区圆心角展现数据的百分比，半径展现数据的大小
            center=["70%", "80%"] #图标中心位置
        ) #设置X轴展示数据

        pie.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle=subtitle),
                            legend_opts=opts.LegendOpts(
                                orient="vertical",pos_top="10%",pos_left="90%",type_="scroll"
                            )
                         )
        pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))#格式化标签输出内容
        # pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))

        # bar.render_notebook() #直接展示
        pie.render(r"../../TestResults/HTML/chart_pie_multiple_001.html") #生成HTML页面
        make_snapshot(snapshot, pie.render(), r"../../TestResults/Picture/chart_pie_multiple_001.png") #导出图片

if __name__ == "__main__":
    title = "某商场销售情况"
    X = ["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"]
    Y = [20, 70, 232, 256, 767, 1356, 1622]
    # Chart_Pie.chart_pie_base(title,X,Y) #饼状图
    # Chart_Pie.chart_pie_radius(title,X,Y) #饼状图-圆环
    # Chart_Pie.chart_pie_rose(title,X,Y) #饼状图-玫瑰花
    Chart_Pie.chart_pie_multiple(title,X,Y) #饼状图-多饼图
