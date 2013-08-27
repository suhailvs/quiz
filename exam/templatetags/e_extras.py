from django import template
register = template.Library()

@register.filter(name='multiply_nums')
def mnums(value,arg):	
	return value*arg

class BtnNode(template.Node):
	def __init__(self, format_string):
		self.nrows = int(format_string)/5
		self.lastrow=int(format_string)%5
	
	def render(self, context):
		str_outp=""
		for i in range(self.nrows):
			str_outp+='<div class="btn-group">'
			for j in range(5):
				k=i*5+j+1
				str_outp+='<button class="btn btn-nav-quests" id="btn-nav%d">%d</button>' %(k,k)
			str_outp+='</div><br>'
		if self.lastrow:
			str_outp+='<div class="btn-group">'
			for i in range(self.lastrow):
				k=5*self.nrows+i+1
				str_outp+='<button class="btn btn-nav-quests" id="btn-nav%d">%d</button>' %(k,k)
			str_outp+='</div><br>'
		return str_outp

@register.tag
def createbtns(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return BtnNode(format_string[1:-1])
