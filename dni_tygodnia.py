import calendar

def date_day(date):
	if date.weekday() == 0:
		return "Poniedziałek"

	if date.weekday() == 1:
		return "Wtorek"

	if date.weekday() == 2:
		return "Środa"

	if date.weekday() == 3:
		return "Czwartek"

	if date.weekday() == 4:
		return "Piątek"

	if date.weekday() == 5:
		return "Sobota"

	if date.weekday() == 6:
		return "Niedziela"

	return None


def date_day_short(date):
	return "{}.".format(date_day(date)[:3])


def month_days_name(date):
	last_day = calendar.monthrange(date.year, date.month)[1]

	return [{i: date_day(date.replace(day=i))} for i in range(1, last_day + 1)]
