# -*- coding: utf-8 -*-
"""
接口：雷达图
创建人：魏奇
更新人：魏奇
更新时间：2020-01-14 11:25
描述：
"""

from pyecharts import options as opts #引入配置项入口
from pyecharts.charts import Radar,Polar #导入雷达图,极地坐标系
from pyecharts.render import make_snapshot #直接生成图片
from pyecharts.globals import ThemeType #内置主题类型可查看
from snapshot_selenium import snapshot

class chart_render():

    #基本雷达图
    def chart_render_base(title,**kwargs,):

        #构造图形对象，初始化配置项
        render = (
            Radar()
            .add_schema( #引入schema架构
                schema=[
                    opts.RadarIndicatorItem(name='销售',max_=6500), # 设置指示器名称和最大值
                    opts.RadarIndicatorItem(name='管理',max_=16000),
                    opts.RadarIndicatorItem(name='信息技术',max_=30000),
                    opts.RadarIndicatorItem(name='客服',max_=38000),
                    opts.RadarIndicatorItem(name='研发',max_=52000),
                    opts.RadarIndicatorItem(name='市场',max_=25000)
                ],
                # shape="circle" # 设置雷达图类型圆形,默认为多边形
            )
            .add(
                "预算分配", #系列名称
                value1, #数据
                color="red", #边框颜色
                areastyle_opts = opts.AreaStyleOpts(
                    opacity = 0.5,#透明度
                    color="red" #填充颜色
                  )
            ) #设置展示数据
            .add(
                "实际开销",
                value2,
                color="blue",
                areastyle_opts = opts.AreaStyleOpts(
                    opacity = 0.5,#透明度
                    color="blue"
                )
            ) #设置展示数据
        )
        render.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle="基本雷达图"))

        # bar.render_notebook() #直接展示
        render.render(r"../../TestResults/HTML/chart_render_base_001.html") #生成HTML页面
        make_snapshot(snapshot, render.render(), r"../../TestResults/Picture/chart_render_base_001.png") #导出图片

    def chart_polar_base(title,**kwargs,):

        #构造图形对象，初始化配置项
        polar = (
            Polar()
                .add_schema( #引入schema架构
                schema=[
                    opts.RadarIndicatorItem(name='销售',max_=6500), # 设置指示器名称和最大值
                    opts.RadarIndicatorItem(name='管理',max_=16000),
                    opts.RadarIndicatorItem(name='信息技术',max_=30000),
                    opts.RadarIndicatorItem(name='客服',max_=38000),
                    opts.RadarIndicatorItem(name='研发',max_=52000),
                    opts.RadarIndicatorItem(name='市场',max_=25000)
                ],
                # shape="circle" # 设置雷达图类型圆形,默认为多边形
            )
                .add(
                "预算分配", #系列名称
                value1, #数据
                color="red", #边框颜色
                areastyle_opts = opts.AreaStyleOpts(
                    opacity = 0.5,#透明度
                    color="red" #填充颜色
                )
            ) #设置展示数据
                .add(
                "实际开销",
                value2,
                color="blue",
                areastyle_opts = opts.AreaStyleOpts(
                    opacity = 0.5,#透明度
                    color="blue"
                )
            ) #设置展示数据
        )
        polar.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle="极地坐标系"))

        # bar.render_notebook() #直接展示
        polar.render(r"../../TestResults/HTML/chart_polar_base_001.html") #生成HTML页面
        make_snapshot(snapshot, polar.render(), r"../../TestResults/Picture/chart_polar_base_001.png") #导出图片


if __name__ == "__main__":
    title = "雷达图示例"
    standard =[ ("销售", 6500), ("管理", 16000), ("信息技术", 30000), ("客服", 38000), ("研发", 52000), ("市场", 25000)]
    value1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
    value2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
    radius =['周一', '周二', '周三', '周四', '周五', '周六', '周日']

    # chart_render.chart_render_base(title,value1=value1,value2=value2)
    chart_render.chart_polar_base(title,value1=value1,value2=value2)