# -*- coding: utf-8 -*-
"""
接口：仪表盘
创建人：魏奇
更新人：魏奇
更新时间：2020-01-13 20:43
描述：
"""
from pyecharts import options as opts #引入配置项入口
from pyecharts.charts import Gauge #导入仪表盘
from pyecharts.render import make_snapshot #直接生成图片
from pyecharts.globals import ThemeType #内置主题类型可查看
from snapshot_selenium import snapshot

def chart_gauge_base(title,theme,content,subtitle="仪表盘"):

    #构造图形对象，初始化配置项
    gauge = Gauge(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    gauge.add(theme,[content]) #设置展示数据

    gauge.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle=subtitle))

    # bar.render_notebook() #直接展示
    gauge.render(r"../../TestResults/HTML/chart_gauge_base_001.html") #生成HTML页面
    make_snapshot(snapshot, gauge.render(), r"../../TestResults/Picture/chart_gauge_base_001.png") #导出图片


if __name__ == "__main__":
    title = "仪表盘示例"
    theme = "业务指标"
    value = ("完成率",68.97)
    chart_gauge_base(title,theme,value)