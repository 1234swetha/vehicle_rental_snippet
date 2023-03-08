import itertools
from odoo import http
from odoo.http import request


class Request(http.Controller):
    @http.route(['/request'], type="json", auth="public")
    def request(self):
        vals = {}
        requests = request.env['rent.request'].sudo().search([]).mapped('vehicle_id')
        for rec in requests:
            req_count = request.env['rent.request'].sudo().search_count([('vehicle_id', '=', rec.id)])
            vals.update({
                rec: req_count
            })
        values = dict(sorted(vals.items(), key=lambda x: x[1], reverse=True))
        val_dicts = dict(itertools.islice(values.items(), 10))
        val_list = []
        for i in val_dicts:
            val_list.append([
                i.name, i.id
            ])
        chunk_size = 4
        top_vehicles = [val_list[i:i + chunk_size] for i in range(0, len(val_list), chunk_size)]
        return top_vehicles

    @http.route(['/snippet_details'], type="http", auth="public", csrf=False)
    def submit(self, **kwargs):
        req_id = eval(kwargs.get('req_id'))
        details = request.env['vehicle.rental'].sudo().search([('id', '=', req_id)])
        values = {}
        values.update({
            'vehicle': details,
        })
        return request.render('vehicle_rental_snippet.veh_details', values)
