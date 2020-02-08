# -*- coding: utf-8 -*-
"""
接口：
创建人：魏奇
更新人：魏奇
更新时间：2020-01-16 15:02
描述：
"""

import random
from unittest.mock import patch
from nose.tools import assert_equal, assert_in
from pyecharts import options as opts
from pyecharts.charts import Bar3D
from pyecharts.faker import Faker


# @patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar3d_base():
    data = [(i, j, random.randint(0, 12)) for i in range(6) for j in range(24)]
    c = (
        Bar3D()
            .add(
            "",
            [[d[1], d[0], d[2]] for d in data],
            xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
            .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=20))
    )
    c.render()
    c.render(r"../../TestResults/HTML/chart_3d_001.html") #生成HTML页面
    # _, content = fake_writer.call_args[0]
    # assert_equal(c.theme, "white")
    # assert_equal(c.renderer, "canvas")



# @patch("pyecharts.render.engine.write_utf8_html_file")
def test_bar3d_stack():
    data1 = [(i, j, random.randint(0, 12)) for i in range(6) for j in range(24)]
    data2 = [(i, j, random.randint(13, 20)) for i in range(6) for j in range(24)]
    c = (
        Bar3D()
            .add(
            "1",
            [[d[1], d[0], d[2]] for d in data1],
            xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
            .add(
            "2",
            [[d[1], d[0], d[2]] for d in data2],
            xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
            yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
            zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        )
            .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=20))
            .set_series_opts(**{"stack": "stack"})
    )
    c.render()
    c.render(r"../../TestResults/HTML/chart_3d_002.html") #生成HTML页面
    # _, content = fake_writer.call_args[0]
    # assert_in("stack", content)


import math
from unittest.mock import patch
from pyecharts import options as opts
from pyecharts.charts import Line3D
from pyecharts.faker import Faker


# @patch("pyecharts.render.engine.write_utf8_html_file")
def test_line3d_base():
    data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        data.append([x, y, z])
    c = (
        Line3D()
            .add(
            "",
            data,
            xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="value"),
            yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="value"),
            grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100),
        )
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                max_=30, min_=0, range_color=Faker.visual_color
            )
        )
    )
    c.render()
    c.render(r"../../TestResults/HTML/chart_3d_003.html") #生成HTML页面
    # _, content = fake_writer.call_args[0]
    # assert_equal(c.theme, "white")
    # assert_equal(c.renderer, "canvas")

from unittest.mock import patch

from nose.tools import assert_equal, assert_in

from pyecharts.charts import Map3D
from pyecharts.faker import Faker


# @patch("pyecharts.render.engine.write_utf8_html_file")
def test_map_3d():
    c = Map3D().add(
        "商家A", [list(z) for z in zip(Faker.provinces, Faker.values())], "china"
    )
    c.render()
    c.render(r"../../TestResults/HTML/chart_3d_004.html") #生成HTML页面
    # _, content = fake_writer.call_args[0]
    # assert_in("map3D", content)
    # assert_equal(c.theme, "white")
    # assert_equal(c.renderer, "canvas")

import random
from unittest.mock import patch

from nose.tools import assert_equal

from pyecharts import options as opts
from pyecharts.charts import Scatter3D
from pyecharts.faker import Faker


# @patch("pyecharts.render.engine.write_utf8_html_file")
def test_scatter3d_base():
    data = [
        [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]
        for _ in range(80)
    ]
    c = (
        Scatter3D()
            .add("", data)
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(range_color=Faker.visual_color)
        )
    )
    c.render()
    c.render(r"../../TestResults/HTML/chart_3d_005.html") #生成HTML页面
    # _, content = fake_writer.call_args[0]
    # assert_equal(c.theme, "white")
    # assert_equal(c.renderer, "canvas")

import math
from unittest.mock import patch

from nose.tools import assert_equal

from pyecharts import options as opts
from pyecharts.charts import Surface3D
from pyecharts.faker import Faker


# @patch("pyecharts.render.engine.write_utf8_html_file")
def test_surface3d_base():
    def surface3d_data():
        for t0 in range(-60, 60, 1):
            y = t0 / 60
            for t1 in range(-60, 60, 1):
                x = t1 / 60
                if math.fabs(x) < 0.1 and math.fabs(y) < 0.1:
                    z = "-"
                else:
                    z = math.sin(x * math.pi) * math.sin(y * math.pi)
                yield [x, y, z]

    c = (
        Surface3D()
            .add(
            "",
            list(surface3d_data()),
            xaxis3d_opts=opts.Axis3DOpts(type_="value"),
            yaxis3d_opts=opts.Axis3DOpts(type_="value"),
            grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100),
        )
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                max_=3, min_=-3, range_color=Faker.visual_color
            )
        )
    )
    c.render()
    c.render(r"../../TestResults/HTML/chart_3d_006.html") #生成HTML页面
    # _, content = fake_writer.call_args[0]
    # assert_equal(c.theme, "white")
    # assert_equal(c.renderer, "canvas")

if __name__ == "__main__":

    test_bar3d_base()
    test_bar3d_stack()
    test_line3d_base()
    test_map_3d()
    test_scatter3d_base()
    test_surface3d_base()