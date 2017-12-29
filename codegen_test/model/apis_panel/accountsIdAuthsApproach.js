/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsIdAuthsApproach = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            approach   'string' approach in path
            
        @success
            status 200    type:object
            date_created   'string' 
            approach   'string' 
            account_id   'integer' 
            identity   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts/" + obj.id + "/auths/" + obj.approach + "",
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
            id   'integer' int id in query
            approach   'string' approach in path
            identity   'string' 
            
        @success
            status 200    type:object
            ok   'boolean' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts/" + obj.id + "/auths/" + obj.approach + "",
            method: "PUT",
            data: {
                identity: obj.identity
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
            id   'integer' int id in query
            approach   'string' approach in path
            
        @success
            status 204    type:object
    */
    this.delete = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts/" + obj.id + "/auths/" + obj.approach + "",
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
    AccountsIdAuthsApproach: new AccountsIdAuthsApproach
};