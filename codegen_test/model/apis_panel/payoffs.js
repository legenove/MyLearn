/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Payoffs = function () {
    /*
        @params obj 'data params'
            account_id   'integer' account id in query
            status   'string' status in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            status   'string' 
            account_id   'ref' 
            date_updated   'ref' 
            amount   'ref' 
            payment_no   'string' 
            settle_amount   'ref' 
            date_created   'ref' 
            id   'string' 
            receipt_account   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/payoffs",
            method: "GET",
            data: {
                account_id: obj.account_id,
                status: obj.status,
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
    Payoffs: new Payoffs
};