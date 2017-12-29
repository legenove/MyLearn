/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var WeixinMenu = function () {
    /*
        @params obj 'data params'
            
        @success
            status 200    type:array
            sub_button   'array' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/weixin/menu",
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
            button   'array' 
            
        @success
            status 201    type:object
            ok   'boolean' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/weixin/menu",
            method: "POST",
            data: {
                button: obj.button
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
    WeixinMenu: new WeixinMenu
};