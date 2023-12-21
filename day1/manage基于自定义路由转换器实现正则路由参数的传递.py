# 导入flask核心类
from flask import Flask

# 初始化web应用程序实例对象
app = Flask(__name__)


# app.debug = False
# 站点加载配置方式1
# app.config['debug'] = False
# 站点加载配置方式2
# config = {
#     "DEBUG": True
# }
# app.config.update(config)
# 站点加载配置方式3
class Config(object):
    DEBUG = True


app.config.from_object(Config)


# 站点配置加载方式4


@app.route("/", methods=["get"])
def index():
    return "<h1>123</h1>"


# rule:当前视图路由地址
# mathods:当前视图的请求方法
@app.route(rule="/index2/<cid>/<gid>", methods=["get", "post"])
def index2(cid, gid):
    return f"显示gid={gid},cid={cid}的商品信息"


# 自定义路由转换
from werkzeug.routing.converters import BaseConverter


class RegexConverter(BaseConverter):
    def __init__(self, map, *args, **kwargs):
        super().__init__(map, *args, **kwargs)
        self.regex = args[0]


app.url_map.converters["regex"] = RegexConverter


@app.route("/sms/<regex('1[3-9]\d{9}'):mobile>")
def sms(mobile):
    return f"发送短信给{mobile}用户"


if __name__ == '__main__':
    # 运行flask
    app.run(host="0.0.0.0", port=5000)
