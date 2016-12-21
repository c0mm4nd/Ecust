import web

render = web.template.render('template')
urls = (
	'/', 'index',
	'/test','test'
	)

class index:
    def GET(self):
    	i = web.input(name=None)
    	time = "now"
    	print i
        return render.test()

class test:
	def GET(self):
		return "test"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()