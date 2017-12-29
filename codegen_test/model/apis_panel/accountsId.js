/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsId = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            
        @success
            status 200    type:object
            introduction   'ref' 
            is_receive_inquiry   'boolean' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts/" + obj.id + "",
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
            status   'ref' 
            title   'ref' 
            introduction   'ref' 
            order_score   'integer' 
            is_star   'boolean' 
            is_admin   'boolean' 
            avatar   'ref' 
            is_receive_inquiry   'boolean' 
            nickname   'ref' 
            
        @success
            status 200    type:object
            introduction   'ref' 
            is_receive_inquiry   'boolean' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/accounts/" + obj.id + "",
            method: "PUT",
            data: {
                status: obj.status,
                title: obj.title,
                introduction: obj.introduction,
                order_score: obj.order_score,
                is_star: obj.is_star,
                is_admin: obj.is_admin,
                avatar: obj.avatar,
                is_receive_inquiry: obj.is_receive_inquiry,
                nickname: obj.nickname
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
            url: "/accounts/" + obj.id + "",
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
    AccountsId: new AccountsId
};