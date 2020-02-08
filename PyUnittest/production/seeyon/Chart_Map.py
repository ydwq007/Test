# -*- coding: utf-8 -*-
"""
接口：地图
创建人：魏奇
更新人：魏奇
更新时间：2020-01-14 9:24
描述：
"""

from pyecharts import options as opts #引入配置项入口
from pyecharts.charts import Map,Geo #导入仪表盘,热力图
from pyecharts.render import make_snapshot #直接生成图片
from pyecharts.globals import ChartType,SymbolType,ThemeType
from snapshot_selenium import snapshot

class Chart_Map():

    #普通地图
    def chart_map_base(title,map,subtitle="普通地图"):

        provice=list(map.keys())
        values=list(map.values())

        #构造图形对象，初始化配置项
        # map = Map(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        # map.add("",[list(z) for z in zip(provice, values)]) #设置展示数据

        map = Map()
        map.add(
            "中国省份产值图",
            [list(z) for z in zip(provice, values)],
            maptype='china', #只显示全国直辖市和省级
            # visual_range=[0, 50],
            # visual_text_color='#000',
            # is_visualmap=True
        )
        map.set_global_opts(title_opts=opts.TitleOpts(title=title,subtitle=subtitle))

        # bar.render_notebook() #直接展示
        map.render(r"../../TestResults/HTML/chart_map_base_001.html") #生成HTML页面
        make_snapshot(snapshot, map.render(), r"../../TestResults/Picture/chart_map_base_001.png") #导出图片

    #热力地图
    def chart_map_heat(title,map,subtitle="热力地图"):

        provice=list(map.keys())
        values=list(map.values())

        #构造图形对象，初始化配置项
        # map = Map(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))

        geo = (
            Geo()
            .add_schema(maptype="china") #地图模型只显示全国直辖市和省级
            #在地图中加入点的属性
            .add(
                "全国主要城市空气质量热力图",
                [list(z) for z in zip(provice, values)],
                symbol_size=15,
                # visual_range=[0, 50],
                # visual_text_color='#000',
                # is_visualmap=True,
                # is_roam=False
            )
            # 设置坐标属性
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(),
                title_opts=opts.TitleOpts(title=title,subtitle=subtitle)
            )
        )

        # bar.render_notebook() #直接展示
        geo.render(r"../../TestResults/HTML/chart_map_heat_001.html") #生成HTML页面
        make_snapshot(snapshot, geo.render(), r"../../TestResults/Picture/chart_map_heat_001.png") #导出图片

    #连线地图
    def chart_map_line(title,coordinate,coordinate_relation,subtitle="连线地图"):

        #构造图形对象，初始化配置项
        # map = Map(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))

        geo = (
            Geo()
            .add_schema(
                    maptype="china",#地图模型只显示全国直辖市和省级
                    itemstyle_opts=opts.ItemStyleOpts(
                        color="#323c48",
                        border_color="#111"
                )
            )
                #在地图中加入点的属性,坐标点
            .add(
                    "广州辐射图",
                    coordinate,
                    type_=ChartType.EFFECT_SCATTER,
                    color="white"
            )
                #坐标点关系
             .add(
                    "",
                coordinate_relation,
                type_=ChartType.LINES,
                effect_opts=opts.EffectOpts(
                    symbol=SymbolType.ARROW,
                    symbol_size=6,
                    color="blue"
                ),
                linestyle_opts=opts.LineStyleOpts(curve=0.2)
            )
                # 设置坐标属性
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(),
                title_opts=opts.TitleOpts(title=title,subtitle=subtitle)
            )
        )

        # bar.render_notebook() #直接展示
        geo.render(r"../../TestResults/HTML/chart_map_line_001.html") #生成HTML页面
        make_snapshot(snapshot, geo.render(), r"../../TestResults/Picture/chart_map_line_001.png") #导出图片

    #动态地图
    def chart_map_effect(title,map,subtitle="动态地图"):

        provice=list(map.keys())
        values=list(map.values())
        #构造图形对象，初始化配置项
        # map = Map(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))

        geo = (
            Geo()
            .add_schema(
                maptype="china",#地图模型只显示全国直辖市和省级
            )
                #在地图中加入点的属性
            .add(
                "",
                [list(z) for z in zip(provice, values)],
                type_=ChartType.EFFECT_SCATTER,
            )
                # 设置坐标属性
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                # visualmap_opts=opts.VisualMapOpts(),
                title_opts=opts.TitleOpts(title=title,subtitle=subtitle)
            )
        )

        # bar.render_notebook() #直接展示
        geo.render(r"../../TestResults/HTML/chart_map_effect_001.html") #生成HTML页面
        make_snapshot(snapshot, geo.render(), r"../../TestResults/Picture/chart_map_effect_001.png") #导出图片

    #连续地图
    def chart_map_visual(title,map,subtitle="连续地图"):

        provice=list(map.keys())
        values=list(map.values())
        #构造图形对象，初始化配置项
        # map = Map(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))

        map = (
            Map()
            #在地图中加入点的属性
            .add(
                "",
                [list(z) for z in zip(provice, values)],
                "china",
            )
                # 设置坐标属性
            # .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                # visualmap_opts=opts.VisualMapOpts(),
                title_opts=opts.TitleOpts(title=title,subtitle=subtitle),
                visualmap_opts=opts.VisualMapOpts(max_=100)
            )
        )

        # bar.render_notebook() #直接展示
        map.render(r"../../TestResults/HTML/chart_map_visual_001.html") #生成HTML页面
        make_snapshot(snapshot, map.render(), r"../../TestResults/Picture/chart_map_visual_001.png") #导出图片

if __name__ == "__main__":
    title = "中国地图"
    province_distribution = {
        '河南': 45.23, '北京': 37.56, '河北': 61, '辽宁': 82, '江西': 96, '上海': 83, '安徽': 78,
        '江苏': 86, '湖南': 99, '浙江': 53, '海南': 62, '广东': 72, '湖北': 88, '黑龙江': 91, '澳门': 53,
        '陕西': 11, '四川': 7, '内蒙古': 23, '重庆': 33, '云南': 46, '贵州': 52, '吉林': 63, '山西': 72,
        '山东': 11, '福建': 4, '青海': 1,  '天津': 1, '其他': 1
    }
    data = {
        "海门": 9,"鄂尔多斯": 12,"招远": 22,"舟山": 32,"齐齐哈尔": 44,"盐城": 55,
        "赤峰": 66,"青岛": 78,"乳山": 88,"金昌": 99,"泉州": 7,"莱西": 21,
        "日照": 11,"胶南": 32,"南通": 43,"拉萨": 54,"云浮": 64,"梅州": 75
    }

    coordinate = [("广州", 55), ("北京", 66), ("杭州", 77), ("重庆", 88)]
    coordinate_relation = [("广州", "上海"), ("广州", "北京"), ("广州", "杭州"), ("广州", "重庆")]


    # Chart_Map.chart_map_base(title,province_distribution)
    # Chart_Map.chart_map_heat(title,data)
    # Chart_Map.chart_map_line(title,coordinate,coordinate_relation)
    # Chart_Map.chart_map_effect(title,data)
    Chart_Map.chart_map_visual(title,province_distribution)