odoo.define('pos_product_varients_ext', function (require) {
    "use strict";

    var models = require('point_of_sale.models');
    require('l10n_do_pos.screens');

    var core = require('web.core');
    var PosPopWidget = require('point_of_sale.popups');
    var gui = require('point_of_sale.gui');
    var chrome = require('point_of_sale.chrome');
    var screens = require('point_of_sale.screens');
    var _t = core._t;
    var rpc = require('web.rpc');
    var QWeb = core.qweb;
    var floor_screen = require('pos_restaurant.floors');
    var PosDB = require('point_of_sale.DB');

    models.load_fields('product.template', ['categ_id']);
    models.Order = models.Order.extend({
        initialize: function () {
            this.client_order_print = this.client_order_print || "";
            _super_order_model.initialize.apply(this, arguments);

        },
        init_from_JSON: function (json) {
            _super_order_model.init_from_JSON.call(this, json);
            this.client_order_print = json.client_order_print;
        },
        add_product: function (product, options) {

            _super_order_model.init_from_JSON.call(this, product, options);
            console.log(product);


        }
    });



})