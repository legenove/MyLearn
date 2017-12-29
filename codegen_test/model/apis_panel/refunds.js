/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Refunds = function () {
    /*
        @params obj 'data params'
            transaction_id   'string' transaction id in query
            status   'string' status in query
            payer_id   'integer' payer id in query
            order_id   'string' order id in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            status   'string' 
            operator_id   'integer' 
            date_updated   'ref' 
            pay   'ref' 
            amount   'ref' 
            date_created   'ref' 
            transaction_id   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/refunds",
            method: "GET",
            data: {
                transaction_id: obj.transaction_id,
                status: obj.status,
                payer_id: obj.payer_id,
                order_id: obj.order_id,
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
    Refunds: new Refunds
};