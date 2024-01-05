import tornado.ioloop
import tornado.web
import pymysql

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        title = "My Tornado App"
        header = "Welcome to My App!"
        message = "ChatGPT helped me make this app."

        # Render the template and pass in the dynamic content
        self.render("/app/templates/index.html", title=title, header=header, message=message)

class ProbeHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            db = pymysql.connect('')
            cursor = db.cursor()
            cursor.execute("SELECT VERSION()")
            result = cursor.fetchone()
            title = "OK - DB version: %s" % result
            bgcolor = "limegreen"
            self.set_status(200)
        except pymysql.Error as e:
            title = "NOT OK - %s" % e
            bgcolor = "darkred"
            self.set_status(503)
        self.render("template.html", title=title, bgcolor=bgcolor) 

def make_app():
    return tornado.web.Application ([
        (r"/", MainHandler),
        (r"/isalive", ProbeHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()