/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var ZonesTenantIdAnswers = function () {
    /*
        @params obj 'data params'
            tenant_id   'string' tenant id in path
            offset   'integer' offset number
            limit   'integer' limit number
            page   'integer' page number
            per_page   'integer' per_page number
            order_by   'string' 
            
        @success
            status 200    type:array
            None   'None' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/zones/" + obj.tenant_id + "/answers",
            method: "GET",
            data: {
                offset: obj.offset,
                limit: obj.limit,
                page: obj.page,
                per_page: obj.per_page,
                order_by: obj.order_by
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
    ZonesTenantIdAnswers: new ZonesTenantIdAnswers
};