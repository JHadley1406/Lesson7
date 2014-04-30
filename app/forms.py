from flask.ext.wtf import Form
from wtforms import TextField, Button
from wtforms.validators import Required

class MileageForm(Form):
	startingMileage = TextField('Starting Mileage', validators = [Required()])
	endingMileage = TextField('Current Mileage', validators = [Required()])
	fuel = TextField('Gallons of Gas', validators = [Required()])
	submit = Button('Submit')
	
class Disemvoweler(Form):
	voweledText = TextField('Text to Disemvowel')
	unVoweledText = TextField('Disemvoweled Text')
	disemvowel = Button('Disemvowel')
	reemvowel = Button('ReEmvowel')