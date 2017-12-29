/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Pays = function () {
    /*
        @params obj 'data params'
            payer_id   'integer' payer id in query
            order_id   'string' order id in query
            order_type   'string' order type in query
            status   'string' status in query
            pay_type   'string' pay type in query
            transaction_id   'string' transaction id in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            extend_order_id   'string' 
            pay_type   'string' 
            order_type   'string' 
            order_id   'string' 
            pay_account_id   'string' 
            payer_id   'integer' 
            date_updated   'ref' 
            amount   'ref' 
            status   'string' 
            date_created   'ref' 
            transaction_id   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/pays",
            method: "GET",
            data: {
                payer_id: obj.payer_id,
                order_id: obj.order_id,
                order_type: obj.order_type,
                status: obj.status,
                pay_type: obj.pay_type,
                transaction_id: obj.transaction_id,
                limit: obj.limit,
                offset: obj.offset,
                page: obj.page,
                per_page: obj.per_page
                },
            success: function (res) {
                typeof obj.success === 'function' && obj.success(res);
            },
            fail: function (res) {
                typeof obj.fail === 'function' && obj.fail(res);
            },
            complete: function (res) {
                typeof obj.complete === 'function' && obj.complete(res);
            }
        })
    };
    

};

module.exports = {
    Pays: new Pays
};