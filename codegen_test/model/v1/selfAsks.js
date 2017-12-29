/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var SelfAsks = function () {
    /*
        @params obj 'data params'
            ask_filter   'string' filter in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            answer   'ref' 
            visit_income   'integer' 
            is_public   'boolean' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/self/asks",
            method: "GET",
            data: {
                ask_filter: obj.ask_filter,
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
    SelfAsks: new SelfAsks
};