/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TenantsTenantIdRespondentsAccountId = function () {
    /*
        @params obj 'data params'
            tenant_id   'string' tenant id in path
            account_id   'integer' account id in path
            order_score   'integer' 
            
        @success
            status 200    type:object
            status   'string' 
            comment   'string' 
            account   'ref' 
            account_id   'integer' 
            date_updated   'string' 
            tenant_id   'string' 
            order_score   'integer' 
            date_created   'string' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/tenants/" + obj.tenant_id + "/respondents/" + obj.account_id + "",
            method: "PUT",
            data: {
                order_score: obj.order_score
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
            account_id   'integer' account id in path
            
        @success
            status 204    type:object
    */
    this.delete = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/tenants/" + obj.tenant_id + "/respondents/" + obj.account_id + "",
            method: "DELETE",
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
    TenantsTenantIdRespondentsAccountId: new TenantsTenantIdRespondentsAccountId
};