import svgwrite

# 创建SVG对象
dwg = svgwrite.Drawing('nervous_yet_calm.svg', size=('600px', '1000px'))

# 定义阴影效果
shadow = svgwrite.filters.Filter(id='shadow')
shadow.feDropShadow(dx=0, dy=4, stdDeviation=4, flood_color='#AAA')
dwg.defs.add(shadow)

# 背景卡片，圆角边框和阴影
dwg.add(dwg.rect(insert=(20, 20), size=('560px', '960px'), rx=20, ry=20,
                 fill='#F9F9F9', stroke='#DDD', filter='url(#shadow)'))

# 标题
dwg.add(dwg.text('紧张且镇定 Nervous Yet Calm', insert=(300, 80),
                 text_anchor='middle', font_size=32, font_weight='bold', fill='purple'))

# 内容区域
content_group = dwg.g(font_size=16, fill='#333')

# 添加情绪解析标题
content_group.add(dwg.text('情绪解析', insert=(50, 130), font_size=24, font_weight='bold'))

# 源起
content_group.add(dwg.text('源起:', insert=(50, 170), font_weight='bold'))
content_group.add(dwg.text('在面对突发事件或重要决策时，人们可能同时感到紧张和镇定。', insert=(50, 190)))

# 体验
content_group.add(dwg.text('体验:', insert=(50, 230), font_weight='bold'))
content_group.add(dwg.text('内心涌动着压力，但头脑保持清晰，能够冷静思考。', insert=(50, 250)))

# 具身
content_group.add(dwg.text('具身:', insert=(50, 290), font_weight='bold'))
content_group.add(dwg.text('心跳加速，呼吸深沉，但表面平静，动作稳健。', insert=(50, 310)))

# 意象
content_group.add(dwg.text('意象:', insert=(50, 350), font_weight='bold'))
content_group.add(dwg.text('如同暴风雨中的船长，面对巨浪但目光坚定，掌舵前行。', insert=(50, 370)))

# 阶段
content_group.add(dwg.text('阶段:', insert=(50, 410), font_weight='bold'))
content_group.add(dwg.text('在成年期，承担责任和面对挑战时更易出现。', insert=(50, 430)))

# 事件
content_group.add(dwg.text('事件:', insert=(50, 470), font_weight='bold'))
content_group.add(dwg.text('经历过紧急情况或高压环境的人，更容易在这种感受上有所不同。', insert=(50, 490)))

# 性格
content_group.add(dwg.text('性格:', insert=(50, 530), font_weight='bold'))
content_group.add(dwg.text('培养出沉着冷静的性格，善于在压力下作出决策。', insert=(50, 550)))

# 改变
content_group.add(dwg.text('改变:', insert=(50, 590), font_weight='bold'))
content_group.add(dwg.text('通过自我调节和支持，这种感受可转化为自信和从容。', insert=(50, 610)))

# 文学
content_group.add(dwg.text('文学:', insert=(50, 650), font_weight='bold'))
content_group.add(dwg.text('“泰山崩于前而色不变，麋鹿兴于左而目不瞬。”——《史记》', insert=(50, 670)))

# 将内容组添加到SVG
dwg.add(content_group)

# 图形元素 - 场景：暴风雨中的灯塔

# 海洋
dwg.add(dwg.rect(insert=(100, 720), size=('400px', '240px'), fill='#B3E5FC',
                 stroke='#0288D1', stroke_width=2, rx=15, ry=15))

# 灯塔主体
dwg.add(dwg.rect(insert=(290, 750), size=(20, 100), fill='#FF7043'))

# 灯塔顶部
dwg.add(dwg.polygon(points=[(300, 730), (280, 750), (320, 750)], fill='#FF7043'))

# 灯光
dwg.add(dwg.polygon(points=[(300, 750), (250, 820), (350, 820)], fill='rgba(255, 238, 88, 0.5)'))

# 波浪
dwg.add(dwg.path(d="M100 860 Q150 840 200 860 T300 860 T400 860 T500 860",
                 fill='none', stroke='#0288D1', stroke_width=4))

# 保存SVG文件
dwg.save()
