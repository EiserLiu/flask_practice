from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis

app = Flask(__name__)
# redis中默认有16个库,我们可以让flask_redis初始化时,默认连接到不同库中,需要我们设置配置redis的前缀config_prefix

app.config.update({
    "REDIS_SESSION": "redis://root:123456@127.0.0.1:6379/0",
    "REDIS_USER": "redis://root:123456@127.0.0.1:6379/1",
    "REDIS_ORDER": "redis://root:123456@127.0.0.1:6379/2",
})

session_redis = FlaskRedis(config_prefix="REDIS_SESSION")
user_redis = FlaskRedis(config_prefix="REDIS_USER")
order_redis = FlaskRedis(config_prefix="REDIS_ORDER")

session_redis.init_app(app)
user_redis.init_app(app)
order_redis.init_app(app)


@app.route("/")
def index():
    session_redis.setnx("age", 100)
    user_redis.setnx("user_id", 100)
    order_redis.setnx("order_id", 100)
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
