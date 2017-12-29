/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TenantsIdApplication = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            
        @success
            status 200    type:object
            status   'string' 
            tenant_id   'string' 
            account_id   'integer' 
            date_updated   'string' 
            date_created   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/tenants/" + obj.id + "/application",
            method: "GET",
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
            id   'string' string id in path
            comment   'string' 
            
        @success
            status 201    type:object
            status   'string' 
            tenant_id   'string' 
            account_id   'integer' 
            date_updated   'string' 
            date_created   'string' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/tenants/" + obj.id + "/application",
            method: "POST",
            data: {
                comment: obj.comment
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
    TenantsIdApplication: new TenantsIdApplication
};