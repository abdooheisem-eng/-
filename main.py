from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is Running!"

if __name__ == '__main__':
    # تشغيل السيرفر على جميع مخارج الجهاز بورت 80
    app.run(host='0.0.0.0', port=80)
