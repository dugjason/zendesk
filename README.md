Zendesk API Wrapper for Python
=========================================================================================
Python Zendesk is wrapper for the Zendesk API. This library provides an
easy and flexible way for developers to communicate with their Zendesk
account in their application. 


Requirements
------------
[Requests](http://www.python-requests.org/en/latest/) is used for authentication and requests

    (pip install | easy_install) requests


Installation
------------
This Zendesk Python Library has been forked and modified ([eventbrite/zendesk](https://github.com/eventbrite/zendesk)) and must be compiled from source

    python setup.py install


Example Use
-----------

	from zendesk import Zendesk

	################################################################
	## NEW CONNECTION CLIENT
	################################################################
	zendesk = Zendesk('https://yourcompany.zendesk.com', 'you@yourcompany.com', 'passwd', api_version=2)

	################################################################
	## TICKETS
	################################################################

	# List
	zendesk.list_tickets(view_id=1) # Must have a view defined

	# Create
	new_ticket = {
	    'ticket': {
	        'requester_name': 'Howard Schultz',
	        'requester_email': 'howard@starbucks.com',
	        'subject':'My Starbucks coffee is cold!',
	        'description': 'please reheat my coffee',
	        'set_tags': 'coffee drinks',
	        'ticket_field_entries': [
	            {
	                'ticket_field_id': 1,
	                'value': 'venti'
	            },
	            {
	                'ticket_field_id': 2,
	                'value': '$10'
	            }
	        ]
	    }
	}
	ticket_url = zendesk.create_ticket(data=new_ticket)
	ticket_id = get_id_from_url(ticket_url)

	# Show
	zendesk.show_ticket(ticket_id=ticket_id)

	# Delete
	zendesk.delete_ticket(ticket_id=ticket_id)

	# More examples in `examples` folder!


