/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TenantsTenantIdRespondents = function () {
    /*
        @params obj 'data params'
            tenant_id   'string' tenant id in path
            page   'integer' page number
            per_page   'integer' per_page number
            offset   'integer' offset number
            limit   'integer' limit number
            
        @success
            status 200    type:array
            status   'string' 
            comment   'string' 
            account   'ref' 
            account_id   'integer' 
            date_updated   'string' 
            tenant_id   'string' 
            order_score   'integer' 
            date_created   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/tenants/" + obj.tenant_id + "/respondents",
            method: "GET",
            data: {
                page: obj.page,
                per_page: obj.per_page,
                offset: obj.offset,
                limit: obj.limit
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
    
    /*
        @params obj 'data params'
            tenant_id   'string' tenant id in path
            account_id   'integer' 
            
        @success
            status 201    type:object
            status   'string' 
            comment   'string' 
            account   'ref' 
            account_id   'integer' 
            date_updated   'string' 
            tenant_id   'string' 
            order_score   'integer' 
            date_created   'string' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/tenants/" + obj.tenant_id + "/respondents",
            method: "POST",
            data: {
                account_id: obj.account_id
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
    TenantsTenantIdRespondents: new TenantsTenantIdRespondents
};