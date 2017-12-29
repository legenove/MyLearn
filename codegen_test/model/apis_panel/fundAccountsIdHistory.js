/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var FundAccountsIdHistory = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            order_id   'string' order id in query
            fund_type   'string' fund type in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            from_account_id   'ref' 
            account_id   'ref' 
            order_id   'ref' 
            payoff_id   'integer' 
            fund_type   'string' 
            amount   'integer' 
            date_created   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/fund_accounts/" + obj.id + "/history",
            method: "GET",
            data: {
                order_id: obj.order_id,
                fund_type: obj.fund_type,
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
    FundAccountsIdHistory: new FundAccountsIdHistory
};