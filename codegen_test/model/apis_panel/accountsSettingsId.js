/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsSettingsId = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            
        @success
            status 200    type:object
            account   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts/settings/" + obj.id + "",
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
            _value   'string' 
            
        @success
            status 200    type:object
            account_id   'integer' 
            date_updated   'string' 
            _value   'string' 
            key   'string' 
            date_created   'string' 
            id   'integer' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts/settings/" + obj.id + "",
            method: "PUT",
            data: {
                _value: obj._value
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
            
        @success
            status 204    type:object
            ok   'boolean' 
            
    */
    this.delete = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts/settings/" + obj.id + "",
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
    AccountsSettingsId: new AccountsSettingsId
};