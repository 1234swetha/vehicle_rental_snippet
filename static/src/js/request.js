odoo.define('vehicle_rental_snippet.dynamic', function (require) {
   var PublicWidget = require('web.public.widget');
   var rpc = require('web.rpc');
   var core = require('web.core');
   var Qweb = core.qweb;
   var Dynamic = PublicWidget.Widget.extend({
       selector: '.dynamic_snippet_blog',
       start: function () {
           var self = this;
           rpc.query({
               route: '/request',
               params: {},
           }).then(function (result) {
             result[0].set_active=true;
             var name = result
             $('.qweb_req').append(Qweb.render('vehicle_rental_snippet.req_template',{name}));
           });
       },
   });
   PublicWidget.registry.dynamic_snippet_blog = Dynamic;
   return Dynamic;
});

