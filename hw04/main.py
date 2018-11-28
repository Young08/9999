import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,n):

       
        n=int(n) if n is not None else 9

    
        html='''
        <html>
        <body>
        <table>
        '''
        for a in range(1,n+1):
            html +='<TR>'
            for b in range(1,a+1):
                html +='<TD>%d*%d=%d</TD>'% (b,a,a*b)
            html +='</TR>'
        
        html +='''
        </table>
        </body>
        </html>
        '''

        self.write(html)

application = tornado.web.Application([
    (r"/([0-9])?", MainHandler),
],debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
