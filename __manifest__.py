{
    'name': 'Vehicle Rental Snippet',
    'version': '16.0.1.0.0',
    'sequence': 5,
    'depends': [
             'website',
             'vehicle_rental',
    ],
    'data': [
        'views/request.xml',
        'views/dynamic_req.xml',
        'views/veh_details.xml',
        ],
    'assets': {
       'web.assets_frontend': [
           '/vehicle_rental_snippet/static/src/css/snippet.scss',
           '/vehicle_rental_snippet/static/src/xml/snippet.xml',
           '/vehicle_rental_snippet/static/src/js/request.js',
       ],
    },
    'installable': True,
    'application': True,
    'auto_install': False
}