odoo.define('RestaurantPOS.PrintKitchenButton', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { useListener } = require('web.custom_hooks');
    const Registries = require('point_of_sale.Registries');

    class PrintKitchenButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this.onClick);
        }
        onClick() {
            alert("Enviar a cocina y guardar");
        }
    }
    PrintKitchenButton.template = 'PrintKitchenButton';

    ProductScreen.addControlButton({
        component: PrintKitchenButton,
        condition: function() {
            return this.env.pos.config.iface_floorplan;
        },
    });

    Registries.Component.add(PrintKitchenButton);

    return PrintKitchenButton;
});
